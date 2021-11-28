import tkinter as tk
import pygame
from pygame import Vector2 as vector
import mysql.connector
from tkinter import messagebox





class launcher():
    def __init__(self, window):
        #general widgets
        self.window = window
        self.congratsWindow = tk.Toplevel(window, bg = "#004ecc")
        self.congratsWindow.withdraw()
        self.congratsWindow.protocol("WM_DELETE_WINDOW", self.congratsWindow.withdraw)

        #sets window dimensions, and makes it so that the size cannot be changed
        self.window.geometry("1095x700")
        self.window.minsize(1095,700)
        self.window.maxsize(1095,700)
        self.congratsWindow.geometry("325x100")
        self.congratsWindow.minsize(325,100)
        self.congratsWindow.maxsize(325,100)

        #makes lists from 0-(n-1) inclusive        
        self.rowColumn = list(range(19))
        self.row = list(range(2))
        #sets up grids and frames for windows
        self.mainFrame = tk.Frame(self.window, width = 1096, height = 701, bg = "#004ecc")
        self.mainFrame.columnconfigure(9, weight = 1)
        self.mainFrame.rowconfigure(self.rowColumn, minsize = 35)
        self.mainFrame.pack(fill = "both", expand = True)
        self.window.title("McCrindle's Maze")

        #common widgets
        #ideally all buttons should be 375 pixels wide and 32 pixels high
        self.quitButton = tk.Button(self.mainFrame, text = "Exit Game", command = self.window.destroy, font = ("Helvetica", 12))
        self.mainMenu = tk.Button(self.mainFrame, text = "Return", command = self.setUpMain, font = ("Helvetica", 12))

        #main menu widgets
        self.mainTitle = tk.Label(self.mainFrame, text= "Welcome to McCrindle's Maze", fg = "white", bg = "#004ecc", font = ("Helvetica", 20))
        self.levelSelect = tk.Button(self.mainFrame, text = "Select Level", command = self.setUpSelect, font = ("Helvetica", 12))
        self.leaderboard = tk.Button(self.mainFrame, text = "Open Leaderboard", command = self.setUpLeaderboard, font = ("Helvetica", 12))
        self.login = tk.Button(self.mainFrame, text = "Login", command = self.setUpLogin, font = ("Helvetica", 12))
        self.signUp = tk.Button(self.mainFrame, text = "New Account", command = self.setUpSignUp, font = ("Helvetica", 12))

        #level select widgets
        self.selectTitle = tk.Label(self.mainFrame, text = "Level Select", fg = "white", bg = "#004ecc", font = ("Helvetica", 20))
        self.selectOne = tk.Button(self.mainFrame, text = "Level One", command = self.levelOne, font = ("Helvetica", 12))
        self.selectTwo = tk.Button(self.mainFrame, text = "Level Two", command = self.levelTwo, font = ("Helvetica", 12))
        self.selectThree = tk.Button(self.mainFrame, text = "Level Three", command = self.levelThree, font = ("Helvetica", 12))
        self.selectFour = tk.Button(self.mainFrame, text = "Level Four", command = self.levelFour, font = ("Helvetica", 12))
        self.selectFive = tk.Button(self.mainFrame, text = "Level Five", command = self.levelFive, font = ("Helvetica", 12))

        #leaderboard widgets
        self.leaderboardTitle = tk.Label(self.mainFrame, text = "Leaderboard", fg = "white", bg = "#004ecc", font = ("Helvetica", 20))

        #signup/login widgets
        self.signUpTitle = tk.Label(self.mainFrame, text = "Sign Up", fg = "white", bg = "#004ecc", font = ("Helvetica", 20))
        self.userNameTitle = tk.Label(self.mainFrame, text = "Username", fg = "white", bg = "#004ecc", font = ("Helvetica", 12))
        self.userNameInput = tk.Entry(self.mainFrame, font = ("Helvetica", 10))
        self.passwordTitle = tk.Label(self.mainFrame, text = "Password", fg = "white", bg = "#004ecc", font = ("Helvetica", 12))
        self.passwordInput = tk.Entry(self.mainFrame, font = ("Helvetica", 10), show = "*")
        self.signUpButton = tk.Button(self.mainFrame, text = "Create Account" , command = self.sqlSignUp, font = ("Helvetica", 12))
        self.loginButton = tk.Button(self.mainFrame, text = "Login" , command = self.sqlLogin, font = ("Helvetica", 12))
        
        #congrats window widget
        self.congratsTitle = tk.Label(self.congratsWindow, text= "Congratulations! You won!", fg = "white", bg = "#004ecc", font = ("Helvetica", 20))
        self.congratsTitle.pack(pady=(0,30))
        self.congratsButton = tk.Button(self.congratsWindow, text = "OK", command = self.congratsWindow.withdraw, font = ("Helvetica", 12))
        self.congratsButton.pack()

        #database stuff
        self.myDB = mysql.connector.connect(
            host = "localhost",
            user = "ruairidh",
            password ="password",
            database = "mazeGame"
        )
        self.myCursor = self.myDB.cursor()
        self.newUser = "INSERT INTO Users (username, password) VALUES (%s,%s)"
        self.userCheck = "SELECT username, password FROM Users WHERE %s, %s"
        self.sqlValues = []



    def setUpMain(self):
        for widget in self.mainFrame.winfo_children():
            widget.grid_forget()
        self.mainTitle.grid(column = 9, row = 0)
        self.levelSelect.grid(column = 9, row = 14, pady = 2, ipadx = 138)
        self.leaderboard.grid(column = 9, row = 15, pady = 2, ipadx = 114)
        self.login.grid(column = 9, row = 16, pady = 2, ipadx = 161)
        self.signUp.grid(column = 9, row = 17, pady = 2, ipadx = 135)
        self.quitButton.grid(column = 9, row = 18, pady = 2, ipadx = 144)


    def setUpSelect(self):
        #note: checks must be done to ensure an account is logged in before opening level select menu. implement after login system is implemented
        for widget in self.mainFrame.winfo_children():
            widget.grid_forget()
        self.selectTitle.grid(column = 9, row = 0, pady = 2, ipadx = 187)
        self.selectOne.grid(column = 9, row = 12, pady = 2, ipadx = 145)
        self.selectTwo.grid(column = 9, row = 13, pady = 2, ipadx = 145)
        self.selectThree.grid(column = 9, row = 14, pady = 2, ipadx = 140)
        self.selectFour.grid(column = 9, row = 15, pady = 2, ipadx = 144)
        self.selectFive.grid(column = 9, row = 16, pady = 2, ipadx = 145)
        self.mainMenu.grid(column = 9, row = 17, pady = 2, ipadx = 158)
        self.quitButton.grid(column = 9, row = 18, pady = 2, ipadx = 144)

    def setUpLeaderboard(self):
        for widget in self.mainFrame.winfo_children():
            widget.grid_forget()
        self.leaderboardTitle.grid(column = 9, row = 0)
        self.mainMenu.grid(column = 9, row = 17, pady = 2, ipadx = 158)
        self.quitButton.grid(column = 9, row = 18, pady = 2, ipadx = 144)

    def setUpLogin(self):
        pass

    def setUpSignUp(self):
        for widget in self.mainFrame.winfo_children():
            widget.grid_forget()
        self.signUpTitle.grid(column = 9, row = 0)
        self.userNameTitle.grid(column = 9, row = 2, padx = (0,1000))
        self.userNameInput.grid(column = 9, row = 3, padx = (0,948))
        self.passwordTitle.grid(column = 9, row = 4, padx = (0,1000))
        self.passwordInput.grid(column = 9, row = 5, padx = (0,948))
        self.signUpButton.grid(column= 9, row = 16, pady = 2, ipadx = 126)
        self.mainMenu.grid(column = 9, row = 17, pady = 2, ipadx = 158)
        self.quitButton.grid(column = 9, row = 18, pady = 2, ipadx = 144)
        self.userNameInput.delete(0,"end")
        self.passwordInput.delete(0,"end")
        

    def popUpWindow(self):
        pass

    def levelOne(self):
        self.firstLevel = levelOne()
        self.firstLevel.run()
        pygame.quit()
        if self.firstLevel.win == True:
            self.congrats()
        

    def levelTwo(self):
        self.secondLevel = levelTwo()
        self.secondLevel.run()
        pygame.quit()
        if self.secondLevel.win == True:
            self.congrats()

    def levelThree(self):
        self.thirdLevel = levelThree()
        self.thirdLevel.run()
        pygame.quit()
        if self.thirdLevel.win == True:
            self.congrats()

    def levelFour(self):
        self.fourthLevel = levelFour()
        self.fourthLevel.run()
        pygame.quit()
        if self.fourthLevel.win == True:
            self.congrats()
    
    def levelFive(self):
        self.fifthLevel = levelFive()
        self.fifthLevel.run()
        pygame.quit()
        if self.fifthLevel.win == True:
            self.congrats()

    def congrats(self):
        self.congratsWindow.deiconify()
    
    def sqlSignUp(self):
        try:
            #make sure that user has not entered nothing as username and password, and make sure to account for other errors
            self.sqlValues.clear()
            self.sqlValues.append(self.userNameInput.get())
            self.sqlValues.append(self.passwordInput.get())
            self.myCursor.execute(self.newUser, self.sqlValues)
            self.myDB.commit()
            self.setUpMain()
        except mysql.connector.errors.IntegrityError:
            messagebox.showerror(title = "Error", message = "That username is already taken")

    def sqlLogin(self):
        self.myCursor.execute(self.userCheck, self.sqlValues)
        self.myDB.commit()
        


