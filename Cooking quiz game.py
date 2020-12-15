import random
import time
import wikipedia
import tkinter as tk
global score

class Question:
    def __init__(self, question, answer, points = 100):
        self.q = question
        self.a = answer
        self.r = ""
        self.p = points

    @property
    def points(self):
        return self.p
        
    # show the user a question and get their answer, returns true if they got it correct and false if they were wrong
    def ask(self, player_name):
        #Creates a window for player to answer the question
        window = tk.Tk()
        question = tk.Label(window, font=('calibre',20), text="(" + player_name + "): " + self.q)
        response = tk.Entry(window, font=('calibre',20))
        #Once player responds the window gets deleted and it pops up with new window for next player
        def on_enter(e):
            self.r = response.get()
            window.destroy()
            #Once player hits enter then will loop to ask another question
        window.bind("<Return>", on_enter)
        question.pack()
        response.pack()
        window.mainloop()

        if self.r.lower() == self.a.lower():
            return True
        else:
            return False

#This class assigns the name to the player and to add points to the certain player
class Player:
    def __init__(self, name):
        self.n = name
        self.score = 0

    @property
    def name(self):
        return self.n

    def add_points(self, points):
        self.score += points


class Round:
    #playercount
    def __init__(self, players, questions):
        self.p = players
        self.q = []

        for player in players:
            self.q.append(random.choice(questions))
#Asking the player a new question
    def ask(self, player_index):
        question = self.q[player_index]
        player = self.p[player_index]

        print("It is " + player.name + "'s turn to answer a question!")
        print("Please enter in the textbox in the window that just appeared.")
        correct = question.ask(player.name)
#if person got correct than tell them and add points
        if correct:
            player.add_points(question.points)
            print(player.name + "got their question correct!")
        else:
            print(player.name + " got their question incorrect!")
            print("If you would like to know what the correct answer is please look into the Q&A.txt file.\nOr you can research it after the game.")

        print(player.name + " has " + str(player.score) + " points.")
        
    def start(self):
        for x in range(0, len(self.p)):
            self.ask(x)
        
    
#Question, answer, points
            #40 questions so far
            #Note to self: If you need to add more questions remeber to put a ',' after each one.-_-
quiz_questions = [
    Question("What is the process of letting foods cook in their juices?", "sweating"),
    Question("What is the process of cutting foods into cubes?","Dicing"),
    Question("What type of wood should NOT be used for smoking foods on outdoor grills?", "Softwoods"),
    Question("What should you look for when buying mussels?","Closed shells"),
    Question("What was the 18th century word for flattening chicken?","Spatchcock"),
    Question("What is something that can become even more dangerous than knives in the kitchen?","Spills"),
    Question("What does CAYG mean?","Clean as you go", 200),
    Question("How long should you roast a duck @350F? 11/2 hours, 2 hours, or 21/2 hours?","!1/2 hours"),
    Question("What is the best cook level for meat?\nMedium, Medium rare, or your choice?","Your choice"),
    Question("You may have heard of nut meat, why exactly is it called that?","Solid food"),
    Question("What was the food item that the astronaut was suspended from the GEMINI 3 for?","A corned beef sandwich",300),
    Question("During WW2 what was the rationing in ounces for meat per day for American soldiers?"," 6 ounces"),
    Question("During WW2 what was the rationing in ounces for meat per day for British soldiers?","16 ounces"),
    Question("True or false? It was illegal until recently to sell/export kobe beef that has come from anywhere except China.","True"),
    Question("Which salad dressing got it's name for being popular with the local hunters of the region.","Thousand island"),
    Question("What was the first meal/meat eaten on the moon","Bacon"),
    Question("What year was the first year in recorded history for consumption of fish surpass beef?","2013"),
    Question("What is the process some companies do in order to make beef look more fresh or redder?","Carbon monoxide treatement"),
    Question("How should cooked and uncooked meat go in the fridge","Seperated"),
    Question("How often should you clean your fridge?How many months?","3 months"),
    Question("How often should you clean your oven?","3 months"),
    Question("How many different types of cuts of meat are in a cow?","9"),
    Question("What's the best way to determine if an egg is bad?","Smells bad"),
    Question("What's the most important thing to do before cooking anything?","Wash your hands"),
    Question("True or false? Your knives can break more easily if they are dull.","True"),
    Question("What is the most important thing for a kitchen to be?","Clean"),
    Question("What is the process for a food to be scalding in boiling water then removed and plunged into ice cold water?","Blanching"),
    Question("Process for pouring alcohol over food and ignite.","Flambé"),
    Question("What does OAMC","Once a month cooking", 200),
    Question("What is the outer layer of citrus fruit called especially when you grate it for flavouring ingredient?","Zest"),
    Question("What is a good rule for food and drinks that aren't yours","Not consuming it"),
    Question("What is a good thing to do with food especially leftovers?","Label"),
    Question("When having a shared kitchen with roomates what is a good rule to have for everyone?","Leave it the way you saw or better"),
    Question("What should you do if you notice you are running low on an item everyone uses?","Let them know",150),
    Question("Cooking was and still is considered what part of Science?","Alchemy"),
    Question("What is the most stolen food? Meat, bread, or Cheese","Cheese"),
    Question("If Romans understood lead mining and pipes were toxic did they also know lead cooking vessels were toxic?Yes or No","No"),
    Question("Since 2011 there have been at least 4 incidents of people cooking what inside Walmarts? fish, pancakes/waffles, or meth","Meth"),
    Question("What is a common ingriedient Rome used and is now extinct?","Laser"),
    Question("What is considered the more 'grand' of milk according to medival cooking?","Almond"),
    Question("Were chopsticks created for cooking or eating?","Eating")
]

