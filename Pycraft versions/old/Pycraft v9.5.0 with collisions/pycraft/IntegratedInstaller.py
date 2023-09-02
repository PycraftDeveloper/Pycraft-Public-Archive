if not __name__ == "__main__":
    print("Started <Pycraft_IntegratedInstaller>")
    class IntegInstaller:
        def __init__(self):
            pass

        def CheckVersions(self):
            if (not self.mod_urllib_request_ == None) and self.ConnectionPermission == True and self.ConnectionStatus == True:
                List = self.mod_Subprocess__.check_output([self.mod_Sys__.executable, "-m","pip","list","--outdated"], False)

                for i in range(len(List)):
                    if List[i:i+14] == b"Python-Pycraft":
                        self.Outdated = True
                        self.TotalNumUpdate += 1
                    if List[i:i+6] == b"pygame":
                        self.Outdated = True
                        self.TotalNumUpdate += 1
                    if List[i:i+6] == b"Pillow":
                        self.Outdated = True
                        self.TotalNumUpdate += 1
                    if List[i:i+5] == b"numpy":
                        self.Outdated = True
                        self.TotalNumUpdate += 1
                    if List[i:i+8] == b"moderngl":
                        self.Outdated = True
                        self.TotalNumUpdate += 1
                    if List[i:i+15] == b"moderngl-window":
                        self.Outdated = True
                        self.TotalNumUpdate += 1
                    if List[i:i+9] == b"PyAutoGUI":
                        self.Outdated = True
                        self.TotalNumUpdate += 1
                    if List[i:i+6] == b"psutil":
                        self.Outdated = True
                        self.TotalNumUpdate += 1
                    if List[i:i+10] == b"py-cpuinfo":
                        self.Outdated = True
                        self.TotalNumUpdate += 1
                    if List[i:i+6] == b"GPUtil":
                        self.Outdated = True
                        self.TotalNumUpdate += 1
                    if List[i:i+8] == b"tabulate":
                        self.Outdated = True
                        self.TotalNumUpdate += 1
                    if List[i:i+4] == b"pyrr":
                        self.Outdated = True
                        self.TotalNumUpdate += 1
                    
                        
    class CheckConnection:
        def __init__(self):
            pass
        
        def test(self):
            try:
                self.mod_urllib_request_.urlopen('https://www.google.com')
                return True
            except Exception as Error:
                return False
                
else:
    print("You need to run this as part of Pycraft")
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")
    quit()