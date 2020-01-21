'''
Com Sci Summative Project
@author: Rakshaa
'''
from Functions import GameFunctions
class Variables(): 
    '''
    Variables that will be used throughout the game are stored here
    '''  
    game_name = "A New Neighbour"
    nights_spent = "1"
    neighbour_name = "???"
    current_room = "FOYER"
    password = "2000"
    bob_gift = ""
    
    action = ""
    
    key_taken = False
    plunger_taken = False
    cookies_taken = False
    candleabra_taken = False
    statue_taken = False
    wine_taken = False
    
    go_to_bob = False
    bob_mad = False
    door_open = False
    photo_album_looked_at = False
    alive = True
    safe_locked = False
    
    item_1 = ""
    item_2 = ""
    item_3 = ""
    
    exploration_timer = 0
    safe_tries = 1



'''
tutorial of how the game would work
'''
print("Welcome to " + Variables.game_name + "! This is a text based game so you will need to type in what you want to do based on the options that" 
      
      + " you are given.")


example = raw_input("Test this out by typing 'next' and then press enter!" + '\n')    
    
example_counter = 0
while example_counter == 0:
    if example.upper() == "NEXT":
        print("Good job!")
        example_counter += 1
        
    else:
        print("Try again")    
        example = raw_input("Type 'next' and then press enter. Make sure that you don't add any spaces at the end of the word!" + '\n')


example2 = raw_input("Are you ready to start? Type 'yes' if you are and 'no' if you are not" + '\n')

example2_counter = 0
while example2_counter == 0:
    if example2.upper() == "YES":
        example2_counter += 1
    
    elif example2.upper() == "NO":
        example3 = raw_input("After compleate this you will go straight in to the game! Type the word 'okay'" + '\n')
        
        example3_counter = 0
        while example3_counter == 0:
            if example3.upper() == "OKAY":
                example3_counter += 1
                example2_counter += 1
        
            else:
                print("Try again")    
                example3 = raw_input("Type 'ok' and then press enter. Make sure that you don't add any spaces at the end of the word!" + '\n')
        
    else:
        example2 = raw_input("Type 'yes' if you are ready to start and 'no' if you are not ready to start" + '\n')

       
print ("Okay let's start!" + '\n')


'''
Title vvv
'''

print ("    .-.      "+ Variables.game_name)
print ("  .'   `.  /")
print ("  :o o   :/")
print ("  : o    `. ")
print ("  :         ``.")
print (" :             `.")
print (":  :         .   `.")
print (":   :          ` . `.")
print (" `.. :            `. ``;")
print ("    `:;             `:'")
print ("       :              `.")
print ("        `.              `.     .")
print ("          `'`'`'`---..,___`;.-'")


'''
Game  vvv
'''

action = raw_input('\n' + "You got an email! You think that it is from the mansion give away that you had entered. Do you want to open it?" + '\n')

counter = 0
while counter == 0:
    if action.upper() == "YES":
        print("Hello, there friend! I see that you have entered the mansion giveaway! And you won the lottery for it! As the contest rules state you will" +
              "spend "  + Variables.nights_spent + " nights in a haunted" + '\n' + "house. If you survive all " + Variables.nights_spent + " nights you will" 
              + "win a 100 billion-dollar mansion and am not legally responsible for anything that happens in the haunted house. Oh" + '\n' + 
              "another thing, by opening this email you legally have to participate, if you don't you will be fined $100 billion! Good Luck!" + '\n')
        counter += 1
        
    else:
        action = raw_input("Are you sure? Type 'yes' if you want to open the email!" + '\n')


item_text = raw_input("'Okay' you thought. 'I would rather have a chance to win a house that is worth $100 billion that pay $100 billion' so you decided to " 
                            "participate." + '\n' + "While packing your suit case you have space to pack something extra. Do you want to bring your portable "
                            + "charger, a book or some cake?" + '\n')

counter = 0

while counter == 0:
    
    if item_text.upper() == "PORTABLE CHARGER":
        Variables.item_1 = "portable charger"
        counter += 1
     
    elif item_text.upper() == "BOOK":
        Variables.item_1 = "book"
        counter += 1
    
    elif item_text.upper() == "CAKE":
        Variables.item_1 = "cake"
        counter += 1
    
    else:
        item_text = raw_input("Do you want to bring your portable charger, a book or some cake?"  + '\n')

print("Okay. You left to go to the adress of the haunted house that was in the e-mail. Once you arrive you see that your neighbour " + 
      "is outside mowing his lawn.")


action = raw_input("Do you want to go talk to your neighbour?"  + '\n')

counter = 0

while counter == 0:
    
    if action.upper() == "YES":
        print("You decided to walk up to your neighbour and talk to him")
        print("??? - Hello there stranger who are you?" + '\n' +
              "You - I'm your new neighbour, I'm going to live in the house next to you for a couple days")
        
        Variables.neighbour_name = "Bob"
        action_2 = raw_input(Variables.neighbour_name + " - Cool! I'm Bob! Your new neighbour then. Do you want to come over to my house after " +
                             "you are settled in?" + '\n')


        while counter == 0:
            
            if action_2.upper() == "YES":
                Variables.exploration_timer = 9
                Variables.go_to_bob = True
                print("You - Yeah sure. I'm fine with comming over." + '\n' + 
                      Variables.neighbour_name + " - Okay neighbour, I'll see you at my place at around 6. Is that fine?" + '\n' + 
                      "You - Okay, sounds good! Bye, Bob!" + '\n' +
                      Variables.neighbour_name + " - Okay! Bye!")
                counter += 1
            
            elif action_2.upper() == "NO":
                Variables.exploration_timer = 12
                print("You - I don't think that I can, sorry!" + '\n' +
                      Variables.neighbour_name + " - That is okay. See you later!" + '\n' +
                      "You - Okay see you later")

                counter += 1
              
            else:
                action_2 = raw_input(Variables.neighbour_name + " - Cool! I'm Bob! Your new neighbour then. Do you want to come over to my house after you " 
                                     + "are settled in?" + '\n')
    
    elif action.upper() == "NO":
        Variables.exploration_timer = 16
        print("You decided to not waste his time and go straight to the haunted house.")
        counter += 1
        
    else:
        action = raw_input("Do you want to go talk to your neighbour? Yes or no?"  + '\n')
    
    print('\n' + "You went to the haunted house to 'move in'. Once inside you decided to explore. You start in the front foyer. Type the directions north," 
           + " south, east " + '\n' + "and west to move around the house. Type up and down to move between floors and type search to look in depth through " 
           + " rooms." + '\n')
    
    
