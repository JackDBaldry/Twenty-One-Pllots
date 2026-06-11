from types import ClassMethodDescriptorType

"""
Twenty One Pilots Text Adventure
Authors: Jack B and Helena A
A text-based adventure game written in Python.
Demonstrates:
- Variables, lists, tuples, booleans
- Loops and recursion
- Conditionals and branching
- String, integer, and boolean puzzles
- Inventory system
- Multiple endings based on morality score
"""

# ===========================
# GLOBAL VARIABLES
# ===========================

#Game Control
gameOn = True   # game running flag

#User Status
BG = 0          # Black Goop collected
YBC = 0         # Yellow Box Coins
moralityTracker = 0 #Overall score

#User Items
weapon="yellow tape" #Boss fight weapon
inventory = [] #user inventory
playerName = ""
capture_TB = False # Initialize capture_TB globally
# ===========================
# GLOBAL CONSTANTS
# ===========================

#Districts
#Keons District 1, Nico District 2, Listo District 3, Andre District 4 Store
#Sacarver District 5, Vetomo District 6, Nills District 7, Reisdro District 8, Lisden District 9

#Tuple
DISTRICTS = (
    "Keons District 1",
    "Nico District 2",
    "Listo District 3",
    "Andre District 4",
    "Sacarver District 5",
    "Vetomo District 6",
    "Nills District 7",
    "Reisdro District 8",
    "Lisden District 9"
)

#Items
bowl = "bowl"
jumpsuit = "Jumpsuit"
soup = "tomato soup"
poisonous_soup = "poisonous soup" # New global variable for poisonous soup
antlers = "antlers"
bendSymbol = "bend symbol"
battleItem = "Nico's cloak"
room9_item = "Neon Vial" # Making room9_item globally accessible for use in other functions

#People
villain = "Nico"

# ===========================
# DEMA ROOM VARIABLES
# ===========================

#Central Location in Dema
waiting_area_name = "Clancy's House"
waiting_area_description = "A red and yellow interior with his little friend called Ned."
#Clancy's Password
clancyCode = "15398642_14"

#Keons District 1 - SIMPLE ADD ITEM TO LIST (ARRAY)
#Gives key for locked room3_item
room1_name = "Keons District 1"
room1_description = "You see a glistening object in the corner of the room."
room1_item = "Keons Key"

#Nico District 2 - HARD PUZZLE AND LIST (ARRAY) SEARCH
#Requires room3_item or room5_item room6_item in inventory
#Gives money for store to get room4_item
#Easy Battle
demaWeapon = "bare hands" #Default setting
room2_name = "Nico District 2"
room2_description = "As you enter, it is extremely dull and you see a huge shadowy figure in the distance."
room2_item = "Trash's Gold?"
room2_monster = "Trash the Dragon?"

#Listo District 3 - SIMPLE PUZZLE AND LIST (ARRAY) SEARCH
#Requires room1_item in inventory
#Gives locked Dema weapon
room3_name = "Listo District 3"
room3_description = "You walk in and see a box."
room3_item = "Listo Easy Puzzle Weapon"
room3_item2 = "Listo Locked Box"

#Andre District 4 Store - REMOVE ITEM FROM LIST (ARRAY)
#Requires room2_item in inventory
#Removes room2_item from inventory
room4_name = "Andre District 4 Store"
room4_description = "There are many items but one catches your eye."
room4_item = "a spoon" #for your soup

#Sacarver District 5 - BOOLEAN PUZZLE
#Gives Dema weapon
#room7_item is a clue to help solve it
room5_name = "Sacarver District 5"
room5_description = "You see a dodgy guy chilling in the shadows."
room5_item = "Sacarver Weapon"

#Vetomo District 6 - STRING PUZZLE
#Requires entry of clancyCode = "15398642_14" - the password
#Gives Dema stun weapon
room6_name = "Vetomo District 6"
room6_description = "You happen to notice an out of place item in a bookshelf."
room6_item = "Vetomo Stun Weapon"

#Nills District 14/2=7 - NUMBER PUZZLE
#Uses integer division
#Gives the clue that Nico is Blurryface for room5()
room7_name = "Nills District 14/2"
room7_description = "You enter a small and rather cramped room. There appears to be security cameras littered around. It seems heavily guarded for some reason."
room7_item = "Clue: Nico is Blurryface"

#Reisdro District 8 - JACK'S PUZZLE
room8_name = "Reisdro District 8"
room8_description = "You see a man with an important question."
room8_item = "Trash's Diamond"

#Lisden District 9 - HELENA'S PUZZLE
room9_name = "Lisden District 9"
room9_description = "A man named Lisden is inside who wants to trade for something very specific."
# room9_item is now declared globally

# ==========================
# EXPLORE DEMA ROOMS
# ==========================

#Keons District 1, Nico District 2, Listo District 3, Andre District 4 Store
#Sacarver District 5, Vetomo District 6, Nills District 7, Reisdro District 8, Lisden District 9

