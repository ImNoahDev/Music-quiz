# import modules
import os
import random

# fill first space
import readline
def linput(prompt, prefill=''):
   readline.set_startup_hook(lambda: readline.insert_text(prefill))
   return input(prompt)

# Login function
def login():
  if input("username: ") == "user":
    if input("password: ") == "pssw":
      return True
    else:
      print("wrong password")
      return False
    
# initialise variables
playing = True
points = 0
songs = ""

# import high scores
with open('./score.txt', 'r') as f:
    high=f.read()

# import songs
exec(open("./songs.txt", 'r').read())

if login():
  while playing:
    # initialise song picker
    rand = random.randint(0,27)
    current_songs = [songs[rand][0][0], songs[rand][1]]
    print(current_songs)

    # guess song and add scores
    ans = linput("song: ", songs[rand][0][0])
    if ans.lower() == songs[rand][0].lower():
      points+=3
      print(f"Points: {points}")
    else:  
      # if fail
      os.system('clear')
      print("try again")
      print(current_songs)
      ans = linput("song: ", songs[rand][0][0])
      if ans.lower() == songs[rand][0].lower():
        points+=1
        print(f"Points: {points}")
      else:
        # end game
        os.system('cls')
        print(f"Failed, Points: {points}")
        os.system('clear')
        if int(points) > int(high.split(" ")[1]):
          high = input("Name: ") + ": " + str(points)
          print(f"NEW HIGH SCORE")
        print(high)
        playing = False

# write high scores
with open('./score.txt', 'w') as f:
    f.write(high)
f.close()



# from flask import Flask, render_template, request
# app = Flask(__name__)
# @app.route('/')
# def loginpage():
#     return render_template('index.html')

# @app.route('/questions', methods=['POST'])
# def questions():
#   pass

# @app.route('/results', methods=['POST'])
# def results():
#   pass

# if __name__ == '__main__':
#     app.run()