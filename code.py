import random
import time #imports random and time, this is useful so I can add pauses in text and choose random questions

cargo = ["thread", "paper", "ink"]

#these are easy ways to add colour and different styles to the text displayed so when I add something like f("{BLUE}hello")" it will change the colour to blue in a printout
Underline = '\033[4m' 
Bold = '\033[1m'
Italic = '\x1B[3m'
Reset = '\033[0m' #resets text to normal
Red = '\033[31m'
Blue = '\033[34m'
Green = '\033[32m'
Yellow = '\033[33m'
RED_BG = '\033[41m' #background colour is red, same logic applies for the other BGs
BLUE_BG = '\033[44m'
RED_BG = '\033[41m'

def tw(text): 
    for character in text: print(character,end='',flush=True); time.sleep(0.017)
    print()

def dialogue():
    dialoguee = { #dialogue options
            'You continue driving down the road.': 1,
            'A bright blue car passes you going the opposite direction.': 2,
            'You merge onto the highway, passing a sign, "Next rest stop is in 5 kilometres".': 3,
            'You adjust your mirror and notice storm clouds gathering ahead.': 4,
            'You pass a recycling plant, mountains of cardboard and paper visible through the fence.': 5,
            'You see the warehouse exit sign: 87 miles to go.': 6,
            'The rain intensifies. The windshield wipers struggle to keep up.': 7,
            'You pass a billboard: "Save Paper, Save Trees - Go Digital Today!"': 8,
            'An hour passes. The rain eases. You pull into a truck stop for fuel.': 9,
            'A bookstore approaches you. A "Going Out of Business" sign hangs in the window.': 10,
            'You pass a landfill. Seagulls circle overhead.': 11,
            'You think about the 540 trees in yesterdays load. The 112 tons of CO2. The 50 gallons of diesel you burned.': 12,
            'The mile marker climbs up: 220. 230. 240.': 13,
            'The sun climbs higher. The road continues.': 14,
        }
    random_pair = random.choice(list(dialoguee.items())) #chooses random dialogue option from list
    key, value = random_pair #the key is the writing part and the value is the number, this is so that it doesn't print entire dictionary line
    tw(f"{Italic}{key}{Reset}")
    time.sleep(1)

    randomChoice = random.randint(1,5) #after random dialogue it chooses random dialogue with pauses in text
    if randomChoice == 1:
        tw(f"{Italic}The CB radio crackles to life:"); time.sleep(1) #another way to add time.sleep
        tw(f"{Green}Dispatcher: Unit 47, whats your 20?"); time.sleep(1.5)
        tw(f"{Blue}You: Just passed mile marker 182 on I-90. Should hit the warehouse by 1400 hours."); time.sleep(1.8)
        tw(f"{Green}Dispatcher: Copy.{Reset}");time.sleep(0.7)
    elif randomChoice == 2:
        tw(f"{Italic}You glance at your fuel gauge—half a tank."); time.sleep(1)
        tw("You calculate the emissions in your head:"); time.sleep(1.8)
        tw(f"'Roughly 6 kilometers per gallon, 300 kilometers to go.'{Reset}"); time.sleep(1.4)
    elif randomChoice == 3:
        tw(f"{Italic}The CB radio crackles again.");time.sleep(1.8)
        tw(f"{Green}Dispatcher: Unit 47, be advised—theres a weigh station ahead at mile 205."); time.sleep(2)
        tw(f"{Blue}You: Copy. I'm legal, but it'll cost me twenty minutes."); time.sleep(1.7)
        tw(f"{Green}Dispatcher: Copy.{Reset}"); time.sleep(1.2)
    elif randomChoice == 4:
        tw(f"{Italic}The CB radio turns on."); time.sleep(1.5)
        tw(f"{Yellow}Some random trucker: Unit 47, you there?."); time.sleep(1.8)
        tw(f"{Blue}You: Yep."); time.sleep(1)
        tw(f"{Yellow}Some random trucker: Ever think about switching loads? Maybe something lighter on the conscience?."); time.sleep(1.9)
        tw(f"{Blue}You: Every day, buddy. But someone's gotta do it. People still love their books."); time.sleep(1.7)
        tw(f"{Yellow}Some random trucker: Fair enough. Stay safe out there."); time.sleep(1)
        tw(f"{Blue}You: You too.{Reset}"); time.sleep(1.3)
    elif randomChoice == 5:
        tw(f"{Italic}The CB radio crackles."); time.sleep(1.5)
        tw(f"{Yellow}Some other random trucker: Unit 47, how many loads you have today?"); time.sleep(1.8)
        tw(f"{Blue}You: Unit 11, second one. You?"); time.sleep(1)
        tw(f"{Yellow}Some other random trucker: Third. All paper products."); time.sleep(1.9)
        tw(f"{Blue}You: Ever wonder where it all goes?"); time.sleep(1.7)
        tw(f"{Yellow}Some other random trucker: I think landfills, mostly."); time.sleep(1)
        tw(f"{Blue}You: Yeah probably."); time.sleep(1.3)
        tw(f"{Yellow}Some other random trucker: But we get paid either way."); time.sleep(1)
        tw(f"{Reset}{Italic}*Static.{Reset}"); time.sleep(1)

    scary = { #before displaying question, this happens to transition between dialogue and questions to show a book roober
        'You glance in the rearview mirror, a book roober appears!': 1,
        'A loud bang is heard in by your truck, you realize there is a book roober behind you!': 2,
        'As you look back to change lanes, you realize a book roober is beside your truck!': 3,
        'GEE WILIKERS !!!! There is a book roober behind you!': 4,
        'You adjust your mirror, but something is wrong...\nThere is a book roober behind your truck!': 5,
    }
    random_pair = random.choice(list(scary.items())) #chooses random dialogue option from list
    key, value = random_pair
    tw(f"\n{Italic}{Bold}{Red}{key}{Reset}"); time.sleep(2)