#Main explore Dema function - go to rooms and come back to Clancy's house
def exploreDema():
    global gameOn

    while gameOn:   # keep asking forever until a valid input is given and the game is being played
        print(f"\nYou are at {waiting_area_name} - {clancyCode}.")
        print(waiting_area_description)
        print("\nExplore the Dema Districts:")
        print(f"1: {room1_name}")
        print(f"2: {room2_name}")
        print(f"3: {room3_name}")
        print(f"4: {room4_name}")
        print(f"5: {room5_name}")
        print(f"6: {room6_name}")
        print(f"7: {room7_name}")
        print(f"8: {room8_name}")
        print(f"9: {room9_name}")
        print("0: Return to the main story")

        raw = input("\nEnter choice 0-9: ").strip()
        if not raw.isdigit():
            print("\nPlease enter a number.")
            continue
        number = int(raw)

        if number == 1:
            room1()
        elif number == 2:
            room2()
        elif number == 3:
            room3()
        elif number == 4:
            room4()
        elif number == 5:
            room5()
        elif number == 6:
            room6()
        elif number == 7:
            room7()
        elif number == 8:
            room8()
        elif number == 9:
            room9()
        elif number == 0:
            return  # back to main story
        else:
            print("You can't go that way.")

#=============================
# DEMA ROOM FUNCTIONS
#=============================

#Inventory helper function - add to list
def take_item(item, inventory):
    if item not in inventory:
        while True:  # keep asking forever until a valid input is given
            choice = input(f"\nDo you want to take the {item}? (y/n): ").lower()

            if choice == "y":   # only break if "y"
                inventory.append(item)
                print(f"\nYou picked up the {item}.")
                print("\nYour inventory is now:", inventory)
                break

            elif choice == "n":  # only break if "n"
                print(f"\nYou leave the {item} where it is.")
                print("\nYour inventory is still:", inventory)
                break

            else:
                # any other input does NOT break — the loop repeats
                print("\nPlease type y or n.")

    else:
        print("\nThere's nothing else to take here.")


#Inventory helper function - remove from list
def remove_item (item, inventory):
    #inventory check
    if item in inventory:
      inventory.remove(item)
      print(f"\nYou used the {item}.")
      return
    else:
        print(f"\nYou don't have {item}.")

#Return to waiting area helper function
def return_to_waiting_area():
    print(f"\nYou head back to {waiting_area_name}.")
    input("\nPress Enter to continue.") # Pause to let them read

#Keons District 1 - SIMPLE ADD ITEM TO LIST (ARRAY)
#Gives key for locked room3_item
def room1(): #Key
    global YBC, BG, inventory

    print(f"\n{room1_name}")
    print(room1_description)

    #inventory helper function
    take_item(room1_item, inventory)

    #Pause and then return
    return_to_waiting_area()

#Nico District 2 - HARD PUZZLE AND LIST (ARRAY) SEARCH
#Requires room3_item or room5_item room6_item in inventory
#Gives money for store to get room4_item
#Easy Battle
def room2():
    global YBC, BG, inventory, demaWeapon

    print(f"\n{room2_name}")
    print(room2_description)

    # check for any usable item
    if room3_item in inventory or room5_item in inventory or room6_item in inventory:
        demaWeapon = (
            room6_item if room6_item in inventory
            else room3_item if room3_item in inventory
            else room5_item
        )
        # special Room 6 Item message
        if demaWeapon == room6_item:
            print(f"\nCongratulations, you kept yourself and {room2_monster} calm with {demaWeapon}. +1 YBC")
            YBC = YBC + 1
            print(f"\nYou now have {YBC} YBC and {BG} BG.")
        else:
            print(f"\nUsing a {demaWeapon}, you defeat {room2_monster}. Shame you didn't have a {room6_item}. +1 BG")
            BG = BG + 1
            print(f"\nYou now have {YBC} YBC and {BG} BG.")

        #inventory helper function
        take_item(room2_item, inventory)

        #Pause and then return
        return_to_waiting_area()

    else:
        print(f"\nYou can't defeat {room2_monster} with {demaWeapon}.") #bare hands
        #Pause and then return
        return_to_waiting_area()

#Listo District 3 - SIMPLE PUZZLE AND LIST (ARRAY) SEARCH
#Requires room1_item in inventory
#Gives locked Dema weapon
def room3():
    global YBC, BG, inventory

    print(f"\n{room3_name}")
    print(room3_description)

    #Lock puzzle
    if room1_item in inventory: #if you have the key
        print(f"\nUsing the {room1_item}, you unlock the {room3_item2}.")

        #inventory helper function
        take_item(room3_item, inventory)

        #Pause and then return
        return_to_waiting_area()
    else:
        print(f"\nThe {room3_item2} is locked tight.")
        #Pause and then return
        return_to_waiting_area()

