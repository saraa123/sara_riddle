import os
import json 
from flask import Flask, render_template
from random import randint 

app = Flask(__name__)

# def riddle_questions():
#     with open("data/riddles.json", "r") as json_riddles:
#         riddles_data = json.load(json_riddles)
#         return riddles_data 
        
@app.route('/')
def index():
    return render_template("index.html")
    
@app.route('/riddles')
def riddles():
    return render_template("riddles.html")

@app.route('/leaderboard')
def leaderboard():
    return render_template("leaderboard.html")

# riddle questions function 
def question():
    question_pool = []
    question_pool.append({'question' : "The more you take, the more you leave behind. What am I?" , 'a' : "Money" , 'b' : "Food" , 'c' : "Footsteps" , 'd' : "Time" , 'answer' : 'c'})
    question_pool.append({'question' : "What has a head, a tail, is brown, and has no legs?" , 'a' : "A dog" , 'b' : "A cat" , 'c' : "A bird" , 'd' : "A penny" , 'answer' : 'd'})
    question_pool.append({'question' : "What belongs to you, but is used by others?" , 'a' : "Clothes" , 'b' : "Jewellery" , 'c' : "Your house" , 'd' : "Your name" , 'answer' : 'd'})
    random_idx = randint(0, len(question_pool) - 1)
    print(question_pool[random_idx]['question'])
    print(" ")
    print("A:", question_pool[random_idx]['a']), 
    print("B:", question_pool[random_idx]['b']),
    print("C:", question_pool[random_idx]['c']),
    print("D:", question_pool[random_idx]['d'])

    guess = input("Your guess: ")
    guess = guess.lower()
    
    number_of_questions = len(question_pool)
    
    score = 0
    
    if guess == question_pool[random_idx]['answer']:
        print(" ")
        print("Correct!")
        score += 1
        print(score)
    else:
        print(" ")
        print("Sorry, that was wrong!")
    
    print("You got {0} correct out of {1}".format(score, number_of_questions))
        

question()
        
    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True) 
            