def questionss(): 

    questions = [ #dictionary for multiple chocice questions
        {
            "question": "Where are books made?",
            "options": ["Printer", "Library", "Book factory", "A book publisher"],
            "correct": "A"
        },
        {
            "question": "What is one material used to make books?",
            "options": ["Metal", "Plastic", "Glue", "Printer"],
            "correct": "C"
        },
        {
            "question": "What is the first step to make a book?",
            "options": ["Gather materials", "Ship the book", "Timmy", "Order a book"],
            "correct": "A"
        },
        {
            "question": "What is the primary raw material used in making paper for books?",
            "options": ["Cotton", "Wood pulp", "Recycled plastic", "Bamboo"],
            "correct": "B"
        },
        {
            "question": "Which process is commonly used to bind the pages of a book together?",
            "options": ["Sewing", "Gluing", "Stapling", "Wiring"],
            "correct": "B"
        },
        {
            "question": "What environmental concern is associated with traditional paper production?",
            "options": ["Air pollution", "Water consumption", "Deforestation", "All of the above"],
            "correct": "D"
        },
        {
            "question": "Which of the following is a sustainable alternative for book production?",
            "options": ["Using recycled paper", "Using plastic covers", "Using synthetic ink", "Using non-renewable resources"],
            "correct": "A"
        },
        {
            "question": "What is the role of ink in book production?",
            "options": ["To bind pages", "To print text and images", "To protect the cover", "To add weight to the book"],
            "correct": "B"
        },
        {
            "question": "Which stage of a paper book's life cycle typically uses the most water?",
            "options": ["Tree harvesting", "Pulp and paper production", "Printing and binding", "Recycling"],
            "correct": "B"
        },
            {"question": "What is one way to reduce the environmental impact of book production?",
            "options": ["Using more plastic", "Increasing paper thickness", "Choosing eco-friendly materials", "Printing more copies"],
            "correct": "C"
        },
    ]
    # chooses random question
    question = random.choice(questions)
    tw(f"{BLUE_BG}\n{question['question']}{Reset}")
    
    # displays every multple choice option from the dictionary that I used above
    print("A.", question["options"][0]) #options for corresponding question/option from dicitionary, e.g. question calls question from question dictionary
    time.sleep(0.06)
    print("B.", question["options"][1])
    time.sleep(0.06)
    print("C.", question["options"][2])
    time.sleep(0.06)
    print("D.", question["options"][3])
    time.sleep(0.06)
    tw(f"\n{Underline}Please enter your answer (A/B/C/D): {Reset}") #typewriter prompt (not actual input but just for visuals)
    user_answer = input().upper() #actual input for user
    
    # check answer
    if user_answer == question["correct"]:
        tw(f"{Green}Correct!! {Reset}")
    else:
        tw(f"{Red}Incorrect! The correct answer was {question['correct']}{Reset}."); time.sleep(0.5) #I want to show that you can put time.sleep on the same line as somethign else with a semicolon
        removed = cargo.pop(random.randint(0,len(cargo)-1))
        tw(f"{RED_BG}A book roober stole a {removed} box!{Reset}")
              
        if (len(cargo)) == 0: #checks to see if user lost all of their cargo
            tw(f"{Red}You have lost all your cargo! Game Over!{Reset}")
            exit()
              
