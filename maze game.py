import tkinter as tk
import pygame
import mysql.connector
from tkinter import messagebox
from time import time





class launcher():
    def __init__(self, window):
        #general widgets
        self.window = window
        self.congratsWindow = tk.Toplevel(window, bg = "#004ecc")
        self.congratsWindow.withdraw()
        self.congratsWindow.protocol("WM_DELETE_WINDOW", self.congratsWindow.withdraw) #when close window button is pressed, hides window instead

        #sets window dimensions, and makes it so that the size cannot be changed
        self.window.geometry("1095x700")
        self.window.minsize(1095,700)
        self.window.maxsize(1095,700)
        self.congratsWindow.geometry("325x100")
        self.congratsWindow.minsize(325,100)
        self.congratsWindow.maxsize(325,100)

        #makes lists from 0-(n-1) inclusive        
        self.rowColumn = list(range(19))
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

        #leaderboard widgets and variables
        self.leaderboardTitle = tk.Label(self.mainFrame, text = "Leaderboard", fg = "white", bg = "#004ecc", font = ("Helvetica", 20))
        self.leaderboardDisplay = tk.Text(self.mainFrame,  fg = "white", bg = "#004ecc", font = ("Courier", 14), wrap = "none", selectbackground = "#004ecc", highlightcolor = "#cc5200")
        self.changeDisplay = tk.Button(self.mainFrame, text = "Fastest Times", command = self.setUpLeaderboardDisplay, font = ("Helvetica", 12))
        self.insertString = ""

        #signup/login widgets
        self.signUpTitle = tk.Label(self.mainFrame, text = "New Account", fg = "white", bg = "#004ecc", font = ("Helvetica", 20))
        self.loginTitle = tk.Label(self.mainFrame, text = "Login", fg = "white", bg = "#004ecc", font = ("Helvetica", 20))
        self.userNameTitle = tk.Label(self.mainFrame, text = "Username", fg = "white", bg = "#004ecc", font = ("Helvetica", 12))
        self.userNameInput = tk.Entry(self.mainFrame, font = ("Helvetica", 10))
        self.passwordTitle = tk.Label(self.mainFrame, text = "Password", fg = "white", bg = "#004ecc", font = ("Helvetica", 12))
        self.passwordInput = tk.Entry(self.mainFrame, font = ("Helvetica", 10), show = "*")
        self.signUpButton = tk.Button(self.mainFrame, text = "Create Account" , command = self.sqlSignUp, font = ("Helvetica", 12))
        self.loginButton = tk.Button(self.mainFrame, text = "Login" , command = self.sqlLogin, font = ("Helvetica", 12))
        
        #congrats window widget
        self.congratsTitle = tk.Label(self.congratsWindow, text= "Congratulations! You won!", fg = "white", bg = "#004ecc", font = ("Helvetica", 20))
        self.congratsTitle.pack()
        self.completedTime = tk.Label(self.congratsWindow, text = "", fg = "white", bg = "#004ecc", font = ("Helvetica", 16))
        self.completedTime.pack(pady=(0,5))
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
        self.userNameCheck = "SELECT username FROM Users WHERE username = %s"
        self.passwordCheck = "SELECT username, Users.password FROM Users WHERE username = %s AND Users.password = %s"
        self.newTime = "INSERT INTO mazetimes (time, level, userName) VALUES (%s,%s,%s)"
        self.getFastTimes = "SELECT level, username, time FROM mazetimes ORDER BY level DESC, time ASC"
        self.getFastUsers = "SELECT username, ROUND(AVG(time),2) FROM mazetimes GROUP BY username"
        self.sqlUserValues = []
        self.sqlTimeValues = []
        self.sqlResult = []
        self.time = 0.0






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
        try:
            if self.sqlUserValues == []:
                raise Exception
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
        except Exception:
            messagebox.showerror(title = "Error", message = "Please login to an account before playing")

    def setUpLeaderboard(self):
        for widget in self.mainFrame.winfo_children():
            widget.grid_forget()
        self.leaderboardTitle.grid(column = 9, row = 0)
        self.leaderboardDisplay.grid(column = 9, row = 1)
        self.changeDisplay.grid(column = 9, row = 2, ipadx = 131)
        self.mainMenu.grid(column = 9, row = 3, pady = 2, ipadx = 158)
        self.quitButton.grid(column = 9, row = 4, pady = 2, ipadx = 144)
        self.setUpLeaderboardDisplay()
        self.leaderboardDisplay.config(state = "disabled")
        
        

    def setUpLeaderboardDisplay(self):
        self.leaderboardDisplay.config(state = "normal")
        self.leaderboardDisplay.delete("1.0", "end")
        if self.changeDisplay["text"] == "Fastest Times":
            self.sqlGetFastTimes()
            self.leaderboardDisplay.insert("1.0", "Level    User        Time (seconds)\n")
            self.leaderboardDisplay.tag_add("highlightline", "1.0", "2.0")
            self.leaderboardDisplay.tag_config("highlightline", background = "#cc5200", foreground = "black")
            #string manipulation so that everything aligns
            for i in range(0,len(self.sqlResult)):
                self.insertString = ""
                self.insertString += str(self.sqlResult[i][0]) + "        " + self.sqlResult[i][1]
                for j in range(0,(12-len(self.sqlResult[i][1]))):
                    self.insertString += " "
                self.insertString += str(self.sqlResult[i][2])
                self.insertString += "\n"
                self.leaderboardDisplay.insert("end", self.insertString)
            self.changeDisplay.config(text = "Fastest Users")
            self.changeDisplay.grid(column = 9, row = 2, ipadx = 132)
            self.leaderboardDisplay.config(state = "disabled")
        else:
            self.sqlGetFastUsers()
            self.leaderboardDisplay.insert("1.0", "User        Avg Time (seconds)\n")
            self.leaderboardDisplay.tag_add("highlightline", "1.0", "2.0")
            self.leaderboardDisplay.tag_config("highlightline", background = "#cc5200", foreground = "black")
            #insertion sort
            for i in range(1, len(self.sqlResult)):
                self.insert = self.sqlResult[i]
                j = i
                while self.insert[1] < self.sqlResult[j-1][1] and j > 0:
                    self.sqlResult[j] = self.sqlResult[j-1]
                    j -= 1
                self.sqlResult[j] = self.insert
            #string manipulation so everything aligns
            for i in range(0,len(self.sqlResult)):
                self.insertString = ""
                self.insertString += self.sqlResult[i][0]
                for j in range(0,(12-len(self.sqlResult[i][0]))):
                    self.insertString += " "
                self.insertString += str(self.sqlResult[i][1])
                self.insertString += "\n"
                self.leaderboardDisplay.insert("end", self.insertString)
            self.changeDisplay.config(text = "Fastest Times")
            self.changeDisplay.grid(column = 9, row = 2, ipadx = 131)
            self.leaderboardDisplay.config(state = "disabled")



    def setUpLogin(self):
        for widget in self.mainFrame.winfo_children():
            widget.grid_forget()
        self.loginTitle.grid(column = 9, row = 0)
        self.userNameTitle.grid(column = 9, row = 2, padx = (0,1000))
        self.userNameInput.grid(column = 9, row = 3, padx = (0,948))
        self.passwordTitle.grid(column = 9, row = 4, padx = (0,1000))
        self.passwordInput.grid(column = 9, row = 5, padx = (0,948))
        self.loginButton.grid(column= 9, row = 16, pady = 2, ipadx = 161)
        self.mainMenu.grid(column = 9, row = 17, pady = 2, ipadx = 158)
        self.quitButton.grid(column = 9, row = 18, pady = 2, ipadx = 144)
        self.userNameInput.delete(0,"end")
        self.passwordInput.delete(0,"end")

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
        


    def levelOne(self):
        self.firstLevel = levelOne()
        self.firstLevel.run()
        pygame.quit()
        if self.firstLevel.win == True:
            self.time = round(self.firstLevel.endTime - self.firstLevel.startTime,2)
            self.congrats(1)
        

    def levelTwo(self):
        self.secondLevel = levelTwo()
        self.secondLevel.run()
        pygame.quit()
        if self.secondLevel.win == True:
            self.time = round(self.secondLevel.endTime - self.secondLevel.startTime,2)
            self.congrats(2)

    def levelThree(self):
        self.thirdLevel = levelThree()
        self.thirdLevel.run()
        pygame.quit()
        if self.thirdLevel.win == True:
            self.time = round(self.thirdLevel.endTime - self.thirdLevel.startTime,2)
            self.congrats(3)

    def levelFour(self):
        self.fourthLevel = levelFour()
        self.fourthLevel.run()
        pygame.quit()
        if self.fourthLevel.win == True:
            self.time = round(self.fourthLevel.endTime - self.fourthLevel.startTime,2)
            self.congrats(4)
    
    def levelFive(self):
        self.fifthLevel = levelFive()
        self.fifthLevel.run()
        pygame.quit()
        if self.fifthLevel.win == True:
            self.time = round(self.fifthLevel.endTime - self.fifthLevel.startTime,2)
            self.congrats(5)

    def congrats(self, level): 
        self.completedTime.config(text = "You completed the maze in %ss" % (self.time))
        self.sqlNewTime(level)
        self.congratsWindow.deiconify()
    
    def sqlSignUp(self):
        try:
            #mysql checks not currently working, wait for that fix before implementing further errors
            self.sqlUserValues.clear()
            self.sqlUserValues.append(self.userNameInput.get())
            self.sqlUserValues.append(self.passwordInput.get())
            if self.sqlUserValues[0] == "":
                raise WrongUsername
            elif self.sqlUserValues[1] == "":
                raise WrongPassword
            self.myCursor.execute(self.newUser, self.sqlUserValues)
            self.myDB.commit()
            self.setUpMain()
        except mysql.connector.errors.IntegrityError:
            self.sqlUserValues.clear()
            messagebox.showerror(title = "Error", message = "That username is already taken")
        except WrongUsername:
            self.sqlUserValues.clear()
            messagebox.showerror(title = "Error", message = "Please enter a valid username")
        except WrongPassword:
            self.sqlUserValues.clear()
            messagebox.showerror(title = "Error", message = "Please enter a valid password")

    def sqlLogin(self):
        try:
            self.sqlUserValues.clear()
            self.sqlUserValues.append(self.userNameInput.get())
            self.myCursor.execute(self.userNameCheck, self.sqlUserValues)
            self.sqlResult = self.myCursor.fetchall()
            if self.sqlResult == []:
                raise WrongUsername
            self.sqlUserValues.append(self.passwordInput.get())
            self.myCursor.execute(self.passwordCheck, self.sqlUserValues)
            self.sqlResult = self.myCursor.fetchall()
            if self.sqlResult == []:
                raise WrongPassword
            self.setUpMain()
        except WrongUsername:
            self.sqlUserValues.clear()
            messagebox.showerror(title = "Error", message = "That username is incorrect")
        except WrongPassword:
            self.sqlUserValues.clear()
            messagebox.showerror(title = "Error", message = "That password is incorrect")
    
    def sqlNewTime(self,level):
        self.sqlTimeValues.clear()
        self.sqlTimeValues.append(self.time)
        self.sqlTimeValues.append(level)
        self.sqlTimeValues.append(self.sqlUserValues[0])
        self.myCursor.execute(self.newTime, self.sqlTimeValues)
        self.myDB.commit()

    def sqlGetFastTimes(self):
        self.myCursor.execute(self.getFastTimes)
        self.sqlResult = self.myCursor.fetchall()
    
    def sqlGetFastUsers(self):
        self.myCursor.execute(self.getFastUsers)
        self.sqlResult = self.myCursor.fetchall()
        


