if __name__ != "__main__":
    try:
        import os
        import json
        import traceback
        from tkinter import messagebox
        import datetime
        
        import send2trash

        from registry_utils import Registry
        import logging_utils
        import error_utils
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
            
    class delete_files(Registry):
        def clear_temporary_files():
            
            message = None
            for file in Registry.files_to_trash:
                try:
                    send2trash.send2trash(str(Registry.base_folder / file))
                except Exception as warning:
                    message = warning
            
            try:
                send2trash.send2trash(str(Registry.base_folder / "temporary"))
                os.mkdir(str(Registry.base_folder / "temporary"))
            except Exception as message:
                message = warning
                
            if message != None:
                log_message = "".join(("FileUtils > delete_files > ",
                                        "clear_temporary_files: Unable ",
                                        "to remove file as it likely ",
                                        "doesn't exist. More details:\n",
                                        f"{str(message)}"))

                logging_utils.create_log_message.update_log_warning(
                    log_message)

            else:
                logging_utils.create_log_message.update_log_information(
                    f"Cleared temporary files")
                
    class scan_folder(Registry):
        def search_files():
            
            logging_utils.create_log_message.update_log_information(
                f"Scanning {Registry.base_folder}")

            for key in Registry.file_structure:
                Registry.file_structure[key]["size"] = 0

            Registry.folder_size = 0
            trash_files_array = []
            for i in range(len(Registry.files_to_trash)):
                trash_files_array.append(Registry.base_folder / Registry.files_to_trash[i])
                
            files_array = []
            for dirpath, _, files in os.walk(Registry.base_folder):
                for name in files:
                    file_path = os.path.join(dirpath, name)
                    Registry.folder_size += os.path.getsize(file_path)
                    if str(Registry.base_folder / "temporary") not in dirpath:
                        files_array.append(file_path)
                    else:
                        Registry.file_structure["Temporary"]["size"] += os.path.getsize(file_path)

            for i in range(len(files_array)):
                if (".ogg" in files_array[i] or
                        ".wav" in files_array[i] or
                        ".mp3" in files_array[i]):
                    
                    Registry.file_structure["Audio"]["size"] += os.path.getsize(
                        files_array[i])

                elif ".ttf" in files_array[i]:
                    Registry.file_structure["Fonts"]["size"] += os.path.getsize(
                        files_array[i])

                elif (".txt" in files_array[i] or
                        ".json" in files_array[i] or
                        ".md" in files_array[i]):
                    
                    Registry.file_structure["Data files"]["size"] += os.path.getsize(
                        files_array[i])

                elif (".py" in files_array[i] or
                        ".glsl" in files_array[i]):
                    
                    Registry.file_structure["Source code"]["size"] += os.path.getsize(
                        files_array[i])

                elif (".obj" in files_array[i] or
                        ".mtl" in files_array[i]):
                    
                    Registry.file_structure["3D objects"]["size"] += os.path.getsize(
                        files_array[i])

                elif (".png" in files_array[i] or
                        ".jpg" in files_array[i] or
                        ".ico" in files_array[i] or
                        ".gif" in files_array[i]):
                    
                    Registry.file_structure["Images"]["size"] += os.path.getsize(
                        files_array[i])

                else:
                    logging_utils.create_log_message.update_log_information(
                        f"Not currently categorized: {files_array[i]}")

                    Registry.file_structure["Misc"]["size"] += os.path.getsize(
                        files_array[i])
                        
    class fix_installer(Registry):
        def set_install_location():
            repair = {"PATH": Registry.base_folder}

            installer_config_path = Registry.base_folder / "data files" / "installer_config.json"

            with open(
                    installer_config_path,
                    "w") as file:

                json.dump(
                    repair,
                    file)

        def get_install_location():
            installer_config_path = Registry.base_folder / "data files" / "installer_config.json"
            with open(
                    installer_config_path,
                    "r") as file:

                data = json.load(file)

            return data["PATH"]

    class pycraft_config_utils(Registry):
        def read_input_key():
            input_key_path = Registry.base_folder / "data files" / "input_key.json"
            
            with open(
                    input_key_path,
                    "r") as file:

                input_key = json.load(file)

            return input_key

        def read_main_save():
            pycraft_config_path = Registry.base_folder / "data files" / "pycraft_config.json"

            with open(
                    pycraft_config_path,
                    "r") as file:

                save = json.load(file)

            error_array = []
            for key in Registry.save_keys:
                try:
                    setattr(Registry, key, save[key])
                    
                except Exception as message_for_array:
                    setattr(Registry, key, Registry.save_keys[key])
                    error_array.append(str(message_for_array))
                    

            if len(error_array) > 0:
                Message = ""

                for error in error_array:
                    Message += error+"\n"
                    
                error_message = "".join(("FileUtils > pycraft_config_utils ",
                                            "> read_main_save: ",
                                            "Your some of your saved file ",
                                            "was missing, we have attempted ",
                                            "to recover missing data."))

                error_message_detailed = "".join(("FileUtils > pycraft_config_utils ",
                                                    "> ReamMainSave: ",
                                                    "Your some of your saved file ",
                                                    "was missing, we have attempted ",
                                                    "to recover missing data.\n",
                                                    "The following entries were ",
                                                    "missing and have been ",
                                                    f"reset:\n{Message}"))

                if Registry.detailed_error_messages:
                    logging_utils.create_log_message.update_log_warning(
                        error_message_detailed)
                    
                    messagebox.showerror(
                        "Some saved data was missing",
                        error_message_detailed)
                    
                else:
                    logging_utils.create_log_message.update_log_warning(
                        error_message)
                    
                    messagebox.showerror(
                        "Some saved data was missing",
                        error_message)

            if Registry.average_fps == float("inf"):
                logging_utils.create_log_message.update_log_warning(
                    "Reset average_fps from infinity")

                Registry.average_fps = 1
                Registry.iteration = 1

        def repair_lost_save():
            pycraft_config_path = Registry.base_folder / "data files" / "pycraft_config.json"
            
            with open(
                    pycraft_config_path,
                    "w") as file:

                json.dump(
                    Registry.save_keys,
                    file,
                    indent=1)

        def save_pycraft_config():
            try:
                if Registry.updated:
                    Registry.updated = False

                SavedData = {
                    "theme": Registry.theme,
                    "settings_preset": Registry.settings_preset,
                    "adaptive_fps": Registry.adaptive_fps,
                    "fps": Registry.fps,
                    "average_fps": round(Registry.average_fps, 3),
                    "iteration": Registry.iteration,
                    "FOV": Registry.FOV,
                    "camera_angle_speed": Registry.camera_angle_speed,
                    "aa": Registry.aa,
                    "render_fog": Registry.render_fog,
                    "fancy_graphics": Registry.fancy_graphics,
                    "fancy_particles": Registry.fancy_particles,
                    "sound": Registry.sound,
                    "sound_volume": Registry.sound_volume,
                    "music": Registry.music,
                    "music_volume": Registry.music_volume,
                    "x": round(Registry.x, 4),
                    "y": round(Registry.y, 4),
                    "z": round(Registry.z, 4),
                    "last_run": Registry.current_date,
                    "run_full_startup": Registry.run_full_startup,
                    "crash": False,
                    "saved_window_width": Registry.saved_window_width,
                    "saved_window_height": Registry.saved_window_height,
                    "fullscreen": Registry.fullscreen,
                    "connection_permission": Registry.connection_permission,
                    "updated": Registry.updated,
                    "load_time": [
                        round(Registry.load_time[0], 3),
                        round(Registry.load_time[1], 3)],
                    
                    "show_message": Registry.show_message,
                    "show_strobe_effects": Registry.show_strobe_effects,
                    "extended_developer_options": Registry.extended_developer_options,
                    "draw_devmode_graph": Registry.draw_devmode_graph,
                    "detailed_error_messages": Registry.detailed_error_messages,
                    "logging_dictionary": Registry.logging_dictionary,
                    "save_on_exit": Registry.save_on_exit,
                    "resolution_preset": Registry.resolution_preset,
                    "vsync": Registry.vsync,
                    "aa_quality": Registry.aa_quality,
                    "detailed_captions": Registry.detailed_captions,
                    "output_log": Registry.output_log,
                    "increased_speed": Registry.increased_speed,
                    "skip_time": Registry.skip_time,
                    "remove_file_permission": Registry.remove_file_permission,
                    "input_configuration": Registry.input_configuration,
                    "resolution": Registry.resolution,
                    "dont_use_set_resolution": Registry.dont_use_set_resolution,
                    "seasonal_events": Registry.seasonal_events,
                    "compile_math": Registry.compile_math,
                    "custom_theme": Registry.custom_theme,
                    "language": Registry.language,
                    "use_transparency_effects": Registry.use_transparency_effects,
                    "auto_save_frequency": Registry.auto_save_frequency,
                    # temp
                    "position": [0, 0, 0],
                    "rotation": [0, 0],
                    "game_time": 0,
                    "weather": "sunny",
                    "day": 1
                }

                pycraft_config_path = Registry.base_folder / "data files" / "pycraft_config.json"

                with open(
                        pycraft_config_path,
                        "w") as file:

                    json.dump(
                        SavedData,
                        file,
                        indent=1)
                        
            except Exception as Message:
                error_message = "FileUtils > pycraft_config_utils > SaveTOpycraft_configFILE: "+str(Message)

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