def double_multi():
    for i in range(4): #repeats double or nothing challenge is blue and red and bolded 4 times
        print(f"\n{Bold}{BLUE_BG}DOUBLE OR NOTHING CHALLENGE!{Reset}"); time.sleep(0.6)
        print(f"\n{Bold}{RED_BG}DOUBLE OR NOTHING CHALLENGE!{Reset}",);time.sleep(0.6)

    tw("You loose -2000 points if you get it wrong")
    tw("But get +2000 points if you get it right :D")
    
    double_multii = [ #double or nothing question dictionary
        {
            "question": "Which stage of the book lifecycle contributes MOST to deforestation?",
            "options": ["Writing", "Production", "Shipping", "Disposal"],
            "correct": "B"
        },
        {
            "question": "What is the CORRECT order of the book lifecycle?",
            "options": ["Raw Material Extraction, Paper Production, Printing & Manufacturing, Marketing & Sales, Distribution & Transportation, Use Phase, End of Life", "Raw Material Extraction, Ink Production, Paper Production, Printing & Manufacturing, Packaging, Distribution & Transportation, Use Phase, End of Life", "Raw Material Extraction, Paper Production, Printing & Manufacturing, Packaging, Distribution & Transportation, Use Phase, End of Life", "Raw Material Extraction, Paper Production, Quality Control & Editing, Printing & Manufacturing, Packaging, Distribution & Transportation, Use Phase, End of Life"],
            "correct": "C"
        },
        {
            "question": "Which chemical process is commonly used to break down wood chips into pulp for papermaking?",
            "options": ["Oxidation", "Kraft process", "Fermentation", "Electrolysis"],
            "correct": "B"
        },
        {
            "question": "What percentage of the original wood mass is typically lost during the chemical pulping process due to lignin removal?",
            "options": ["10-20%", "30-40%", "50-60%", "60-70%"],
            "correct": "C"
        },
        {
            "question": "Which of the following is NOT a common method for recycling paper?",
            "options": ["De-inking", "Hydraulic pressing", "Thermal pulping", "Magnetic separation"],
            "correct": "D"
        },
        {
            "question": "What is the primary greenhouse gas emitted during paper decomposition in landfills?",
            "options": ["Carbon dioxide", "Methane", "Nitrous oxide", "Ozone"],
            "correct": "B"
        },
    ]
    question = random.choice(double_multii) #random question from dictionary
    tw(f"{BLUE_BG}\n{question['question']}{Reset}")
    
    print("A.", question["options"][0]) #display options for bonus questions
    time.sleep(0.067)
    print("B.", question["options"][1])
    time.sleep(0.067)
    print("C.", question["options"][2])
    time.sleep(0.067)
    print("D.", question["options"][3])
    time.sleep(0.067)
    
    tw(f"\n{Underline}Please enter your answer (A/B/C/D): {Reset}") #typewriter prompt (not actual input but just for visuals)
    choice = input("").upper() #actual input for user, upper is used so that when user types answer it goes uppercase so it matches with correct from dictionary
    
    if choice == question["correct"]:
        tw(f"{Green}AMAZING! You won 2000 points!{Reset}")
        return 2000 #+2000 points
    else:
        tw(f"{Red}Wrong! The correct answer was {question['correct']}.{Reset}")
        tw("You lost 2000 points!")
        return -2000 #-2000 points