class game():
    def __init__(self):
        pygame.init()
        pygame.key.set_repeat(500,25)
        self.window = pygame.display.set_mode((1095, 700))
        self.clockRate = pygame.time.Clock()
        #each block in maze is 73 by 70
        #therefore each row is 15 blocks, and each column is 10 blocks
        self.rowValues = [0,70,140,210,280,350,420,490,560,630] #the start y value for each row
        self.columnValues = [0, 73, 146, 219, 292, 365, 438, 511, 584, 657, 730, 803, 876, 949, 1022] #the start x value for each coumn
        self.pathBlocks = [
            [], #first row
            [], #second row
            [], #third row
            [], #fourth row
            [], #fifth row
            [], #sixth row
            [], #seventh row
            [], #eighth row
            [], #ninth row
            []  #tenth row 
        ]
        self.rowValues = [0,70,140,210,280,350,420,490,560,630] #the start y value for each row
        self.columnValues = [0, 73, 146, 219, 292, 365, 438, 511, 584, 657, 730, 803, 876, 949, 1022] #the start x value for each column
        self.position = {"x": 0, "y":0}
        self.move = {"x pos": 10, "x neg": 10,"y pos": 10,"y neg": 10} #where the first index is positive x movement, second is negative x, third is positive y, fourth is negative y
        self.totalMove = {"x": 0,"y": 0}
        self.positionCheck = [False, False, False, False] #top left, top right, bottom right, bottom left. checks for whether any of the players corners are in a path block
        self.win = False
        self.running = True
    def process(self):
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
                    self.move["y neg"] += 1
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.move["y pos"] += 1
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.move["x pos"] += 1
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.move["x neg"] += 1
                
            
    def update(self):
        self.totalMove["x"] = (((2)**(self.move["x pos"] - 10)) - ((2)**(self.move["x neg"] - 10)))
        self.totalMove["y"] = (((2)**(self.move["y pos"] - 10)) - ((2)**(self.move["y neg"] - 10)))
        if self.position["x"] + self.totalMove["x"] < 0 or self.position["x"] + self.totalMove["x"] > 1045 or self.position["y"] + self.totalMove["y"] < 0 or self.position["y"] + self.totalMove["y"] > 650:
            self.move["x pos"], self.move["x neg"], self.move["y pos"], self.move["y neg"] = 0,0,0,0
            self.position["x"], self.position["y"] = 0,0
        else:
            self.positionCheck = [False, False, False, False]
            for i in range(0,10):
                for j in self.pathBlocks[i]:
                    if self.position["x"] + self.totalMove["x"] <= j.x + 73 and self.position["x"] + self.totalMove["x"] >= j.x and self.position["y"] + self.totalMove["y"] <= j.y + 70 and self.position["y"] + self.totalMove["y"] >= j.y:
                        self.positionCheck[0] = True

                    if self.position["x"] + self.totalMove["x"] + 50 <= j.x + 73 and self.position["x"] + self.totalMove["x"] + 50 >= j.x and self.position["y"] + self.totalMove["y"] <= j.y + 70 and self.position["y"] + self.totalMove["y"] >= j.y:
                        self.positionCheck[1] = True

                    if self.position["y"] + self.totalMove["y"] + 50 <= j.y + 70 and self.position["y"] + self.totalMove["y"] + 50 >= j.y and self.position["x"] + self.totalMove["x"] + 50 <= j.x + 73 and self.position["x"] + self.totalMove["x"] + 50 >= j.x:
                        self.positionCheck[2] = True

                    if self.position["y"] + self.totalMove["y"] + 50 <= j.y + 70 and self.position["y"] + self.totalMove["y"] + 50 >= j.y and self.position["x"] + self.totalMove["x"] <= j.x + 73 and self.position["x"] + self.totalMove["x"] >= j.x:
                        self.positionCheck[3] = True
                    
            if self.positionCheck[0] == True and self.positionCheck[1] == True and self.positionCheck[2] == True and self.positionCheck[3] == True:
                self.position["x"] += self.totalMove["x"]
                self.position["y"] += self.totalMove["y"]
            else:
                self.move["x pos"], self.move["x neg"], self.move["y pos"], self.move["y neg"] = 0,0,0,0
                self.position["x"], self.position["y"] = 0,0

            if self.totalMove["x"] == 0:
                self.move["x pos"], self.move["x neg"] = 10, 10

            if self.totalMove["y"] == 0:
                self.move["y pos"], self.move["y neg"] = 10, 10
            
            if self.position["x"] + self.totalMove["x"] <= self.columnValues[14] + 73 and self.position["x"] + self.totalMove["x"] >= self.columnValues[14] and self.position["y"] + self.totalMove["y"] <= self.rowValues[9] + 70 and self.position["y"] + self.totalMove["y"] >= self.rowValues[9]:
                self.win = True
                self.running = False   

            elif self.position["x"] + self.totalMove["x"] + 50 <= self.columnValues[14] + 73 and self.position["x"] + self.totalMove["x"] + 50 >= self.columnValues[14] and self.position["y"] + self.totalMove["y"] <= self.rowValues[9] + 70 and self.position["y"] + self.totalMove["y"] >= self.rowValues[9]:
                self.win = True
                self.running = False
            elif self.position["y"] + self.totalMove["y"] + 50 <= self.rowValues[9] + 70 and self.position["y"] + self.totalMove["y"] + 50 >= self.rowValues[9] and self.position["x"] + self.totalMove["x"] + 50 <= self.columnValues[14] + 73 and self.position["x"] + self.totalMove["x"] + 50 >= self.columnValues[14]:
               self.win = True
               self.running = False
            elif self.position["y"] + self.totalMove["y"] + 50 <= self.rowValues[9] + 70 and self.position["y"] + self.totalMove["y"] + 50 >= self.rowValues[9] and self.position["x"] + self.totalMove["x"] <= self.columnValues[14] + 73 and self.position["x"] + self.totalMove["x"] >= self.columnValues[14]:
                self.win = True
                self.running = False

    def run(self):
        while self.running == True:
            self.process()
            self.update()
            self.render()
            self.clockRate.tick(60)

