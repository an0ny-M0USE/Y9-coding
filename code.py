import random, time #imports random and time

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
        }
        {
            "question": "What is the primary raw material used in making paper for books?",
            "options": ["Cotton", "Wood pulp", "Recycled plastic", "Bamboo"],
            "correct": "B"
        }
        {

        }
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
        }
        {
            "question": "Which chemical process is commonly used to break down wood chips into pulp for papermaking?",
            "options": ["Oxidation", "Kraft process", "Fermentation", "Electrolysis"],
            "correct": "B"
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