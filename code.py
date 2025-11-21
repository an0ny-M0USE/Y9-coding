import random, time #imports random and time

cargo = ["ink", "thread", "paper", "paper", "glue"]

#these are easy ways to add colour and different styles to the text displayed so when I add something like {BLUE} it will change the colour to blue in a printout
UNDERLINE = '\033[4m' 
BOLD = '\033[1m'

RESET = '\033[0m' #resets text to normal

RED = '\033[31m'
BLUE = '\033[34m'
GREEN = '\033[32m'
BLACK = '\033[30m'
RED_BG = '\033[41m'
BLUE_BG = '\033[44m'
RED_BG = '\033[41m'

def tw(text): #typewriter effect defined
    for character in text:
        print(character, end='', flush=True)
        time.sleep(0.018) #speed of typewriting
    print()

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
        {
            "question": "What is one way to reduce the environmental impact of book production?",
            "options": ["Using more plastic", "Increasing paper thickness", "Choosing eco-friendly materials", "Printing more copies"],
            "correct": "C"
        },
    
    ]
    
    # chooses random question
    question = random.choice(questions)
    tw(f"{BLUE_BG}\n{question['question']}{RESET}")
    
    # displays every multple choice option from the dictionary that I used above
    print("A.", question["options"][0]) #options for corresponding question/option from dicitionary, e.g. question calls question from question dictionary
    time.sleep(0.06)
    print("B.", question["options"][1])
    time.sleep(0.06)
    print("C.", question["options"][2])
    time.sleep(0.06)
    print("D.", question["options"][3])
    time.sleep(0.06)

    
    # answer prompt
    tw(f"\n{UNDERLINE}Please enter your answer (A/B/C/D): {RESET}") #typewriter prompt (not actual input but just for visuals)
    user_answer = input().upper() #actual input for user
    
    # check answer
    if user_answer == question["correct"]:
        tw(f"{GREEN}Correct!! {RESET}")
    else:
        print(f"{RED}Incorrect! The correct answer was {question['correct']}{RESET}.")
        removed = cargo.pop(random.randint(0,len(cargo)-1))
        print(f"{RED_BG}You lost a {removed} box!{RESET}")
              
        if (len(cargo)) == 0: #checks to see if user lost all of their cargo
            tw(f"{RED}You have lost all your cargo! Game Over!{RESET}")
            exit()
              
def double_multi():
    for i in range(4):
        print(f"\n{BOLD}{BLUE_BG}DOUBLE OR NOTHING CHALLENGE!{RESET}") 
        time.sleep(0.6)
        print(f"\n{BOLD}{RED_BG}DOUBLE OR NOTHING CHALLENGE!{RESET}",) 
        time.sleep(0.6)

    tw("Youi loose -2000 points if you get it wrong")
    tw("But get +2000 points if you get it right :)")
    
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
    tw(f"{BLUE_BG}\n{question['question']}{RESET}")
    
    print("A.", question["options"][0]) #display options for bonus questions
    time.sleep(0.067)
    print("B.", question["options"][1])
    time.sleep(0.067)
    print("C.", question["options"][2])
    time.sleep(0.067)
    print("D.", question["options"][3])
    time.sleep(0.067)
    
    tw(f"\n{UNDERLINE}Please enter your answer (A/B/C/D): {RESET}") #typewriter prompt (not actual input but just for visuals)
    choice = input("").upper() #actual input for user, upper is used so that when user types answer it goes uppercase so it matches with correct from dictionary
    
    if choice == question["correct"]:
        tw(f"{GREEN}AMAZING! You won 2000 points!{RESET}")
        return 2000 #+2000 points
    else:
        tw(f"{RED}Wrong! The correct answer was {question['correct']}.{RESET}")
        tw("You lost 2000 points!")
        return -2000 #-2000 points

def multi():
    global score #i'm adding global to this so that in the menu() function there won't be an error when called on in the menu() function
    score = 0
    for i in range (1): #main game loop
        #normal question
        questionss()
        tw(f"\n{BOLD}Current cargo: {cargo}")
        tw(f"Current score {score}{RESET}")

        print(*cargo, sep=", ")      

        # 15% chance of double or nothing special question
        if random.random() < 0.15:
            tw("\nA special challenge has appeared!")
            time.sleep(0.5)
            score += double_multi() #score is score plus or minus from double or nothing
            tw(f"Cargo: {cargo}")
            tw(f"Score: {score}")

            if score < 0:
                tw(f"{RED}You have negative points!")
                tw(f"Your final score was {score}.")
                tw(f"(Your final cargo was: {cargo}.)")
                exit()

            elif len(cargo) == 0:
                tw(f"{RED}You have lost all your cargo! Game Over!{RESET}")
                exit()
            
            else:
                continue

        tw(f"{UNDERLINE}\nPlay another question? (y/n): {RESET}")
        play_again = input("").lower()
        if play_again == 'y':
            continue #if yes program continues
        elif play_again == 'n':
            tw(f"\n{BLUE}Game Over! Final cargo: {cargo}.\nFinal score: {score}. {RESET}")
            exit() #ends program
        else:
            tw(f"{RED}Invalid input. Try again{RESET}")
    end() #after 10 repeats, it goes to end function