class levelOne(game):
    def __init__(self):
        super().__init__()
        pygame.display.set_caption("Level One")
    def render(self):
        self.pathBlocks = [
            [vector(self.columnValues[0], self.rowValues[0]), vector(self.columnValues[1], self.rowValues[0]), vector(self.columnValues[2], self.rowValues[0])], #first row
            [vector(self.columnValues[2], self.rowValues[1])], #second row
            [vector(self.columnValues[2], self.rowValues[2])], #third row
            [vector(self.columnValues[2], self.rowValues[3]), vector(self.columnValues[3], self.rowValues[3]), vector(self.columnValues[4], self.rowValues[3]), vector(self.columnValues[5], self.rowValues[3])], #fourth row
            [vector(self.columnValues[5], self.rowValues[4])], #fifth row
            [vector(self.columnValues[5], self.rowValues[5])], #sixth row
            [vector(self.columnValues[5], self.rowValues[6]), vector(self.columnValues[6], self.rowValues[6]), vector(self.columnValues[7], self.rowValues[6]), vector(self.columnValues[8], self.rowValues[6]), vector(self.columnValues[9], self.rowValues[6])], #seventh row
            [vector(self.columnValues[9], self.rowValues[7]), vector(self.columnValues[11], self.rowValues[7]), vector(self.columnValues[12], self.rowValues[7]), vector(self.columnValues[13], self.rowValues[7])], #eighth row
            [vector(self.columnValues[9], self.rowValues[8]), vector(self.columnValues[11], self.rowValues[8]), vector(self.columnValues[13], self.rowValues[8]), vector(self.columnValues[14], self.rowValues[8])], #ninth row
            [vector(self.columnValues[9], self.rowValues[9]), vector(self.columnValues[10], self.rowValues[9]), vector(self.columnValues[11], self.rowValues[9]), vector(self.columnValues[14], self.rowValues[9])]  #tenth row 
        ]
        self.window.fill((204,82,0))
        for i in range(0,10):
            for j in self.pathBlocks[i]:
                pygame.draw.rect(self.window, (0,78,204), (j.x, j.y, 73, 70))
        pygame.draw.rect(self.window, (57,255,20), (self.columnValues[14], self.rowValues[9], 73, 70))
        pygame.draw.rect(self.window, (0,0,0),(self.position["x"], self.position["y"], 50,50))
        pygame.display.update()

