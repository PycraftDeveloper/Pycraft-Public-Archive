if not __name__ == "__main__":
    print("Started <Pycraft_TkinterUtils>")
    class TkinterInfo:
        def __init__(self):
            pass
        
        def GetPermissions(self):
            import tkinter as tk
            from tkinter import messagebox
            root = tk.Tk()
            root.withdraw()
            answer = messagebox.askquestion("Check Permission", "Can we have your permission to check the internet for updates to Pycraft?")
            if answer == "yes":
                self.ConnectionPermission = True
            else:
                self.ConnectionPermission = False

        def CreateTkinterWindow(self):
            DataWindow = self.mod_Tkinter__tk.Tk()
            DataWindow.title("Player Information")
            DataWindow.configure(width = 500, height = 300) 
            DataWindow.configure(bg="lightblue") 
            VersionData = f"Pycraft: v{self.version}"
            CoordinatesData = f"Coordinates: x: {self.X} y: {self.Y} z: {self.Z} Facing: 0.0, 0.0, 0.0" 
            FPSData = f"FPS: Actual: {self.eFPS} Max: {self.FPS}" 
            VersionData = self.mod_Tkinter__tk.Label(DataWindow, text=VersionData) 
            CoordinatesData = self.mod_Tkinter__tk.Label(DataWindow, text=CoordinatesData) 
            FPSData = self.mod_Tkinter__tk.Label(DataWindow, text=FPSData) 
            VersionData.grid(row = 0, column = 0, columnspan = 2) 
            CoordinatesData.grid(row = 1, column = 0, columnspan = 2)
            FPSData.grid(row = 2, column = 0, columnspan = 2)
            DataWindow.mainloop() 
            DataWindow.quit()
else:
    print("You need to run this as part of Pycraft")
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")
    quit()