def run_quiz(questions):
    score = 0
    
    for i, q in enumerate(questions, 1):
        print(f"\nQuestion {i}: {q['question']}")
        
        for j, option in enumerate(q['options']):
            print(f"{j+1}. {option}")
        
        while True:
            try:
                choice = int(input("Enter your choice (1-4): "))
                if 1 <= choice <= 4:
                    break
                print("Please enter a number between 1 and 4")
            except:
                print("Please enter a valid number")
        
        if q['options'][choice-1] == q['answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The answer is: {q['answer']}")
    
    print(f"\nYour final score: {score}/{len(questions)}")
    return score