#Andre District 4 Store - REMOVE ITEM FROM LIST (ARRAY)
#Requires room2_item in inventory
#Removes room2_item from inventory
def room4(): #Store
    global YBC, BG, inventory

    print(f"\n{room4_name}")
    print(room4_description)
    if room2_item in inventory:
        print(f"\nUsing the {room2_item}, you have enough money to buy something.")

        #inventory helper function - buy room4_item
        take_item(room4_item, inventory)

        #inventory helper function - spend room2_item
        remove_item(room2_item, inventory)

        #Pause and then return
        return_to_waiting_area()
    else:
        print("You can't go shopping without money.")
        #Pause and then return
        return_to_waiting_area()

#Sacarver District 5 - BOOLEAN PUZZLE
#Gives Dema weapon
#room7_item is a clue to help solve it
def room5():
    global YBC, BG, inventory
    blurryface = True #Boolean ans
    reallyNico = True #User guess

    print(f"\n{room5_name}")
    print(room5_description)

    #Ask if they want to talk to Sacarver
    while True: # keep asking forever until a valid input is given
      choice = input("\nDo you talk to him? (y/n): ").lower().strip()

      #Talk to Sacarver
      if choice == "y": # only break if "y"

          #Ask if Nico is Blurryface
          print("\nSacarver asks if it's true Blurryface is really named Nico?")

          while True: # keep asking forever until a valid input is given
            choice = input("\nTrue or False? (t/f): ").lower().strip()

            #Get user's guess
            if choice == "t": # only break if "t"
              reallyNico = True
              break
            elif choice == "f": # only break if "f"
              reallyNico = False
              break
            else: # any other input does NOT break — the loop repeats
              print("\nPlease type t or f.")

          #Check user's guess
          if reallyNico == blurryface: #They got it right
              print(f"\nSacarver trusts you. +1BG")
              BG = BG + 1
              print(f"\nYou now have {YBC} YBC and {BG} BG.")
              #inventory helper function
              take_item(room5_item, inventory)
          else: #They got it wrong
              print("\nSacarver looks ar you suspiciously - you run away.")

          break #end of yes talk to Sacarver option

      elif choice == "n": # only break if "n"
          print("\nYou run away from Sacarver.")
          break

      else: # any other input does NOT break — the loop repeats
          print("\nPlease type y or n.")

    return_to_waiting_area()

#Vetomo District 6 - STRING PUZZLE
#Requires entry of clancyCode = "15398642_14" - the password
#Gives Dema stun weapon
def room6():
    global YBC, BG, inventory, clancyCode
    print(f"\n{room6_name}")
    print(room6_description)

    #clancyCode = "15398642_14" - the password

    while True: # keep asking forever until a valid input is given
        choice = input("\nYou see a laptop - it's asking you for a password.\nUse the laptop? (y/n): ").lower().strip()
        if choice == "y":# only break if "y"
            userCode = input("\nEnter code: ").strip()

            #This shows understanding that strings are a type of array/list that can be searched
            if clancyCode in userCode:
                print("\nACCESS GRANTED: Hello Clancy.")
                take_item(room6_item, inventory)
            else:
                print("\nACCESS DENIED: That is not Clancy's password.")
            break
        elif choice == "n":# only break if "n"
            print("\nYou leave the laptop alone.")
            break
        else: # any other input does NOT break — the loop repeats
            print("\nPlease type y or n.")

    return_to_waiting_area()

#Nills District 14/2=7 - NUMBER PUZZLE
#Uses integer division
#Gives the clue that Nico is Blurryface for room5()
def room7():
    global YBC, BG, inventory
    print(f"\n{room7_name}")
    print(room7_description)

    #room7_item tells you that Nico is Blurryface

    print("\nOn the wall you see: 18 \u00f7 2 = ?")
    print("\nEnter the answer as a whole number.")

    while True:  # keep asking until valid
        raw = input("\nYour answer: ").strip()
        if not raw.isdigit():
            print("\nPlease enter a number.")
            continue
        number = int(raw)
        if number == 18 // 2:   # integer division check -break if correct
            print("\nCorrect - a district for all who side with Blurryface.")
            print("\nThere is a file on the leader of the 9 available.")
            take_item(room7_item, inventory)
            break
        else: # any other input does NOT break — the loop repeats
            print("\nThat doesn\u2019t seem right. Try again.")

    return_to_waiting_area()

#Reisdro District 8 - JACK's PUZZLE
def room8(): #Item
    global YBC, BG, inventory

    print(f"\n{room8_name}")
    print(room8_description)

    choice = input("\nInside the district is Reisdro and he says 'Josh Dun is who?' \nOption A = The Torchbearer or Option B = Nico").upper().strip()
    if choice == "A":
        print("\nYou have chosen correctly")
        if room3_item in inventory:
            choice2 = input(f"\nWould you like to give Reisdro {room3_item}? (y/n)").lower().strip()
            if choice2 == "y":
                print(f"\nHe takes apart {room3_item} and inside there is {room8_item}")
                take_item(room8_item, inventory)
                remove_item(room3_item, inventory)
            elif choice2 =="n":
                print(f"\nYou decide not to give him {room3_item} and move on")
            else:
                print("\nPlease type y or n.")
                print(f"\nWould you like to give Reisdro {room3_item}? (y/n)").lower().strip()
        else:
             print(f"\nYou don't have {room3_item} so you continue")
    elif choice == "B":
        print("\nYou have made the wrong choice")
    else:
        print("\nPlease type A or B")
        print("\nInside the district is Reisdro and he says 'Josh Dun is who?' \nOption A = The Torchbearer or Option B = Nico")


    #Pause and then return
    return_to_waiting_area()

