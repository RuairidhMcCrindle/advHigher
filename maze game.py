import tkinter as tk
from tkinter.constants import NSEW
import pygame





class launcher():
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





    def setUpLeaderboard(self):
        for widget in self.mainFrame.winfo_children():
            widget.grid_forget()
        self.leaderboardTitle.grid(column = 9, row = 0)
        self.mainMenu.grid(column = 9, row = 17, pady = 2, ipadx = 285)
        self.quitButton.grid(column = 9, row = 18, pady = 2, ipadx = 144)

    def setUpLogin(self):
        pass

    def setUpSignUp(self):
        pass

    def popUpWindow(self):
        pass

    def levelOne(self):
        self.firstLevel = levelOne()
        self.firstLevel.run()
        pygame.quit()
        

    def levelTwo(self):
        pass

    def levelThree(self):
        pass

    def levelFour(self):
        pass
    
    def levelFive(self):
        pass

        


class game():
    def __init__(self):
        pygame.init()
        pygame.key.set_repeat(500,25)
        self.window = pygame.display.set_mode((1095, 700))
        self.clockRate = pygame.time.Clock()
        self.positionX = 0
        self.positionY = 0
        self.moveX = 0
        self.moveY = 0
        self.running = True
    def process(self):
        self.moveX = 0
        self.moveY = 0
        self.eventList = pygame.event.get()
        for event in self.eventList:
            if event.type == pygame.QUIT:
                self.running = False   
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    break
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.moveY -= 10
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.moveY += 10
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.moveX += 10
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.moveX -= 10
                
            
    def update(self):
        self.positionX += self.moveX
        self.positionY += self.moveY

class levelOne(game):
    def __init__(self):
        super().__init__()
        pygame.display.set_caption("Level One")
    def render(self):
        self.window.fill((0,0,255))
        pygame.draw.rect(self.window, (0,0,0),(self.positionX, self.positionY, 50,50))
        pygame.display.update()

    def run(self):
        while self.running:
            self.process()
            self.update()
            self.render()
            self.clockRate.tick(60)




def main():
    pygame.init()
    root = tk.Tk()
    menuWindow = launcher(root)
    menuWindow.setUpMain()
    root.mainloop()


main()
