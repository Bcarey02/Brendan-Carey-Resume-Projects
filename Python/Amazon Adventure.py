    
import sys

name=""    
monkey=False
rope=False
spear=False
idol=False
fAidKit=False
healthy=False
introText=True
jaguar=True
rig=False
piranhas=True
gold=False

def quit():
    print("\nThanks for playing!")
    sys.exit()
    
def introScene():
    global fAidKit
    global healthy
    global introText
    print("\n")
    print("🌳🌳   🪨🪨")    
    print("🌳        🪨")
    print("🌳   👮     ")
    print("🪨   ✈️   🪨")
    print("🪨🪨🪨🪨🪨")
    print("\n")
    directions = ["north", "east"]
    if introText==True:
        print("Your small plane just crash landed on a mountain in the Amazon Rainforest. Your copilot didn’t make it and your leg is bleeding.")
    introText=False
    if fAidKit == False and healthy == False:
        print("There’s a First Aid Kit in the plane.")
    userInput = ""
    while userInput not in directions:
      print("What will you do?")
      userInput = input()
      print("\n")
      if userInput == "north":
        vantageScene()
      elif userInput == "east":
        spearScene()
      elif userInput == "take first aid kit" and fAidKit==False and healthy==False:
        fAidKit=True
        print("You pick up the first aid kit")
      elif userInput == "use first aid kit" and fAidKit==True:
        healthy=True
        fAidKit=False
        print("You bandage your leg.")
      else: 
        print("Please enter a valid option.")

def spearScene():
    global fAidKit
    global healthy
    global spear
    print("\n")
    print("🌳🌳🌳🌳🌳")    
    print("🪨        🌳")
    if spear==False:
        print("   👮  🥄🌳")
    else:
        print("   👮     🌳")
    print("🪨        🪨")
    print("🪨🪨🪨🪨🪨")
    print("\n")
    directions = ["west"]
    print("You come to a clearing and find a spear sticking out of the mud.")
    userInput = ""
    while userInput not in directions:
      print("What will you do?")
      userInput = input()
      print("\n")
      if userInput == "west":
          introScene()
      elif userInput == "take spear" and spear == False:
          spear = True
          print("You pull the spear out of the mud")
      elif userInput == "use first aid kit" and fAidKit==True:
        healthy=True
        fAidKit=False
        print("You bandage your leg.")
      else: 
        print("Please enter a valid option.")

def vantageScene():
    global fAidKit
    global healthy
    print("\n")
    print("🌳🪨🪨🪨🪨")
    print("🌳        🪨")
    print("     👮   🪨")
    print("🌳           ")
    print("🌳🌳   🪨🪨") 
    print("\n")
    directions = ["south", "west", "east"]
    print("You come to a vantage point on the mountain. You see the Amazon River to the northeast and wilderness all around you.")
    userInput = ""
    while userInput not in directions:
      print("What will you do?")
      userInput = input()
      print("\n")
      if userInput == "south":
          introScene()
      elif userInput == "east":
          cliffScene()
      elif userInput == "west":
          jaguarScene()
      elif userInput == "use first aid kit" and fAidKit==True:
        healthy=True
        fAidKit=False
        print("You bandage your leg.")
      else: 
        print("Please enter a valid option.")

def jaguarScene():
    global fAidKit
    global healthy
    global spear
    global jaguar
    print("\n")
    print("🌳🌳🌳🌳🌳")
    print("🌳    👮    ")
    if jaguar==True:
        print("🌳🐅     🌳")
    else:
        print("🌳     🐅🌳")
    print("🌳        🌳")
    print("🌳  🌳🌳🌳")
    print("\n")
    directions = ["east","south"]
    if jaguar==True:
        print("You find yourself in an area shaded by trees. You spot a hungry jaguar standing on a limb blocking your path.")
    userInput = ""
    while userInput not in directions:
      print("What will you do?")
      userInput = input()
      print("\n")
      if userInput == "south" and jaguar==True:
          print("You try to get past the jaguar. He leaps down from the tree and kills you.")
          quit()
      elif userInput == "south" and jaguar==False: 
          ropeScene()
      elif userInput == "east":
          vantageScene()
      elif userInput == "use spear" and jaguar==True and spear==True:
          jaguar=False
          spear=False
          print("As you walk past the jaguar he leaps at you. You put your spear through his chest.")
      elif userInput == "use first aid kit" and fAidKit==True:
        healthy=True
        fAidKit=False
        print("You bandage your leg.")
      else: 
        print("Please enter a valid option.")

