num1 = int(input("Enter first number: "));
opr = input("Enter operator: ")
num2 = int(input("Enter second number: "));


if opr == "+":
  result = num1 + num2;
elif opr == "-":
  result = num1 - num2;
elif opr == "/":
  if opr and num2 == 0:
    result = "The first number is not divisible by 0";
  else :
    result = num1 / num2;
elif opr == "%":
  result = num1 % num2;
elif opr == "**":
  result = num1 ** num2;
else:
  print("Not a valid operator");

print(result)