#This is for personal use so this way I can print out the text file and customize it, I just like having pen and paper rather electronic. :/
class QandA:
    f = open("QandA.txt", "w")
    #techniques
    #1
    f.write("What is the process of letting foods cook in their juices?")
    f.write("Answer = Sweating")
    f.write("What is the process of cutting into cubes?")
    f.write("Answer = Diceing")
    #2
    f.write("What are woods that you should NOT use for smoking foods on an outdoor grill?")
    f.write("Answer = softwoods like Cedar or pine")
    f.write("What should you look for when buying mussels?")
    f.write("Answer = Mussels with closed/snapped shut shells")
    #3
    f.write("What was the 18th century word for flattening chicken?")
    f.write("Answer = Spatchcock")
    f.write("What is the process for a food to be scalding in boiling water then removed and plunged into ice cold water?")
    f.write("Answer = Blanching")
    #4
    f.write("What does OAMC mean?")
    f.write("Answer = Once a month cooking")
    f.write("What is the outer layer of citrus fruit called especially when you grate it for flavouring ingredient?")
    f.write("Zest")
#Cooking etiquitte
    #1
    f.write("What is something that can become even more dangerous than knives in the kitchen?")
    f.write("Answer = Spills")
    f.write("What does CAYG mean?")
    f.write("Answer = Clean as you go")
    #2
    f.write("Should cooked and uncooked meats go into the fridge together")
    f.write("Answer = Seperated and at the bottom of the fridge.")
    f.write("What is the most imporant thing for a kitchen to be?")
    f.write("Answer = Clean")
    #3
    f.write("What's something you should never do unless someone offers?")
    f.write("Answer = Eat/drink things that aren't yours")
    f.write("What's something that people usually don't do with their food?")
    f.write("Answer = Label")
    #4
    f.write("What's a good rule of thumb to remember with using a shared kitchen?")
    f.write("Answer = Leave it the way you saw it as or better")
    f.write("What should you do when you notice that you are running low on an item eveyone uses?")
    f.write("Answer = Let people know by having a place like a list")
    #Meat
    #1
    f.write("How long should you roast a 5 pound duck at 350 degrees F.?")
    f.write("Answer = Around 1 & half hours")
    f.write("What is the best roasting level for any meat?")
    f.write("Answer = Your choice, I don't judge")
    #2
    f.write("During WW2 what was the rationing for meat per day for American soldiers?")
    f.write("Answer = 6 ounces")
    f.write("During WW2 what was the rationing for meat per day for British soldiers?")
    f.write("Answer = 16 ounces")
    #3
    f.write("You might have heard of nut meats, Why is it called that?")
    f.write("Answer = The term meat reffered to any solid food.")
    f.write("According to Newcastle uni researchers, What can cure a hangover?")
    f.write("Answer = Bacon Sandwich") 
    #4
    f.write("What was the first meal eaten on the moon")
    f.write("Answer = Bacon(freeze dried)")
    f.write("What is the percentage of Americans that would support bacon as their 'national food'?")
    f.write("Answer = 65")
    #Interesting facts
    #1
    f.write("What was the thing/food that got the astronaut suspended from GEMINI 3?")
    f.write("Answer = A corned beef sandwich")
    f.write("True or false?\nIt's illegal to sell/export kobe beef that doesn't come from china.")
    f.write("Answer = true")
    #2
    f.write("Which salad dressing got it's name for being popular with outdoor enthusiasts in that region?")
    f.write("Answer = Thousand Island")
    f.write("Cooking was and is still considered what part of Science?")
    f.write("Answer = Alchemy")
    #3
    f.write("What is the most stolen food? Meat, bread, or Cheese")
    f.write("Answer = Cheese")
    f.write("If Romans understood that lead mining and pipes were toxic did they also put 2 and 2 together and not use lead cooking supplies?")
    f.write("Answer = LOL NOPE (I think this also tells how stupid humans can be at times -_-)")
    #4
    f.write("Since 2011 4 incidents happend at Walmarts of people cooking what?")
    f.write("Answer = Meth")
    f.write("What is a common roman ingridient that's now extinct?")
    f.write("Answer = Laser")
    f.write("According to medival cooking what is the most 'grand' milk?")
    f.write("Almond milk. I mean that is very true but that's because Almond milk tastes really good. :p")
    f.close()



def main():
    #Randomizes the questions for the players
    random.shuffle(quiz_questions)
    #Asks how many players are there
    players = []
    plys = int(input("How many players are there?"))
    #Asks for names for the players
    print("Please enter each player's name.")
    for i in range(0,plys):
        #sets the player to player 1, 2 etc.
        player = Player(input("Name of Player #" + str(i + 1) + ": "))
        players.append(player)
    #Asks for how many rounds which is one question per player
    rounds = int(input("How many rounds would you like to play?"))
    #Creates loop to go to each round
    for r in range(0, rounds):
        print("Starting Round #" + str(r + 1) + "!")
        round = Round(players, quiz_questions)
        round.start()
    #The player with most points is top player
    top_player = players[0]
    #Prints out the scores for all players and tells who is the winner/who has the most points
    print("Final Scores:")
    for player in players:
        if player.score > top_player.score:
            top_player = player

        print("\t-" + player.name + ": " + str(player.score))
        
    print("\nThe Winner is: " + top_player.name)
    print("Saving players and scores for this game")
    f = open("GameHistory.txt","at")
    f.write(player.name)
    f.write("\n")
    f.write(str(player.score))
    f.write("\n")
    f.close()
    Research = input("Would you like to research some of the questions?(y/n)")
    if Research == "y":
        userResearch = input("What would you like to research about? Please be specific.")
        print(wikipedia.summary(userResearch, sentences = 4))
    else:
        print("Ok that's fine thank you for playing ^w^")
    
#Plays the program
if __name__ == "__main__":
    main()
