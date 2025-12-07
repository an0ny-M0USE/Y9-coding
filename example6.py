Bold = '\033[1m'
Reset = '\033[0m' #resets text to normal

print(f"""\n📚 {Bold}BookTruck - How to Play{Reset}

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