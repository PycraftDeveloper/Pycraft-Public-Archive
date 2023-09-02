if __name__ != "__main__":
    try:
        import os
        import json

        import googletrans
        
        from registry_utils import Registry
        
        import logging_utils
        import integrated_installer_utils
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

    class translation_caching(Registry):
        def __init__(self):
            pass

        def write_cache():
            translated_cache_path = Registry.base_folder / "data files" / "translated_data.json"
            
            with open(
                    translated_cache_path,
                    "w") as file:

                json.dump(
                    Registry.translated_text,
                    file,
                    indent=1)

        def read_cache():
            translated_cache_path = Registry.base_folder / "data files" / "translated_data.json"
            
            with open(
                    translated_cache_path,
                    "r") as file:

                Registry.translated_text = json.load(file)

    class string_translator(Registry):
        def __init__(self):
            pass

        def change_language(string):
            if Registry.language != "en" and len(str(string).strip()) > 0:
                found = False
                try:
                    for key in Registry.translated_text:
                        if key == string:
                            found = True
                            translate = Registry.translated_text[key]
                except Exception as Message:
                    log_message = f"Dictionary of translated phrases is empty. More details: {Message}"
                    logging_utils.create_log_message.update_log_warning(
                        log_message)

                if found is False:
                    if Registry.connection_permission:
                        try:
                            translator = googletrans.Translator()
                            translate = str(translator.translate(
                                string,
                                dest=Registry.language).text)
                            
                        except Exception as message:
                            connection_status = integrated_installer_utils.check_connection.test()

                            if connection_status:
                                error_message = "".join(("translation_utils > string_translator > change_language: ",
                                                            "An error occurred whilst trying to translate ",
                                                            f"text ('{string}'). More details: {message}"))

                                raise Exception(error_message) from message

                            else:
                                log_message = f"translation_utils > string_translator > change_language: {str(message)}"

                                logging_utils.create_log_message.update_log_warning(
                                    log_message)
                                
                            translate = string

                    else:
                        translate = string
                                
                Registry.translated_text[string] = translate

                return translate
            
            else:
                return string

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