#Lisden District 9 - HELENA'S PUZZLE
def room9(): #Item
    global YBC, BG, inventory, room9_item

    print(f"\n{room9_name}")
    print(room9_description)

    if room8_item in inventory:
     choice = input(f"\nHe is holding a small vial full of an unknown neon liquid. \nHe asks if you want to trade the second piece of tresure for it. (y/n):").lower().strip()
     if choice == "y":
      print(f"\nYou trade with Lisden and take the vial, it seems to be glowing bright cyan")
      take_item(room9_item, inventory)
      remove_item(room8_item, inventory)
     elif choice == "n":
      print(f"\nYou do not trade with Lisden. Moving on I guess")
     else:
      print("\nPlease type y or n.")
    else:
      print(f"\nHe is holding a small vial full of an unknown neon liquid. \nYou don't have anything he wants to trade with you")

    #Pause and then return
    return_to_waiting_area()


# ===========================
# MAIN PROGRAM
# ===========================

def main():
    global BG, YBC, moralityTracker, gameOn, inventory, capture_TB # Add capture_TB to main's globals
    BG = 0
    YBC = 0
    gameOn = True
    inventory = []
    capture_TB = False # Reset capture_TB for each new game
    scene_a()


# ===========================
# SCENE A – Car Incident
# ===========================

def scene_a():
    global gameOn, bowl, inventory, playerName
    option1 = 1
    option2 = 2
    option3 = 3

    while True:  # keep asking until valid
        playerName = input(f"\nWhat is your name? ").strip()
        if playerName == "Clancy":
            print(f"\nHello {playerName}, we've been expecting you.")
            break
        else:
            print(f"\nHello {playerName}, it's nice to meet you.")
            break
    else:
        print("\nPlease tell me your name. Are you Clancy?")

    input("\nPress Enter to continue.")  # Pause to let them read

    print("\nIt\u2019s a gloomy, cold, winter day.")
    print("\nYou're driving your rustbucket of a car down country lanes.")
    print("\nYou hear a loud clonk noise and begin to see sparks.")
    print("\nWhat do you do?")
    print(f"\n{option1}: Controlled stop and examine car.")
    print(f"\n{option2}: Jump out into a field.")
    print(f"\n{option3}: Jump out into a field and take your {bowl}.")

    while True:  # keep asking until valid
        raw = input(f"\nEnter choice {option1}, {option2} or {option3}: ").strip()
        if not raw.isdigit():           # check BEFORE int()
            print("\nPlease enter a number.")
            continue

        number = int(raw)

        if number == option1: # only break if option1
            ending1()
            break
        elif number == option2: # only break if option2
            print("\nYou land safely with only a grazed arm.")
            scene_a2()
            break
        elif number == option3: # only break if option3
            print(f"\nYou land safely with only a grazed arm and your {bowl} intact.")
            inventory.append(bowl)
            print("\nYour inventory is now:", inventory)
            scene_a2()
            break
        else: # any other input does NOT break — the loop repeats
            print("\nPlease enter a valid option.")


# ===========================
# SCENE A2 – Two Paths
# ===========================

def scene_a2():
    option1 = "B1"
    option2 = "B2"
    print("\nYou notice two paths:")
    print(f"\n{option1}: A high road up towards a forest.")
    print(f"\n{option2}: A low road down a steep hill.")

    while True: # keep asking forever until a valid input is given
      choice = input(f"\nEnter choice {option1} or {option2}: ").strip().upper()
      #High road
      if choice == option1: # only break if option1
          scene_a2_b1()
          break
      #Low road
      elif choice == option2: # only break if option2
          scene_a2_b2()
          break
      else: # any other input does NOT break — the loop repeats
          print("\nPlease enter a valid option.")


# ===========================
# SCENE A2.B1 – Forest & Hut
# ===========================
#Demonstration of recursion to remain
def scene_a2_b1():
    global gameOn
    option1 = "C1"
    option2 = "C2"
    option3 = "D1"
    option4 = "D2"

    print("\nYou find a hut. Do you go inside?")
    print(f"\n{option1}: Go inside.")
    print(f"\n{option2}: Stay outside and continue.")
    choice = input(f"\nEnter choice {option1} or {option2}: ").strip().upper()

    #Go in the hut
    if choice == option1:
        ending2()

    #Stay outside
    elif choice == option2:
        print("\nYou continue and meet random campers.\nThey may be hostile.")
        print(f"\n{option3}: Ask to join them.")
        print(f"\n{option4}: Ignore them and continue.")
        choice = input(f"\nEnter choice {option3} or {option4}: ").strip().upper()

        #Join Campers
        if choice == option3:
            ending3()

        #Ignore Campers
        elif choice == option4:
            ending4()
        else:
            print("\nPlease enter a valid option.")
            scene_a2_b1() #Recursive retry if input invalid, instead of while loop
    else:
        print("\nPlease enter a valid option.")
        scene_a2_b1() #Recursive retry if input invalid, instead of while loop

