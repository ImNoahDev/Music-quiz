# import modules
import os
import random
import readline

# fill first space
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
   high_scores = f.readlines()
   high_scores = [score.strip() for score in high_scores]

# import songs
exec(open("./songs.txt", 'r').read())

if login():
  while playing:
   # initialise song picker
   rand = random.randint(0,27)
   current_songs = [[s[0] for s in songs[rand][0].split()], songs[rand][1]]
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
      os.system('clear')
      print(f"Failed, Points: {points}")
      if int(points) > int(high_scores[-1].split(" ")[1]):
        if len(high_scores) < 5 or int(points) > int(high_scores[-1].split(" ")[1]):
          name = input("Name: ")
          new_score = name + ": " + str(points)
          high_scores.append(new_score)
          high_scores.sort(reverse=True)
          high_scores = high_scores[:5]
          print("NEW HIGH SCORE")
      print("High Scores:")
      for i in range(len(high_scores[:5])):
        print(f"{i+1}. {high_scores[i]}")
      playing = False

# write high scores
with open('./score.txt', 'w') as f:
   for score in high_scores:
      f.write(score + "\n")