def multi():
    global score #i'm adding global to this so that in the menu() function there won't be an error when called on in the menu() function
    score = 0
    for i in range (5): #main game loop
        #normal question
        dialogue()
        questionss()
        tw(f"\n{Bold}Current cargo: {cargo}")
        tw(f"Current score: {score}{Reset}")

        # 25% chance of double or nothing special question
        if random.random() < 0.25:
            dialogue()
            tw("\nA special challenge has appeared!"); time.sleep(0.5)
            score += double_multi() #score is score plus or minus from double or nothing
            tw(f"Cargo: {cargo}")
            tw(f"Score: {score}")

            if score < 0:
                tw(f"{Red}You have negative points!")
                tw(f"Your final score was {score}.")
                tw(f"Your final cargo was: {cargo}.")
                exit()

            elif len(cargo) == 0:
                tw(f"{Red}You have lost all your cargo! Game Over!{Reset}")
                exit()
            
            else:
                continue #if none of the stuff above happened, the program just continues

        tw(f"{Underline}\nPlay another question? (y/n): {Reset}")
        play_again = input("").lower()
        if play_again == 'y':
            continue #if yes program continues
        elif play_again == 'n':
            tw(f"\n{Blue}Game Over! Final cargo: {cargo}.\nFinal score: {score}. {Reset}"); time.sleep(0.8)
            tw(f"If you have the time next time you should try to finish the game, it's only 10 questions!")
            exit() #ends program
        else:
            tw(f"{Red}Invalid input. Try again{Reset}")
    end() #after 5 repeats, it goes to end function

def shortquestions():
    questionsss = [ #dictionary for questions
       {
            "question": "Where are books made?",
            "answers": ["Printer", "Book factory", "Factory", "printing process", "book printer"],
        },
        {
            "question": "What is one material used to make books?",
            "answers": ["Glue", "Threading", "Thread", "Paper", "Ink"],
        },
        {
            "question": "What is the first PHYSICAL step to make a paper book?",
            "answers": ["Gather materials", "Gathering materials", "Material gathering", "Getting paper", "paper", "getting the materials", "getting mateerials"],
        },
        {
            "question": "What is the primary raw material used in making paper for books?",
            "answers": ["Wood pulp" "pulp", "paper", "paper production"],
        },
        {
            "question": "Which process is commonly used to bind the pages of a book together?",
            "answers": ["Gluing", "Glue"],
        },
        {
            "question": "What environmental concern is associated with traditional paper production?",
            "answers": ["Air pollution", "Water consumption", "Deforestation", "pollution", "CO2 emmissions", "emmissions", "Co2", "Co2 pollution"],
        },
        {
            "question": "What is a sustainable alternative for book production?",
            "answers": ["Using recycled paper", "Recycling", "recycle", "Choosing eco-friendly materials", "Recycle", "recycling", "share books", "donate", "sharing books"],
        },
        {
            "question": "What is the role of ink in book production?",
            "answers": ["To print text and images", "Printing", "To print", "print", "text"],
        },
        {
            "question": "Which stage of a paper book's life cycle typically uses the most water?",
            "answers": ["Pulp and paper production", "make paper", "printing paper", "paper production", "make paper"],
        },
        {
            "question": "What is one way to reduce the environmental impact of book production?",
            "answers": ["Choosing eco-friendly materials", "Recycle", "recycling", "share books", "donate", "to donate", "choosing sustainable materials"],
        },
    ]
    question = random.choice(questionsss)# chooses random question from the dictonary using rnadom functio 
    tw(f"{Underline}\n" + question["question"] + f"{Reset}") #shows question from dictionary, tw is to call typewriter effect for this line
    user_answer = input("").lower().strip() #.strip() makes it so that even if there is a space in the user's answer the program removes it

    if user_answer in [ans.lower() for ans in question['answers']]: #I used StackOverflow for this part to check if one of the answers is right from the valid answers dictionary 
        tw(f"{Green}Correct!! {Reset}")
    else:
        print(f"{Red}Incorrect! The correct answers were either one of these: {question['answers']}{Reset}.")
        removed = cargo.pop(random.randint(0,len(cargo)-1))
        print(f"{RED_BG}Oh no! A roober stole a {removed} box from your truck!{Reset}")
            
        if (len(cargo)) == 0: #checks to see if user lost all of their cargo
            tw(f"{Red}You have lost all your cargo! Game Over!{Reset}"); time.sleep(0.8)
            tw(f"If you have the time next time you should try to finish the game, it's only 10 questions!")
            exit()

