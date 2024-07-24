from data import fetchdata
import random
from logo import logo

logo()

questions = fetchdata()


def checkanswer(useranswer , correctanswer):
    score=0
    if useranswer==correctanswer:
        score +=1
        print(f"Score = 1/1")
    else:
       score =0
       print(f"Score = 0/1")
    return score
        
score = 0
for i, question in enumerate(questions, 1):
    print(f"Question {i}: {question['question']}")
    print("Options:")
    options = question['incorrect_answers'] + [question['correct_answer']]
    random.shuffle(options)        
    for j, option in enumerate(options, 1):
        print(f"{j}. {option}")
    user_option = int(input("Choose:"))
    correct_option = options.index(question['correct_answer'])+1
    score +=checkanswer(user_option,correct_option)    
    print(f"Correct Answer: {correct_option}.{question['correct_answer']}")
    print()

print(f"Total Score = {score}/10")