def ropeScene():
    global fAidKit
    global healthy
    global rope
    print("\n")
    print("🌳🌳   🌳🌳")    
    print("🪨        🌳")
    print("🪨   👮  🪨")
    if rope==False:
        print("🪨🩻🪢🩻🪨")
    else:
        print("🪨🩻   🩻🪨") 
    print("🪨🪨🪨🪨🪨")
    print("\n")
    directions = ["north"]
    print("You walk over to a rocky area of the mountain. You come across a couple of skeletons.")
    if rope==False:
        print("They have climbing gear on.")
    userInput = ""
    while userInput not in directions:
      print("What will you do?")
      userInput = input()
      print("\n")
      if userInput == "take climbing gear" and rope==False:
          rope=True
          print("You relieve one of the skeltons of their climbing gear. He won't be needing it.")
      elif userInput == "north":
          jaguarScene()
      elif userInput == "use first aid kit" and fAidKit==True:
        healthy=True
        fAidKit=False
        print("You bandage your leg.")
      else: 
        print("Please enter a valid option.")

def cliffScene():
    global fAidKit
    global healthy
    global rope
    global rig
    print("\n")
    print("🌳🌳   🌳🌳")   
    print("🌳        🪨")
    print("🪨🪨   🌳🪨")
    print("     👮   🪨")
    print("🪨🪨🪨🪨🪨")
    print("\n")
    directions = ["west","north"]
    print("You come to the edge of the mountain. It has a flat cliff face. A tree hangs over the edge.")
    userInput = ""
    while userInput not in directions:
      print("What will you do?")
      userInput = input()
      print("\n")
      if userInput == "west":
          vantageScene()
      elif userInput == "north" and rig==False:
          print("You try climbing down the cliff. You fall to your death. What did you think would happen?")
          quit()
      elif userInput == "north" and rig==True:
          fAidKit=False
          print("You leave all your items behind and slowly make your way down the cliff. You walk north.")      
          monkeyScene()
      elif userInput == "use climbing gear" and rig==False and rope==True:
          rope=False
          rig=True
          print("You rig your gear to tree.")
      elif userInput == "use first aid kit" and fAidKit==True:
        healthy=True
        fAidKit=False
        print("You bandage your leg.")
      else: 
        print("Please enter a valid option.")

def monkeyScene():
    global monkey
    print("\n")
    print("🌳🌳🌳🌳🌳")   
    if monkey==False:
        print("🌳   🙈  🌳")
    else:
        print("🌳        🌳")
    print("     👮   🌳")
    print("🌳        🌳")
    print("🌳🌳   🌳🌳")   
    print("\n")
    directions = ["south","west"]
    if monkey==False:
        print("You find the body of a monkey. There’s a broken branch nearby. It must have fallen from the trees.")
    userInput = ""
    while userInput not in directions:
      print("What will you do?")
      userInput = input()
      print("\n")
      if userInput == "west":
          trailScene()
      elif userInput == "south":
          print("Your leg won't allow you to climb back up the cliff.")
          monkeyScene()
      elif userInput == "take monkey" and monkey==False:
          monkey=True
          print("You pick up the monkey and take him with you. Poor thing.")
      else: 
        print("Please enter a valid option.")
        
def trailScene():
    print("\n")
    print("🌳🌳   🌳🌳")   
    print("🌳        🌳")
    print("🌳   👮     ")
    print("          🌳")
    print("🌳🌳🌳🌳🌳")   
    print("\n")
    directions = ["north","east","west"]
    print("You find what looks to be an overgrown trail that leads north and west.")
    userInput = ""
    while userInput not in directions:
      print("What will you do?")
      userInput = input()
      print("\n")
      if userInput == "west":
          antScene()
      elif userInput == "north":
          waterScene()
      elif userInput == "east":
          monkeyScene()
      else: 
        print("Please enter a valid option.")
        
def antScene():
    global healthy
    print("\n")
    print("🌳🌳   🌳🌳")   
    print("🌳🐜🪵🐜🌳")
    print("🌳🐜🪵🐜🌳")
    print("🌳  👮      ")
    print("🌳🌳🌳🌳🌳")   
    print("\n")
    directions = ["north","east"]
    print("You follow the trail to a clearing. You spot a Bullet Ant nest in a ditch.")
    print("A fallen tree lies across the ditch. It’s the only way to get across.")
    userInput = ""
    while userInput not in directions:
      print("What will you do?")
      userInput = input()
      print("\n")
      if userInput == "north" and healthy==True:
          print("You walk carefully on the fallen tree and make it across unscathed. You continue north.")
          idolScene()
      elif userInput == "north" and healthy==False:
          print("You try to walk across,  but your leg gives out and you fall in the ditch. The Bullet Ants eat you alive.")
          quit()
      elif userInput == "east":
          trailScene()
      else: 
        print("Please enter a valid option.")
        