'''
house explortion code vvv
'''

print("Type north, south, east or west to move around the house in their respective directions." + '\n' +  
      "You can type search to search a room and find items" + '\n' 
      "You can type up or down to go up or down a staircase" + '\n' 
      + "You are currently in the foyer" + '\n')
print("Foyer - A tiny room that you find yourself in after entering the house. There is a library room to your east, stairs to the north and closet" 
      + " to your west. " + '\n' + "There is also a tiny drawer in the foyer, it might be worth while to check it out." +'\n')

while Variables.exploration_timer != 0:
    
    Variables.action = raw_input('\n' + "Type what you want to do" + '\n')    
    
    counter = 0
    
    while counter == 0:
        if (Variables.action.upper() == "NORTH" or Variables.action.upper() == "SOUTH" or Variables.action.upper() == "EAST" or 
            Variables.action.upper() == "WEST" or Variables.action.upper() == "UP" or Variables.action.upper() == "DOWN" or 
            Variables.action.upper() == "SEARCH" or Variables.action.upper() == "KICK DOWN DOOR" or Variables.action.upper() == "OPEN DOOR"):
            counter += 1
        else:
            print("Try again" + '\n')    
            Variables.action = raw_input("Type north, south, east, west, up, down to move or search to search a room" + '\n')
    
    '''
    middle floor exploration code vvv
    '''
    
    if Variables.action.upper() == "WEST" and Variables.current_room == "FOYER":
        Variables.current_room = "CLOSET"  
        print("Closet - It's just a closet, nothing new.")
        Variables.exploration_timer -= 1
        
    elif Variables.action.upper() == "SEARCH" and Variables.current_room == "CLOSET": 
        print("Searched Closet - There is nothing in here, just some cobwebs and... a bunch of spiders")
        Variables.exploration_timer -= 1
        
        
        
    elif (Variables.action.upper() == "SOUTH" and Variables.current_room == "STAIRS_1" or Variables.action.upper() == "EAST" and 
          Variables.current_room == "CLOSET" or Variables.action.upper() == "WEST" and Variables.current_room == "LIBRARY_ROOM"):
        Variables.current_room = "FOYER"
        print("Foyer - A tiny room that you find yourself in after entering the house. There is a library room to your east and closet to your west and" + '\n' 
              + " stairs to the north" + "There is also a tiny drawer in the foyer, it might be worth while to check it out.")
        Variables.exploration_timer -= 1
    
    elif Variables.action.upper() == "SEARCH" and Variables.current_room == "FOYER":
        GameFunctions().getItem(Variables.action, "key", Variables.key_taken, "Searched Foyer - You looked inside a tiny drawer and found a key!", 
                              Variables.item_1, Variables.item_2, Variables.item_3)
        
        Variables.exploration_timer -= 1
        
            
    
    elif Variables.action.upper() == "EAST" and Variables.current_room == "FOYER":
        print("Library Room - A room that is filled with old books, mabey one of these books has some info on the history of the house")
        Variables.current_room = "LIBRARY_ROOM"
        Variables.exploration_timer -= 1
    
    elif Variables.action.upper() == "SEARCH" and Variables.current_room == "LIBRARY_ROOM":
        choise = raw_input("Seached Library Room - there is a photo album that looks old, do you want to look at it?")
        counter_1 = 0
        
        while counter_1 == 0:
            if choise.upper() == "YES":
                print("While looking throug the photo album you see a photo of a family in front of the house. Flipping through the book some more you see "  
                      + "a photo of the same family" + '\n' + "but a couple years later, everyone seems to have aged but one. A little girl who looks to be " 
                      + "around 10 looks the same in both photos.")
                Variables.photo_album_looked_at = True
                counter_1 += 1
            
            elif choise.upper() == "NO":
                print("You didn't look at the photo album")
                counter_1 += 1
                
            else:
                choise = raw_input("Seached Library Room - there is a photo album that looks old, do you want to look at it, yes or no?")
        
        Variables.exploration_timer -= 1
        
        
        
    elif Variables.action.upper() == "WEST" and Variables.current_room == "STAIRS_1":
        print("Bathroom - A room with an old toilet and sink.")
        Variables.current_room = "BATHROOM_1"
        Variables.exploration_timer -= 1
    
    elif Variables.action.upper() == "SEARCH" and Variables.current_room == "BATHROOM_1":
        if Variables.plunger_taken == False:
            
            print("Seached Bathroom  - There is a plunger!")
            choise = raw_input("Do you want to pick up this item? Yes or No?" + '\n')
            
            counter_1 = 0
            while counter_1 == 0:
                if choise.upper() == "YES":
                    if Variables.item_1 == "":
                        Variables.item_1 = "plunger"
                        Variables.plunger_taken = True
                        print ("You got a plunger!")
                        counter_1 += 1 
                        
                    elif Variables.item_2 == "":
                        Variables.item_2 = "plunger"
                        Variables.plunger_taken = True
                        print ("You got a plunger!")
                        counter_1 += 1
                    
                    elif Variables.item_3 == "":
                        Variables.item_3 = "plunger"
                        Variables.plunger_taken = True
                        print ("You got a plunger!")
                        counter_1 += 1
                        
                    else:
                        delete = raw_input("You don't have enough space to carry this item, do you want to drop one of your items? Here are your items " + 
                                           '\n' + Variables.item_1 + ", " + Variables.item_2 + " and " + Variables.item_3 +'\n')
                        while counter_1 == 0:
                            
                            if delete.upper() == "YES":
                                delete_item = raw_input("Which item do you want to drop? Here are your options: " + '\n' + Variables.item_1 + ", " 
                                                        + Variables.item_2 + " and " + Variables.item_3 + '\n')
                                
                                while counter_1 == 0:
                                    if delete_item.upper() == Variables.item_1.upper():
                                        Variables.item_1 = "plunger" 
                                        print("You dropped " + Variables.item_1 + " and got a plunger")
                                        Variables.plunger_taken = True
                                        counter_1 += 1
                                    
                                    elif delete_item.upper() == Variables.item_2.upper(): 
                                        Variables.item_2 = "plunger" 
                                        print("You dropped " + Variables.item_2 + " and got a plunger")
                                        Variables.plunger_taken = True
                                        counter_1 += 1
                                    
                                    elif delete_item.upper() == Variables.item_3.upper(): 
                                        Variables.item_3 = "plunger" 
                                        print("You dropped " + Variables.item_3 + " and got a plunger")
                                        Variables.plunger_taken = True
                                        counter_1 += 1
                                    
                                    else:
                                        delete_item = raw_input("Which item do you want to drop? Here are your options: " + '\n' + Variables.item_1 + ", " 
                                                        + Variables.item_2 + " and " + Variables.item_3 + '\n' + "Type in the name of the item you want " +
                                                        "to drop" + '\n')
                            
                            elif delete.upper() == "NO":
                                print("You didn't get the plunger")
                                counter_1 += 1
                            
                            else:
                                delete = raw_input("You don't have enough space to carry this item, do you want to drop one of your items")
                            
                elif choise.upper() == "NO":
                    print("You didn't get the plunger")
                    counter_1 += 1
                    
                else: choise = raw_input("Do you want to pick up this item? Yes or No?")
                
        
        else:
            print("You already took the item that was here")
        
        Variables.exploration_timer -= 1
        
        
        
    elif (Variables.action.upper() == "NORTH" and Variables.current_room == "FOYER" or Variables.action.upper() == "SOUTH" and 
          Variables.current_room == "HALLWAY_1" or Variables.action.upper() == "EAST" and Variables.current_room == "BATHROOM_1" or 
          Variables.action.upper() == "WEST" and Variables.current_room == "DINING_ROOM" or Variables.current_room == "STAIRS_2" and 
          Variables.action.upper() == "UP" or Variables.current_room == "STAIRS_3" and Variables.action.upper() == "DOWN"):
        print("Staircase - There are two sets of stairs, one that leads upstairs and one that leads downstairs. To the north there is a hallway, south there " 
              + '\n' + "is the foyer, east is the dining room and west is the bathroom. Type up or down to go upstairs or downstairs")
        Variables.current_room = "STAIRS_1"
        Variables.exploration_timer -= 1
    
    elif Variables.action.upper() == "SEARCH" and Variables.current_room == "STAIRS_1":
        print("Seached Staircase - You notice that at the end of the stairs that lead downstairs there is a door, it could be locked.")
        
        Variables.exploration_timer -= 1
     
        
        
    elif Variables.action.upper() == "EAST" and Variables.current_room == "STAIRS_1":
        print("Dining Room - A room where a family eats, I think. There is a glass cabinet here, there might be something interesting in it")
        Variables.current_room = "DINING_ROOM"
        Variables.exploration_timer -= 1
    
    elif Variables.action.upper() == "SEARCH" and Variables.current_room == "DINING_ROOM":
        if Variables.cookies_taken == False:
            
            print("Seached Dining Room  - There is an old candelabra!")
            choise = raw_input("Do you want to pick up this item? Yes or No?" + '\n')
            
            counter_1 = 0
            while counter_1 == 0:
                if choise.upper() == "YES":
                    if Variables.item_1 == "":
                        Variables.item_1 = "candleabra"
                        Variables.candleabra_taken = True
                        print ("You got a candleabra!")
                        counter_1 += 1 
                        
                    elif Variables.item_2 == "":
                        Variables.item_2 = "candleabra"
                        Variables.candleabra_taken = True
                        print ("You got a candleabra!")
                        counter_1 += 1
                    
                    elif Variables.item_3 == "":
                        Variables.item_3 = "candleabra"
                        Variables.candleabra_taken = True
                        print ("You got a candleabra!")
                        counter_1 += 1
                        
                    else:
                        delete = raw_input("You don't have enough space to carry this item, do you want to drop one of your items? Here are your items " + 
                                           '\n' + Variables.item_1 + ", " + Variables.item_2 + " and " + Variables.item_3 +'\n')
                        while counter_1 == 0:
                            
                            if delete.upper() == "YES":
                                delete_item = raw_input("Which item do you want to drop? Here are your options: " + '\n' + Variables.item_1 + ", " 
                                                        + Variables.item_2 + " and " + Variables.item_3 + '\n')
                                
                                while counter_1 == 0:
                                    if delete_item.upper() == Variables.item_1.upper(): 
                                        print("You dropped " + Variables.item_1 + " and got a candleabra")
                                        Variables.candleabra_taken = True
                                        Variables.item_1 = "candleabra"
                                        counter_1 += 1
                                    
                                    elif delete_item.upper() == Variables.item_2.upper(): 
                                        Variables.item_2 = "candleabra" 
                                        print("You dropped " + Variables.item_2 + " and got a candleabra")
                                        Variables.candleabra_taken = True
                                        Variables.item_2 = "candleabra"
                                        counter_1 += 1
                                    
                                    elif delete_item.upper() == Variables.item_3.upper(): 
                                        Variables.item_3 = "candleabra" 
                                        print("You dropped " + Variables.item_3 + " and got a candleabra")
                                        Variables.candleabra_taken = True
                                        Variables.item_3 = "candleabra"
                                        counter_1 += 1
                                    
                                    else:
                                        delete_item = raw_input("Which item do you want to drop? Here are your options: " + '\n' + Variables.item_1 + ", " 
                                                        + Variables.item_2 + " and " + Variables.item_3 + '\n' + "Type in the name of the item you want " +
                                                        "to drop" + '\n')
                            
                            elif delete.upper() == "NO":
                                print("You didn't get the candleabra")
                                counter_1 += 1
                            
                            else:
                                delete = raw_input("You don't have enough space to carry this item, do you want to drop one of your items")
                            
                elif choise.upper() == "NO":
                    print("You didn't get the candleabra")
                    counter_1 += 1
                    
                else: choise = raw_input("Do you want to pick up this item? Yes or No?")
                
        
        else:
            print("You already took the item that was here")
        
        Variables.exploration_timer -= 1
    
    
    
    elif Variables.action.upper() == "WEST" and Variables.current_room == "HALLWAY_1":
        print("Family Room - A room fild with old sofas... thats it")
        Variables.current_room = "FAMILY_ROOM"
        Variables.exploration_timer -= 1
    
    elif Variables.action.upper() == "SEARCH" and Variables.current_room == "FAMILY_ROOM":
        print("Family Room - There is nothing useful here")
        Variables.exploration_timer -= 1
        
        
        
    elif (Variables.action.upper() == "NORTH" and Variables.current_room == "STAIRS_1" or Variables.action.upper() == "EAST" and 
          Variables.current_room == "FAMILY_ROOM" or Variables.action.upper() == "WEST" and Variables.current_room == "KITCHEN_1"):
        print("Hallway - It's a hallway filled with old creepy pictures. The family room is to the west, the kitchen is to the east and " + '\n' +
              " the stars are to the south")
        Variables.current_room = "HALLWAY_1"
        Variables.exploration_timer -= 1
        
    elif Variables.action.upper() == "SEARCH" and Variables.current_room == "HALLWAY_1":
        print("Searched Hallway - There is a picture of a little girl with a label tat says her name is Anna, it looks like she was the only girl " + 
              "of the family who lived here")
        
        choise = raw_input("Do you want to look at more pictures? Yes or No?" + '\n')
        counter = 0
        
        while counter == 0:
            if Variables.action.upper() == "YES":
                print("There is a picture of a statue of a cat? it says that his name is Picklez")
                    
                Variables.action = raw_input("Do you want to look at more pictures? Yes or No?" + '\n')
        
                while counter == 0:
                    if Variables.action.upper() == "YES":
                        print("There is a picture of a an old lady named March. She looks mean.")
                        counter += 1
        
                    elif Variables.action.upper() == "NO":
                        print ("Okay, you didn't look at the pictures")
                        counter += 1
                    
            elif Variables.action.upper() == "NO":
                print ("Okay, you didn't look at the pictures")
                counter_1 += 1
    
        
        Variables.exploration_timer -= 1
        
        
        
    elif Variables.action.upper() == "EAST" and Variables.current_room == "HALLWAY_1":
        print("Kitchen - It's an old kitchen. There are a lot of cubords. It might be worth it to look through them.")
        Variables.current_room = "KITCHEN_1"
        Variables.exploration_timer -=1
    
    elif Variables.action.upper() == "SEARCH" and Variables.current_room == "KITCHEN_1":
        GameFunctions.getItem(Variables.action, "cookie jar", Variables.cookies_taken, 
                              "Seached Kitchen  - There is a jar filled with cookies that are really old!", Variables.item_1, 
                              Variables.item_2, Variables.item_3)
        
        Variables.exploration_timer -= 1


        '''
        basement exploration code vvv
        '''
        
    elif Variables.action.upper() == "SOUTH" and Variables.current_room == "BEDROOM_2":
        print("Bathroom - It is a bathroom. Nothing special. North of the bathroom is the bedroom" )
        Variables.current_room = "BATHROOM_2"
    
    elif Variables.action.upper() == "SEARCH" and Variables.current_room == "BATHROOM_2":
        print("Searched Bathroom - There is nothing useful")
        
            
            
    elif Variables.action.upper() == "SOUTH" and Variables.current_room == "KITCHEN_2":
        print("Cellar - A room that was used to store wine. North of the cellar is the kitchen")
        Variables.current_room = "CELLAR"
    
    elif Variables.action.upper() == "SEARCH" and Variables.current_room == "CELLAR":
        if Variables.wine_taken == False:
            
            print("Seached Cellar  - There is bottle of aged wine!")
            choise = raw_input("Do you want to pick up this item? Yes or No?" + '\n')
            
            counter_1 = 0
            while counter_1 == 0:
                if choise.upper() == "YES":
                    if Variables.item_1 == "":
                        Variables.item_1 = "wine"
                        Variables.wine_taken = True
                        print ("You got a bottle of aged wine!")
                        counter_1 += 1 
                        
                    elif Variables.item_2 == "":
                        Variables.item_2 = "wine"
                        Variables.wine_taken = True
                        print ("You got a bottle of aged wine!")
                        counter_1 += 1
                    
                    elif Variables.item_3 == "":
                        Variables.item_3 = "wine"
                        Variables.wine_taken = True
                        print ("You got a bottle of aged wine!")
                        counter_1 += 1
                        
                    else:
                        delete = raw_input("You don't have enough space to carry this item, do you want to drop one of your items? Here are your items " + 
                                           '\n' + Variables.item_1 + ", " + Variables.item_2 + " and " + Variables.item_3 +'\n')
                        while counter_1 == 0:
                            
                            if delete.upper() == "YES":
                                delete_item = raw_input("Which item do you want to drop? Here are your options: " + '\n' + Variables.item_1 + ", " 
                                                        + Variables.item_2 + " and " + Variables.item_3 + '\n')
                                
                                while counter_1 == 0:
                                    if delete_item.upper() == Variables.item_1.upper():
                                        Variables.item_1 = "wine" 
                                        print("You dropped " + Variables.item_1 + " and got a bottle of aged wine")
                                        Variables.wine_taken = True
                                        counter_1 += 1
                                    
                                    elif delete_item.upper() == Variables.item_2.upper(): 
                                        Variables.item_2 = "wine" 
                                        print("You dropped " + Variables.item_2 + " and got a bottle of aged wine!")
                                        Variables.wine_taken = True
                                        counter_1 += 1
                                    
                                    elif delete_item.upper() == Variables.item_3.upper(): 
                                        Variables.item_3 = "wine" 
                                        print("You dropped " + Variables.item_3 + " and got a bottle of aged wine!")
                                        Variables.wine_taken = True
                                        counter_1 += 1
                                    
                                    else:
                                        delete_item = raw_input("Which item do you want to drop? Here are your options: " + '\n' + Variables.item_1 + ", " 
                                                        + Variables.item_2 + " and " + Variables.item_3 + '\n' + "Type in the name of the item you want " +
                                                        "to drop" + '\n')
                            
                            elif delete.upper() == "NO":
                                print("You didn't get the bottle of aged wine")
                                counter_1 += 1
                            
                            else:
                                delete = raw_input("You don't have enough space to carry this item, do you want to drop one of your items")
                            
                elif choise.upper() == "NO":
                    print("You didn't get the bottle of aged wine")
                    counter_1 += 1
                    
                else: choise = raw_input("Do you want to pick up this item? Yes or No?")
                
        
        else:
            print("You already took the item that was here")
        
        Variables.exploration_timer -= 1
        
        
                
    elif (Variables.action.upper() == "SOUTH" and Variables.current_room == "HALLWAY_2.1" or Variables.action.upper() == "NORTH" 
          and Variables.current_room == "BATHROOM_2"):
        print("Bedroom - An extra bedroom that is in the basement. To the north is the west hallway and south is a bathroom")
        Variables.current_room = "BEDROOM_2"
    
    elif Variables.action.upper() == "SEARCH" and Variables.current_room == "BEDROOM_2":
        print("Searched Bedroom - There isn't anything useful")
        
        
        
    elif (Variables.action.upper() == "DOWN" and Variables.current_room == "STAIRS_1" or Variables.action.upper() == "SOUTH" and 
        Variables.current_room == "HALLWAY_2"):
        print("Downstairs Stairs - There is only one door north of where you are that leads to the basement and its locked. " + 
              '\n' + "Mabye if you find a key and type open door it might open?")
        Variables.current_room = "STAIRS_2"
        Variables.exploration_timer -= 1
    
    elif Variables.action.upper() == "SEARCH" and Variables.current_room == "STAIRS_2":
        print("Searched Downstairs Stairs - Its a room and some stairs what did you expect to find?")
        Variables.current_room = "STAIRS_2"
        Variables.exploration_timer -= 1
    
    elif Variables.action.upper() == "KICK DOWN DOOR" and Variables.current_room == "STAIRS_2":
        print("You can't do that, the door is made of iron!")
        Variables.current_room = "STAIRS_2"
    
    elif (Variables.action.upper() == "OPEN DOOR" and Variables.current_room == "STAIRS_2" and Variables.item_1.upper() == "KEY" or 
          Variables.action.upper() == "OPEN DOOR" and Variables.current_room == "STAIRS_2" and Variables.item_2.upper() == "KEY" or
          Variables.action.upper() == "NORTH" and Variables.current_room == "STAIRS_2" and Variables.item_3.upper() == "KEY"):
        print("You opened the door that is to the north of you!")
        Variables.door_open = True
    
    
    
    elif (Variables.action.upper() == "SOUTH" and Variables.current_room == "HALLWAY_2.2" or Variables.action.upper() == "NORTH" 
          and Variables.current_room == "CELLAR" ):
        print("Kitchen - A small kitchen in the basement")
        Variables.current_room = "KITCHEN_2"
    
    elif Variables.action.upper() == "SEARCH" and Variables.current_room == "KITCHEN_2":
        print("Searched Kitchen - There is nothing useful here just some old plates and cups")
        
        
        
    elif (Variables.action.upper() == "WEST" and Variables.current_room == "HALLWAY_2" or Variables.action.upper() == "NORTH" 
          and Variables.current_room == "BEDROOM_2" ):
        print("West Hallway - It's just a hallway, nothing special. To the south there is a bedroom and to the east there is another hallway.")
        Variables.current_room = "HALLWAY_2.1"
    
    elif Variables.action.upper() == "SEARCH" and Variables.current_room == "HALLWAY_2.1":
        print("Searched West Hallway - There isn't anything useful. ")
        
        
        
    elif (Variables.action.upper() == "NORTH" and Variables.current_room == "STAIRS_2" and Variables.door_open == True or 
          Variables.action.upper() == "WEST" and Variables.current_room == "HALLWAY_2.2" or Variables.action.upper() == "EAST" 
          and Variables.current_room == "HALLWAY_2.1"):
        print("Hallway - It is a hallway. To the east and west there are halways and south is the staircase.")
        Variables.current_room = "HALLWAY_2"
    
    elif Variables.action.upper() == "SEARCH" and Variables.current_room == "HALLWAY_2":
        print("Searched Hallway - There isn't anything special.")
    
    
    
    elif (Variables.action.upper() == "EAST" and Variables.current_room == "HALLWAY_2" or Variables.action.upper() == "NORTH" 
          and Variables.current_room == "KITCHEN_2"):
        print("East Hallway - It is just a hallway. To the west there is another hallway and to the south there is a kitchen.")
        Variables.current_room = "HALLWAY_2.2"
    
    elif Variables.action.upper() == "SEARCH" and Variables.current_room == "HALLWAY_2.2":
        print("Searched East Hallway - There isn't anything special.")
   
        
        '''
        upstairs exploration code vvv
        '''
        
        
        
    elif Variables.action.upper() == "SOUTH" and Variables.current_room == "KIDS_BEDROOM":
        print("Kids Bathroom - A bathroom that is south of the kids bedroom.")
        Variables.current_room = "KIDS_BATHROOM"
        Variables.exploration_timer -= 1
    
    elif Variables.action.upper() == "SEARCH" and Variables.current_room == "KIDS_BATHROOM":
        print("Kids Bathroom Bathroom - There is nothing useful here")
        Variables.exploration_timer -= 1
        
        
        
    elif Variables.action.upper() == "SOUTH" and Variables.current_room == "MASTER_BEDROOM":
        print("Master Bathroom - It is the bathroom that is south of the master bedroom.")
        Variables.current_room = "MASTER_BATHROOM"
        Variables.exploration_timer -= 1
    
    elif Variables.action.upper() == "SEARCH" and Variables.current_room == "MASTER_BATHROOM":
        print("Searched Master Bathroom - There is nothing useful here")
        Variables.exploration_timer -= 1
        
        
        
    elif (Variables.action.upper() == "WEST" and Variables.current_room == "STAIRS_3" or Variables.action.upper() == "NORTH" and 
    Variables.current_room == "KIDS_BATHROOM"):
        print("Kids Bedroom - A bedroom that is filled with old toys and posters. To teh south there is a bathroom and to the east is the stairs")
        Variables.current_room = "KIDS_BEDROOM"
        Variables.exploration_timer -= 1
    
    elif Variables.action.upper() == "SEARCH" and Variables.current_room == "KIDS_BEDROOM":
        print("Searched Kids Bedroom - You found a safe, looks like it is protected by a four digit password." + '\n')
        
        Variables.action = raw_input("Do you want to try and enter a password?")
        
        counter = 0
        while counter == 0:
            if Variables.action.upper() == "YES":
                Variables.action = raw_input("Type the four digit password here")
                        
                while Variables.safe_tries != 0:
                    if Variables.action == Variables.password and Variables.statue_taken == False:
                    
                        print("Seached Safe  - There is statue that looks like someone very familiar!")
                        choise = raw_input("Do you want to pick up this item? Yes or No?" + '\n')
                                    
                        counter_1 = 0
                        while counter_1 == 0:
                            if choise.upper() == "YES":
                                if Variables.item_1 == "":
                                    Variables.item_1 = "statue"
                                    Variables.statue_taken = True
                                    print ("You got a statue!")
                                    counter_1 += 1 
                                            
                                elif Variables.item_2 == "":
                                    Variables.item_2 = "statue"
                                    Variables.statue_taken = True
                                    print ("You got a statue!")
                                    counter_1 += 1
                                            
                                elif Variables.item_3 == "":
                                    Variables.item_3 = "statue"
                                    Variables.statue_taken = True
                                    print ("You got a statue!")
                                    counter_1 += 1
                                                
                                else:
                                    delete = raw_input("You don't have enough space to carry this item, do you want to drop one of your items? Here are " + 
                                                        "your items " + '\n' + Variables.item_1 + ", " + Variables.item_2 
                                                         + " and " + Variables.item_3 +'\n')
                                    while counter_1 == 0:
                                                    
                                        if delete.upper() == "YES":
                                            delete_item = raw_input("Which item do you want to drop? Here are your options: " + '\n' + Variables.item_1 + ", " 
                                                                    + Variables.item_2 + " and " + Variables.item_3 + '\n')
                                                        
                                            while counter_1 == 0:
                                                if delete_item.upper() == Variables.item_1.upper():
                                                    Variables.item_1 = "statue" 
                                                    print("You dropped " + Variables.item_1 + " and got a statue!")
                                                    Variables.statue_taken = True
                                                    counter_1 += 1
                                                            
                                                elif delete_item.upper() == Variables.item_2.upper(): 
                                                    Variables.item_2 = "statue" 
                                                    print("You dropped " + Variables.item_2 + " and got a statue!")
                                                    Variables.statue_taken = True
                                                    counter_1 += 1
                                                            
                                                elif delete_item.upper() == Variables.item_3.upper(): 
                                                    Variables.item_3 = "statue" 
                                                    print("You dropped " + Variables.item_3 + " and got a statue!")
                                                    Variables.statue_taken = True
                                                    counter_1 += 1
                                                        
                                                else:
                                                    delete = raw_input("You don't have enough space to carry this item, do you want to drop one of your" + 
                                                        " items? Here are your items " + '\n' + Variables.item_1 + ", " + Variables.item_2 
                                                            + " and " + Variables.item_3 +'\n' + "Type the name of the item you want to drop.")
                                                    
                                        elif delete.upper() == "NO":
                                            print("You didn't get the statue")
                                            counter_1 += 1
                                                    
                                        else:
                                            delete = raw_input("You don't have enough space to carry this item, do you want to drop one of your items")
                                                    
                            elif choise.upper() == "NO":
                                print("You didn't get the statue")
                                counter_1 += 1
                                            
                            else: choise = raw_input("Do you want to pick up this item? Yes or No?")
                                        
                                
                        else:
                            print("You already took the item that was here")
                                                                
                    elif Variables.action != Variables.password:   
                        if Variables.safe_tries > 0:
                            Variables.safe_tries -= 1
                            print("You put the wrong password")
                            Variables.action = raw_input("Type the four digit password here")
                        
                        elif Variables.safe_tries < 0:
                            print("You ran out of tries")
                            Variables.safe_tries = 0
                            counter += 1
                                             
            elif Variables.action.upper() == "NO":
                counter += 1
                    
            else:
                Variables.action = raw_input("Do you want to try and enter a password? If you do type yes." + '\n')
        
        if Variables.statue_taken == True:
            print("You took what was in here." "Type what you want to do")
            counter += 1
        
        Variables.exploration_timer -= 1
        
        
        
    elif (Variables.action.upper() == "UP" and Variables.current_room == "STAIRS_1" or Variables.action.upper() == "SOUTH" and 
    Variables.current_room == "HALLWAY_3" or Variables.action.upper() == "EAST" and Variables.current_room == "KIDS_BEDROOM" or
    Variables.action.upper() == "WEST" and Variables.current_room == "MASTER_BEDROOM"):
        print("Upstairs Stairs - The upper part of the stairs. If you go down you will be on the first floor, east is the master bedroom, " + '\n' + 
              "to the west is a kids bedroom and to the north is a hallway.")
        Variables.current_room = "STAIRS_3"
        Variables.exploration_timer -= 1
    
    elif Variables.action.upper() == "SEARCH" and Variables.current_room == "STAIRS_3":
        print("Searched Upstairs Stairs - There is nothing useful here")
        Variables.exploration_timer -= 1
        
        
        
    elif (Variables.action.upper() == "EAST" and Variables.current_room == "STAIRS_3" or Variables.action.upper() == "NORTH" 
    and Variables.current_room == "MASTER_BATHROOM"):
        print("Master Bedroom - The biggest bedroom in the house. To the south there is a bathroom and to the west there are stairs")
        Variables.current_room = "MASTER_BEDROOM"
        Variables.exploration_timer -= 1
    
    elif Variables.action.upper() == "SEARCH" and Variables.current_room == "MASTER_BEDROOM":
        print("Searched Master Bedroom - There is nothing useful here")
        Variables.exploration_timer -= 1
        
        
        
    elif Variables.action.upper() == "WEST" and Variables.current_room == "HALLWAY_3":
        print("Guest Room #1 - An extra room in the house. To the east there is a hallway.")
        Variables.current_room = "GUEST_ROOM_1"
        Variables.exploration_timer -= 1
    
    elif Variables.action.upper() == "SEARCH" and Variables.current_room == "GUEST_ROOM_1":
        print("Guest Room #1 - There is nothing useful here")
        Variables.exploration_timer -= 1
    
    
    
    elif (Variables.action.upper() == "NORTH" and Variables.current_room == "STAIRS_3" or Variables.action.upper() == "EAST" 
    and Variables.current_room == "GUEST_ROOM_1" or Variables.action.upper() == "WEST"  and Variables.current_room == "GUEST_ROOM_2"):
        print("Hallway - It is just a hallway. To the south there are stairs, to the east and west there are stairs.")
        Variables.current_room = "HALLWAY_3"
        Variables.exploration_timer -= 1
    
    elif Variables.action.upper() == "SEARCH" and Variables.current_room == "HALLWAY_3":
        print("Searched Hallway - There is nothing useful here")
        Variables.exploration_timer -= 1
        
        
        
    elif Variables.action.upper() == "EAST" and Variables.current_room == "HALLWAY_3":
        print("Guest Room #2 - An extra room in the house. To the west there is a hallway.")
        Variables.current_room = "GUEST_ROOM_2"
        Variables.exploration_timer -= 1
    
    elif Variables.action.upper() == "SEARCH" and Variables.current_room == "GUEST_ROOM_2":
        print("Searched Guest Room #2 - There is nothing useful here")
        Variables.exploration_timer -= 1
    
         
    else:
        print("You hit a wall, try again!")      
        
