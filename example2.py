import random

def ask_question():
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
    ]
    
    # chooses random question
    question = random.choice(questions)
    print("\n" + question["question"])
    
    # displays options
    print("A.", question["options"][0]) #options for corresponding question from dicitionary
    print("B.", question["options"][1]) 
    print("C.", question["options"][2])
    print("D.", question["options"][3])
    
    # get answer
    user_answer = input("\nYour answer (A/B/C/D): ").upper()
    
    # check answer
    if user_answer == question["correct"]:
        print("Correct! +1000 points!")
        return 1000
    else:
        print(f"Wrong! The correct answer was {question['correct']}.")
        return 0

def double_or_nothing(): #double or nothing random chance
    print("\nDOUBLE OR NOTHING CHALLENGE!")
    print("Get it right: +2000 points")
    print("Get it wrong: -2000 points")
    
    bonus_questions = [ #double or nothing question dictionary
        {
            "question": "Which stage of the book lifecycle contributes MOST to deforestation?",
            "options": ["Writing", "Production", "Shipping", "Throwing away"],
            "correct": "B"
        },
        {
            "question": "What is the CORRECT order of the book lifecycle?",
            "options": ["Raw Material Extraction, Paper Production, Printing & Manufacturing, Marketing & Sales, Distribution & Transportation, Use Phase, End of Life", "Raw Material Extraction, Ink Production, Paper Production, Printing & Manufacturing, Packaging, Distribution & Transportation, Use Phase, End of Life", "Raw Material Extraction, Paper Production, Printing & Manufacturing, Packaging, Distribution & Transportation, Use Phase, End of Life", "Raw Material Extraction, Paper Production, Quality Control & Editing, Printing & Manufacturing, Packaging, Distribution & Transportation, Use Phase, End of Life"],
            "correct": "C"
        }
    ]
    
    question = random.choice(bonus_questions) #random question from dictionary
    print("\n" + question["question"])
    
    print("1.", question["options"][0]) #display options for bonus questions
    print("2.", question["options"][1])
    print("3.", question["options"][2])
    print("4.", question["options"][3])
    
    user_answer = input("\nYour answer (A/B/C/D): ").upper()
    
    if user_answer == question["correct"]:
        print("AMAZING! You won 2000 points!")
        return 2000 #+2000 points
    else:
        print(f"Wrong! The correct answer was {question['correct']}.")
        print("You lost 2000 points!")
        return -2000 #-2000 points

def main(): #main loop def
    score = 0 #score starts at 0
    while True: #main game loop
        # normal question
        score += ask_question()
        print(f"Current score: {score}")
        
        # 10% chance of double or nothing
        if random.random() < 0.1:
            print("\nA special challenge has appeared!")
            score += double_or_nothing() #score is score plus or minus from double or nothing
            print(f"Score after challenge: {score}")
        
        play_again = input("\nPlay another question? (y/n): ").lower()
        if play_again != 'y':
            break
    
    print(f"\nGame Over! Final score: {score}")

main() #runs main function to start game