class levelTwo(game):
    def __init__(self):
        super().__init__()
        pygame.display.set_caption("Level Two")
    def render(self):
        self.pathBlocks = [
            [vector(self.columnValues[0], self.rowValues[0]), vector(self.columnValues[1], self.rowValues[0]), vector(self.columnValues[2], self.rowValues[0]), vector(self.columnValues[3], self.rowValues[0]), vector(self.columnValues[4], self.rowValues[0]), vector(self.columnValues[5], self.rowValues[0]), vector(self.columnValues[6], self.rowValues[0]), vector(self.columnValues[7], self.rowValues[0]), vector(self.columnValues[8], self.rowValues[0]), vector(self.columnValues[9], self.rowValues[0]), vector(self.columnValues[10], self.rowValues[0]), vector(self.columnValues[11], self.rowValues[0]), vector(self.columnValues[12], self.rowValues[0]), vector(self.columnValues[13], self.rowValues[0]), vector(self.columnValues[14], self.rowValues[0])], #first row
            [vector(self.columnValues[14], self.rowValues[1])], #second row
            [vector(self.columnValues[14], self.rowValues[2])], #third row
            [vector(self.columnValues[14], self.rowValues[3])], #fourth row
            [vector(self.columnValues[14], self.rowValues[4])], #fifth row
            [vector(self.columnValues[10], self.rowValues[5]), vector(self.columnValues[11], self.rowValues[5]), vector(self.columnValues[12], self.rowValues[5]), vector(self.columnValues[14], self.rowValues[5])], #sixth row
            [vector(self.columnValues[10], self.rowValues[6]), vector(self.columnValues[12], self.rowValues[6]), vector(self.columnValues[14], self.rowValues[6])], #seventh row
            [vector(self.columnValues[8], self.rowValues[7]), vector(self.columnValues[9], self.rowValues[7]), vector(self.columnValues[10], self.rowValues[7]), vector(self.columnValues[12], self.rowValues[7]), vector(self.columnValues[13], self.rowValues[7]), vector(self.columnValues[14], self.rowValues[7])], #eighth row
            [vector(self.columnValues[8], self.rowValues[8])], #ninth row
            [vector(self.columnValues[8], self.rowValues[9]), vector(self.columnValues[9], self.rowValues[9]), vector(self.columnValues[10], self.rowValues[9]), vector(self.columnValues[11], self.rowValues[9]), vector(self.columnValues[12], self.rowValues[9]), vector(self.columnValues[13], self.rowValues[9]), vector(self.columnValues[14], self.rowValues[9])]  #tenth row 
        ]
        self.window.fill((204,82,0))
        for i in range(0,10):
            for j in self.pathBlocks[i]:
                pygame.draw.rect(self.window, (51,78,153), (j.x, j.y, 73, 70))
        pygame.draw.rect(self.window, (57,255,20), (self.columnValues[14], self.rowValues[9], 73, 70))
        pygame.draw.rect(self.window, (0,0,0),(self.position["x"], self.position["y"], 50,50))
        pygame.display.update()