def double_short():
    for i in range(4):
        print(f"\n{Bold}{BLUE_BG}DOUBLE OR NOTHING CHALLENGE!{Reset}"); time.sleep(0.6)
        print(f"\n{Bold}{RED_BG}DOUBLE OR NOTHING CHALLENGE!{Reset}"); time.sleep(0.6)
    tw("Youi loose -2000 points if you get it wrong")
    tw("But get +2000 points if you get it right :)")

    double_shortt = [ #double or nothing question dictionary for short answers
        {
            "question": "Which stage of the book lifecycle contributes MOST to deforestation?",
            "answers": ["Production", "producing", "printing", "producing books", "printing books", "book printing", "book producing"],
        },
        {
            "question": "Which chemical process is commonly used to break down wood chips into pulp for papermaking?",
            "answers": ["Kraft process", "Krafting", "crafting", "craft process"],
        },
        {
            "question": "What percentage of the original wood mass is typically lost during the chemical pulping process due to lignin removal? (Enter your answer as a percentage (%) with the percent at the end)",
            "answers": ["50-60%", "45%", "60%", "45-60%", "50%", "55%", "65%"],
        },
        {
            "question": "What should you do after finishing reading a book?",
            "answers": ["Recycle it", "recycling", "Donate it", "donating", "donation", "give it to a friend", "give it away", "donate it to a library", "give it to a drive", "donate"]
        },
        {
            "question": "What gas is released when trees are cut down for paper?",
            "answers": ["Carbon dioxide", "CO2", "greenhouse gases", "GHG", "GHGs", "green house gases"],
        },
        {
            "question": "What type of pollution results from transporting books?",
            "answers": ["Greenhouse gases", "Green house gases", "GHGs", "CO2", "Carbon dioxide", "gas", "air", "air pollution"],
        },
        {
            "question": "What process gives old books life?",
            "answers": ["Recycling", "recycle", "book bank", "donating", "donations", "donating to a book bank", "donation"],
        },
        {
            "question": "Where do unwanted books often end?",
            "answers": ["Landfills", "dump", "garbage dump", "trash", "garbage", "bin", "garbage bin", "trash bin"],
        },
        ]
    question = random.choice(double_shortt)
    tw(f"{Underline}\n" + question["question"] + f"{Reset}") #shows question from dictionary, tw is to call typewriter effect for this line
    user_answer = input("").lower().strip() #.strip() makes it so that even if there is a space in the user's answer the program removes it

    if user_answer in [ans.lower() for ans in question['answers']]: #I used StackOverflow for this part to check if one of the answers is right from the valid answers dictionary 
        tw(f"{Green}AMAZING! You won 2000 points!{Reset}")
        return 2000 #+2000 points
    else:
        tw(f"{Red}Wrong! The correct answer was one of these options: {question['answers']}.{Reset}")
        tw("You lost 2000 points!")
        return -2000 #-2000 points

def short():
    global score
    score = 0
    for i in range(5): #main game loop with 5 questions
        time.sleep(0.8); dialogue(); time.sleep(0.5)
        shortquestions()
        tw(f"{Bold}Current cargo: {cargo}")
        tw(f"Current score: {score}{Reset}")
        
        if random.random() < 0.25:  # 25% chance of double or nothing
            dialogue()
            tw("\nA special challenge has appeared!"); time.sleep(0.5)
            score += double_short() #score is score plus or minus from double or nothing
            tw(f"Cargo: {cargo}")
            tw(f"Score: {score}")

            if score < 0:
                tw(f"{Red}You have negative points!")
                tw(f"Your final score was {score}.")
                tw(f"Your final cargo was: {cargo}.")
                exit()

            elif len(cargo) == 0:
                tw(f"{Red}You have lost all your cargo! Game Over!{Reset}")
                exit()
            
            else:
                continue #if none of the stuff above happened, the program just continues
        
        tw(f"{Underline}\nPlay another question? (y/n): {Reset}")
        play_again = input("").lower()
        if play_again == 'y':
            continue #if yes program continues
        elif play_again == 'n':
            tw(f"\n{Blue}Game Over! Final cargo: {cargo}.\nFinal score: {score}. {Reset}"); time.sleep(0.8)
            tw(f"If you have the time next time you should try to finish the game, it's only 10 questions!")
            exit() #ends program
        else:
            tw(f"{Red}Invalid input. Try again{Reset}")
    end()
    
