if __name__ != "__main__":
    try:
        import random
        import tkinter
        import re

        import pygame

        from registry_utils import Registry
        
        import translation_utils
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
            
    class installer_text(Registry):
        def __init__(self):
            pass

        def create_text(root, OUTPUTtext):
            text = tkinter.Text(
                root,
                wrap=tkinter.WORD,
                relief=tkinter.FLAT,
                font=(None, 10))

            text.insert(
                tkinter.INSERT,
                OUTPUTtext)

            text["state"] = tkinter.DISABLED
            text.place(x=200, y=80)
            root.update_idletasks()

    class text_formatter(Registry):
        def __init__(self):
            pass

        def format_text(
                string,
                position,
                font,
                backup_font,
                blit=True,
                underline=False,
                bold=False,
                italics=False,
                font_color=None):
            
            if font_color is None:
                font_color = Registry.font_color
            
            pygame.event.pump()
            
            font.set_underline(underline)
            font.set_bold(bold)
            font.set_italic(italics)
            
            position = [*position]

            broken_string = string.split(" ")
            color = font_color

            broken_string = re.split('(\W)', string)

            if (Registry.language == "ar" or
                    Registry.language == "hy" or
                    Registry.language == "zh-tw" or
                    Registry.language == "zh-cn" or
                    Registry.language == "ka" or
                    Registry.language == "el" or
                    Registry.language == "hi" or
                    Registry.language == "he" or
                    Registry.language == "iw" or
                    Registry.language == "ja" or
                    Registry.language == "kk" or
                    Registry.language == "km" or
                    Registry.language == "ko" or
                    Registry.language == "mn" or
                    Registry.language == "my" or
                    Registry.language == "ne" or
                    Registry.language == "ps" or
                    Registry.language == "ru" or
                    Registry.language == "ta" or
                    Registry.language == "th" or
                    Registry.language == "uk" or
                    Registry.language == "ur"):
                font = backup_font

            cleaned_string = ""
            for word in range(len(broken_string)):
                pos = 0
                for letter in range(len(broken_string[word])):
                    try:
                        if broken_string[word][pos] == "$":
                            if broken_string[word][pos+1] == "(":
                                while not broken_string[word][pos] == ")":
                                    print("Special character detected! Currently not implemented", broken_string[word][pos])
                                    pos += 1
                            else:
                                pos += 1
                            if broken_string[word][pos+1] == "*":
                                pos += 1
                            print("Special character detected! Currently not implemented")
                        else:
                            cleaned_string += broken_string[word][pos]

                        pos += 1
                    except:
                        break

                cleaned_string += ""

            translated_string = translation_utils.string_translator.change_language(
                cleaned_string)

            if str(position[0]).lower() == "left":
                position[0] = 0

            elif str(position[0]).lower() == "right":
                position[0] = pygame.display.get_window_size()[0]
                text = font.render(translated_string, Registry.aa, color)
                position[0] -= text.get_width()
                
            elif str(position[0]).lower() == "center":
                position[0] = 0
                text = font.render(translated_string, Registry.aa, color)
                width = text.get_width()
                position[0] = (pygame.display.get_window_size()[0] - width)/2

            if str(position[1]).lower() == "top":
                position[1] = 0

            elif str(position[1]).lower() == "bottom":
                position[1] = 0
                text = font.render(translated_string, Registry.aa, color)
                height = text.get_height()
                position[1] = pygame.display.get_window_size()[1] - height

            elif str(position[1]).lower() == "center":
                position[1] = 0
                text = font.render(translated_string, Registry.aa, color)
                height = text.get_height()
                position[1] = (pygame.display.get_window_size()[1] - height)/2

            returned_text = font.render(translated_string, Registry.aa, color)

            if blit:
                for word in range(len(translated_string)):
                    for letter in range(len(translated_string[word])):
                        font.set_underline(underline)
                        font.set_bold(bold)
                        font.set_italic(italics)
                        text = font.render(translated_string[word][letter], Registry.aa, color)
                        Registry.display.blit(text, position)
                        position[0] += text.get_width()

            return returned_text

    class generate_text(Registry):
        def __init__(self):
            pass

        def load_quick_text():
            LoadingText = ["Use W, A, S, D to move",
                            "Use W to move forward",
                            "Use S to move backward",
                            "Use A to move left",
                            "Use D to move right",
                            "Access your inventory with E",
                            "Access your map with R",
                            "Use SPACE to jump",
                            "Did you know there is a light mode?",
                            "Did you know there is a dark mode?",
                            "Check us out on GitHub",
                            "Use ESC to exit",
                            "Hold W for 3 seconds to sprint",
                            "Did you know you can change the sound volume in settings?",
                            "Did you know you can change the music volume in settings?",
                            "Did you know you can use L to lock the camera",
                            "Did you know the project now supports controllers?",
                            "Use L to free your cursor",
                            "Now with time",
                            "Did you know a full day and night cycle is 20 minutes long?",
                            "Use F11 to full-screen your game!",
                            "Now with less bugs",
                            "What is that lurking in those shadows?",
                            "Pycraft is now a shady place!",
                            "Now with animations!",
                            "Check us out on Twitter!",
                            f"This is Pycraft v{Registry.version}",
                            "Now with clouds!",
                            "Check us out on Twitter: @PycraftDev",
                            "Like and subscribe",
                            "Now with lightning",
                            "Lights, camera and... action!",
                            "Now in 3D!",
                            "Thanks for playing!",
                            "Multi-Dimensional!",
                            "Multi-Dimensional! (Oooh)",
                            "Easter Egg?",
                            "What's this for?",
                            "False by default!"]

            locat = random.randint(0, (len(LoadingText)-1))
            text = LoadingText[locat]
            return text

    class text_wrap(Registry):
        def __init__(self):
            pass

        def blit_text(
                text,
                pos,
                font,
                backup_font,
                text_width=None,
                font_color=None):
            
            if text_width is None:
                text_width = Registry.display.get_width()
            
            if font_color is None:
                font_color = Registry.font_color
            
            if (Registry.language == "ar" or
                    Registry.language == "hy" or
                    Registry.language == "zh-tw" or
                    Registry.language == "zh-cn" or
                    Registry.language == "ka" or
                    Registry.language == "el" or
                    Registry.language == "hi" or
                    Registry.language == "he" or
                    Registry.language == "iw" or
                    Registry.language == "ja" or
                    Registry.language == "kk" or
                    Registry.language == "km" or
                    Registry.language == "ko" or
                    Registry.language == "mn" or
                    Registry.language == "my" or
                    Registry.language == "ne" or
                    Registry.language == "ps" or
                    Registry.language == "ru" or
                    Registry.language == "ta" or
                    Registry.language == "th" or
                    Registry.language == "uk" or
                    Registry.language == "ur"):
                font = backup_font

            translated_string = translation_utils.string_translator.change_language(
                text)
                
            # 2D array where each row is a list of words.
            words = [word.split(" ") for word in translated_string.splitlines()]
            # The width of a space.
            space = font.size(" ")[0]
            x, y = pos
            TextHeight = 0
            for line in words:
                for word in line:
                    word_surface = font.render(
                        word,
                        Registry.aa,
                        font_color)

                    word_width, word_height = word_surface.get_size()
                    if x + word_width >= text_width:
                        TextHeight += word_height
                        # Reset the x.
                        x = pos[0]
                        # start on new row.
                        y += word_height

                    Registry.display.blit(
                        word_surface,
                        (x, y))

                    x += word_width + space

                TextHeight += word_height
                # Reset the x.
                x = pos[0]
                # start on new row.
                y += word_height
                
            return TextHeight

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
