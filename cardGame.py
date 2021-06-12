#
#
# ██████╗██╗  ██╗ █████╗ ██████╗ ██╗   ██╗    ███╗   ███╗ █████╗ ███╗   ██╗ ██████╗ ██╗    ██╗
#██╔════╝██║  ██║██╔══██╗██╔══██╗╚██╗ ██╔╝    ████╗ ████║██╔══██╗████╗  ██║██╔═══██╗██║    ██║
#██║     ███████║███████║██████╔╝ ╚████╔╝     ██╔████╔██║███████║██╔██╗ ██║██║   ██║██║ █╗ ██║
#██║     ██╔══██║██╔══██║██╔══██╗  ╚██╔╝      ██║╚██╔╝██║██╔══██║██║╚██╗██║██║   ██║██║███╗██║
#╚██████╗██║  ██║██║  ██║██████╔╝   ██║       ██║ ╚═╝ ██║██║  ██║██║ ╚████║╚██████╔╝╚███╔███╔╝
# ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝    ╚═╝       ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝  ╚══╝╚══╝ 
#                                                                                             
#
#                 ___         |              ( ( (             .                         |              _   _      #   ___         
#     ooo          .|||.        |.===.       '. ___ .'       ,-_-|             )))         |.===.        '\\-//`     #  <_*_>     
#    (o o)         (o o)        {}o o{}     '  (> <) '      ([o o])           (o o)        {}o o{}        (o o)      #  (o o)      
#ooO--(_)--Ooo-ooO--(_)--Ooo-ooO--(_)--Ooo-ooO--(_)--Ooo-ooO--(_)--Ooo----ooO--(_)--Ooo-ooO--(_)--Ooo-ooO--(_)--Ooo--8---(_)--Ooo-
###########################################################################################################################################
#                                                                                                                                         #
# HI-LOW game from Chabymanow                                                                                                             #
# You can play alone or against another player.                                                                                           #
# All player start with 100$. The players can set the amount of bet.                                                                      #
# If someone lost all money, that player lost the game.                                                                                   #
#                                                                                                                                         #
# This program can`t working perfectly in the editor, but it`s fine in the windows shell. I can`t check it on linux, but should be good   #
#                                                                                                                                         #
###########################################################################################################################################
import cards
import random
from os import system, name
import time
import sys

ranks = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
suits = ["Clubs","Hearts","Diamonds","Spades"]
deck = []
player1 = ""
player2 = ""
whatPlayer = 1
choice = ""
actCard = 0
nextCard = 0
actCardNumber = 0
nextValue = 0
actValue = 0
Message = ""
gameOver = False
multiGame = False
reason = 0
happening = 0
name1 = ""
name2 = ""

class Player:
    def __init__(self, name = "Anonymus", money = 0, bet = 0):
        self.Name = name
        self.Money = money
        self.Bet = bet        
        
    def setName(self, name):
        self.Name = name
        
    def getName(self):
        return str(self.Name)
    
    def setMoney(self, money):
        self.Money = money
        
    def getMoney(self):
        return int(self.Money)

    def setBet(self, bet):
        self.Bet = bet
        
    def getBet(self):
        return self.Bet

def myClear():
    if name == 'nt':
        _ = system ('cls')
        
    else:
        _= system('clear')

def drawLogo():
    myClear()
    print("\n")
    print(" "*10+"██╗  ██╗██╗      ██╗      ██████╗ ██╗    ██╗")
    print(" "*10+"██║  ██║██║      ██║     ██╔═══██╗██║    ██║")
    print(" "*10+"███████║██║█████╗██║     ██║   ██║██║ █╗ ██║")
    print(" "*10+"██╔══██║██║╚════╝██║     ██║   ██║██║███╗██║")
    print(" "*10+"██║  ██║██║      ███████╗╚██████╔╝╚███╔███╔╝")
    print(" "*10+"╚═╝  ╚═╝╚═╝      ╚══════╝ ╚═════╝  ╚══╝╚══╝")