# ===========================
# A2.B2 – Steep Hill & Trench
# ===========================
#JACK CHANGE RECURSION TO WHILE LOOP
def scene_a2_b2():
    global BG, YBC
    option1 = "C3"
    option2 = "C4"
    print("\nYou wander down the steep hill into a trench.")
    print("\nA red figure is following you.")
    print(f"\n{option1}: Run away immediately.")
    print(f"\n{option2}: Scope out the threat.")

    #Run away
    while True:

      #Get input
      choice = input(f"\nEnter choice {option1} or {option2}: ").strip().upper()

      #Option 1
      if choice == option1: #only break if choice is option 1
        print("\nIt catches you on a horse (no Black Goop BG gained and +1 Yellow Bandito Coin YBC).")
        YBC = YBC + 1
        print(f"\nYou now have {YBC} YBC and {BG} BG.")
        scene_dema()
        break #Need this to exit the loop

      #Option 2 - Scope
      elif choice == option2: #only break if choice is option 1
        print("\nIt catches you sooner (+2 Black Goop BG).")
        BG = BG + 2
        print(f"\nYou now have {YBC} Yellow Bandito Coins YBC - these are good.\nYou have {BG} Black Goop BG points - these are bad.")
        scene_dema()
        break #Need this to exit the loop

      else: # any other input does NOT break — the loop repeats
        print("\nPlease enter a valid option.")

# ===========================
# Dema City Branch
# ===========================

def scene_dema():
    global BG, YBC, antlers, inventory, bendSymbol
    option1 = 1
    option2 = 2
    option3 = 3

    print("\nYou are taken to a city called Dema.")
    print("\nYou cannot leave until you complete your mission.")
    print("\nFree Dema or rule it - the choice is up to you.")
    print("\nYou find yourself in a small room.")

    # ----- BOXES -----
    if antlers not in inventory: #They don't already have the antlers
        print("\nYou see two boxes.")
        print(f"\n{option1}: Open left box.")
        print(f"\n{option2}: Open right box.")
        print(f"\n{option3}: Walk away")

        while True: #Keep asking until valid
            raw = input(f"\nEnter choice {option1}, {option2} or {option3}: ").strip()
            if not raw.isdigit():
                print("\nPlease enter a number.")
                continue
            number = int(raw)

            if number == option1: #only break if option1 antlers
                inventory.append(antlers)
                YBC += 1
                print(f"\nYou now have {YBC} YBC and {BG} BG.")
                print("\nYour inventory is now:", inventory)
                break
            elif number == option2: #only break if option2 BG
                BG += 1
                print(f"\nYou now have {YBC} YBC and {BG} BG.")
                break
            elif number == option3: #only break if option3 Nothing
                print("\nYou can't be bothered. Boring.")
                break
            else: # any other input does NOT break — the loop repeats
                print("\nPlease enter a valid option.")
    else: #They have the antlers
        print("\nThere's nothing of interest in the boxes.")

    # ----- NOTE -----
    print("\nYou see a note on the wall.")
    if bendSymbol not in inventory: #They don't already have the bend symbol
        print(f"\n{option1}: Read the note")
        print(f"\n{option2}: Leave the note.")
        print(f"\n{option3}: Throw it away. Honestly, litter.")

        while True: #Keep asking until valid
            raw = input(f"\nEnter choice {option1}, {option2} or {option3}: ").strip()
            if not raw.isdigit():
                print("\nPlease enter a number.")
                continue
            number = int(raw)

            if number == option1: #only break if option1 Read note
                inventory.append(bendSymbol)
                print(f"\nYour inventory is now:", inventory)
                break
            elif number == option2: #only break if option2 Leave note
                print("\nYou leave the note where it is.")
                break
            elif number == option3: #only break if option3 Litter
                BG += 1
                print(f"\nYou now have {YBC} YBC and {BG} BG.")
                break
            else: # any other input does NOT break — the loop repeats
                print("\nPlease enter a valid option.")

    else: #They have the bend symbol
        print("\nThe note seems blank now.")

    # ----- NEXT STEP -----
    print("\nYou can explore Dema or follow a man in yellow.")
    print(f"\n{option1}: Explore Dema")
    print(f"\n{option2}: Follow the man in yellow")

    while True: #Keep asking until valid
        raw = input(f"\nEnter choice {option1} or {option2}: ").strip()
        if not raw.isdigit():
            print("\nPlease enter a number.")
            continue
        number = int(raw)

        if number == option1: #only break if option1 Explore Dema
            #print("\nYou wander around Dema, but nothing else seems useful.")
            exploreDema()
            print("\nAfter exploring Dema you follow the man in yellow...")
            scene_banditos()  #game continues
            break
        elif number == option2: #only break if option2 follow the man
            scene_banditos()
            break
        else: # any other input does NOT break — the loop repeats
            print("\nPlease enter a valid option.")

