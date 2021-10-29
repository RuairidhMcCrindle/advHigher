import tkinter as tk
from tkinter.constants import NSEW
import pygame





class menus():
    def __init__(self, window):
        #general widgets
        self.window = window

        #sets window dimensions, and makes it so that the size cannot be changed
        self.window.geometry("1095x700")
        self.window.minsize(1095,700)
        self.window.maxsize(1095,700)

        #makes list from 0-18 inclusive        
        self.rowColumn = list(range(19))

        self.mainFrame = tk.Frame(self.window, width = 1096, height = 701, background = "dark blue")
        self.mainFrame.columnconfigure(self.rowColumn, minsize = 40, weight = 1)
        self.mainFrame.rowconfigure(self.rowColumn, minsize = 35)
        self.mainFrame.pack(fill = tk.BOTH, expand = True)
        self.window.title("McCrindle's Maze")

        #common widgets
        #ideally all buttons should be 375 pixels wide and 32 pixels high
        self.quitButton = tk.Button(self.mainFrame, text = "Exit Game", command = self.window.destroy, font = ("Helvetica", 12))
        self.mainMenu = tk.Button(self.mainFrame, text = "Main Menu", command = self.setUpMain, font = ("Helvetica", 12))

        #main menu widgets
        self.mainTitle = tk.Label(self.mainFrame, text= "Welcome to McCrindle's Maze", fg = "white", bg = "dark blue", font = ("Helvetica", 20))
        self.levelSelect = tk.Button(self.mainFrame, text = "Select Level", command = self.setUpSelect, font = ("Helvetica", 12))
        self.leaderboard = tk.Button(self.mainFrame, text = "Open Leaderboard", command = self.setUpLeaderboard, font = ("Helvetica", 12))
        self.login = tk.Button(self.mainFrame, text = "Login", command = self.setUpLogin, font = ("Helvetica", 12))
        self.signUp = tk.Button(self.mainFrame, text = "Sign Up", command = self.setUpSignUp, font = ("Helvetica", 12))

        #level select widgets
        self.selectTitle = tk.Label(self.mainFrame, text = "Level Select", fg = "white", bg = "dark blue", font = ("Helvetica", 20))
        self.selectOne = tk.Button(self.mainFrame, text = "Level One", command = self.levelOne, font = ("Helvetica", 12))
        self.selectTwo = tk.Button(self.mainFrame, text = "Level Two", command = self.levelTwo, font = ("Helvetica", 12))
        self.selectThree = tk.Button(self.mainFrame, text = "Level Three", command = self.levelThree, font = ("Helvetica", 12))
        self.selectFour = tk.Button(self.mainFrame, text = "Level Four", command = self.levelFour, font = ("Helvetica", 12))
        self.selectFive = tk.Button(self.mainFrame, text = "Level Five", command = self.levelFive, font = ("Helvetica", 12))

        #leaderboard widgets
        self.leaderboardTitle = tk.Label(self.mainFrame, text = "Leaderboard", fg = "white", bg = "dark blue", font = ("Helvetica", 20))
        
    


    def setUpMain(self):
        for widget in self.mainFrame.winfo_children():
            widget.grid_forget()
        self.mainTitle.grid(column = 9, row = 0)
        self.levelSelect.grid(column = 9, row = 14, pady = 2, ipadx = 138)
        self.leaderboard.grid(column = 9, row = 15, pady = 2, ipadx = 114)
        self.login.grid(column = 9, row = 16, pady = 2, ipadx = 322)
        self.signUp.grid(column = 9, row = 17, pady = 2, ipadx = 305)
        self.quitButton.grid(column = 9, row = 18, pady = 2, ipadx = 144)
        #debug code to find size of widgets
        #self.mainTitle.update()
        #self.levelSelect.update()
        #self.leaderboard.update()
        #self.login.update()
        #self.signUp.update()
        #self.quitButton.update()
        #print(str(self.mainTitle.winfo_width()) + " " + str(self.mainTitle.winfo_height()))
        #print(str(self.levelSelect.winfo_width()) + " " + str(self.levelSelect.winfo_height()))
        #print(str(self.leaderboard.winfo_width()) + " " + str(self.leaderboard.winfo_height()))
        #print(str(self.login.winfo_width()) + " " + str(self.login.winfo_height()))
        #print(str(self.signUp.winfo_width()) + " " + str(self.signUp.winfo_height()))
        #print(str(self.quitButton.winfo_width()) + " " + str(self.quitButton.winfo_height()))


    def setUpSelect(self):
        #note: checks must be done to ensure an account is logged in before opening level select menu. implement after login system is implemented
        for widget in self.mainFrame.winfo_children():
            widget.grid_forget()
        self.selectTitle.grid(column = 9, row = 0, pady = 2, ipadx = 187)
        self.selectOne.grid(column = 9, row = 12, pady = 2, ipadx = 291)
        self.selectTwo.grid(column = 9, row = 13, pady = 2, ipadx = 291)
        self.selectThree.grid(column = 9, row = 14, pady = 2, ipadx = 290)
        self.selectFour.grid(column = 9, row = 15, pady = 2, ipadx = 288)
        self.selectFive.grid(column = 9, row = 16, pady = 2, ipadx = 290)
        self.mainMenu.grid(column = 9, row = 17, pady = 2, ipadx = 285)
        self.quitButton.grid(column = 9, row = 18, pady = 2, ipadx = 144)
        #debug code to find size of widgets
        #self.selectTitle.update()
        #self.selectOne.update()
        #self.selectTwo.update()
        #self.selectThree.update()
        #self.selectFour.update()
        #self.selectFive.update()
        #self.mainMenu.update()
        #self.quitButton.update()
        #print(str(self.selectOne.winfo_width()) + " " + str(self.selectOne.winfo_height()))
        #print(str(self.selectTwo.winfo_width()) + " " + str(self.selectTwo.winfo_height()))
        #print(str(self.selectThree.winfo_width()) + " " + str(self.selectThree.winfo_height()))
        #print(str(self.selectFour.winfo_width()) + " " + str(self.selectFour.winfo_height()))
        #print(str(self.selectFive.winfo_width()) + " " + str(self.selectFive.winfo_height()))
        #print(str(self.selectTitle.winfo_width()) + " " + str(self.selectTitle.winfo_height()))
        #print(str(self.mainMenu.winfo_width()) + " " + str(self.mainMenu.winfo_height()))
        #print(str(self.quitButton.winfo_width()) + " " + str(self.quitButton.winfo_height()))




    def setUpLeaderboard(self):
        for widget in self.mainFrame.winfo_children():
            widget.grid_forget()
        self.leaderboardTitle.grid(column = 9, row = 0)
        self.mainMenu.grid(column = 9, row = 17, pady = 2, ipadx = 285)
        self.quitButton.grid(column = 9, row = 18, pady = 2, ipadx = 144)
        #self.leaderboardTitle.update()
        #self.mainMenu.update()
        #self.quitButton.update()
        #print(str(self.leaderboardTitle.winfo_width()) + " " + str(self.leaderboardTitle.update()))
        #print(str(self.mainMenu.winfo_width()) + " " + str(self.mainMenu.winfo_height()))
        #print(str(self.quitButton.winfo_width()) + " " + str(self.quitButton.winfo_height()))

    def setUpLogin(self):
        pass

    def setUpSignUp(self):
        pass

    def popUpWindow(self):
        pass

    def levelOne(self):
        test()
        

    def levelTwo(self):
        pass

    def levelThree(self):
        pass

    def levelFour(self):
        pass
    
    def levelFive(self):
        pass

        



def test():
    window = pygame.display.set_mode((640,480))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        pygame.draw.rect(window,(0,0,255),(120,120,400,240))
        pygame.display.update()
    pygame.quit()    

def main():
    pygame.init()
    root = tk.Tk()
    menuWindow = menus(root)
    menuWindow.setUpMain()
    root.mainloop()


main()