def initMulti():
    global player1, player2, whatPlayer, name1, name2
    
    whatPlayer = 1
    drawLogo()
    for rank in ranks:
        for suit in suits:
            deck.append([suit, rank])
    random.shuffle(deck)     
    if name1 == "" or name1 == "--help":    
        name1 = str(input("What is your name player1: "))
    else:
        print("Player1 name is {}".format(player1.getName()))        
    if "--help" in name1:
        drawHelp(4)
    else:
        player1 = Player(name1, 100)
        
    if name2 == "" or name2 == "--help":     
        name2 = str(input("What is your name player2: "))
    if "--help" in name2:
        drawHelp(4)
    else:
        player2 = Player(name2, 100)
    drawScreen()

def initSingle():
    global player1, player2, whatPlayer, happening
    
    whatPlayer = 1
    drawLogo()
    for rank in ranks:
        for suit in suits:
            deck.append([suit, rank])
    random.shuffle(deck)         
    name1 = str(input("What is your name player1: "))
    if "--help" in name1:
        drawHelp(5)
    else:
        player1 = Player(name1, 100)
        player2 = Player("No player", 0)
    happening = 3
    drawScreen()

def drawHeader():
    global player1, player2, Message
    
    space = 35-len(player1.getName())
    space1 = 33-len(str(player1.getMoney()))
    print(" "*5+"Name: "+player1.getName()+" "*space+"Name: "+player2.getName())
    print(" "*5+"Money: "+str(player1.getMoney())+"$"+" "*space1+"Money: "+str(player2.getMoney())+"$")
    print("\n")
    print(" "*20+str(Message)+"\n")
    
def drawScreen():
    global player1, player2, Message, reason
    
    drawLogo()
    drawHeader()
    if gameOver == False:
        print (changeCard())        
        betting()  
    else:
        print (changeCard())
        drawReason(reason)
        input(" "*18+"Press Enter to continue...")
        drawMenu()
        
def drawReason(reason):
    global multiGame
    if reason == 1:
        if multiGame:
            return print(" "*13+"{} lost all money! {} WIN!".format(player1.getName(), player2.getName()))
        else:
            return print(" "*16+"{} lost all money! Sorry".format(player1.getName(), player2.getName()))
    elif reason == 2:
        return print(" "*13+"{} lost all money! {} WIN!".format(player2.getName(), player1.getName()))
    elif reason == 3:
        return print(" "*17+"This was the last card. No winner!")

def changeCard():
    global actCard, nextCard, actCardNumber, actValue, nextValue

    actCard = cards.Card(deck[actCardNumber][0], deck[actCardNumber][1])
    nextCard = cards.Card(deck[actCardNumber+1][0], deck[actCardNumber+1][1])
    actValue = actCard.getValue()
    nextValue = nextCard.getValue()
    return cards.drawHiddenCard(nextCard, actCard)
    
def checkBetValue(message):
    
    while True:
      print("Press x to exit or write --help to help")
      userInput = input(message)
      try:
         val = int(userInput)
         #userInput = int(input(message))   
      except ValueError:
          try:
              val = str(userInput)
              if "--help" in userInput:
                  drawHelp(2)
              elif userInput == "x":
                  drawMenu()
              else:
                  print("Not a valid command! Try again.")
                  continue
                  #break
          except ValueError:
              print("Not a valid bet! Try again.")
              continue
      else:
         return val 
         break  

def drawMenu():
    global multiGame, reason, gameOver, actCardNumber, Message, name1, name2
    
    reason = 0
    gameOver = False
    actCardNumber = 0
    Message = ""
    name1 = ""
    name2 = ""
    drawLogo()
    print("\n"+" "*30+"Game Menu")
    print(" "*29+"-----------")
    print(" "*25+"1: Single player game")
    print(" "*25+"2: Two player game")
    print(" "*25+"H: Help")
    print(" "*25+"x: Exit")
    choise = str(input(""))
    if choise[0] == "1":
        multiGame = False
        initSingle()
    elif choise[0] == "2":
        multiGame = True
        initMulti()
    elif choise[0].lower() == "h":
        drawHelp(0)
    elif choise[0].lower() == "x":
        sys.exit()

