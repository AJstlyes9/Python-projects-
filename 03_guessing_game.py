import random

def difficulty_level():
  level = int(input("Please select difficulty level range (10 | 20 | 50)"))
  if level == 10:
    max_range = 10;
  elif level == 20:
    max_range = 20;
  else:
    max_range = 50;

  secret_number = random.randint(1,max_range);
  print(secret_number)
  guess_limit = 3;
  guess_count = 0;

  while guess_count < guess_limit:
    guess = int(input(f"Guess a number between 1 and {max_range}: "));
    guess_count+=1;
    if guess < secret_number:
      print("Too low!");
    elif guess > secret_number:
      print("Too High!");
    else:
      print("Congratulations, you guessed it!")
      print(f"Number of attempts: {attempts}")
      break;

difficulty_level();