def idolScene():
    global idol
    print("\n")
    print("🪨🪨🪨🪨🪨")
    if idol==False:
        print("🪨  👮 🗿🪨")
    else:
        print("🪨  👮   🪨")
    print("🪨   🪨🪨🪨")
    print("🌳        🌳")
    print("🌳🌳   🌳🌳")   
    print("\n")
    directions = ["south"]
    print("You see an ancient shrine made of stone.")
    if idol==False:
        print("Inside, you find the Idol of the River God on an altar.")
    userInput = ""
    while userInput not in directions:
      print("What will you do?")
      userInput = input()
      print("\n")
      if userInput == "south":
          antScene()
      elif idol==False and userInput == "take idol" or userInput == "take Idol of the River God":
          idol=True
          print("As you take the idol, you feel as if it holds an archaic and long-dormant power.")
      else: 
        print("Please enter a valid option.")
        
def waterScene():
    global monkey
    global piranhas
    print("\n")
    print("🌳🌳🌳🌳🌳")   
    print("🌳           ")
    print("🟦🟦🟦🟦🟦")
    print("🌳   👮   🌳")
    print("🌳🌳   🌳🌳")   
    print("\n")
    directions = ["south","east"]
    print("The trail suddenly stops at the bank of a slow-moving tributary. It's too wide to jump across but looks swimmable.")
    userInput = ""
    while userInput not in directions:
      print("What will you do?")
      userInput = input()
      print("\n")
      if userInput == "south":
          trailScene()
      elif userInput == "east" and piranhas==True:
          print("You try to swim across, but a school of piranhas smell the blood from your leg. You don't make it out of the water.")
          quit()
      elif userInput == "east" and piranhas==False:
          print("With the piranhas distracted, you swim across the water safely. You head east.")
          boatScene()
      elif userInput == "use monkey" and monkey==True and piranhas==True:
          piranhas=False
          monkey==False
          print("You toss the monkey into the water. A school of piranhas swim over and start eating it. They look busy.")
      else: 
        print("Please enter a valid option.")

def boatScene():
    global idol
    global gold
    global name
    print("\n")
    print("🌳🌳🌳🟦🟦")   
    print("        🟦🟦")
    print("🌳 👮  🛶🟦")
    print("🌳     🟦🟦")
    print("🌳🌳🌳🟦🟦")   
    print("\n")
    print("You follow the trail to a small wooden dock on the Amazon River. There’s an old, sturdy-looking canoe tied to it.")
    print("What will you do? Type a number:")
    print("1) Take the canoe")
    print("2) Go back")   
    userInput = input()
    print("\n")
    if userInput == "1":
        print("You get into the canoe and follow the stream of the river east.") 
        if idol==True:
            print("You eventually reach the village of Salgada. There's not much around except for a church.")
            print("You decide to stop inside to take a rest. A priest greets you and offers you water. You accept.")
            print("You show him the Idol of the River God. He has an astonished look on his face.")
            print("He goes into another room and brings you a chunk of gold the size of your fist.")
            print("He offers it to you in exchange for the Idol. Do you accept?")
            print("1) Yes")
            print("2) No")
            idolInput = input()
            print("\n")
            if idolInput == "1":
                idol=False
                gold=True
                print("You hand the Idol over in exchange for the gold. The priest looks relieved.")
                print("You get back into your canoe and continue downstream.")
            elif idolInput == "2":
                print("You refuse his offer. The mood is tense, so you leave.")
                print("You get back into your canoe and continue downstream.")
            else:
                print("Please enter a valid option.")
        
        print("Finally, you reach the city of Manaus. You make your way to the airport and get on the first flight to Miami.")
        if idol==True:
            print("Three months later, you mysteriously die. Your family finds the Idol of the River God in your belongings.")
            quit()
        elif gold==True:
            print("You make it home safely with your gold. You sell it and make a tidy sum of $50K. Nicely done, "+name+"!")
            quit()
        else:
            print("You make it home safely! Well done, "+name+"!")
            quit()
    elif userInput == "2":
        waterScene()
    else: 
        print("Please enter a valid option.")

if __name__ == "__main__":
    print("\nWelcome to the Rainforest Adventure!\n")
    while True:
        print("Please select an option by typing a number:")
        print("1) Play")
        print("2) Instructions")
        print("3) Exit Game")
        homeOption=input("")
        if homeOption=="1":
            print("----------------------------------------------------------")
            print("\nLet's start with your name: ")
            name = input()
            print("Good luck, " +name+ ".\n")
            print("----------------------------------------------------------")
            print("\nYou and your copilot are flying from Rio de Janeiro to Miami.")
            print("You take in the views as you pass over the Amazon Rainforest.")
            print("Suddenly, the needle on your fuel guage starts to fall.")
            print("Your only option is to try to land on the flat part of a mountain.")
            introScene()
        elif homeOption=="2":
            print("\n----------------------------------------------------------")
            print("\nInstructions:\n")
            print("To move your character, type \"north\", \"south\", \"east\", or \"west\"")
            print("To pick up items, type \"take <item>\"")
            print("To use items, type \"use <item>\"\n")
            print("follow the openings in the minimap and all commands are case sensitive")
            print("----------------------------------------------------------")
        elif homeOption=="3":
            quit()
        else: 
          print("Please enter a valid option.")
        
        
   