# ===========================
# Banditos Encounter
# ===========================
#LENA CHANGE RECURSION TO WHILE LOOP
def scene_banditos():
    global gameOn, YBC, inventory, jumpsuit
    option1 = "D5"
    option2 = "D6"
    print("\nA man in yellow leads you to a tunnel.")
    print(f"\nBanditos arrive and offer you a {jumpsuit} to join them.")
    print(f"\n{option1}: Decline.")
    print(f"\n{option2}: Put on {jumpsuit} (requires YBC).")
    print(f"\nYou have {YBC} YBC and {BG} BG.")

    while True: # Keep asking until valid

      choice = input(f"\nEnter choice {option1} or {option2}: ").strip().upper()

      #Only break if choice = option 1
      if choice == option1:
        print(f"\nYou didn't take {jumpsuit}.")
        print("\nYour inventory is now:", inventory)
        ending5()
        break  # Exit the loop after choosing an ending

      #Only break if choice = option 2
      elif choice == option2:
        if YBC >= 1:
          print(f"\nYou take the {jumpsuit}.")
          inventory.append(jumpsuit)
          print("\nYour inventory is now:", inventory)
          print("\nYou join the Banditos and escape Dema.")
          scene_camp()
        else:
          print(f"\nYou didn't take {jumpsuit}.")
          print("\nYour inventory is now:", inventory)
          ending6()
        break  # Exit the loop after making a choice

      #any other input does NOT break — the loop repeats
      else:
        print("\nPlease enter a valid option.\n")

# ===========================
# Campsite Scene
# ===========================
#LENA CHANGE RECURSION TO WHILE LOOP
def scene_camp():
    global gameOn
    option1 = "E1"
    option2 = "E2"
    print("\nThe Banditos lead you to a campsite.")
    print(f"\n{option1}: Leave immediately.")
    print(f"\n{option2}: Stay the night.")

    while True: # Keep asking until valid
        choice = input(f"\nEnter choice {option1} or {option2}: ").strip().upper()

        if choice == option1:
            ending7()
            break # Exit the loop after choosing an ending
        elif choice == option2:
            scene_campfire()
            break # Exit the loop after making a choice
        else:
            print("\nPlease enter a valid option.")

# ===========================
# Campfire Conversation
# ===========================
#JACK CHANGE RECURSION TO WHILE LOOP
def scene_campfire():
    global soup, inventory, room9_item, poisonous_soup, capture_TB # Added capture_TB to globals
    option1 = "F1"
    option2 = "F2"
    print("\nYou are around the campfire.")
    print(f"\n{option1}: Sleep early.")
    print(f"\n{option2}: Talk to the Torchbearer and others (gain info).")

    while True:
        choice = input(f"\nEnter choice {option1} or {option2}: ").strip().upper()
        if choice == option1:
          if room5_item in inventory:
            while True: # Keep asking until valid
               choice2 = input(f"The Torchbearer and the Banditos are asleep. Do you use the weapon from Sacarver to capture them them? Y or N?").lower().strip()
               if choice2 == "y":
                 print("In the middle of the night you decide to get up. With your weapon from Sacarver in hand, you quietly leave the tent")
                 print("Using the elemet of surprise, you surprise attack the Torchbearer and capture him.")
                 capture_TB = True # Set capture_TB to True if this path is taken
                 scene_finalbattle()
                 break # Break from inner while loop
               elif choice2 == "n":
                 print("\nYou decide to rest and prepare for the next day.")
                 scene_finalbattle()
                 break
               else:
                 print("PLease type y or n.")
            break # Break from outer while loop after handling option1

        elif choice == option2:
            torchbearer_warned_about_vial = False # Flag to track if vial was shown and warned
            if room9_item in inventory: # Check if player has the Neon Vial
                while True:
                    show_vial_choice = input(f"\nDo you want to show the {room9_item} to the Torchbearer? (y/n): ").lower().strip()
                    if show_vial_choice == "y":
                        print(f"\nThe Torchbearer examines the {room9_item} and says, 'Be careful with this. It's toxic.'")
                        torchbearer_warned_about_vial = True
                        break
                    elif show_vial_choice == "n":
                        print(f"\nYou keep the {room9_item} to yourself.")
                        break
                    else:
                        print("\nPlease type y or n.")

            if bowl in inventory: # Check for bowl before offering soup
                print(f"\nYou have a {bowl}, so you can have some soup.")
                inventory.append(soup) # Add regular soup first
                print("\nYour inventory is now:", inventory)

                # Offer to poison the soup if vial was shown and is still in inventory
                if torchbearer_warned_about_vial and room9_item in inventory: # Only offer if vial was shown and is still in inventory
                    while True:
                        poison_soup_choice = input(f"\nDo you want to add the {room9_item} liquid to your soup? (y/n): ").lower().strip()
                        if poison_soup_choice == "y":
                            if soup in inventory: # Check if regular soup is there to remove
                                inventory.remove(soup)
                            inventory.append(poisonous_soup)
                            inventory.remove(room9_item) # Remove the vial as it's been used
                            print(f"\nYou carefully pour the {room9_item} liquid into your soup, making it {poisonous_soup}.")
                            print("\nYour inventory is now:", inventory)
                            break
                        elif poison_soup_choice == "n":
                            print("\nYou decide against adding the liquid to your soup.")
                            break
                        else:
                            print("\nPlease type y or n.")
                scene_finalbattle()
            else: # Player doesn't have a bowl
                print(f"\nYou don't have a {bowl}, so you talk but stay hungry.")
                scene_finalbattle()
            break
        else:
            print("\nPlease enter a valid option.")