'''
What happens after house exploration
'''      
        
if Variables.go_to_bob == True:
        print ('\n' + "Okay it is time to go to Bob's house" + '\n')
            
            
        Variables.bob_gift = raw_input ("Once you arrive to Bob's house you relised that you should probably give something to him as a present." + 
                                          "What do you want to give him?" + '\n' + "Here are your options: " + Variables.item_1 + ", " +
                                          Variables.item_2 + ", " + Variables.item_3 + " or do you want to give him nothing")
        counter = 0

        while counter == 0:
            if Variables.bob_gift == Variables.item_1:
                print("You gave Bob " + Variables.item_1)
                Variables.item_1 = ""
                counter +=1
                    
            elif Variables.bob_gift == Variables.item_2:
                print("You gave Bob " + Variables.item_2)
                Variables.item_2 = ""
                counter +=1
                    
            elif Variables.bob_gift == Variables.item_3:
                print("You gave Bob " + Variables.item_3)
                Variables.item_3 = ""
                counter +=1
                
            elif Variables.bob_gift == "NOTHING":
                print("You gave Bob nothing")
                counter +=1
                
            else:
                Variables.bob_gift = raw_input ("Once you arrive to Bob's house you relised that you should probably give something to him as a present." + 
                                          "What do you want to give him?" + '\n' + "Here are your options: " + Variables.item_1 + ", " +
                                          Variables.item_2 + ", " + Variables.item_3 + " or do you want to give him nothing")
                
        print("You walk up to Bob's house and ring the door bell and he opens the door. You hand over his gift, a " + Variables.bob_gift + '\n')
            
        print("You and Bob talked and had dinner. He told you that recentley many people have disapeared from their homes." 
                  + '\n' + "People say that a mystery killer has been taking them." + '\n' + "Eventualy you left and went home to sleep")
            
            
