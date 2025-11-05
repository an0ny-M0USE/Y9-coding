import random, time #imports random and time

def tw(text): #typewriter effect def
    for character in text:
        print(character, end='', flush=True)
        time.sleep(0.018) #speed of typewriting
    print()

def loading():
    for i in range(3):
        print("\rLoading game     ", end="", flush=True)
        print("\rLoading game", end="", flush=True)
        time.sleep(0.2) 
    
    # one dot at a time
    for i in range(1, 4):  # 3 dots total
        print("\rLoading game" + "." * i + "   ", end="", flush=True) #adds 3 dots in 0.2 second intervals
        time.sleep(0.2)

def load_anim(): #easy way to call loading animation
    print("")
    for i in range(3):
        loading()  # 
        print("\r" + " " * 20 + "\r", end="")  # Clear the line

def questionss(): #defines dictionary for questions
    questions = [ #dictionary for questions
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
    tw("\n" + question["question"]) #shows question from dictionary, tw is to call typewriter effect for this line
    
    # displays options
    print("A.", question["options"][0]) #options for corresponding question/option from dicitionary, e.g. question calls question from question dictionary
    time.sleep(0.06)
    print("B.", question["options"][1])
    time.sleep(0.06)
    print("C.", question["options"][2])
    time.sleep(0.06)
    print("D.", question["options"][3])
    time.sleep(0.06)

    
    # answer prompt
    tw("\nPlease enter your answer (A/B/C/D):") #typewriter prompt (not actual input but just for visuals)
    user_answer = input().upper() #actual input for user
    
    # check answer
    if user_answer == question["correct"]:
        tw("Correct! +1000 points!")
        return 1000 #+1000 points
    else:
        print(f"Wrong! The correct answer was {question['correct']}.")
        return 0 #no points

def double_multi(): #double or nothing random chance for display
    tw("\nDOUBLE OR NOTHING CHALLENGE!")
    tw("Get it right: +2000 points")
    tw("Get it wrong: -2000 points")
    
    bonus_questions = [ #double or nothing question dictionary
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
            "options": ["10-20%", "30-40%", "50-60%", "70-80%"],
            "correct": "C"
        },
        {
            "question": "Which of the following is NOT a common method for recycling paper?",
            "options": ["De-inking", "Hydraulic pressing", "Thermal pulping", "Magnetic separation"],
            "correct": "D"
        }
    ]
    
    question = random.choice(bonus_questions) #random question from dictionary
    tw("\n" + question["question"])
    
    print("1.", question["options"][0]) #display options for bonus questions
    time.sleep(0.06)
    print("2.", question["options"][1])
    time.sleep(0.06)
    print("3.", question["options"][2])
    time.sleep(0.06)
    print("4.", question["options"][3])
    time.sleep(0.06)
    
    tw("\nPlease enter your answer (A/B/C/D):") #typewriter prompt for visuals
    user_answer = input("").upper() #actual input for user
    
    if user_answer == question["correct"]:
        tw("AMAZING! You won 2000 points!")
        return 2000 #+2000 points
    else:
        tw(f"Wrong! The correct answer was {question['correct']}.")
        tw("You lost 2000 points!")
        return -2000 #-2000 points

def multi():
    score = 0 #score variable
    while True: #main game loop
        #normal question
        score += questionss() # adds score that the user got from above and runs questionss
        tw(f"Current score: {score}") #shows score
        
        # 10% chance of double or nothing
        if random.random() < 0.1:
            tw("\nA special challenge has appeared!")
            score += double_multi() #score is score plus or minus from double or nothing
            tw(f"Score: {score}")
        
        tw("Play another question? (y/n):")
        play_again = input("").lower()
        if play_again == 'y':
            continue #if yes program continues
        elif play_again == 'n':
            tw(f"\nGame Over! Final score: {score}")
            return False #ends program
        else:
            tw("Invalid input. Try again")

def short_answer_questions():
    questionsss = [ #dictionary for questions
        {
            "question": "Where are books physically made? ",
            "correct": ["Printer", "the Printer", "Printing house"]
        },
        {
            "question": "What is one material used to make books? ",
            "correct": ["Glue", "Paper", "Ink", "Threading"]
        },
        {
            "question": "What is the first step to make a book? ",
            "correct": "Gather materials"
        },
        {
            "question": "What is the primary raw material used in making paper for books? ",
            "correct": "Wood pulp"
        },
        {
            "question": "Which process is commonly used to bind the pages of a book together? ",
            "correct": "Gluing"
        },
    ]
    # chooses random question
    question = random.choice(questionsss)
    tw("\n" + question["question"]) #shows question from dictionary, tw is to call typewriter effect for this line
    user_answer = input("").lower()

    if user_answer == question["correct"]:
        tw("Correct! +1500 points!")
        return 1500 #+1500 points
    else:
        tw(f"Incorrect! The correct answer was {question['correct']}.")

def double_short():
    tw("\nDOUBLE OR NOTHING CHALLENGE!")
    tw("Get it right: +2000 points")
    tw("Get it wrong: -2000 points")

