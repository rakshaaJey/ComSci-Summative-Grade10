'''
Game Functions

@author: Rakshaa
'''

class GameFunctions():
    
    '''
    code used to gain an item and lose an item if there is not enough space for one
    
    @param action: This is equal to whatever the user types
    @param item: The item that you can gain
    @param itemTaken: A boolean that tells you if the item was taken or not
    @param searchText: The text that will initially show when you search the room
    @param itemOne: The first item in your inventory
    @param itemTwo: The second item in your inventory
    @param itemThree: The third item in your inventory
    '''
    def getItem (self, action, item, itemTaken, searchText, itemOne, itemTwo, itemThree):
        if itemTaken == False:
            
            print(searchText)
            action = raw_input("Do you want to pick up this item? Yes or No?" + '\n')
            
            counter = 0
            while counter == 0:
                if action.upper() == "YES":
                    if itemOne == "":
                        itemOne = item
                        itemTaken = True
                        print ("You got a " + item)
                        counter += 1 
                        
                    elif itemTwo == "":
                        itemTwo = item
                        itemTaken = True
                        print ("You got a " + item)
                        counter += 1
                    
                    elif itemThree == "":
                        itemThree = item
                        itemTaken = True
                        print ("You got a " + item)
                        counter += 1
                        
                    else:
                        delete = raw_input("You don't have enough space to carry this item, do you want to drop one of your items? Here are your items " + 
                                           '\n' + itemOne + ", " + itemTwo + " and " + itemThree +'\n')
                        while counter == 0:
                            
                            if delete.upper() == "YES":
                                delete_item = raw_input("Which item do you want to drop? Here are your options: " + '\n' + itemOne + ", " 
                                                        + itemTwo + " and " + itemThree + '\n')
                                
                                while counter == 0:
                                    if delete_item.upper() == itemOne.upper():
                                        itemOne = item 
                                        print("You dropped " + itemOne + " and got a " + item)
                                        itemTaken = True
                                        counter += 1
                                    
                                    elif delete_item.upper() == itemTwo.upper(): 
                                        itemTwo = item 
                                        print("You dropped " + itemTwo + " and got a " + item)
                                        itemTaken = True
                                        counter += 1
                                    
                                    elif delete_item.upper() == itemThree.upper(): 
                                        itemThree = item 
                                        print("You dropped " + itemThree + " and got a " + item)
                                        itemTaken = True
                                        counter += 1
                                    
                                    else:
                                        delete_item = raw_input("Which item do you want to drop? Here are your options: " + '\n' + itemOne + ", " 
                                                        + itemTwo + " and " + itemThree + '\n' + "Type in the name of the item you want " +
                                                        "to drop" + '\n')
                            
                            elif delete.upper() == "NO":
                                print("You didn't get the " + item)
                                counter += 1
                            
                            else:
                                delete = raw_input("You don't have enough space to carry this item, do you want to drop one of your items")
                            
                elif action.upper() == "NO":
                    print("You didn't get the " + item)
                    counter += 1
                    
                else: action = raw_input("Do you want to pick up this item? Yes or No?")
                
        
        else:
            print("You already took the item that was here")
            
    '''
    code used to explore the house
    
    @param timer: how many moves that the player may make
    @param action: this is equal to whatever the user types
    @param currentRoom: this is the room that the player is currently in 
    @param keyTaken: a boolean that checks if the key is taken
    @param cookieTaken: a boolean that checks if the cookie jar is taken
    @param wineTaken: a boolean that checks if the wine is taken
    @param plungerTaken: a boolean that checks if the plunger is taken
    @param candelabraTaken: a boolean that checks if the candelabra is taken
    @param doorOpen: a boolean that checks if the door is open
    @param photoAlbumLookedAt: a boolean that checks if the player has looked at the photo album
    @param itemOne: The first item in your inventory
    @param itemTwo: The second item in your inventory
    @param itemThree: The third item in your inventory
    '''
    def houseExploration(self, timer, action, currentRoom, keyTaken, cookieTaken, wineTaken, plungerTaken, candelabraTaken, 
                         doorOpen, photoAlbumLookedAt, itemOne, itemTwo, itemThree):
        
        while timer != 0:
    
            action = raw_input('\n' + "Type what you want to do" + '\n')    
            
            counter = 0
            
            while counter == 0:
                if (action.upper() == "NORTH" or action.upper() == "SOUTH" or action.upper() == "EAST" or 
                    action.upper() == "WEST" or action.upper() == "UP" or action.upper() == "DOWN" or 
                    action.upper() == "SEARCH" or action.upper() == "KICK DOWN DOOR" or action.upper() == "OPEN DOOR"):
                    counter += 1
                else:
                    print("Try again" + '\n')    
                    action = raw_input("Type north, south, east, west, up, down to move or search to search a room" + '\n')
            
            '''
            middle floor exploration code vvv
            '''
            
            if action.upper() == "WEST" and currentRoom == "FOYER":
                currentRoom = "CLOSET"  
                print("Closet - It's just a closet, nothing new.")
                timer -= 1
                
            elif action.upper() == "SEARCH" and currentRoom == "CLOSET": 
                print("Searched Closet - There is nothing in here, just some cobwebs and... a bunch of spiders")
                timer -= 1
                
            elif (action.upper() == "SOUTH" and currentRoom == "STAIRS_1" or action.upper() == "EAST" and 
                  currentRoom == "CLOSET" or action.upper() == "WEST" and currentRoom == "LIBRARY_ROOM"):
                currentRoom = "FOYER"
                print("Foyer - A tiny room that you find yourself in after entering the house. There is a library room to your east and closet to your west and" + '\n' 
                      + " stairs to the north" + "There is also a tiny drawer in the foyer, it might be worth while to check it out.")
                timer -= 1
            
            elif action.upper() == "SEARCH" and currentRoom == "FOYER":
                GameFunctions().getItem(action, "key", keyTaken, "Searched Foyer - You looked inside a tiny drawer and found a key!", 
                                      itemOne, itemTwo, itemThree)
                
                timer -= 1
                
                    
            
            elif action.upper() == "EAST" and currentRoom == "FOYER":
                print("Library Room - A room that is filled with old books, mabey one of these books has some info on the history of the house")
                currentRoom = "LIBRARY_ROOM"
                timer -= 1
            
            elif action.upper() == "SEARCH" and currentRoom == "LIBRARY_ROOM":
                choise = raw_input("Seached Library Room - there is a photo album that looks old, do you want to look at it?")
                counter_1 = 0
                
                while counter_1 == 0:
                    if choise.upper() == "YES":
                        print("While looking throug the photo album you see a photo of a family in front of the house. Flipping through the book some more you see "  
                              + "a photo of the same family" + '\n' + "but a couple years later, everyone seems to have aged but one. A little girl who looks to be " 
                              + "around 10 looks the same in both photos.")
                        photoAlbumLookedAt = True
                        counter_1 += 1
                    
                    elif choise.upper() == "NO":
                        print("You didn't look at the photo album")
                        counter_1 += 1
                        
                    else:
                        choise = raw_input("Seached Library Room - there is a photo album that looks old, do you want to look at it, yes or no?")
                
                timer -= 1
                
                
                
            elif action.upper() == "WEST" and currentRoom == "STAIRS_1":
                print("Bathroom - A room with an old toilet and sink.")
                currentRoom = "BATHROOM_1"
                timer -= 1
            
            elif action.upper() == "SEARCH" and currentRoom == "BATHROOM_1":
                GameFunctions.getItem(self, action, "plunger", plungerTaken, "Seached Bathroom  - There is a plunger!", itemOne, itemTwo, itemThree)
                timer -= 1
                
                
                
            elif (action.upper() == "NORTH" and currentRoom == "FOYER" or action.upper() == "SOUTH" and 
                  currentRoom == "HALLWAY_1" or action.upper() == "EAST" and currentRoom == "BATHROOM_1" or 
                  action.upper() == "WEST" and currentRoom == "DINING_ROOM" or currentRoom == "STAIRS_2" and 
                  action.upper() == "UP" or currentRoom == "STAIRS_3" and action.upper() == "DOWN"):
                print("Staircase - There are two sets of stairs, one that leads upstairs and one that leads downstairs. To the north there is a hallway, south there " 
                      + '\n' + "is the foyer, east is the dining room and west is the bathroom. Type up or down to go upstairs or downstairs")
                currentRoom = "STAIRS_1"
                timer -= 1
            
            elif action.upper() == "SEARCH" and currentRoom == "STAIRS_1":
                print("Seached Staircase - You notice that at the end of the stairs that lead downstairs there is a door, it could be locked.")
                
                timer -= 1
             
                
                
            elif action.upper() == "EAST" and currentRoom == "STAIRS_1":
                print("Dining Room - A room where a family eats, I think. There is a glass cabinet here, there might be something interesting in it")
                currentRoom = "DINING_ROOM"
                timer -= 1
            
            elif action.upper() == "SEARCH" and currentRoom == "DINING_ROOM":
                GameFunctions.getItem(action, "candelabra", candelabraTaken, "Seached Dining Room  - There is a candelabra!", 
                                      itemOne, itemTwo, itemThree)
                timer -= 1
            
            
            
            elif action.upper() == "WEST" and currentRoom == "HALLWAY_1":
                print("Family Room - A room fild with old sofas... thats it")
                currentRoom = "FAMILY_ROOM"
                timer -= 1
            
            elif action.upper() == "SEARCH" and currentRoom == "FAMILY_ROOM":
                print("Family Room - There is nothing useful here")
                timer -= 1
                
                
                
            elif (action.upper() == "NORTH" and currentRoom == "STAIRS_1" or action.upper() == "EAST" and 
                  currentRoom == "FAMILY_ROOM" or action.upper() == "WEST" and currentRoom == "KITCHEN_1"):
                print("Hallway - It's a hallway filled with old creepy pictures. The family room is to the west, the kitchen is to the east and " + '\n' +
                      " the stars are to the south")
                currentRoom = "HALLWAY_1"
                timer -= 1
                
            elif action.upper() == "SEARCH" and currentRoom == "HALLWAY_1":
                print("Searched Hallway - There is a picture of a little girl with a label tat says her name is Anna, it looks like she was the only girl " + 
                      "of the family who lived here")
                
                choise = raw_input("Do you want to look at more pictures? Yes or No?" + '\n')
                counter = 0
                
                while counter == 0:
                    if action.upper() == "YES":
                        print("There is a picture of a statue of a cat? it says that his name is Picklez")
                            
                        action = raw_input("Do you want to look at more pictures? Yes or No?" + '\n')
                
                        while counter == 0:
                            if action.upper() == "YES":
                                print("There is a picture of a an old lady named March. She looks mean.")
                                counter += 1
                
                            elif action.upper() == "NO":
                                print ("Okay, you didn't look at the pictures")
                                counter += 1
                            
                    elif action.upper() == "NO":
                        print ("Okay, you didn't look at the pictures")
                        counter_1 += 1
            
                
                timer -= 1
                
                
                
            elif action.upper() == "EAST" and currentRoom == "HALLWAY_1":
                print("Kitchen - It's an old kitchen. There are a lot of cubords. It might be worth it to look through them.")
                currentRoom = "KITCHEN_1"
                timer -=1
            
            elif action.upper() == "SEARCH" and currentRoom == "KITCHEN_1":
                GameFunctions.getItem(action, "cookie jar", cookieTaken, 
                                      "Seached Kitchen  - There is a jar filled with cookies that are really old!", itemOne, 
                                      itemTwo, itemThree)
                
                timer -= 1
        
        
                '''
                basement exploration code vvv
                '''
                
            elif action.upper() == "SOUTH" and currentRoom == "BEDROOM_2":
                print("Bathroom - It is a bathroom. Nothing special. North of the bathroom is the bedroom" )
                currentRoom = "BATHROOM_2"
            
            elif action.upper() == "SEARCH" and currentRoom == "BATHROOM_2":
                print("Searched Bathroom - There is nothing useful")
                
                    
                    
            elif action.upper() == "SOUTH" and currentRoom == "KITCHEN_2":
                print("Cellar - A room that was used to store wine. North of the cellar is the kitchen")
                currentRoom = "CELLAR"
            
            elif action.upper() == "SEARCH" and currentRoom == "CELLAR":
                GameFunctions.getItem(action, "wine", wineTaken, "Searched Cellar - You found a bottle of old wine", itemOne, itemTwo, itemThree)
                
                timer -= 1
                
                
                        
            elif (action.upper() == "SOUTH" and currentRoom == "HALLWAY_2.1" or action.upper() == "NORTH" 
                  and currentRoom == "BATHROOM_2"):
                print("Bedroom - An extra bedroom that is in the basement. To the north is the west hallway and south is a bathroom")
                currentRoom = "BEDROOM_2"
            
            elif action.upper() == "SEARCH" and currentRoom == "BEDROOM_2":
                print("Searched Bedroom - There isn't anything useful")
                
                
                
            elif (action.upper() == "DOWN" and currentRoom == "STAIRS_1" or action.upper() == "SOUTH" and 
                currentRoom == "HALLWAY_2"):
                print("Downstairs Stairs - There is only one door north of where you are that leads to the basement and its locked. " + 
                      '\n' + "Mabye if you find a key and type open door it might open?")
                currentRoom = "STAIRS_2"
                timer -= 1
            
            elif action.upper() == "SEARCH" and currentRoom == "STAIRS_2":
                print("Searched Downstairs Stairs - Its a room and some stairs what did you expect to find?")
                currentRoom = "STAIRS_2"
                timer -= 1
            
            elif action.upper() == "KICK DOWN DOOR" and currentRoom == "STAIRS_2":
                print("You can't do that, the door is made of iron!")
                currentRoom = "STAIRS_2"
            
            elif (action.upper() == "OPEN DOOR" and currentRoom == "STAIRS_2" and itemOne.upper() == "KEY" or 
                  action.upper() == "OPEN DOOR" and currentRoom == "STAIRS_2" and itemTwo.upper() == "KEY" or
                  action.upper() == "NORTH" and currentRoom == "STAIRS_2" and itemThree.upper() == "KEY"):
                print("You opened the door that is to the north of you!")
                doorOpen = True
            
            
            
            elif (action.upper() == "SOUTH" and currentRoom == "HALLWAY_2.2" or action.upper() == "NORTH" 
                  and currentRoom == "CELLAR" ):
                print("Kitchen - A small kitchen in the basement")
                currentRoom = "KITCHEN_2"
            
            elif action.upper() == "SEARCH" and currentRoom == "KITCHEN_2":
                print("Searched Kitchen - There is nothing useful here just some old plates and cups")
                
                
                
            elif (action.upper() == "WEST" and currentRoom == "HALLWAY_2" or action.upper() == "NORTH" 
                  and currentRoom == "BEDROOM_2" ):
                print("West Hallway - It's just a hallway, nothing special. To the south there is a bedroom and to the east there is another hallway.")
                currentRoom = "HALLWAY_2.1"
            
            elif action.upper() == "SEARCH" and currentRoom == "HALLWAY_2.1":
                print("Searched West Hallway - There isn't anything useful. ")
                
                
                
            elif (action.upper() == "NORTH" and currentRoom == "STAIRS_2" and doorOpen == True or 
                  action.upper() == "WEST" and currentRoom == "HALLWAY_2.2" or action.upper() == "EAST" 
                  and currentRoom == "HALLWAY_2.1"):
                print("Hallway - It is a hallway. To the east and west there are halways and south is the staircase.")
                currentRoom = "HALLWAY_2"
            
            elif action.upper() == "SEARCH" and currentRoom == "HALLWAY_2":
                print("Searched Hallway - There isn't anything special.")
            
            
            
            elif (action.upper() == "EAST" and currentRoom == "HALLWAY_2" or action.upper() == "NORTH" 
                  and currentRoom == "KITCHEN_2"):
                print("East Hallway - It is just a hallway. To the west there is another hallway and to the south there is a kitchen.")
                currentRoom = "HALLWAY_2.2"
            
            elif action.upper() == "SEARCH" and currentRoom == "HALLWAY_2.2":
                print("Searched East Hallway - There isn't anything special.")
           
                
                '''
                upstairs exploration code vvv
                '''
                
            elif action.upper() == "SOUTH" and currentRoom == "KIDS_BEDROOM":
                print("Kids Bathroom - A bathroom that is south of the kids bedroom.")
                currentRoom = "KIDS_BATHROOM"
                timer -= 1
            
            elif action.upper() == "SEARCH" and currentRoom == "KIDS_BATHROOM":
                print("Kids Bathroom Bathroom - There is nothing useful here")
                timer -= 1
                
                
                
            elif action.upper() == "SOUTH" and currentRoom == "MASTER_BEDROOM":
                print("Master Bathroom - It is the bathroom that is south of the master bedroom.")
                currentRoom = "MASTER_BATHROOM"
                timer -= 1
            
            elif action.upper() == "SEARCH" and currentRoom == "MASTER_BATHROOM":
                print("Searched Master Bathroom - There is nothing useful here")
                timer -= 1
                
                
                
            elif (action.upper() == "WEST" and currentRoom == "STAIRS_3" or action.upper() == "NORTH" and 
            currentRoom == "KIDS_BATHROOM"):
                print("Kids Bedroom - A bedroom that is filled with old toys and posters. To teh south there is a bathroom and to the east is the stairs")
                currentRoom = "KIDS_BEDROOM"
                timer -= 1
            
            elif action.upper() == "SEARCH" and currentRoom == "KIDS_BEDROOM":
                print("Searched Kids Bedroom - You found a safe, looks like it is protected by a four digit password." + '\n')
                '''
                code to get the statue
                '''
                timer -= 1
                
                
                
            elif (action.upper() == "UP" and currentRoom == "STAIRS_1" or action.upper() == "SOUTH" and 
            currentRoom == "HALLWAY_3" or action.upper() == "EAST" and currentRoom == "KIDS_BEDROOM" or
            action.upper() == "WEST" and currentRoom == "MASTER_BEDROOM"):
                print("Upstairs Stairs - The upper part of the stairs. If you go down you will be on the first floor, east is the master bedroom, " + '\n' + 
                      "to the west is a kids bedroom and to the north is a hallway.")
                currentRoom = "STAIRS_3"
                timer -= 1
            
            elif action.upper() == "SEARCH" and currentRoom == "STAIRS_3":
                print("Searched Upstairs Stairs - There is nothing useful here")
                timer -= 1
                
                
                
            elif (action.upper() == "EAST" and currentRoom == "STAIRS_3" or action.upper() == "NORTH" 
            and currentRoom == "MASTER_BATHROOM"):
                print("Master Bedroom - The biggest bedroom in the house. To the south there is a bathroom and to the west there are stairs")
                currentRoom = "MASTER_BEDROOM"
                timer -= 1
            
            elif action.upper() == "SEARCH" and currentRoom == "MASTER_BEDROOM":
                print("Searched Master Bedroom - There is nothing useful here")
                timer -= 1
                
                
                
            elif action.upper() == "WEST" and currentRoom == "HALLWAY_3":
                print("Guest Room #1 - An extra room in the house. To the east there is a hallway.")
                currentRoom = "GUEST_ROOM_1"
                timer -= 1
            
            elif action.upper() == "SEARCH" and currentRoom == "GUEST_ROOM_1":
                print("Guest Room #1 - There is nothing useful here")
                timer -= 1
            
            
            
            elif (action.upper() == "NORTH" and currentRoom == "STAIRS_3" or action.upper() == "EAST" 
            and currentRoom == "GUEST_ROOM_1" or action.upper() == "WEST"  and currentRoom == "GUEST_ROOM_2"):
                print("Hallway - It is just a hallway. To the south there are stairs, to the east and west there are stairs.")
                currentRoom = "HALLWAY_3"
                timer -= 1
            
            elif action.upper() == "SEARCH" and currentRoom == "HALLWAY_3":
                print("Searched Hallway - There is nothing useful here")
                timer -= 1
                
                
                
            elif action.upper() == "EAST" and currentRoom == "HALLWAY_3":
                print("Guest Room #2 - An extra room in the house. To the west there is a hallway.")
                currentRoom = "GUEST_ROOM_2"
                timer -= 1
            
            elif action.upper() == "SEARCH" and currentRoom == "GUEST_ROOM_2":
                print("Searched Guest Room #2 - There is nothing useful here")
                timer -= 1
            
                 
            else:
                print("You hit a wall, try again!")      
                
        
        