def drawHelp(fromWhere):   
    drawLogo()
    print("\n")
    print(" "*15+"How to play high low card game?")
    print(" "*15+"-------------------------------")
    print("When cards are shuffled, the dealer will place one card face-down on the table and another one face-up.")
    print("He will set aside the rest of the deck; players will then start predicting the value.")
    print("After cards are dealt, the player is required to make his first bet. The house will then match the bet to the pot.")
    print("The player is then required to predict whether the card is high or low")
    print("  he will win or lose the pot depending on the results of his prediction.")
    print("Depending on the card that shows, the player needs to make a guess on whether the face-down")
    print("  card will be higher or lower than the face-up card.")
    print("When the guessing is over, the dealer will flip the face-down card to show.")
    print("When the guess is correct, the player will win and is able to choose to either double or collect winnings.")
    print("When the guess is incorrect, the player will lose.") 
    print("\n")
    while True:
        back = input(" "*18+"Write --resume to go back...")
        if "--resume" in back:
            if fromWhere == 0:
                drawMenu()
            elif fromWhere == 1:
                drawScreen()
            elif fromWhere == 2:
                betting()
            elif fromWhere == 3:
                decision()
            elif fromWhere == 4:
                initMulti()
            elif fromWhere == 5:
                initSingle()        

def drawGame():
    drawLogo()
    drawHeader()
    print (changeCard()) 
    
def decision():
    global whatPlayer, player1, player2, choice, gameOver, multiGame, happening
    
    drawGame()
    choice = ""
    if multiGame == True:
        if not gameOver:
            if whatPlayer == 1:
                while True:
                    print("Press x to exit or write --help to help")
                    choice = str(input("Higher or Lower?"))
                    if len(choice) > 0:
                        if choice[0].lower() in ["h", "l", "x"] or choice == "--help":
                            break   
                                        
            elif whatPlayer == 2:
                while True:
                    print("Press x to exit or write --help to help")
                    choice = str(input("Higher or Lower?"))
                    if len(choice) > 0:
                        if choice[0].lower() in ["h" ,"l" ,"x"] or choice == "--help":
                            break
            if choice[0] == "x":
                gameOver = True
                drawMenu()
            if "--help" in choice:
                drawHelp(3)
    elif multiGame == False:
            if not gameOver:
                while True:
                    print("Press x to exit or write --help to help")
                    choice = str(input("Higher or Lower?"))
                    if len(choice) > 0:
                        if choice[0].lower() in ["h", "l", "x"] or choice == "--help":
                            break   
    if choice[0] == "x":
        gameOver = True
        drawMenu()
    if "--help" in choice:
        drawHelp(3)
    checkBetting(choice)            
    
def betting():
    global whatPlayer, player1, player2, choice, gameOver, multiGame, happening
    
    drawGame()
    if multiGame:
        if not gameOver:
            if whatPlayer == 1:
                while True:
                    print("{} please take your bet: ".format(player1.getName()))
                    bet = checkBetValue("Bet:")
                    if int(bet) >= player1.getMoney():
                        player1.setBet(player1.getMoney())   
                        player1.setMoney(player1.getMoney()-player1.getBet())
                    else:
                        player1.setBet(bet)
                        player1.setMoney(player1.getMoney()-player1.getBet()) 
                    break                
            elif whatPlayer == 2:
                while True:
                    print("{} please take your bet: ".format(player2.getName()))
                    bet = checkBetValue("Bet:")
                    if int(bet) <= player2.getMoney():
                        player2.setBet(bet)
                        player2.setMoney(player2.getMoney()-player2.getBet())
                    else:
                        player2.setBet(player2.getMoney())
                        player2.setMoney(player2.getMoney()-player2.getBet())
                    break
            decision()
    elif multiGame == False:
            if not gameOver:
                while True:
                    print("{} please take your bet: ".format(player1.getName()))
                    bet = checkBetValue("Bet: ")
                    if int(bet) >= player1.getMoney():
                        player1.setBet(player1.getMoney())  
                        player1.setMoney(player1.getMoney()-player1.getBet())
                        break
                    else:
                        player1.setBet(bet)
                        player1.setMoney(player1.getMoney()-player1.getBet())
                        break

    print(str(player1.getBet())+":"+str(player1.getMoney()))
    decision()
                