class game():
    def __init__(self):
        pygame.init()
        self.startTime = 0.0
        self.endTime = 0.0
        pygame.key.set_repeat(500,25)
        self.window = pygame.display.set_mode((1095, 700))
        self.clockRate = pygame.time.Clock()
        #each block in maze is 73 by 70
        #therefore each row is 15 blocks, and each column is 10 blocks
        self.rowValues = [0,70,140,210,280,350,420,490,560,630] #the start y value for each row
        self.columnValues = [0, 73, 146, 219, 292, 365, 438, 511, 584, 657, 730, 803, 876, 949, 1022] #the start x value for each column
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
            self.move["x pos"], self.move["x neg"], self.move["y pos"], self.move["y neg"] = 10,10,10,10
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
                self.move["x pos"], self.move["x neg"], self.move["y pos"], self.move["y neg"] = 10,10,10,10
                self.position["x"], self.position["y"] = 0,0

            if self.totalMove["x"] == 0:
                self.move["x pos"], self.move["x neg"] = 10, 10

            if self.totalMove["y"] == 0:
                self.move["y pos"], self.move["y neg"] = 10, 10
            
            if self.position["x"] + self.totalMove["x"] <= self.columnValues[14] + 73 and self.position["x"] + self.totalMove["x"] >= self.columnValues[14] and self.position["y"] + self.totalMove["y"] <= self.rowValues[9] + 70 and self.position["y"] + self.totalMove["y"] >= self.rowValues[9]:
                self.win = True
                self.running = False  
                self.endTime = time() 

            elif self.position["x"] + self.totalMove["x"] + 50 <= self.columnValues[14] + 73 and self.position["x"] + self.totalMove["x"] + 50 >= self.columnValues[14] and self.position["y"] + self.totalMove["y"] <= self.rowValues[9] + 70 and self.position["y"] + self.totalMove["y"] >= self.rowValues[9]:
                self.win = True
                self.running = False
                self.endTime = time()
            elif self.position["y"] + self.totalMove["y"] + 50 <= self.rowValues[9] + 70 and self.position["y"] + self.totalMove["y"] + 50 >= self.rowValues[9] and self.position["x"] + self.totalMove["x"] + 50 <= self.columnValues[14] + 73 and self.position["x"] + self.totalMove["x"] + 50 >= self.columnValues[14]:
               self.win = True
               self.running = False
               self.endTime = time()
            elif self.position["y"] + self.totalMove["y"] + 50 <= self.rowValues[9] + 70 and self.position["y"] + self.totalMove["y"] + 50 >= self.rowValues[9] and self.position["x"] + self.totalMove["x"] <= self.columnValues[14] + 73 and self.position["x"] + self.totalMove["x"] >= self.columnValues[14]:
                self.win = True
                self.running = False
                self.endTime = time()

    def render(self, colour):
        self.window.fill((204,82,0))
        for i in range(0,10):
            for j in self.pathBlocks[i]:
                pygame.draw.rect(self.window, colour, (j.x, j.y, 73, 70))
        pygame.draw.rect(self.window, (57,255,20), (self.columnValues[14], self.rowValues[9], 73, 70))
        pygame.draw.rect(self.window, (0,0,0),(self.position["x"], self.position["y"], 50,50))
        pygame.display.update()

    def run(self):
        self.startTime = time()
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
        super().render((0,78,204))

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
        super().render((51,78,153))

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
        super().render((102,78,102))

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
        super().render((153,78,51))

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
        super().render((204,78,0))

class vector():
    def __init__(self, paramX, paramY):
        self.x = paramX
        self.y = paramY

#error definitions for sql
class WrongUsername(Exception):
    pass
class WrongPassword(Exception):
    pass



def main():
    root = tk.Tk()
    menuWindow = launcher(root)
    menuWindow.setUpMain()
    root.mainloop()


main()

