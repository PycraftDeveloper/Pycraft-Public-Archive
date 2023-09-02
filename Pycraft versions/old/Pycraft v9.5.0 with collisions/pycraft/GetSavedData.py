if not __name__ == "__main__":
    print("Started <Pycraft_GetSavedData>")
    class LoadSaveFiles:
        def __init__(self):
            pass
                        
        def ReadMainSave(self):
            with open(self.mod_OS__.path.join(self.base_folder, ("Data_Files\\SaveGameConfig.json")), 'r') as openfile:
                save = self.mod_JSON__.load(openfile)
        
            self.theme = save["theme"]
            self.RunFullStartup = save["startup"]
            self.crash = save["crash"]
            self.Fullscreen = save["WindowStatus"]
            self.RecommendedFPS = save["AdaptiveFPS"]
            self.Devmode = save["Devmode"]
            self.SettingsPreference = save["profile"]
            self.FPS = save["FPS"]
            self.aFPS = save["aFPS"]
            self.Iteration = save["Iteration"]
            self.FOV = save["FOV"]
            self.cameraANGspeed = save["cameraANGspeed"]
            self.RenderFOG = save["RenderFOG"]
            self.aa = save["aa"]
            self.X = save["X"]
            self.Y = save["Y"]
            self.Z = save["Z"]
            self.FanSky = save["FanSky"]
            self.FanPart = save["FanPart"]
            self.sound = save["sound"]
            self.soundVOL = save["soundVOL"]
            self.music = save["music"]
            self.musicVOL = save["musicVOL"]
            self.lastRun = save["lastRun"]
            self.SavedWidth = save["DisplayWidth"]
            self.SavedHeight = save["DisplayHeight"]
            self.ConnectionPermission = save["ConnectionPermission"]
            self.Total_Vertices = save["Total_Vertices"]
            if self.Total_Vertices == 0:
                self.Total_Vertices = 1

        def RepairLostSave(self):
            try:
                SavedData = {"Total_Vertices":0, "theme":False, "profile":"Medium", "Devmode":0, "AdaptiveFPS": 60, "FPS":60, "aFPS":60, "Iteration":1, "FOV":75, "cameraANGspeed":3, "aa":True, "RenderFOG":True, "FanSky":True, "FanPart":True, "sound":True, "soundVOL":75, "music":True, "musicVOL":50, "X":0, "Y":0, "Z":0, "lastRun":"29/09/2021", 'startup':True, 'crash': False, 'DisplayWidth':1280, 'DisplayHeight':720, 'WindowStatus':True, 'ConnectionPermission': None}
                with open(self.mod_OS__.path.join(self.base_folder, ("Data_Files\\SaveGameConfig.json")), 'w') as openfile:
                    self.mod_JSON__.dump(SavedData, openfile)
            except Exception as Message:
                return Message
            else:
                return None

        def SaveTOconfigFILE(self):
            try:
                current_time = self.mod_Datetime__.datetime.now()
                currentDate = f"{current_time.day}/{current_time.month}/{current_time.year}"
                SavedData = {"Total_Vertices":self.Total_Vertices, "theme":self.theme, "profile":self.SettingsPreference, "Devmode":self.Devmode, "AdaptiveFPS": self.RecommendedFPS, "FPS":self.FPS, "aFPS":self.aFPS, "Iteration":self.Iteration, "FOV":self.FOV, "cameraANGspeed":self.cameraANGspeed, "aa":self.aa, "RenderFOG":self.RenderFOG, "FanSky":self.FanSky, "FanPart":self.FanPart, "sound":self.sound, "soundVOL":self.soundVOL, "music":self.music, "musicVOL":self.musicVOL, "X":self.X, "Y":self.Y, "Z":self.Z, "lastRun":currentDate, 'startup':self.RunFullStartup, 'crash': False, 'DisplayWidth':self.SavedWidth, 'DisplayHeight':self.SavedHeight, 'WindowStatus':self.Fullscreen, "ConnectionPermission": self.ConnectionPermission}
                with open(self.mod_OS__.path.join(self.base_folder, ("Data_Files\\SaveGameConfig.json")), 'w') as openfile:
                    self.mod_JSON__.dump(SavedData, openfile)
            except Exception as Message:
                return Message
            else:
                return None
else:
    print("You need to run this as part of Pycraft")
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")
    quit()