class levelThree(game):
    def __init__(self):
        super().__init__()
        pygame.display.set_caption("Level Three")
    def render(self):
        self.pathBlocks = [
            [vector(self.columnValues[0], self.rowValues[0]), vector(self.columnValues[1], self.rowValues[0]), vector(self.columnValues[3], self.rowValues[0]), vector(self.columnValues[4], self.rowValues[0]), vector(self.columnValues[5], self.rowValues[0]), vector(self.columnValues[7], self.rowValues[0]), vector(self.columnValues[8], self.rowValues[0]), vector(self.columnValues[9], self.rowValues[0])], #first row
            [vector(self.columnValues[1], self.rowValues[1]), vector(self.columnValues[3], self.rowValues[1]), vector(self.columnValues[5], self.rowValues[1]), vector(self.columnValues[7], self.rowValues[1]), vector(self.columnValues[9], self.rowValues[1])], #second row
            [vector(self.columnValues[1], self.rowValues[2]), vector(self.columnValues[2], self.rowValues[2]), vector(self.columnValues[3], self.rowValues[2]), vector(self.columnValues[5], self.rowValues[2]), vector(self.columnValues[7], self.rowValues[2]), vector(self.columnValues[9], self.rowValues[2])], #third row
            [vector(self.columnValues[5], self.rowValues[3]), vector(self.columnValues[7], self.rowValues[3]), vector(self.columnValues[9], self.rowValues[3])], #fourth row
            [vector(self.columnValues[2], self.rowValues[4]), vector(self.columnValues[3], self.rowValues[4]), vector(self.columnValues[4], self.rowValues[4]), vector(self.columnValues[5], self.rowValues[4]), vector(self.columnValues[7], self.rowValues[4]), vector(self.columnValues[9], self.rowValues[4])], #fifth row
            [vector(self.columnValues[2], self.rowValues[5]), vector(self.columnValues[7], self.rowValues[5]), vector(self.columnValues[9], self.rowValues[5])], #sixth row
            [vector(self.columnValues[2], self.rowValues[6]), vector(self.columnValues[3], self.rowValues[6]), vector(self.columnValues[4], self.rowValues[6]), vector(self.columnValues[5], self.rowValues[6]), vector(self.columnValues[6], self.rowValues[6]), vector(self.columnValues[7], self.rowValues[6]), vector(self.columnValues[9], self.rowValues[6])], #seventh row
            [vector(self.columnValues[8], self.rowValues[7]), vector(self.columnValues[9], self.rowValues[7]), vector(self.columnValues[11], self.rowValues[7]), vector(self.columnValues[12], self.rowValues[7]), vector(self.columnValues[13], self.rowValues[7])], #eighth row
            [vector(self.columnValues[8], self.rowValues[8]), vector(self.columnValues[11], self.rowValues[8]), vector(self.columnValues[13], self.rowValues[8])], #ninth row
            [vector(self.columnValues[8], self.rowValues[9]), vector(self.columnValues[9], self.rowValues[9]), vector(self.columnValues[10], self.rowValues[9]), vector(self.columnValues[11], self.rowValues[9]), vector(self.columnValues[13], self.rowValues[9]), vector(self.columnValues[14], self.rowValues[9])]  #tenth row 
        ]
        self.window.fill((204,82,0))
        for i in range(0,10):
            for j in self.pathBlocks[i]:
                pygame.draw.rect(self.window, (102,78,102), (j.x, j.y, 73, 70))
        pygame.draw.rect(self.window, (57,255,20), (self.columnValues[14], self.rowValues[9], 73, 70))
        pygame.draw.rect(self.window, (0,0,0),(self.position["x"], self.position["y"], 50,50))
        pygame.display.update()