# ===========================
# Final Battle
# ===========================
#Demonstration of while loop and recursion
def scene_finalbattle():
    global gameOn, soup, poisonous_soup, antlers, bendSymbol, inventory, weapon
    global BG, YBC, battleItem, villain, capture_TB # Declare capture_TB as global

    option1 = "G1"
    option2 = "G2"
    option3 = "G3"

    print("\nThe next morning you leave the camp and the red figure chases you again.")
    print(f"\n{option1}: Run away.")
    print(f"\n{option2}: Fight.")
    if capture_TB == True: # Now capture_TB is guaranteed to be defined
      print(f"{option3}: Hand over the Torchbearer to {villain}")
    else:
      pass
    choice = input(f"\nEnter choice {option1} or {option2} or {option3}: ").strip().upper()

    if choice == option1:
        ending8()
        return # avoid continuing after ending - stop execution

    elif choice == option3 and capture_TB == True: # Only allow this option if Torchbearer was captured
        print("Betraying the Banditos, you hand the Torchbearer and his companions over to Nico and the Bishops")
        print("They are sentenced to be exiled to the island Voldsoy and taken away.")
        print("Nico turns to you and hands you a red cloak resembling his own with a toothy grin.")
        inventory.append(battleItem)
        BG = BG + 5
        print("You join the Bishops in ruling Dema with an iron fist. +5 BG")
        scene_fightresult()

    elif choice == option2:
        # Battle description
        print("\nBattle Description")

        # check inventory for any weapon to fight Nico
        # UPDATED: Check for poisonous_soup too
        if poisonous_soup in inventory or soup in inventory or antlers in inventory or bendSymbol in inventory:
            # choose best available weapon
            # UPDATED: prioritize poisonous_soup
            weapon = chooseWeapon() # Let user choose weapon after all checks

            # special soup message
            # UPDATED: Handle poisonous_soup differently
            if weapon == poisonous_soup:
                print(f"\nYou offer {villain} the {poisonous_soup}. He quickly eats it and started to feel unwell so he has leaves.+5 BG")
                BG = BG + 5
                print(f"\nYou now have {YBC} YBC and {BG} BG.")
            elif weapon == soup: # Original soup logic
                print(f"\nCongratulations, you shared your {soup} with {villain} and he saw the light and freed Dema.\nGood thing {villain} had spoons. +1 YBC")
                YBC = YBC + 1
                print(f"\nYou now have {YBC} YBC and {BG} BG.")
            else:
                print(f"\nUsing a {weapon}, you fight {villain}.\nShame you didn't bring delicious soup or poisonous soup.") # Updated message

            #WHILE LOOP
            # ask if they want Nico's cloak
            if battleItem not in inventory:
              while True: # loop until valid input
                cloakChoice = input(f"\nDo you want to take the {battleItem}? (y or n): ").lower()
                if cloakChoice == "y": # only break if "y"
                    inventory.append(battleItem)
                    print(f"\nYou pick up the {battleItem}.")
                    BG = BG + 5
                    print(f"\nYou now have {YBC} YBC and {BG} BG.")
                    break
                elif cloakChoice == "n": #only break if "n"
                    print(f"\nYou leave the {battleItem} where it is.")
                    break
                else: # any other input does NOT break — the loop repeats
                    print("\nPlease type y or n.")
            else:
              pass

            print("\nYour inventory is now:", inventory)

        else:
            # No special weapon available
            if BG > 0:
               print(f"\nYou try to defeat {villain} with {weapon}. It's not great.")
            else:
               print(f"\nYou try to defeat {villain} with {weapon}... You really shouldn't have...but somehow you won the fight. Clearly you must have plot armour")

        scene_fightresult() # move on to fight result
    else: # This else now handles invalid choices OR G3 when capture_TB is False
        print("\nPlease enter a valid option.\n")
        scene_finalbattle() # RECURSIVE retry if input invalid, instead of while loop