else:
    '''
    What happens if you chose to not interact with Bob and go to his house        
    '''
    print("")
                    
'''
night time choises vvv
'''                   
print ("It is very late and you decided to go to sleep" + '\n')
    
if Variables.door_open == True:
    Variables.action = raw_input("Which room do you want to sleep in? Type '1' for the kids bedroom, '2' for the master bedroom, '3' for the first " +
                                 "guest room, " + '\n' + " '4' for the second guest room or '5' for the bedroom in the basement" + '\n')
        
    counter = 0
    while counter == 0:
        if Variables.action == "1":
            Variables.current_room = "KIDS_BEDROOM"
            print("You decided to stay in the kids bedroom." + '\n')
            counter += 1
            
        elif Variables.action == "2":
            Variables.current_room = "MASTER_BEDROOM"
            print("You decided to stay in the master bedroom." + '\n')
            counter += 1
            
        elif Variables.action == "3":
            Variables.current_room = "GUEST_ROOM_1"
            print("You decided to stay in the first guest room." + '\n')
            counter += 1

        elif Variables.action == "4":
            Variables.current_room = "GUEST_ROOM_2"
            print("You decided to stay in the second guest room." + '\n')
            counter += 1
          
        elif Variables.action == "5":
            Variables.current_room = "BEDROOM_2"
            print("You decided to stay in the basement bedroom." + '\n')
            counter += 1
            
        else:
            Variables.action = raw_input("Which room do you want to sleep in? Type '1' for the kids bedroom, '2' for the master bedroom, '3' for the first" 
                                             + " guest room, " + '\n' + " '4' for the second guest room or '5' for the bedroom in the basement" + '\n')
        