class levelFour(game):
    def __init__(self):
        super().__init__()
        pygame.display.set_caption("Level Four")
    def render(self):
        self.pathBlocks = [
            [vector(self.columnValues[0], self.rowValues[0])], #first row
            [vector(self.columnValues[0], self.rowValues[1]), vector(self.columnValues[1], self.rowValues[1]), vector(self.columnValues[2], self.rowValues[1])], #second row
            [vector(self.columnValues[2], self.rowValues[2]), vector(self.columnValues[4], self.rowValues[2]), vector(self.columnValues[5], self.rowValues[2]), vector(self.columnValues[6], self.rowValues[2]), vector(self.columnValues[8], self.rowValues[2]), vector(self.columnValues[9], self.rowValues[2]), vector(self.columnValues[10], self.rowValues[2]), vector(self.columnValues[11], self.rowValues[2]), vector(self.columnValues[12], self.rowValues[2]), vector(self.columnValues[13], self.rowValues[2]), vector(self.columnValues[14], self.rowValues[2])], #third row
            [vector(self.columnValues[1], self.rowValues[3]), vector(self.columnValues[2], self.rowValues[3]), vector(self.columnValues[4], self.rowValues[3]), vector(self.columnValues[6], self.rowValues[3]), vector(self.columnValues[8], self.rowValues[3]), vector(self.columnValues[14], self.rowValues[3])], #fourth row
            [vector(self.columnValues[1], self.rowValues[4]), vector(self.columnValues[4], self.rowValues[4]), vector(self.columnValues[6], self.rowValues[4]), vector(self.columnValues[8], self.rowValues[4]), vector(self.columnValues[10], self.rowValues[4]), vector(self.columnValues[11], self.rowValues[4]), vector(self.columnValues[12], self.rowValues[4]), vector(self.columnValues[14], self.rowValues[4])], #fifth row
            [vector(self.columnValues[1], self.rowValues[5]), vector(self.columnValues[2], self.rowValues[5]), vector(self.columnValues[3], self.rowValues[5]), vector(self.columnValues[4], self.rowValues[5]), vector(self.columnValues[6], self.rowValues[5]), vector(self.columnValues[8], self.rowValues[5]), vector(self.columnValues[10], self.rowValues[5]), vector(self.columnValues[12], self.rowValues[5]), vector(self.columnValues[14], self.rowValues[5])], #sixth row
            [vector(self.columnValues[5], self.rowValues[6]), vector(self.columnValues[6], self.rowValues[6]), vector(self.columnValues[8], self.rowValues[6]), vector(self.columnValues[9], self.rowValues[6]), vector(self.columnValues[10], self.rowValues[6]), vector(self.columnValues[12], self.rowValues[6]), vector(self.columnValues[14], self.rowValues[6])], #seventh row
            [vector(self.columnValues[5], self.rowValues[7]), vector(self.columnValues[12], self.rowValues[7]), vector(self.columnValues[14], self.rowValues[7])], #eighth row
            [vector(self.columnValues[5], self.rowValues[8]), vector(self.columnValues[6], self.rowValues[8]), vector(self.columnValues[7], self.rowValues[8]), vector(self.columnValues[8], self.rowValues[8]), vector(self.columnValues[9], self.rowValues[8]), vector(self.columnValues[10], self.rowValues[8]), vector(self.columnValues[11], self.rowValues[8]), vector(self.columnValues[12], self.rowValues[8]), vector(self.columnValues[14], self.rowValues[8])], #ninth row
            [vector(self.columnValues[14], self.rowValues[9]), vector(self.columnValues[14], self.rowValues[9])]  #tenth row 
        ]
        self.window.fill((204,82,0))
        for i in range(0,10):
            for j in self.pathBlocks[i]:
                pygame.draw.rect(self.window, (153,78,51), (j.x, j.y, 73, 70))
        pygame.draw.rect(self.window, (57,255,20), (self.columnValues[14], self.rowValues[9], 73, 70))
        pygame.draw.rect(self.window, (0,0,0),(self.position["x"], self.position["y"], 50,50))
        pygame.display.update()