# ===========================
# USER CHOOSE WEAPON
# ===========================
#JACK CHANGE TO WHILE LOOP INSTEAD OF RECURSION
def chooseWeapon():
    global soup, poisonous_soup, antlers, bendSymbol, weapon, inventory # Added poisonous_soup
    print("\nYour inventory is currently:", inventory)
    print("\nWhat would you like to use?")
    # UPDATED: Add poisonous soup as an option
    print(f"\ns = {soup}, p = {poisonous_soup}, a = {antlers}, b = {bendSymbol}")

    while True:
     weaponChoice = input("\nEnter choice: ").strip().lower()
     if weaponChoice == "s" and soup in inventory:
        weapon = soup
        return weapon
     elif weaponChoice == "p" and poisonous_soup in inventory: # New option for poisonous soup
        weapon = poisonous_soup
        return weapon
     elif weaponChoice == "a" and antlers in inventory:
        weapon = antlers
        return weapon
     elif weaponChoice == "b" and bendSymbol in inventory:
        weapon = bendSymbol
        return weapon
     else:
        print("\nInvalid choice or you don't have that item.")
        # try again until a valid weapon is chosen


# ===========================
# Fight Result Depending on BG
# ===========================

def scene_fightresult():
    global gameOn, BG
    if BG >= 5:
        winEndingBad() #Win supervillain
    elif BG ==4:
        ending9() #Fight and die
    elif BG ==3:
        ending10() #Fight and die
    elif BG in [1, 2]:
        winEndingTrue() #True ending - win bad
    else:
        winEndingGood() #Win good

#============================
# ENDINGS
#============================

def winEndingGood():
    global gameOn
    print(f"\nYou defeat {villain} and are saved.")
    gameOn = end_Credits()

def winEndingTrue():
    global gameOn
    print(f"\nYou defeat {villain} but turn to the dark side. A bit.")
    gameOn = end_Credits()

def winEndingBad():
    global gameOn
    print(f"\nYou are worse than {villain}. You now rule Dema.")
    gameOn = end_Credits()

def ending1():
    global gameOn
    print("\nYour car bursts into flames while you\u2019re still in it. You die.")
    gameOn = end_Credits()

def ending2():
    global gameOn
    print("\nArrow trap inside the hut. You die.")
    gameOn = end_Credits()

def ending3():
    global gameOn
    print("\nThey throw you on the fire. You get eaten.")
    gameOn = end_Credits()

def ending4():
    global gameOn
    print("\nNo supplies. You die of dehydration.")
    gameOn = end_Credits()

def ending5():
    global gameOn
    print("\nYou stay trapped in Dema forever. You failed your mission.")
    gameOn = end_Credits()

def ending6():
    global gameOn
    print("\nYou cannot pay. You remain in Dema. You failed your mission.")
    gameOn = end_Credits()

def ending7():
    global gameOn
    print("\nIt finds you at night and re-captures you. Stuck in Dema forever. You failed your mission.")
    gameOn = end_Credits()

def ending8():
    global gameOn
    print("\nYou are caught and returned to Dema. You failed your mission.")
    gameOn = end_Credits()

def ending9():
    global gameOn
    print("\nYou attempt to fight but die.")
    gameOn = end_Credits()

def ending10():
    global gameOn
    print(f"\n{villain} takes pity on you and lets you crawl away.")
    gameOn = end_Credits()



# ===========================
# End Credits
# ===========================

#Morality Score decides if districts are freed
def end_Credits():
    global YBC, BG, moralityTracker, inventory
    moralityTracker = YBC - BG
    print(f"\nYou have {YBC} YBC and {BG} BG.")  # Game scores
    print(f"\nYour morality score was: {moralityTracker}.")  # Morality score
    print("\nYour inventory was:", inventory)  # User's final inventory

    # Banditos free districts if morality > 0
    if moralityTracker > 0:
        print("\nThe Banditos rally with you and free districts from Dema:")
        # Demonstrates a for loop
        for i in range(moralityTracker):
            if i < len(DISTRICTS):
                print(f"- {DISTRICTS[i]}")
            else:
                print("- The people cheer, but there are no more districts left to free!")
                break

        # ----- SCOREBOARD -----
        # Show how many districts were freed out of the total.
        # min() is used so that if moralityTracker is bigger than the number of districts,
        # it doesn't try to count more than exist. For example, if morality = 12, it shows 9/9.
        print(f"\n{min(moralityTracker, len(DISTRICTS))}/{len(DISTRICTS)} districts freed.")

    else:  # Morality was not greater than 0
        print("\nNo districts were freed. Dema remains in control.")

    input("\nPress Enter to exit.")  # Pause to let them read before exit
    return False

# ===========================
# PROGRAM START
# ===========================

if __name__ == "__main__":
    while True:
        main()
        if input("\nPlay again? (Y/N): ").strip().upper() != "Y":
            break