else:
    Variables.action = raw_input("Which room do you want to sleep in? Type '1' for the kids bedroom, '2' for the master bedroom, '3' for the first " +
                                 "guest room, " + '\n' + " or '4' for the second guest room" + '\n')
        
    counter = 0
    while counter == 0:  
        if Variables.action == "1":
            Variables.current_room = "KIDS_BEDROOM"
            print("You decided to stay in the kids bedroom." + '\n')
            counter += 1
            
        elif Variables.action == "2":
            Variables.current_room = "MASTER_BEDROOM"
            print("You decided to stay in the master bedroom." + '\n')
            counter += 1
            
        elif Variables.action == "3":
            Variables.current_room = "GUEST_ROOM_1"
            print("You decided to stay in the first guest room." + '\n')
            counter += 1

        elif Variables.action == "4":
            Variables.current_room = "GUEST_ROOM_2"
            print("You decided to stay in the second guest room." + '\n')
            counter += 1
                            
        else:
            Variables.action = raw_input("Which room do you want to sleep in? Type '1' for the kids bedroom, '2' for the master bedroom, '3' for the first" 
                                             + " guest room, " + '\n' + " or '4' for the second guest room" + '\n')

'''
Ghost interactions below vvv
'''
    
Variables.action = raw_input("You heard a sound from the library room, do you want to check it out?" + '\n')       