def shortquestions():
    questionsss = [ #dictionary for questions
       {
            "question": "Where are books made?",
            "answers": ["Printer", "Book factory", "Factory", "printing process"],
        },
        {
            "question": "What is one material used to make books?",
            "answers": ["Glue", "Threading", "Thread", "Paper", "Ink"],
        },
        {
            "question": "What is the first step to make a book?",
            "answers": ["Gather materials", "Gathering materials", "Material gathering", ],
        },
        {
            "question": "What is the primary raw material used in making paper for books?",
            "answers": ["Wood pulp",],
        },
        {
            "question": "Which process is commonly used to bind the pages of a book together?",
            "answers": ["Gluing", "Glue"],
        },
        {
            "question": "What environmental concern is associated with traditional paper production?",
            "answers": ["Air pollution", "Water consumption", "Deforestation"],
        },
        {
            "question": "Which of the following is a sustainable alternative for book production?",
            "answers": ["Using recycled paper", "Recycling"],
        },
        {
            "question": "What is the role of ink in book production?",
            "answers": ["To print text and images", "Printing", "To print"],
        },
        {
            "question": "Which stage of a paper book's life cycle typically uses the most water?",
            "answers": ["Pulp and paper production"],
        },
        {
            "question": "What is one way to reduce the environmental impact of book production?",
            "answers": ["Choosing eco-friendly materials", "Recycle"],
        },
    ]
    # chooses random question
    question = random.choice(questionsss)
    tw("\n" + question["question"]) #shows question from dictionary, tw is to call typewriter effect for this line
    user_answer = input("").lower().strip() #.strip() makes it so that even if there is a space in the user's answer the program removes it

    if user_answer in [ans.lower() for ans in question['answers']]: #I used StackOverflow for this part to check if one of the answers is right from the valid answers dictionary 
        tw(f"{GREEN}Correct!! {RESET}")
    else:
        print(f"{RED}Incorrect! The correct answers were either one of these: {question['answers']}{RESET}.")
        removed = cargo.pop(random.randint(0,len(cargo)-1))
        print(f"{RED_BG}You lost a {removed} box!{RESET}")
            
        if (len(cargo)) == 0: #checks to see if user lost all of their cargo
            tw(f"{RED}You have lost all your cargo! Game Over!{RESET}")
            exit()

def double_short():
    for i in range(4):
        print(f"\n{BOLD}{BLUE_BG}DOUBLE OR NOTHING CHALLENGE!{RESET}") 
        time.sleep(0.6)
        print(f"\n{BOLD}{RED_BG}DOUBLE OR NOTHING CHALLENGE!{RESET}",) 
        time.sleep(0.6)
    tw("Youi loose -2000 points if you get it wrong")
    tw("But get +2000 points if you get it right :)")

    double_shortt = [ #double or nothing question dictionary for short answers
        {
            "question": "Which stage of the book lifecycle contributes MOST to deforestation?",
            "answers": ["Production", "producing", "printing"],
        },
        {
            "question": "Which chemical process is commonly used to break down wood chips into pulp for papermaking?",
            "answers": ["Kraft process", "Krafting", "crafting", "craft process"],
        },
        {
            "question": "What percentage of the original wood mass is typically lost during the chemical pulping process due to lignin removal? (Enter your answer as a percentage (%))",
            "answers": ["50-60%", "45%", "60%", "45-60%", "50%", "55%"],
        },
        {
            "question": "What should you do after finishing reading a book?",
            "answers": ["Recycle it", "recycling", "Donate it", "donating", "donation", "give it to a friend", "give it away", "donate it to a library", "give it to a drive"]
        },
        {
            "question": "What gas is released when trees are cut down for paper?",
            "answers": ["Carbon dioxide", "CO2", "greenhouse gases", "GHG"],
        },
        {
            "question": "What type of pollution results from transporting books?",
            "answers": ["Greenhouse gases", "Greenhouse gases"],
        },
        {
            "question": "What process gives old books life?",
            "answers": ["Recycling"],
        },
        {
            "question": "Where do unwanted books often end?",
            "answers": ["Landfills", "dump", "garbage dump", "trash", "garbage"],
        },
        ]

    question = random.choice(double_shortt)
    tw("\n" + question["question"]) #shows question from dictionary, tw is to call typewriter effect for this line
    user_answer = input("").lower().strip() #.strip() makes it so that even if there is a space in the user's answer the program removes it

    if user_answer in [ans.lower() for ans in question['answers']]: #I used StackOverflow for this part to check if one of the answers is right from the valid answers dictionary 
        tw(f"{GREEN}AMAZING! You won 2000 points!{RESET}")
        return 2000 #+2000 points
    else:
        tw(f"{RED}Wrong! The correct answer was one of these options: {question['answers']}.{RESET}")
        tw("You lost 2000 points!")
        return -2000 #-2000 points