class levelFive(game):
    def __init__(self):
        super().__init__()
        pygame.display.set_caption("Level Five")
    def render(self):
        self.pathBlocks = [
            [vector(self.columnValues[0], self.rowValues[0]), vector(self.columnValues[2], self.rowValues[0]), vector(self.columnValues[3], self.rowValues[0]), vector(self.columnValues[4], self.rowValues[0]), vector(self.columnValues[5], self.rowValues[0]), vector(self.columnValues[9], self.rowValues[0]), vector(self.columnValues[10], self.rowValues[0]), vector(self.columnValues[11], self.rowValues[0]), vector(self.columnValues[12], self.rowValues[0])], #first row
            [vector(self.columnValues[0], self.rowValues[1]), vector(self.columnValues[2], self.rowValues[1]), vector(self.columnValues[5], self.rowValues[1]), vector(self.columnValues[9], self.rowValues[1]), vector(self.columnValues[12], self.rowValues[1])], #second row
            [vector(self.columnValues[0], self.rowValues[2]), vector(self.columnValues[2], self.rowValues[2]), vector(self.columnValues[4], self.rowValues[2]), vector(self.columnValues[5], self.rowValues[2]), vector(self.columnValues[9], self.rowValues[2]), vector(self.columnValues[11], self.rowValues[2]), vector(self.columnValues[12], self.rowValues[2])], #third row
            [vector(self.columnValues[0], self.rowValues[3]), vector(self.columnValues[2], self.rowValues[3]), vector(self.columnValues[4], self.rowValues[3]), vector(self.columnValues[9], self.rowValues[3]), vector(self.columnValues[11], self.rowValues[3])], #fourth row
            [vector(self.columnValues[0], self.rowValues[4]), vector(self.columnValues[2], self.rowValues[4]), vector(self.columnValues[4], self.rowValues[4]), vector(self.columnValues[5], self.rowValues[4]), vector(self.columnValues[6], self.rowValues[4]), vector(self.columnValues[9], self.rowValues[4]), vector(self.columnValues[11], self.rowValues[4])], #fifth row
            [vector(self.columnValues[0], self.rowValues[5]), vector(self.columnValues[2], self.rowValues[5]), vector(self.columnValues[6], self.rowValues[5]), vector(self.columnValues[8], self.rowValues[5]), vector(self.columnValues[9], self.rowValues[5]), vector(self.columnValues[11], self.rowValues[5]), vector(self.columnValues[12], self.rowValues[5]), vector(self.columnValues[13], self.rowValues[5])], #sixth row
            [vector(self.columnValues[0], self.rowValues[6]), vector(self.columnValues[2], self.rowValues[6]), vector(self.columnValues[3], self.rowValues[6]), vector(self.columnValues[4], self.rowValues[6]), vector(self.columnValues[6], self.rowValues[6]), vector(self.columnValues[8], self.rowValues[6]), vector(self.columnValues[13], self.rowValues[6])], #seventh row
            [vector(self.columnValues[0], self.rowValues[7]), vector(self.columnValues[4], self.rowValues[7]), vector(self.columnValues[6], self.rowValues[7]), vector(self.columnValues[8], self.rowValues[7]), vector(self.columnValues[9], self.rowValues[7]), vector(self.columnValues[12], self.rowValues[7]), vector(self.columnValues[13], self.rowValues[7])], #eighth row
            [vector(self.columnValues[0], self.rowValues[8]), vector(self.columnValues[4], self.rowValues[8]), vector(self.columnValues[6], self.rowValues[8]), vector(self.columnValues[9], self.rowValues[8]), vector(self.columnValues[12], self.rowValues[8])], #ninth row
            [vector(self.columnValues[0], self.rowValues[9]), vector(self.columnValues[1], self.rowValues[9]), vector(self.columnValues[2], self.rowValues[9]), vector(self.columnValues[3], self.rowValues[9]), vector(self.columnValues[4], self.rowValues[9]), vector(self.columnValues[6], self.rowValues[9]), vector(self.columnValues[7], self.rowValues[9]), vector(self.columnValues[8], self.rowValues[9]), vector(self.columnValues[9], self.rowValues[9]), vector(self.columnValues[12], self.rowValues[9]), vector(self.columnValues[13], self.rowValues[9]), vector(self.columnValues[14], self.rowValues[9])]  #tenth row 
        ]
        self.window.fill((204,82,0))
        for i in range(0,10):
            for j in self.pathBlocks[i]:
                pygame.draw.rect(self.window, (204,78,0), (j.x, j.y, 73, 70))
        pygame.draw.rect(self.window, (57,255,20), (self.columnValues[14], self.rowValues[9], 73, 70))
        pygame.draw.rect(self.window, (0,0,0),(self.position["x"], self.position["y"], 50,50))
        pygame.display.update()






def main():
    pygame.init()
    root = tk.Tk()
    menuWindow = launcher(root)
    menuWindow.setUpMain()
    root.mainloop()


main()

