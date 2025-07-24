while True:
  user_input = input("Enter a number (or 'q' to quit: )");
  try:
    if user_input == 'q':
      break;
    else:
      user_input = int(user_input);
      if user_input % 2 ==0:
        print("This is an even number!");
      else:
        print("This is an odd number!");
  except ValueError:
    print("This is not a valid number!");