counter = 0
while counter == 0:
    if Variables.action.upper() == "YES":
        
        if Variables.photo_album_looked_at == True:
            print("It looks like the photo album you looked at before was opened to the page of the little girl." + '\n' + "You went back to the bedroom " + 
                  "and went to sleep." + '\n')
            Variables.exploration_timer -= 1
            counter += 1
        
        else:
            print("It looks like a photo ablum was open to a page with a girl." + '\n' + "You went back to the bedroom and went to sleep." + '\n')
            Variables.exploration_timer -= 1
            counter += 1
    
    elif Variables.action.upper() == "NO":
        print("You went back to sleep" + '\n')
        Variables.exploration_timer += 1
        counter += 1
    
    else:
        Variables.action = raw_input("You heard a sound from the library room, do you want to check it out?" + '\n')  


Variables.action = raw_input("You heard another sound, it seems like it is coming from the down stairs bathroom. Do you want to check it out?" + '\n')       

counter = 0
while counter == 0:
    if Variables.action.upper() == "YES":
        print("You went to the bathroom and saw a ghost!" + '\n')
        
        Variables.action = raw_input("What will you do, throw something at the ghost or run away?")
        
        if Variables.item_1 == "" and Variables.item_2 == "" and Variables.item_3 == "":
            Variables.action = raw_input("You don't have any items to throw so you ran away" + '\n') 
            print("You tried to run away and tripped. The ghost got you. You died.")
            Variables.alive = False
            counter += 1
        
        
        if Variables.action.upper() == "THROW":
            throwItem = raw_input("Which item do you want to throw?" + '\n' + "Here are your options:" + '\n' + "- " + Variables.item_1 + '\n' + 
                                      "- " + Variables.item_2 + '\n' + "- " + Variables.item_3 + '\n')    
  
            while counter == 0:
                if throwItem == Variables.item_1:
                    print("You threw " + Variables.item_1)
                    Variables.item_1 = ""
                    counter +=1
                        
                elif throwItem == Variables.item_2:
                    print("You threw " + Variables.item_2)
                    Variables.item_2 = ""
                    counter +=1
                        
                elif throwItem == Variables.item_3:
                    print("You threw " + Variables.item_3)
                    Variables.item_3 = ""
                    counter +=1
                    
                else:
                    Variables.bob_gift = raw_input("Which item do you want to throw?" + '\n' + "Here are your options:" + '\n' + "- " + Variables.item_1 + '\n' + 
                                      "- " + Variables.item_2 + '\n' + "- " + Variables.item_3 + '\n')
                    
            
        elif Variables.action.upper() == "RUN AWAY":
            print("You tried to run away and tripped. The ghost got you. You died.")
            Variables.alive = False
            counter += 1
                
        else:
            Variables.action = raw_input("What will you do? Throw something at the ghost or run away?")
    
    elif Variables.action.upper() == "NO":
        print("You went back to sleep. The ghost that was haunting the house got you. You died")
        Variables.alive = False
        counter += 1
    
    else:
        Variables.action = raw_input("You went to the bathroom and saw a ghost! What will you do, throw something at the ghost or run away?")  
        
        
'''
tells you if you win or lose based off of your desisions
'''
if Variables.alive == True:
    print("You were able to distract the ghost and escape! You were able to survive the night and win the mansion! You win!")

else:
    print("You lost") 
        
