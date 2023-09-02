if __name__ != "__main__":
    try:
        import time
        import typing
        import random
        import math
        import traceback
        import multiprocessing

        import pygame
        import moderngl
        import moderngl_window
        from moderngl_window.scene.camera import KeyboardCamera
        from moderngl_window import geometry
        import numpy
        import pyrr
        import pyautogui
        import dill

        import inventory as inventoryGUI
        import map_gui
        import loading_screen
        
        from registry_utils import Registry
        
        import display_utils
        import logging_utils
        import sound_utils
        import caption_utils
        import tkinter_utils
        import error_utils
        import shader_utils
        import particle_utils
        import weather_utils
        import math_utils
        import menu_utils
        import camera_utils
        import shadow_mapping_utils
    except Exception as Message:
        try:
            import sys
            import tkinter as tk
            from tkinter import messagebox
            root = tk.Tk()
            root.withdraw()
            messagebox.showerror(
                "startup Fail",
                str(Message))
            sys.exit()

        except Exception as Message:
            print(Message)
            sys.exit()
            
    class create_game_engine(Registry):
        def start():
            ctx = moderngl.create_context(standalone=False)

            wnd = moderngl_window.get_local_window_cls("pygame2")

            moderngl_window.activate_context(wnd, ctx)

            return ctx, wnd

        def game_engine():
            try:
                startLoading = time.perf_counter()

                if Registry.dont_use_set_resolution is False:
                    fullscreen_x = pyautogui.size()[0]
                    fullscreen_y = pyautogui.size()[1]
                    
                else:
                    formatted_resolution = Registry.resolution.split(",")
                    fullscreen_x = int(formatted_resolution[0][1:])
                    fullscreen_y = int(formatted_resolution[1][1:-1])

                display_utils.display_utils.set_display(
                        fullscreen_size=(
                            fullscreen_x,
                            fullscreen_y),
                        opengl=True)

                ctx, wnd = create_game_engine.start()

                wnd.vsync = False

                converted_theme_col_r = (1/255)*Registry.background_color[0]
                converted_theme_col_g = (1/255)*Registry.background_color[1]
                converted_theme_col_b = (1/255)*Registry.background_color[2]

                ctx.clear(converted_theme_col_r,
                        converted_theme_col_g,
                        converted_theme_col_b)

                pygame.display.flip()

                if Registry.aa:
                    samples = int(
                        str(Registry.aa_quality).split("x")[0])

                else:
                    samples = 1

                wnd.samples = samples

                skybox_distance = 1600

                Registry.real_window_width = pygame.display.get_window_size()[
                    0]
                Registry.real_window_height = pygame.display.get_window_size()[
                    1]

                aspect_ratio = Registry.real_window_width / Registry.real_window_height

                camera = KeyboardCamera(
                    wnd.keys,
                    aspect_ratio=aspect_ratio,
                    far=2000.0,
                    near=0.1)

                camera_enabled = True

                camera.projection.update(
                    near=1,
                    far=skybox_distance,
                    fov=70)

                wnd.mouse_exclusivity = True
                
                self_dict = {}

                for element in Registry.__dict__:
                    if not ("<" in str(Registry.__dict__[element]) and
                                ">" in str(Registry.__dict__[element])):
                        
                        self_dict[element] = Registry.__dict__[element]
                    else:
                        logging_utils.create_log_message.update_log_information(
                            f"Omitted input {element} to additional GameEngine menus")
                
                start_loading = multiprocessing.Event()
                (recieve_additional_data,
                    send_additional_data) = multiprocessing.Pipe()
                
                loading_process = multiprocessing.Process(
                        target=loading_screen.generate_load_screen.load,
                        args=(
                            start_loading,
                            recieve_additional_data,
                            self_dict,))

                loading_process.start()

                start_loading.set()

                send_additional_data.send({"loading_progress":20})

                start_inventory = multiprocessing.Event()
                
                inventory_process = multiprocessing.Process(
                        target=inventoryGUI.generate_inventory.inventory_gui,
                        args=(start_inventory,
                              self_dict,))

                inventory_process.start()

                start_map = multiprocessing.Event()
                
                map_process = multiprocessing.Process(
                        target=map_gui.generate_map_gui.map_gui,
                        args=(start_map,
                              self_dict,))

                map_process.start()

                # Offscreen buffer
                offscreen_size = 1024, 1024
                offscreen_depth = ctx.depth_texture(offscreen_size)
                offscreen_depth.compare_func = ""
                offscreen_depth.repeat_x = False
                offscreen_depth.repeat_y = False
                # Less ugly by default with linear. May need to be NEAREST for some techniques
                offscreen_depth.filter = (moderngl.LINEAR,
                                            moderngl.LINEAR)

                sun_radius = 50

                sun = geometry.sphere(
                    radius=sun_radius)

                moon = geometry.sphere(
                    radius=80)

                send_additional_data.send({"loading_progress":30})

                SkySphere = geometry.sphere(
                    radius=skybox_distance)

                objects: typing.Dict[
                    str,
                    moderngl.VertexArray] = {}

                objects_shadow: typing.Dict[
                    str,
                    moderngl.VertexArray] = {}

                map_object_path = Registry.base_folder / "resources" / "game engine resources" / "map" / "map.obj"

                # Use 'u' to do things with UVs that this really needs
                scene: moderngl_window.scene.Scene = moderngl_window.WindowConfig.load_scene(
                    wnd,
                    path=map_object_path,
                    cache=True)

                send_additional_data.send({"loading_progress":40})

                skysphere_object_path = Registry.base_folder / "resources" / "game engine resources" / "skysphere" / "ClearSkyTransition.gif"

                SkyBox_texture_Sun = moderngl_window.WindowConfig.load_texture_array(
                    wnd,
                    path=skysphere_object_path,
                    anisotropy=samples)

                send_additional_data.send({"loading_progress":50})

                # Programs
                (CloudsProgram,
                    depth_prog,
                    shadowmap,
                    sun_prog,
                    moon_prog,
                    skysphere_prog,
                    particles_screen) = shader_utils.load_programs.load_program_files(
                        wnd)

                (particles_transform,
                    gpu_emitter_particles) = shader_utils.load_programs.load_program_text(ctx)
                
                send_additional_data.send({"loading_progress":60})

                vao = scene.root_nodes[0].mesh.vao
                objects["map"] = vao.instance(shadowmap)
                objects_shadow["map"] = vao.instance(depth_prog)

                skysphere_prog["texture0"].value = 0
                skysphere_prog["num_layers"].value = 41.0

                # affects the velocity of the particles over time
                # grav?
                particles_transform["gravity"].value = -.005
                ctx.point_size = 2  # point size

                if Registry.fancy_particles:
                    N = 5_000  # particle count

                else:
                    N = 2_500

                # Initial / current number of active particles
                active_particles = N // 100
                # Maximum number of particles to emit per frame
                max_emit_count = N // 100
                stride = 28  # byte stride for each vertex
                floats = 7
                # Note that passing dynamic=True probably doesn't mean
                # anything to most drivers toRegistry.day
                try:
                    vbo1 = ctx.buffer(
                        reserve=N * stride)
                    vbo2 = ctx.buffer(
                        reserve=N * stride)

                except Exception as Message:
                    log_message = "GameEngine > GameEngine > __init__: " + \
                        str(Message)

                    logging_utils.create_log_message.update_log_warning(
                        log_message)

                    vbo1 = Registry.ctx.buffer(
                        reserve=N * stride,
                        dynamic=True)
                    
                    vbo2 = Registry.ctx.buffer(
                        reserve=N * stride,
                        dynamic=True)

                # Write some initial particles
                vbo1.write(
                    numpy.fromiter(
                        particle_utils.particles.gen_particles(
                            N),
                        
                        count=active_particles * floats,
                        dtype="f4"))

                # Transform vaos. We transform data back and forth to avoid buffer copy
                transform_vao1 = ctx.vertex_array(
                    particles_transform,
                    [(vbo1, "2f 2f 3f", "in_pos", "in_vel", "in_color")],
                )
                transform_vao2 = ctx.vertex_array(
                    particles_transform,
                    [(vbo2, "2f 2f 3f", "in_pos", "in_vel", "in_color")],
                )

                send_additional_data.send({"loading_progress":60})

                # Render vaos. The render to screen version of the tranform vaos above
                render_vao1 = ctx.vertex_array(
                    particles_screen,
                    [(vbo1, "2f 2x4 3f", "in_pos", "in_color")],
                )
                render_vao2 = ctx.vertex_array(
                    particles_screen,
                    [(vbo2, "2f 2x4 3f", "in_pos", "in_color")],
                )

                # The emit buffer size is only max_emit_count.
                emit_buffer_elements = max_emit_count

                gpu_emitter_vao = ctx._vertex_array(
                    gpu_emitter_particles, [])

                # Query object to inspect render calls
                query = ctx.query(primitives=True)

                # Cycle emit methods per frame
                particles_screen["projection"].write(
                    pyrr.matrix44.create_orthogonal_projection(
                        -aspect_ratio, aspect_ratio,
                        -1, 1,
                        -1, 100,
                        dtype='f4',)
                )

                shadowmap["u_sampler_shadow"].value = 0
                shadowmap["grass_color"].value = 1
                shadowmap["rock_color"].value = 2

                shadowmap["light_level"] = 0.5

                mvp = (shadowmap["projection_matrix"], shadowmap["matrix"])
                mvp_depth = (shadowmap["bias_matrix"], shadowmap["mvp_light"])

                light = shadowmap["u_light"]
                color = shadowmap["u_color"]

                mvp_shadow = depth_prog["u_mvp"]

                sun_prog["color"].value = (1.0, 1.0, 0.0, 1.0)
                moon_prog["color"].value = (1.0, 1.0, 1.0, 1.0)

                color.value = (1.0, 1.0, 1.0)

                send_additional_data.send({"loading_progress":70})

                grass_texture_path = Registry.base_folder / "resources" / "game engine resources" / "map" / "GrassTexture.png"
                rock_texture_path = Registry.base_folder / "resources" / "game engine resources" / "map" / "RockTexture.png"

                tex1 = moderngl_window.WindowConfig.load_texture_2d(
                    wnd,
                    path=grass_texture_path,
                    mipmap=True,
                    anisotropy=samples)

                tex2 = moderngl_window.WindowConfig.load_texture_2d(
                    wnd,
                    path=rock_texture_path,
                    mipmap=True,
                    anisotropy=samples)

                tex1.use(location=1)
                tex2.use(location=2)

                SHADOW_SIZE: typing.Final[int] = 2 << 7
                
                shadow_size = (SHADOW_SIZE,
                               SHADOW_SIZE,)

                send_additional_data.send({"loading_progress":80})

                tex_depth = ctx.depth_texture(shadow_size)

                sampler_depth = ctx.sampler(
                    filter=(moderngl.LINEAR,
                                moderngl.LINEAR),
                    compare_func=">=",
                    repeat_x=False,
                    repeat_y=False,)

                z = 1000
                size = (z, z)

                CloudData = weather_utils.compute_weather.compute_cloud_noise(
                    size)

                height_range = numpy.max(
                    CloudData) - numpy.min(CloudData)

                CloudsProgram["CloudHeight"] = 500.0
                CloudsProgram["height_max"] = height_range
                CloudsProgram["render_fog"] = Registry.render_fog

                shadowmap["render_fog"] = Registry.render_fog

                vertices, index = weather_utils.compute_weather.compute_cloud_model(size[0])

                vbo = ctx.buffer(vertices.astype("f4"))
                ibo = ctx.buffer(index.astype("i4"))

                cloud_vao_content = [(
                    vbo,
                    "2f",
                    "in_vert"), ]

                vao = ctx.vertex_array(
                    CloudsProgram,
                    cloud_vao_content,
                    ibo)

                cloud_noise_path = Registry.base_folder / "resources" / "game engine resources" / "clouds" / "Rnd_noise.png"

                cloud_texture = moderngl_window.WindowConfig.load_texture_2d(
                    wnd,
                    path=cloud_noise_path,
                    anisotropy=samples)

                send_additional_data.send({"loading_progress":90})

                Onstart = True

                frametime = 1

                inventory = False
                Map = False

                Time_Percent = 0

                total_move_x = 0
                total_move_y = 0
                total_move_z = 0

                timer = 0

                play_time = 0

                WeatherDelta = 1
                DefaultSkyCol = 1.0

                (LengthenStorm,
                    CloudHeightMultiplier,
                    skysphere_prog_Transparency) = weather_utils.compute_weather.compute_weather(
                        color,
                        shadowmap,
                        CloudsProgram,
                        skysphere_prog,
                        Time_Percent)

                weather_change = True

                WeatherTime = 0
                Thundertimer = 0
                Lightningtimer = 0
                show_strobe_effects = False

                Thundertimer_Target = random.randint(
                    15, 30)

                switchWeather = random.randint(60, 120)

                Flashtimer = 0
                ShowFlash = False
                LengthenStorm = False
                PreviousWeather = Registry.weather

                target = numpy.array((0, 0, 0), dtype="f4")

                up = numpy.array((0, 0, 1), dtype="f4")

                camera_up = numpy.array((0, 1, 0), dtype="f4")

                scene_pos = numpy.array((0, -5, -32), dtype="f4")

                scene_translation = pyrr.Matrix44.from_translation(
                    (0.0, 0.0, 0.0),
                    dtype="f4")

                bias_matrix = (
                    pyrr.Matrix44.from_translation(
                        (0.5, 0.5, 0.5),
                        dtype="f4")
                    *
                    pyrr.Matrix44.from_scale(
                        (0.5, 0.5, 0.5),
                        dtype="f4")
                )

                orthogonal_perspective = pyrr.matrix44.create_orthogonal_projection(
                    -aspect_ratio, aspect_ratio,
                    -1, 1,
                    -1, 100,
                    dtype='f4',)

                Previous_Fog_Distance_Min = shadowmap["w_min"].value
                Previous_Fog_Distance_Max = shadowmap["w_max"].value

                Previous_color = color.value[0]

                Previous_CloudsProgram_Alpha = CloudsProgram["WeatherAlpha"].value
                Previous_CloudsProgram_CloudColor = CloudsProgram["CloudColor"].value

                Previous_multiplier = CloudsProgram["CloudHeightMultiplier"].value

                Previous_prog_transparency = skysphere_prog["transparency"].value

                if Registry.music:
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()

                send_additional_data.send({"loading_progress":100})

                camera_enabled = True

                Registry.display.set_alpha(False)

                jump = False
                start_jumping = False
                collision = False
                increased_speed = False
                modifier = 20
                increase_speed = False
                base_camera_velocity = camera.velocity

                if Registry.compile_math:
                    projection = math_utils.compiled_math_functions.perspective_fov(
                        70,
                        aspect_ratio,
                        1,
                        skybox_distance)

                else:
                    projection = math_utils.math_functions.perspective_fov(
                        70,
                        aspect_ratio,
                        1,
                        skybox_distance)

                camera.set_position(*Registry.position)
                camera.set_rotation(*Registry.rotation)
                    
                game_starts_running = time.perf_counter()
                
                auto_save_counter = time.perf_counter()
                        
                while True:
                    # 250 is base fps w/ shadowmapping
                    # 205 is avg w/ shadowmapping + dynamic skybox

                    matrix, position = camera_utils.compute_camera.get_camera_values(
                        camera,
                        camera_up)

                    if inventory or Map:
                        inventory, Map = menu_utils.access_other_guis.access_gui(
                            inventory,
                            Map,
                            start_inventory,
                            start_map,
                            camera)
                        
                    ctx.clear(DefaultSkyCol,
                                DefaultSkyCol,
                                DefaultSkyCol)
                    
                    dx, dy = pygame.mouse.get_rel()

                    if camera_enabled:
                        camera.rot_state(
                            -dx,
                            -dy)

                    Registry.real_window_width = pygame.display.get_window_size()[0]
                    Registry.real_window_height = pygame.display.get_window_size()[1]

                    aspect_ratio = Registry.real_window_width / Registry.real_window_height

                    for event in pygame.event.get():
                        if (event.type == pygame.QUIT or
                                (event.type == pygame.KEYDOWN and
                                    event.key == Registry.input_key[
                                        Registry.input_configuration["keyboard"]["Back"]][0])):

                            pygame.event.set_grab(False)
                            pygame.mouse.set_visible(True)
                            inventory_process.terminate()
                            map_process.terminate()

                            return

                        if event.type == pygame.KEYDOWN:
                            if event.key == Registry.input_key[
                                    Registry.input_configuration["keyboard"]["Walk forwards"]][0]:
                                
                                camera_utils.compute_camera.camera_move_state(
                                    camera,
                                    Registry.FORWARD,
                                    True)
                                
                            if event.key == Registry.input_key[
                                    Registry.input_configuration["keyboard"]["Walk backwards"]][0]:
                                
                                camera_utils.compute_camera.camera_move_state(
                                    camera,
                                    Registry.BACKWARD,
                                    True)
                                
                            if event.key == Registry.input_key[
                                    Registry.input_configuration["keyboard"]["Walk left"]][0]:
                                
                                camera_utils.compute_camera.camera_move_state(
                                    camera,
                                    Registry.LEFT,
                                    True)
                                
                            if event.key == Registry.input_key[
                                    Registry.input_configuration["keyboard"]["Walk right"]][0]:
                                
                                camera_utils.compute_camera.camera_move_state(
                                    camera,
                                    Registry.RIGHT,
                                    True)
                            
                            if event.key == Registry.input_key[
                                    Registry.input_configuration["keyboard"]["Unlock mouse"]][0]:
                                
                                pygame.event.set_grab(not pygame.event.get_grab())
                                pygame.mouse.set_visible(not pygame.event.get_grab())

                                camera_enabled = not camera_enabled

                            if event.key == Registry.input_key[
                                    Registry.input_configuration["keyboard"]["Toggle full-screen"]][0]:
                                
                                Registry.data_average_fps = []
                                Registry.data_CPU_usage = []
                                Registry.data_current_fps = []
                                Registry.data_memory_usage = []

                                Registry.timer = 0

                                Registry.data_average_fps_Max = 1
                                Registry.data_CPU_usage_Max = 1
                                Registry.data_current_fps_Max = 1
                                Registry.data_memory_usage_Max = 1

                                if Registry.dont_use_set_resolution is False:
                                    fullscreen_x = pyautogui.size()[0]
                                    fullscreen_y = pyautogui.size()[1]
                                    
                                else:
                                    formatted_resolution = Registry.resolution.split(",")
                                    fullscreen_x = int(formatted_resolution[0][1:])
                                    fullscreen_y = int(formatted_resolution[1][1:-1])
                                
                                display_utils.display_utils.update_display(
                                        fullscreen_x,
                                        fullscreen_y,
                                        opengl=True)

                                ctx.viewport = (0, 0, *pygame.display.get_window_size())

                            if (event.key == Registry.input_key[
                                    Registry.input_configuration["keyboard"]["Jump"]][0] and
                                    jump is False):
                                
                                start_jumping = True

                            if (event.key == Registry.input_key[
                                    Registry.input_configuration["keyboard"]["Skip time"]][0] and
                                    Registry.skip_time):
                                
                                timer += 30
                                Registry.game_time += 30
                                WeatherTime += 30

                            if (event.key == Registry.input_key[
                                    Registry.input_configuration["keyboard"]["List variables"]][0] and
                                    Registry.extended_developer_options):

                                tkinter_utils.tkinter_info.create_tkinter_window()

                            if (event.key == Registry.input_key[
                                    Registry.input_configuration["keyboard"]["Increase speed"]][0] and
                                    Registry.increased_speed):
                                
                                increase_speed = True

                            if event.key == Registry.input_key[
                                    Registry.input_configuration["keyboard"]["Open inventory"]][0]:
                                
                                inventory = True

                            if event.key == Registry.input_key[
                                    Registry.input_configuration["keyboard"]["Open map"]][0]:
                                
                                Map = True

                        elif event.type == pygame.KEYUP:
                            if event.key == Registry.input_key[
                                    Registry.input_configuration["keyboard"]["Walk forwards"]][0]:
                                
                                camera_utils.compute_camera.camera_move_state(
                                    camera,
                                    Registry.FORWARD,
                                    False)
                                
                            if event.key == Registry.input_key[
                                    Registry.input_configuration["keyboard"]["Walk backwards"]][0]:
                                
                                camera_utils.compute_camera.camera_move_state(
                                    camera,
                                    Registry.BACKWARD,
                                    False)
                                
                            if event.key == Registry.input_key[
                                    Registry.input_configuration["keyboard"]["Walk left"]][0]:
                                
                                camera_utils.compute_camera.camera_move_state(
                                    camera,
                                    Registry.LEFT,
                                    False)
                                
                            if event.key == Registry.input_key[
                                    Registry.input_configuration["keyboard"]["Walk right"]][0]:
                                
                                camera_utils.compute_camera.camera_move_state(
                                    camera,
                                    Registry.RIGHT,
                                    False)

                            if event.key == Registry.input_key[
                                    Registry.input_configuration["keyboard"]["Jump"]][0]:
                                
                                start_jumping = False

                            if event.key == Registry.input_key[
                                    Registry.input_configuration["keyboard"]["Increase speed"]][0]:
                                
                                increase_speed = False

                    if increase_speed:
                        camera.velocity = base_camera_velocity * modifier

                    else:
                        camera.velocity = base_camera_velocity

                    if start_jumping and jump is False:
                        jump = True
                        jump_timer = time.perf_counter()
                        jump_starting_y_pos = camera.position.y

                    if jump:
                        current_time = time.perf_counter()
                        delta = current_time - jump_timer
                        offset = delta*180
                        offset_radians = math.radians(offset)

                        if increased_speed:
                            calculation = jump_starting_y_pos + (math.sin(
                                offset_radians) / (2 / modifier))

                        else:
                            calculation = jump_starting_y_pos + (math.sin(
                                offset_radians) / 2)

                        camera.position.y = calculation
                        if delta > 1:
                            jump = False
                            if collision == False:
                                camera.position.y = jump_starting_y_pos

                    if WeatherTime >= switchWeather:
                        switchWeather = random.randint(
                            60, 120)
                        WeatherTime = 0
                        WeatherDelta += 1
                        weather_change = True

                        Previous_Fog_Distance_Min = shadowmap["w_min"].value
                        Previous_Fog_Distance_Max = shadowmap["w_max"].value

                        Previous_color = color.value[0]

                        Previous_CloudsProgram_Alpha = CloudsProgram["WeatherAlpha"].value
                        Previous_CloudsProgram_CloudColor = CloudsProgram["CloudColor"].value

                        Previous_multiplier = CloudsProgram["CloudHeightMultiplier"].value

                        Previous_prog_transparency = skysphere_prog["transparency"].value

                        (LengthenStorm,
                            CloudHeightMultiplier,
                            skysphere_prog_Transparency) = weather_utils.compute_weather.compute_weather(
                            color,
                            shadowmap,
                            CloudsProgram,
                            skysphere_prog,
                            Time_Percent)

                    if weather_change and Onstart is False:
                        weather_change = False
                        if Registry.weather != "sunny":
                            pygame.mixer.Channel(4).unpause()
                            if Registry.weather == "rain.light":
                                RandomiseVolumeReduction = random.randint(
                                    2, 5)

                                pygame.mixer.Channel(2).set_volume(
                                    (Registry.sound_volume/100)/RandomiseVolumeReduction)

                                pygame.mixer.Channel(4).set_volume(
                                    (((Registry.sound_volume/100)*10)/100))

                            else:
                                pygame.mixer.Channel(2).pause()
                                if Registry.weather == "rain.heavy.thundery":
                                    pygame.mixer.Channel(4).set_volume(
                                        (((Registry.sound_volume/100)*30)/100)
                                    )

                                else:
                                    pygame.mixer.Channel(4).set_volume(
                                        (((Registry.sound_volume/100)*20)/200)
                                    )

                        else:
                            pygame.mixer.Channel(4).pause()
                            pygame.mixer.Channel(2).set_volume(
                                Registry.sound_volume/100)

                            pygame.mixer.Channel(2).unpause()

                    Registry.current_fps = Registry.clock.get_fps()
                    Registry.average_fps += Registry.current_fps
                    Registry.iteration += 1
                    
                    if Registry.detailed_captions:
                        caption_utils.generate_captions.set_OpenGL_caption(
                            play_time,
                            Time_Percent,
                            total_move_x,
                            total_move_y,
                            total_move_z,
                            camera)

                    total_move_x = 0
                    total_move_y = 0
                    total_move_z = 0

                    try:
                        if (pygame.mixer.Channel(2).get_busy() is False and
                                Registry.sound and
                                Onstart is False):

                            sound_utils.play_sound.play_ambient_sound()

                    except Exception as Message:
                        error_message = "".join(("GameEngine > GameEngine ",
                                                      f"> __init__: {str(Message)}"))

                        error_message_detailed = "".join(
                            traceback.format_exception(
                                None,
                                Message,
                                Message.__traceback__))

                        error_utils.generate_error_screen.error_screen(
                            error_message,
                            error_message_detailed)

                    try:
                        if (pygame.mixer.Channel(4).get_busy() is False and
                                Registry.sound and
                                Registry.weather != "sunny" and
                                Onstart is False):

                            sound_utils.play_sound.play_rain_sound()

                    except Exception as Message:
                        error_message = "".join(("GameEngine > GameEngine ",
                                                      f"> __init__: {str(Message)}"))

                        error_message_detailed = "".join(
                            traceback.format_exception(
                                None,
                                Message,
                                Message.__traceback__))

                        error_utils.generate_error_screen.error_screen(
                            error_message,
                            error_message_detailed)

                    Time_Percent = ((100/1056)*(Registry.game_time))

                    (sun_lightpos,
                        moon_lightpos) = shadow_mapping_utils.shadowmapping_mathematics.compute_celestial_entities(
                        skybox_distance,
                        sun_radius,
                        sun_prog,
                        moon_prog,
                        scene_pos,
                        projection,
                        matrix,
                        position)  # slow

                    ctx.enable(
                        moderngl.DEPTH_TEST |
                        moderngl.CULL_FACE)

                    shadow_mapping_utils.shadowmapping_mathematics.compute_shadows(
                        mvp,
                        light,
                        sun_lightpos,
                        aspect_ratio,
                        mvp_depth,
                        mvp_shadow,
                        bias_matrix,
                        projection,
                        matrix,
                        target,
                        up)  # slowest

                    # --- PASS 2: Render scene to screen
                    cam = matrix
                    x = int(position.x*100)/100
                    y = int(position.y*100)/100
                    z = int(position.z*100)/100
                    cam[3][0] = 0
                    cam[3][1] = 0
                    cam[3][2] = 0
                    skysphere_prog["m_proj"].write(
                        projection)
                    skysphere_prog["m_model"].write(scene_translation)
                    skysphere_prog["m_camera"].write(cam)

                    particles_screen["projection"].write(
                        orthogonal_perspective)

                    if Time_Percent < 40:  # Registry.day
                        skysphere_prog["time"].value = 0
                        DefaultSkyCol = 1.0

                    elif Time_Percent < 50:  # sunset
                        DefaultSkyCol = 1 - \
                            ((0.7/10)*(Time_Percent-40))
                        skysphere_prog["time"].value = (
                            (19/10)*(Time_Percent-40))+1

                    elif Time_Percent < 90:  # night
                        skysphere_prog["time"].value = 21
                        DefaultSkyCol = 0.3

                    else:  # sunrise
                        DefaultSkyCol = 1 - \
                            ((0.7/10)*(100-Time_Percent))
                        skysphere_prog["time"].value = 21 - \
                            (((21/10)*(Time_Percent-90)))

                    CloudsProgram["DefaultSkyCol"] = DefaultSkyCol

                    ctx.front_face = "cw"

                    weather_utils.compute_weather.blend_weather(
                        PreviousWeather,
                        WeatherTime,
                        shadowmap,
                        Previous_Fog_Distance_Min,
                        Previous_Fog_Distance_Max,
                        Previous_color,
                        color,
                        CloudsProgram,
                        Previous_CloudsProgram_Alpha,
                        Previous_CloudsProgram_CloudColor,
                        Previous_multiplier,
                        CloudHeightMultiplier,
                        skysphere_prog,
                        Previous_prog_transparency,
                        skysphere_prog_Transparency)

                    if Thundertimer > Thundertimer_Target and Onstart is False:
                        Thundertimer_Target = random.randint(
                            5, 30)
                        Thundertimer = 0
                        Flashtimer = 0
                        Lightningtimer = 0

                        if show_strobe_effects:
                            color.value = (1.0, 1.0, 1.0)

                        show_strobe_effects = True
                        ShowFlash = True
                        if Registry.sound:
                            sound_utils.play_sound.play_thunder_sound()

                    if Registry.weather == "rain.heavy.thundery":
                        LightningDelay = random.randint(
                            30, 75)/100

                        if (Lightningtimer > LightningDelay and
                                show_strobe_effects):

                            Flashtimer = 0
                            DefaultSkyCol = 1
                            Lightningtimer = 0
                            show_strobe_effects = False
                            ShowFlash = True

                    if ShowFlash:
                        if Flashtimer <= 1/60:
                            DefaultSkyCol = 1
                            if show_strobe_effects:
                                color.value = (1.0, 1.0, 1.0)
                        else:
                            ShowFlash = False

                    if Registry.weather != "sunny":
                        ctx.enable(moderngl.BLEND)

                    SkyBox_texture_Sun.use(location=0)
                    SkySphere.render(skysphere_prog)

                    if Registry.weather != "sunny":
                        ctx.disable(moderngl.BLEND)

                    ctx.front_face = "ccw"

                    # pass 5: Render the sun position
                    moon.render(moon_prog)
                    sun.render(sun_prog)

                    ctx.front_face = "cw"

                    if Registry.weather != "sunny":
                        particles_transform["ft"].value = frametime

                        active_particles = particle_utils.particles.emit_gpu(
                            query,
                            transform_vao1,
                            vbo2,
                            N,
                            emit_buffer_elements,
                            max_emit_count,
                            gpu_emitter_particles,
                            timer,
                            gpu_emitter_vao,
                            stride,
                            render_vao2,
                            active_particles)

                    CloudPos = pyrr.Vector3(
                        (position.x,
                            0,
                            position.z),
                        dtype="f4")

                    CloudsProgram["m_proj"].write(
                        projection)

                    CloudsProgram["m_camera"].write(matrix)

                    CloudsProgram["m_model"].write(
                        pyrr.Matrix44.from_translation(
                            CloudPos,
                            dtype="f4"))

                    # shadows, variable rendering maybe
                    CloudsProgram["X_Offset"] = math.sin(
                        timer/50)/10
                    CloudsProgram["Y_Offset"] = math.cos(
                        timer/50)/10

                    cloud_texture.use(location=0)

                    ctx.enable(moderngl.BLEND)

                    vao.render(
                        mode=moderngl.TRIANGLE_STRIP)

                    ctx.blend_func = moderngl.DEFAULT_BLENDING

                    # pass 2: render the scene and retro project depth shadow-map
                    # counter clock wise -> render front faces

                    sampler_depth.use(location=0)
                    tex_depth.use(location=0)
                    cloud_texture.use(location=0)

                    ctx.front_face = "ccw"

                    # pass 4: render textured scene with shadow

                    objects["map"].render()
                    ctx.disable(moderngl.BLEND)

                    if (Registry.weather == "rain.heavy.thundery" and
                            LengthenStorm and
                            weather_change):
                        
                        switchWeather = switchWeather * (random.randint(
                            15,
                            30)/10)
                        LengthenStorm = False

                    if Onstart:
                        Onstart = False

                        pygame.event.set_grab(True)
                        pygame.mouse.set_visible(False)

                        GameEngine_Initialisation = False

                        Currentload_time = time.perf_counter()-startLoading
                        Registry.load_time = [
                            Registry.load_time[0] + Currentload_time,
                            Registry.load_time[1] + 1]

                        start_loading.clear()

                    # Swap around objects for next frame
                    pygame.display.flip()

                    target_fps = display_utils.display_utils.get_play_status()
                        
                    Registry.clock.tick(target_fps)
                    
                    if time.perf_counter()-auto_save_counter >= Registry.auto_save_frequency:
                        auto_save_counter = time.perf_counter()
                        
                        logging_utils.create_log_message.update_log_information(
                            "Creating Auto-Save")

                    if Registry.weather != "sunny":
                        transform_vao1, transform_vao2 = transform_vao2, transform_vao1
                        render_vao1, render_vao2 = render_vao2, render_vao1
                        vbo1, vbo2 = vbo2, vbo1

                    frametime = Registry.clock.get_time() / 1000
                    timer = time.perf_counter() - game_starts_running
                    Registry.game_time += frametime
                    WeatherTime += frametime

                    if Registry.weather == "rain.heavy.thundery":
                        if pygame.mixer.Channel(3).get_busy() is False:
                            Thundertimer += frametime

                        Lightningtimer += frametime
                        Flashtimer += frametime

                    play_time = timer

            except Exception as Message:
                error_message = (
                    f"pygame_game > create_game_engine > game_engine: {str(Message)}")

                error_message_detailed = "".join(
                    traceback.format_exception(
                        None,
                        Message,
                        Message.__traceback__))

                error_utils.generate_error_screen.error_screen(
                    error_message,
                    error_message_detailed)

else:
    print("You need to run this as part of Pycraft")
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror(
        "startup Fail",
        "You need to run this as part of Pycraft, please run the 'main.py' file")

    quit()
