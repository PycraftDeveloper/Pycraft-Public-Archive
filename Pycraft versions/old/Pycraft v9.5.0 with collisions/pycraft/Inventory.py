if not __name__ == "__main__":
    print("Started <Pycraft_Inventory>")
    class GenerateInventory:
        def __init__(self):
            pass

        def Inventory(self):
            try:
                Message = self.mod_DisplayUtils__.DisplayUtils.SetDisplay(self)
                self.Display.fill(self.BackgroundCol)
                self.mod_Pygame__.display.update()

                MainInventoryFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 60) 
                PycraftTitle = MainInventoryFont.render("Pycraft", self.aa, self.FontCol)
                TitleWidth = PycraftTitle.get_width()

                icon = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\Icon.jpg"))).convert()
                realWidth, realHeight = self.mod_Pygame__.display.get_window_size()
                AlphaSurface = self.mod_Pygame__.Surface((realWidth, realHeight), self.mod_Pygame__.HWSURFACE|self.mod_Pygame__.SRCALPHA)
                self.mod_Pygame__.display.set_icon(icon)
                AlphaSurface.set_alpha(204) 
                AlphaSurface.fill(self.BackgroundCol)

                Selector = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, (f"Resources\\General_Resources\\selectorICON{self.theme}.jpg"))).convert()
                SelectorWidth = Selector.get_width()

                hover1 = False 
                hover2 = False 
                hover3 = False 
                hover4 = False 
                hover5 = False 
                hover6 = False 
                hover7 = False
                hover8 = False
                mousebuttondown = False

                ButtonFont1 = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 30) 
                WeaponsText = ButtonFont1.render("Weapons", self.aa, self.FontCol)
                WeaponsTextWidth = WeaponsText.get_width()
                WeaponsTextHeight = WeaponsText.get_height()

                ButtonFont2 = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 30) 
                RangedWeaponsText = ButtonFont2.render("Ranged Weapons", self.aa, self.FontCol)
                RangedWeaponsTextWidth = RangedWeaponsText.get_width()
                RangedWeaponsTextHeight= RangedWeaponsText.get_height()

                ButtonFont3 = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 30) 
                ShieldsText = ButtonFont3.render("Shields", self.aa, self.FontCol)
                ShieldsTextWidth = ShieldsText.get_width()
                ShieldsTextHeight = ShieldsText.get_height()

                ButtonFont4 = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 30) 
                ArmourText = ButtonFont4.render("Armour", self.aa, self.FontCol)
                ArmourTextWidth = ArmourText.get_width()
                ArmourTextHeight = ArmourText.get_height()

                ButtonFont5 = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 30) 
                FoodText = ButtonFont5.render("Food", self.aa, self.FontCol)
                FoodTextWidth = FoodText.get_width()
                FoodTextHeight = FoodText.get_height()

                ButtonFont6 = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 30) 
                ItemsText = ButtonFont6.render("Items", self.aa, self.FontCol)
                ItemsTextWidth = ItemsText.get_width()
                ItemsTextHeight = ItemsText.get_height()

                ButtonFont7 = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 30) 
                SpecialItemsText = ButtonFont7.render("Special Items", self.aa, self.FontCol)
                SpecialItemsTextWidth = SpecialItemsText.get_width()
                SpecialItemsTextHeight = SpecialItemsText.get_height()

                ButtonFont8 = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 30) 
                OptionsText = ButtonFont7.render("Options", self.aa, self.FontCol)
                OptionsTextWidth = OptionsText.get_width()
                OptionsTextHeight = OptionsText.get_height()

                self.mod_Pygame__.display.set_caption(f"Pycraft: v{self.version}: Playing | Inventory")

                FullscreenX, FullscreenY = self.mod_Pyautogui__.size()

                while True:
                    realWidth, realHeight = self.mod_Pygame__.display.get_window_size()

                    if realWidth < 1280:
                        self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, 1280, self.SavedHeight)
                    if realHeight < 720:
                        self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, self.SavedWidth, 720)

                    yScaleFact = realHeight/720
                    xScaleFact = realWidth/1280

                    Mx, My = self.mod_Pygame__.mouse.get_pos() 
                    self.Display.fill(self.BackgroundCol)

                    if self.aa == True:
                        pilImage = self.mod_PIL_Image_.open(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\PauseIMG.png"))).resize((realWidth, realHeight), self.mod_PIL_Image_.ANTIALIAS)
                    else:
                        pilImage = self.mod_PIL_Image_.open(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\PauseIMG.png"))).resize((realWidth, realHeight))
                    
                    BLURRED_pilImage = pilImage.filter(self.mod_PIL_ImageFilter_.BoxBlur(4))

                    PauseImg = self.mod_ImageUtils__.ConvertImage.pilImageToSurface(self, BLURRED_pilImage)
                    self.Display.blit(PauseImg, (0, 0))
                    self.Display.blit(AlphaSurface, (0, 0))

                    self.Display.blit(PycraftTitle, ((realWidth-TitleWidth)/2, 0))

                    for event in self.mod_Pygame__.event.get():
                        if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and event.key == self.mod_Pygame__.K_ESCAPE) or (event.type == self.mod_Pygame__.KEYDOWN and event.key == self.mod_Pygame__.K_e):
                            self.Load3D = False
                            if self.sound == True:
                                self.mod_SoundUtils__.PlaySound.PlayClickSound(self)
                            return None
                        if event.type == self.mod_Pygame__.VIDEORESIZE:
                            realWidth, realHeight = self.mod_Pygame__.display.get_window_size()
                            AlphaSurface = self.mod_Pygame__.Surface((realWidth, realHeight), self.mod_Pygame__.HWSURFACE|self.mod_Pygame__.SRCALPHA)
                            AlphaSurface.set_alpha(204)
                            AlphaSurface.fill(self.BackgroundCol)
                        if event.type == self.mod_Pygame__.MOUSEBUTTONDOWN:
                            mousebuttondown = True 
                        if event.type == self.mod_Pygame__.MOUSEBUTTONUP:
                            mousebuttondown = False
                        if event.type == self.mod_Pygame__.KEYDOWN:
                            if event.key == self.mod_Pygame__.K_F11:
                                self.mod_DisplayUtils__.DisplayUtils.UpdateDisplay(self)
                                AlphaSurface = self.mod_Pygame__.Surface((FullscreenX, FullscreenY), self.mod_Pygame__.HWSURFACE|self.mod_Pygame__.SRCALPHA)
                                AlphaSurface.set_alpha(204) 
                                AlphaSurface.fill(self.BackgroundCol)
                                
                    if My >= 202*yScaleFact and My <= 247*yScaleFact and Mx >= 1155:
                        hover1 = True
                        if mousebuttondown == True:
                            self.Display.fill(self.BackgroundCol)
                            self.mod_Pygame__.display.flip() 
                            if self.sound == True:
                                self.mod_SoundUtils__.PlaySound.PlayClickSound(self)
                            mousebuttondown = False
                    else: 
                        hover1 = False 

                    if My >= 252*yScaleFact and My <= 297*yScaleFact and Mx >= 1105: 
                        hover2 = True
                        if mousebuttondown == True:
                            self.Display.fill(self.BackgroundCol)
                            self.mod_Pygame__.display.flip()
                            if self.sound == True:
                                self.mod_SoundUtils__.PlaySound.PlayClickSound(self)
                            mousebuttondown = False
                    else:
                        hover2 = False

                    if My >= 302*yScaleFact and My <= 347*yScaleFact and Mx >= 865:
                        hover3 = True
                        if mousebuttondown == True:
                            self.Display.fill(self.BackgroundCol)
                            self.mod_Pygame__.display.flip()
                            if self.sound == True:
                                self.mod_SoundUtils__.PlaySound.PlayClickSound(self)
                            mousebuttondown = False
                    else:
                        hover3 = False

                    if My >= 402*yScaleFact and My <= 447*yScaleFact and Mx >= 1035:
                        hover4 = True
                        if mousebuttondown == True:
                            self.Display.fill(self.BackgroundCol)
                            self.mod_Pygame__.display.flip()
                            if self.sound == True:
                                self.mod_SoundUtils__.PlaySound.PlayClickSound(self)
                            mousebuttondown = False
                    else:
                        hover4 = False

                    if My >= 352*yScaleFact and My <= 397*yScaleFact and Mx >= 880:
                        hover5 = True
                        if mousebuttondown == True:
                            self.Display.fill(self.BackgroundCol)
                            self.mod_Pygame__.display.flip()
                            if self.sound == True:
                                self.mod_SoundUtils__.PlaySound.PlayClickSound(self)
                            mousebuttondown = False
                    else:
                        hover5 = False

                    if My >= 502*yScaleFact and My <= 547*yScaleFact and Mx >= 1095:
                        hover6 = True
                        if mousebuttondown == True:
                            self.Display.fill(self.BackgroundCol)
                            self.mod_Pygame__.display.flip()
                            if self.sound == True:
                                self.mod_SoundUtils__.PlaySound.PlayClickSound(self)
                            mousebuttondown = False
                    else:
                        hover6 = False

                    if My >= 452*yScaleFact and My <= 497*yScaleFact and Mx >= 1095:
                        hover7 = True
                        if mousebuttondown == True:
                            self.Display.fill(self.BackgroundCol)
                            self.mod_Pygame__.display.flip()
                            if self.sound == True:
                                self.mod_SoundUtils__.PlaySound.PlayClickSound(self)
                            mousebuttondown = False
                    else:
                        hover7 = False

                    if My >= 552*yScaleFact and My <= 597*yScaleFact and Mx >= 1095:
                        hover8 = True
                        if mousebuttondown == True:
                            self.Display.fill(self.BackgroundCol)
                            self.mod_Pygame__.display.flip()
                            if self.sound == True:
                                self.mod_SoundUtils__.PlaySound.PlayClickSound(self)
                            mousebuttondown = False
                    else:
                        hover8 = False
                    
                    ButtonFont1.set_underline(hover1) 
                    ButtonFont2.set_underline(hover2) 
                    ButtonFont3.set_underline(hover3)
                    ButtonFont4.set_underline(hover4)
                    ButtonFont5.set_underline(hover5)
                    ButtonFont6.set_underline(hover6)
                    ButtonFont7.set_underline(hover7)
                    ButtonFont8.set_underline(hover8)
                    AlphaSurface.fill(self.BackgroundCol) 
                        
                    self.Display.blit(WeaponsText, ((realWidth-WeaponsTextWidth)-2, 200*yScaleFact)) # ???

                    if hover1 == True: 
                        AlphaSurface.blit(Selector, (realWidth-(WeaponsTextWidth+SelectorWidth)-2, 200*yScaleFact))
                        
                    self.Display.blit(RangedWeaponsText, ((realWidth-RangedWeaponsTextWidth)-2, 250*yScaleFact))
                    if hover2 == True: 
                        AlphaSurface.blit(Selector, (realWidth-(RangedWeaponsTextWidth+SelectorWidth)-2, 250*yScaleFact))
                        
                    self.Display.blit(ShieldsText, ((realWidth-ShieldsTextWidth)-2, 300*yScaleFact))
                    if hover3 == True: 
                        AlphaSurface.blit(Selector, (realWidth-(ShieldsTextWidth+SelectorWidth)-2, 300*yScaleFact))
                        
                    self.Display.blit(ArmourText, ((realWidth-ArmourTextWidth)-2, 350*yScaleFact))
                    if hover4 == True: 
                        AlphaSurface.blit(Selector, (realWidth-(FoodTextWidth+SelectorWidth)-2, 400*yScaleFact))
                        
                    self.Display.blit(FoodText, ((realWidth-FoodTextWidth)-2, 400*yScaleFact))
                    if hover5 == True: 
                        AlphaSurface.blit(Selector, (realWidth-(ArmourTextWidth+SelectorWidth)-2, 350*yScaleFact))
                        
                    self.Display.blit(ItemsText, ((realWidth-ItemsTextWidth)-2, 450*yScaleFact))
                    if hover6 == True: 
                        AlphaSurface.blit(Selector, (realWidth-(SpecialItemsTextWidth+SelectorWidth)-2, 500*yScaleFact))
                        
                    self.Display.blit(SpecialItemsText, ((realWidth-SpecialItemsTextWidth)-2, 500*yScaleFact))
                    if hover7 == True: 
                        AlphaSurface.blit(Selector, (realWidth-(ItemsTextWidth+SelectorWidth)-2, 450*yScaleFact))

                    self.Display.blit(OptionsText, ((realWidth-OptionsTextWidth)-2, 550*yScaleFact))
                    if hover8 == True:
                        AlphaSurface.blit(Selector, (realWidth-(OptionsTextWidth+SelectorWidth)-2, 550*yScaleFact))

                    self.mod_Pygame__.display.update()
                    self.clock.tick(self.FPS)
            except Exception as Message:
                print(''.join(self.mod_Traceback__.format_exception(None, Message, Message.__traceback__)))
                return Message
else:
    print("You need to run this as part of Pycraft")
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")
    quit()