bonus_questions = [ #double or nothing question dictionary for short answers
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
            "options": ["10-20%", "30-40%", "50-60%", "70-80%"],
            "correct": "C"
        },
        {
            "question": "Which of the following is NOT a common method for recycling paper?",
            "options": ["De-inking", "Hydraulic pressing", "Thermal pulping", "Magnetic separation"],
            "correct": "D"
        }
    ]

def short():
    score = 0
    while True: #main game loop
        # normal question
        score += short_answer_questions()
        tw(f"Current score: {score}")
        
        # 10% chance of double or nothing
        if random.random() < 0.1:
            tw("\nA special challenge has appeared!")
            score += double_multi() #score is score plus or minus from double or nothing
            tw(f"Score after challenge: {score}")
        
        tw("Play another question? (y/n):")
        play_again = input("").lower()
        if play_again == 'y':
            continue
        elif play_again == 'n':
            tw(f"\nGame Over! Final score: {score}")
            return False
        else:
            tw("Invalid input. Try again")
    
def menu():
    tw("Welcome to BookTruck!!")
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
    print(logo)
    while True:
        tw("\nMenu:\n1. Begin Game\n2. Tutorial\n3. Exit")
        tw("Please enter your choice (1/2/3):")
        choice = input("")
        if choice == '1':
            
            tw("\nWhich difficulty would you like to play on?\n1. Multiple Choice (easy) \n2. Short Answer (hard)")
            choice2 = input("")
            if choice2 == '1':
                tw("You chose mulitple choice difficulty!")
                load_anim() #starts loading animation
                multi() #starts multiple function
            
            elif choice2 == '2':
                tw("You chose short answer difficulty!")
                load_anim() 
                short()

            else:
                tw("Invalid choice. Please try again.")
            
        elif choice == '2':
            tw("")
            menu()
        elif choice == '3':
            tw("Thank you for playing BookTruck! Goodbye!")
            break #break so the loop doesn't go on infinitely since its a while true loop
        else:
            tw("Invalid choice. Please try again.")

menu() #runs menu function to start programimport random, time #imports random and time

def tw(text): #typewriter effect def
    for character in text:
        print(character, end='', flush=True)
        time.sleep(0.018) #speed of typewriting
    print()

def questionss(): #defines dictionary for questions
    questions = [ #dictionary for questions
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
    tw("\n" + question["question"]) #shows question from dictionary, tw is to call typewriter effect for this line
    
    # displays options
    print("A.", question["options"][0]) #options for corresponding question/option from dicitionary, e.g. question calls question from question dictionary
    time.sleep(0.06)
    print("B.", question["options"][1])
    time.sleep(0.06)
    print("C.", question["options"][2])
    time.sleep(0.06)
    print("D.", question["options"][3])
    time.sleep(0.06)

    
    # answer prompt
    tw("\nPlease enter your answer (A/B/C/D):") #typewriter prompt (not actual input but just for visuals)
    user_answer = input().upper() #actual input for user
    
    # check answer
    if user_answer == question["correct"]:
        tw("Correct! +1000 points!")
        return 1000 #+1000 points
    else:
        print(f"Wrong! The correct answer was {question['correct']}.")
        return 0 #no points

def double_or_nothing(): #double or nothing random chance for display
    tw("\nDOUBLE OR NOTHING CHALLENGE!")
    tw("Get it right: +2000 points")
    tw("Get it wrong: -2000 points")
    
    bonus_questions = [ #double or nothing question dictionary
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
            "options": ["10-20%", "30-40%", "50-60%", "70-80%"],
            "correct": "C"
        },
        {
            "question": "Which of the following is NOT a common method for recycling paper?",
            "options": ["De-inking", "Hydraulic pressing", "Thermal pulping", "Magnetic separation"],
            "correct": "D"
        }
    ]
    
    question = random.choice(bonus_questions) #random question from dictionary
    tw("\n" + question["question"])
    
    print("1.", question["options"][0]) #display options for bonus questions
    time.sleep(0.06)
    print("2.", question["options"][1])
    time.sleep(0.06)
    print("3.", question["options"][2])
    time.sleep(0.06)
    print("4.", question["options"][3])
    time.sleep(0.06)
    
    tw("\nPlease enter your answer (A/B/C/D):") #typewriter prompt for visuals
    user_answer = input("").upper() #actual input for user
    
    if user_answer == question["correct"]:
        tw("AMAZING! You won 2000 points!")
        return 2000 #+2000 points
    else:
        tw(f"Wrong! The correct answer was {question['correct']}.")
        tw("You lost 2000 points!")
        return -2000 #-2000 points



def main():
    score = 0 #score variable
    while True: #main game loop
        #normal question
        score += questionss() # adds score that the user got from above and runs questionss
        tw(f"Current score: {score}") #shows score
        
        # 10% chance of double or nothing
        if random.random() < 0.1:
            tw("\nA special challenge has appeared!")
            score += double_or_nothing() #score is score plus or minus from double or nothing
            tw(f"Score: {score}")
        
        tw("Play another question? (y/n):")
        play_again = input("").lower()
        if play_again == 'y':
            continue #if yes program continues
        elif play_again == 'n':
            tw(f"\nGame Over! Final score: {score}")
            return False #ends program
        else:
            tw("Invalid input. Try again")
        

    

main() #runs main