def end(): 
    global score
    time.sleep(0.5)
    tw(f"{Bold}{Blue}Congratulations! You have successfully delivered your cargo of books!{Reset}"); time.sleep(0.5)
    tw("You now know how about the full life cycle of a book and the enviornmental impact of it."); time.sleep(0.5)
    tw("If you tried multiple choice mode, try doing short answer mode for a harder difficulty!"); time.sleep(0.5)
    tw(f"{Bold}Your final cargo: {cargo}\n")
    tw(f"Your final score: {score}{Reset}\n")

    tw("Would you like to play again? (y/n): ")
    end1 = input()

    if end1 == 'y':
        menu()
    else:
        tw(f"{BLUE_BG}Thank you for playing BookTruck! Goodbye!{Reset}")
        exit()  
    
def menu():
    time.sleep(1)
    tw(f"{Bold}Welcome to BookTruck!!{Reset}"); time.sleep(0.4)
    print('''
   ___            __  ______             __  
  / _ )___  ___  / /_/_  __/_____ ______/ /__
 / _  / _ \/ _ \/  '_// / / __/ // / __/  '_/
/____/\___/\___/_/\_\/_/ /_/  \_,_/\__/_/\_\ 
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMW0dolllllllllllllllllllllllllllllllllllllllllloxKWMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMNo. .''''''''''''''''''''''''''''''''''''''''''. 'kMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMWNNNNNk. ;OKKKKKKKKKKXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNd. oWMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMM0:'''''    '''''''''''lXMMMMMMMMMMMMMMMMMMMMMMMMMMMMWo .xMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMXxoooooooooooooooooooookNMMMMMMMMMMMMMMMMMMMMMMMMMMMMN: .:dddddddddkKWMMMMMMMMMMMMMMMM
MMMMMMMMMXOkkkkkkkkkkkkkkkkkkkkkk0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMK,  ............;kNMMMMMMMMMMMMMM
MMMMMMMMWx'......................cKMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMO. :KXXKKKKKXKk:..;OWMMMMMMMMMMMM
MMMMMMMMMNK0000000000000000000000XWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMx. dWKl,,,,,;o0NO;..c0WMMMMMMMMMM
MMMMMMMMMMMNxccc::::::::::::::::cc:::ccxNMMMMMMMMMMMMMMMMMMMMMMMMMWl .kMx.       .lKXx, .lKMMMMMMMMM
MMMMMMMMMMMNd:;;;;;;;;;;;;;;;;;;;;;;;;:dXMMMMMMMMMMMMMMMMMMMMMMMMMX: '0Wo          .dXXd. 'xNMMMMMMM
MMMMMMNXKKKKKKKKKKKKKKKKKKKKKNWWWWWWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMM0' ;XNo............cKWKc .xWMMMMMM
MMMMMXc......................cXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMk. lNMNXKKKKKKKKKKKXNMMO. :NMMMMMM
MMMMMW0xxxxxxxxxxxx:  ;dxxxxx0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWd..dWMMMMMMMMMMMMMMMMMMk. lWMMMMMM
MMMMMMMMMMMMMMMMMMWo .xMMMMMMMMMWNNNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMNl .OMMMMMMMWNNWWMMMMMMWd..dMMMMMMM
MMMMMMMMMMMMMMMMMMNc .OMMMMMWXxc;'.';oONMMMMMMMMMMMMMMMMMMMMMMMMMX; ,KMMMW0o:,'',:dKWMMMNl .OMMMMMMM
MMMMMMMMMMMMMMMMMMK; ,KMMMMXd. .:lol,..cKMMMMMMMMMMMMMMMMMMMMMMMM0' :XMW0:..,col:. .xWMMX; ,KMMMMMMM
MMMMMMMMMMMMMMMMMM0' ,k000Oc .lKWMMMNd. :O00000000000000000000000o. :O0x' 'kNMMMMK; .d00o. cNMMMMMMM
MMMMMMMMMMMMMMMMMMNd.......  cNMMMMMMO.  .........................  ...  .xMMMMMMWo  .....:0WMMMMMMM
MMMMMMMMMMMMMMMMMMMWXOkkkko. ,KMMMMW0: .lkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk: .oNMMMMNx. ,dkkOKWMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMWx. .cddo:. 'kWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXc..;oddl,..cKMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMWKo;....,cxXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNOc,...';o0WMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNXXXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXXXNWMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
          ''')
    time.sleep(0.8)
    while True: #infinite loop so that if the user gives incorrect option it loops back to the question
        tw(f"\n{Bold}Menu:{Reset}\n1. Begin Game\n2. Tutorial\n3. Exit")
        tw(f"{Underline}Please enter your choice (1/2/3):{Reset}")
        choice = input("")
        if choice == '1':
            while True: #same logic as the first while True, if the user gives invalid choice it loops back to this question
                tw(f"\nWhich difficulty would you like to play on?\n1. Multiple Choice (easy) \n2. Short Answer (hard)\n{Underline}Enter here (1/2):{Reset}")
                choice2 = input("")
                if choice2 == '1':
                    tw("You chose mulitple choice difficulty!")
                    time.sleep(2)
                    print("\n" * 50); time.sleep(1.3) #adds 50 lines of blank stuff
                    tw(f"{Italic}\nYou enter your truck, ready to start your long day ahead."); time.sleep(1.5)
                    tw(f"You merge onto the road."); time.sleep(2.3)
                    tw(f"Time passes by.{Reset}"); time.sleep(2.3)
                    multi() #starts multiple function
                
                elif choice2 == '2':
                    tw("You chose short answer difficulty!"); time.sleep(2)
                    print("\n" * 38); time.sleep(1.3)
                    tw(f"{Italic}\nYou enter your truck, ready to start your long day ahead.");time.sleep(1.5)
                    tw(f"You merge onto the road."); time.sleep(2.3)
                    tw(f"Time passes by.{Reset}"); time.sleep(2.3)
                    short()

                else:
                    tw(f"{Red}Invalid choice. Please try again.{Reset}")
            
        elif choice == '2':
            tw(f"""\n📚 {Bold}BookTruck - How to Play{Reset}

{Bold}Your Mission:{Reset}
You're a truck driver transporting precious book production materials to their destination. Your cargo includes threading, ink, paper, and glue—everything needed to make books! But be careful. There are book roobers trying to steal your precious cargo.

{Bold}The Goal:{Reset}
Answer 10 questions about the book life cycle and environmental impacts correctly to reach your destination and win the game.

{Bold}How to Play:{Reset}
- You'll face 10 questions during your journey (multiple choice or short answer based on your chosen difficulty)
- Each question tests your knowledge about how books are made and their impact on the environment
- Answer correctly to keep moving forward
- Wrong answers may cost you points or cargo

{Bold}Scoring:{Reset}
- You start with a certain number of points
- Correct answers earn you points
- Incorrect answers lose you points or damage your cargo

{Bold}Losing Conditions - You lose if:{Reset}
1. Your score drops to zero or below (negative points)
2. You lose all your cargo materials (threading, ink, paper, and glue)

{Bold}Winning Condition:{Reset}
Successfully answer all 10 questions while keeping your score positive and at least some cargo intact!

{Bold}Tips for Success:{Reset}
- Think carefully about each answer
- Remember: books go through many stages from tree to reader
- Consider environmental factors like recycling, transportation, and resource use

Good luck, driver! 🚚📖
""")
            time.sleep(1)
            menu()
        elif choice == '3':
            tw("Thank you for playing BookTruck! Goodbye!")
            exit()

        #secret option to immediently acess multiple choice or short answer questions if the user wants to skip to either question
        elif choice == '4': 
            multi()
        elif choice == '5':
            short()
        else:
            tw(f"{Red}Invalid choice. Please try again.{Reset}")
menu() #runs menu function to start program
