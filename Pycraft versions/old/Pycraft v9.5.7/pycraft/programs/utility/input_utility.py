if __name__ != "__main__":
    try:
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
            
    class identify_patterns:
        def __init__(self):
            pass

        def identify_hex(string_pattern):
            formatted_string = string_pattern.lstrip('#')
            try:
                return tuple(int(formatted_string[i:i+2], 16) for i in (0, 2, 4))
            except Exception:
                return False

        def identify_text(string_pattern, comparison_dict):
            for key in comparison_dict:
                if str(key.lower()) in str(string_pattern.lower()):
                    return comparison_dict[key]

            return False

        def identify_rgb(string_pattern):
            data = ""
            try:
                for i in range(len(string_pattern)):
                    if str(string_pattern[i]) in "0123456789, _-#":
                        data += str(string_pattern[i])

                split_data = data.split(",")
                if len(split_data) == 3:
                    final_array = []
                    for k in range(len(split_data)):
                        value = int(split_data[k])
                        if value >= 0 and value <= 255:
                            final_array.append(value)
                        else:
                            raise ValueError
                                    
                else:
                    split_data = data.split()
                    if len(split_data) == 3:
                        final_array = []
                        for k in range(len(split_data)):
                            value = int(split_data[k])
                            if value >= 0 and value <= 255:
                                final_array.append(value)
                            else:
                                raise ValueError

                return final_array
            except:
                return False

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