def short():
    global score
    score = 0
    for i in range(1): #main game loop
        shortquestions()
        tw(f"C{BOLD}urrent cargo {cargo}")
        tw(f"Current score: {score}{RESET}")
        
        # 15% chance of double or nothing
        if random.random() < 0.15:
            tw("\nA special challenge has appeared!")
            time.sleep(0.5)
            score += double_short() #score is score plus or minus from double or nothing
            tw(f"Cargo: {cargo}")
            tw(f"Score: {score}")
        
        tw(f"{UNDERLINE}\nPlay another question? (y/n): {RESET}")
        play_again = input("").lower()
        if play_again == 'y':
            continue #if yes program continues
        elif play_again == 'n':
            tw(f"\n{BLUE}Game Over! Final cargo: {cargo}.\nFinal score: {score}. {RESET}")
            exit() #ends program
        else:
            tw(f"{RED}Invalid input. Try again{RESET}")
    end()
    
def end(): 
    global score
    time.sleep(0.5)
    tw(f"{BOLD}{BLUE}Congratulations! You have successfully delivered your cargo of books!{RESET}")
    time.sleep(0.5)
    tw("You now know how about the full life cycle of a book and the enviornmental impact of it.")
    time.sleep(0.5)
    tw("If you tried multiple choice mode, try doing short answer mode for a harder difficulty!")
    time.sleep(0.5)
    tw(f"{BOLD}Your final cargo: {cargo}\n")
    tw(f"Your final score: {score}{RESET}\n")

    tw("Would you like to play again? (y/n): ")
    end1 = input()

    if end1 == 'y':
        menu()
    else:
        tw(f"{BLUE_BG}Thank you for playing BookTruck! Goodbye!{RESET}")
        exit()  
    
def menu():
    print(logo)
    while True: #infinite loop so that if the user gives incorrect option it loops back to the question
        tw(f"\n{BOLD}Menu:{RESET}\n1. Begin Game\n2. Tutorial\n3. Exit")
        tw(f"{UNDERLINE}Please enter your choice (1/2/3):{RESET}")
        choice = input("")
        if choice == '1':
            
            while True: #same logic as the first while True, if the user gives invalid choice it loops back to this question
                tw(f"\nWhich difficulty would you like to play on?\n1. Multiple Choice (easy) \n2. Short Answer (hard)\n{UNDERLINE}Enter here (1/2):{RESET}")
                choice2 = input("")
                if choice2 == '1':
                    tw("You chose mulitple choice difficulty!")
                    multi() #starts multiple function
                
                elif choice2 == '2':
                    tw("You chose short answer difficulty!")
                    short()

                else:
                    tw("Invalid choice. Please try again.")
            
        elif choice == '2':
            tutorial = f"""\n📚 BookTruck - How to Play

{BOLD}Your Mission:{RESET}
You're a truck driver transporting precious book production materials to their destination. Your cargo includes threading, ink, paper, and glue—everything needed to make books!

{BOLD}The Goal:{RESET}
Answer 10 questions about the book life cycle and environmental impacts correctly to reach your destination and win the game.

{BOLD}How to Play:{RESET}
- You'll face 10 questions during your journey (multiple choice or short answer based on your chosen difficulty)
- Each question tests your knowledge about how books are made and their impact on the environment
- Answer correctly to keep moving forward
- Wrong answers may cost you points or cargo

{BOLD}Scoring:{RESET}
- You start with a certain number of points
- Correct answers earn you points
- Incorrect answers lose you points or damage your cargo

{BOLD}Losing Conditions - You lose if:{RESET}
1. Your score drops to zero or below (negative points)
2. You lose all your cargo materials (threading, ink, paper, and glue)

{BOLD}Winning Condition:{RESET}
Successfully answer all 10 questions while keeping your score positive and at least some cargo intact!

{BOLD}Tips for Success:{RESET}
- Think carefully about each answer
- Remember: books go through many stages from tree to reader
- Consider environmental factors like recycling, transportation, and resource use

Good luck, driver! 🚚📖

"""
            
            tw(tutorial)
            time.sleep(1)

            menu()
        elif choice == '3':
            tw("Thank you for playing BookTruck! Goodbye!")
            exit()

        #secret option to immediently acess multiple choice or short answer questions
        elif choice == '4': 
            multi()
        elif choice == '5':
            short()
        else:
            tw("Invalid choice. Please try again.")
        
tw(f"{BOLD}Welcome to BookTruck!!{RESET}")
time.sleep(0.4)
logo = """
   ___            __  ______             __  
  / _ )___  ___  / /_/_  __/_____ ______/ /__
 / _  / _ \/ _ \/  '_// / / __/ // / __/  '_/
/____/\___/\___/_/\_\/_/ /_/  \_,_/\__/_/\_\ 
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMW0dolllllllllllllllllllllllllllllllllllllllllloxKWMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMNo. .''''''''''''''''''''''''''''''''''''''''''. 'kMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMWNNNNNk. ;OKKKKKKKKKKXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNd. oWMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMM0:'''''.  ..'''''''''''lXMMMMMMMMMMMMMMMMMMMMMMMMMMMMWo .xMMMMMMMMMMMMMMMMMMMMMMMMMMMM
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
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM

"""
time.sleep(0.8)
menu() #runs menu function to start program
