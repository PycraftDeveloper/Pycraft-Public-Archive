if __name__ != "__main__":
    try:
        import os
        import random
            
        import pygame
        
        from registry_utils import Registry
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
            
    class play_sound(Registry):
        def __init__(self):
            pass

        def play_inventory_sound():
            audio_path = Registry.base_folder / "resources" / "general resources" / "inventoryGeneral.ogg"
            
            pygame.mixer.music.load(audio_path)

            pygame.mixer.music.set_volume(Registry.music_volume/100)
            pygame.mixer.music.play(loops=-1)

        def play_click_sound():
            channel0 = pygame.mixer.Channel(0)
            audio_path = Registry.base_folder / "resources" / "general resources" / "Click.ogg"
            
            clickMUSIC = pygame.mixer.Sound(audio_path)

            channel0.set_volume(Registry.sound_volume/100)
            channel0.play(clickMUSIC)
            pygame.time.wait(40)
                
        def play_footsteps_sound():
            channel1 = pygame.mixer.Channel(1)
            RandomNum = random.randint(0, 5)

            audio_path = Registry.base_folder / "resources" / "game engine resources" / "GameSounds" / "footstep" / f"footsteps{RandomNum}.wav"

            Footsteps = pygame.mixer.Sound(audio_path)

            channel1.set_volume(Registry.sound_volume/100)
            channel1.play(Footsteps)

        def play_ambient_sound():
            channel2 = pygame.mixer.Channel(2)
            audio_path = Registry.base_folder / "resources" / "game engine resources" / "GameSounds" / "FieldAmb.ogg"
            
            LoadAmb = pygame.mixer.Sound(audio_path)

            channel2.set_volume(Registry.sound_volume/100)
            channel2.play(LoadAmb)

        def play_thunder_sound():
            channel3 = pygame.mixer.Channel(3)
            RandomNum = random.randint(0, 10)

            audio_path = Registry.base_folder / "resources" / "game engine resources" / "GameSounds" / "thunder" / f"thunder{RandomNum}.ogg"

            Thunder = pygame.mixer.Sound(audio_path)

            channel3.set_volume(Registry.sound_volume/100)
            channel3.play(Thunder)

        def play_rain_sound():
            channel4 = pygame.mixer.Channel(4)
            audio_path = Registry.base_folder / "resources" / "game engine resources" / "GameSounds" / "rain.ogg"

            Rain = pygame.mixer.Sound(audio_path)

            channel4.set_volume(Registry.sound_volume/100)
            channel4.play(Rain)

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
