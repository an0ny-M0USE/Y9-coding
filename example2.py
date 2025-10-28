import random

def ask_question():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["London", "Paris", "Berlin", "Madrid"],
            "correct": "B"
        },
        {
            "question": "What is 8 x 7?",
            "options": ["54", "56", "58", "60"],
            "correct": "B"
        },
        {
            "question": "Which planet is closest to the Sun?",
            "options": ["Venus", "Mars", "Mercury", "Earth"],
            "correct": "C"
        }
    ]
    
    # chooses random question
    question = random.choice(questions)
    print("\n" + question["question"])
    
    # displays options
    print("A.", question["options"][0])
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

def double_or_nothing():
    print("\nDOUBLE OR NOTHING CHALLENGE!")
    print("Get it right: +2000 points")
    print("Get it wrong: -2000 points")
    
    bonus_questions = [
        {
            "question": "What is the square root of 144?",
            "options": ["10", "12", "14", "16"],
            "correct": "B"
        },
        {
            "question": "Which year did World War II end?",
            "options": ["1943", "1944", "1945", "1946"],
            "correct": "C"
        }
    ]
    
    question = random.choice(bonus_questions)
    print("\n" + question["question"])
    
    print("1.", question["options"][0])
    print("2.", question["options"][1])
    print("3.", question["options"][2])
    print("4.", question["options"][3])
    
    user_answer = input("\nYour answer (A/B/C/D): ").upper()
    
    if user_answer == question["correct"]:
        print("AMAZING! You won 2000 points!")
        return 2000
    else:
        print(f"Wrong! The correct answer was {question['correct']}.")
        print("You lost 2000 points!")
        return -2000

def main():
    score = 0
    while True:
        # normal question
        score += ask_question()
        print(f"Current score: {score}")
        
        # 10% chance of double or nothing
        if random.random() < 0.1:
            print("\nA special challenge has appeared!")
            score += double_or_nothing()
            print(f"Score after challenge: {score}")
        
        play_again = input("\nPlay another question? (y/n): ").lower()
        if play_again != 'y':
            break
    
    print(f"\nGame Over! Final score: {score}")

main()