def checkBetting(choice):
     global actCardNumber, actValue, nextValue, whatPlayer, Message, gameOver, multiGame, reason, player1, player2
     
     if multiGame:
         if choice[0] == "h" and nextValue > actValue:
             if whatPlayer == 1:
                 Message = "Correct. {} win {}$".format(player1.getName(), player1.getBet())
                 player1.setMoney(player1.getMoney()+(player1.getBet()*2))
             elif whatPlayer == 2:
                 Message = "Correct. {} win {}$".format(player2.getName(), player2.getBet())
                 player2.setMoney(player2.getMoney()+(player2.getBet()*2))
         elif choice[0] == "h" and nextValue < actValue:
             if whatPlayer == 1:
                  Message = "Wrong. {} lose {}$".format(player1.getName(), player1.getBet())
             elif whatPlayer == 2:
                  Message = "Wrong. {} lose {}$".format(player2.getName(), player2.getBet())
         elif choice[0] == "l" and nextValue < actValue:
             if whatPlayer == 1:
                 Message = "Correct. {} win {}$".format(player1.getName(), player1.getBet())
                 player1.setMoney(player1.getMoney()+(player1.getBet()*2))
             elif whatPlayer == 2:
                 Message = "Correct. {} win {}$".format(player2.getName(), player2.getBet())
                 player2.setMoney(player2.getMoney()+(player2.getBet()*2))
         elif choice[0] == "l" and nextValue > actValue:
             if whatPlayer == 1:
                  Message = "Wrong. {} lose {}$".format(player1.getName(), player1.getBet())
             elif whatPlayer == 2:
                  Message = "Wrong. {} lose {}$".format(player2.getName(), player2.getBet())
         else:
             if whatPlayer == 1:
                 Message = "Draw! {} get back the bet".format(player1.getName())
                 player1.setMoney(player1.getMoney()+(player1.getBet()))
             elif whatPlayer == 2:
                 Message = "Draw! {} get back the bet".format(player2.getName())
                 player2.setMoney(player2.getMoney()+(player2.getBet()))
     else:
         if choice[0] == "h" and nextValue > actValue:
            Message = "Correct. {} win {}$".format(player1.getName(), player1.getBet())
            player1.setMoney(player1.getMoney()+(player1.getBet()*2))
         elif choice[0] == "h" and nextValue < actValue:
            Message = "Wrong. {} lose {}$".format(player1.getName(), player1.getBet())
         elif choice[0] == "l" and nextValue < actValue:
            Message = "Correct. {} win {}$".format(player1.getName(), player1.getBet())
            player1.setMoney(player1.getMoney()+(player1.getBet()*2))
         elif choice[0] == "l" and nextValue > actValue:
            Message = "Wrong. {} lose {}$".format(player1.getName(), player1.getBet())
         else:
            Message = "Draw! {} get back the bet".format(player1.getName())
            player1.setMoney(player1.getMoney()+(player1.getBet()))
     
     time.sleep(1)
     if whatPlayer == 1:
         whatPlayer = 2
     else:
         whatPlayer = 1
     
     actCardNumber += 1
     
     if actCardNumber >= len(deck):
         gameOver = True
         reason = 3
     if player1.getMoney() <= 0:
         gameOver = True
         reason = 1
     
     if multiGame and player2.getMoney() <= 0:
         gameOver = True
         reason = 2
     drawScreen()

        
# def game():
#     global happening
                 
#         drawMenu() 
#     elif happening == 1:
#         happening = 2
#         drawScreen()
     
#init() 
drawMenu()  

# print("The card`s value is: "+str(cardValue))
# print("The card`s value is: "+str(cardValue1))
# if cardValue1 > cardValue:
#     print("You lost!")


# for x in range(len(deck)):
#     print("{} : {}".format(deck[x][0], deck[x][1]))
# for x in range(len(deck)):
#         number = deck[x][1]
#         suit = deck[x][0]
#         myCard = cards.Card(suit, number)
#         print(cards.drawCard(myCard))