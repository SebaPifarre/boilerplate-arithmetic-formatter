import re


def arithmetic_arranger(problems, show = False):
  # Defining varibles
  firstRow = ""
  secondRow = ""
  lines = ""
  ans = ""
  
  #Checking for errors
  if len(problems) > 5:
    return "Error: Too many problems."
  
  for problem in problems:
    if re.search("[^\s0-9.+-]",problem):
      if re.search("[/]", problem) or re.search("[*]", problem):
        return "Error: Operator must be '+' or '-'."
      return "Error: Numbers must only contain digits."

    # Spliting each problem in the loop to get the numbers and the operator
    firstNumber = problem.split()[0]
    operator = problem.split()[1]
    secondNumber = problem.split()[2]
    
    #Another error check
    if len(firstNumber) >= 5 or len(secondNumber) >= 5:
      return "Error: Numbers cannot be more than four digits."

    # Checking wich operation I need to perform
    if operator == "+":
      sum = str(int(firstNumber) + int(secondNumber))
    elif operator == "-":
      sum = str(int(firstNumber) - int(secondNumber))

    # Getting the reference so I can adjust all the numbers
    length = max(len(firstNumber), len(secondNumber)) + 2

    # Adjusting the numbers, dashes and resolution
    top = firstNumber.rjust(length)
    bottom = operator + secondNumber.rjust(length - 1)
    line = "-" * length
    sum = sum.rjust(length)

    # This if statement is to make sure I don't get empty spaces following the last problem
    if problem != problems[-1]:
      firstRow += top + "    "
      secondRow += bottom + "    "
      lines += line + "    "
      ans += sum + "    "
      
    else:
      firstRow += top
      secondRow += bottom
      lines += line
      ans += sum

  # Returning the complete string, with or without the answers
  if show:
    return firstRow + "\n" + secondRow + "\n" + lines + "\n" + ans
  else:
    return firstRow + "\n" + secondRow + "\n" + lines

  #['32 + 698', '3801 - 2', '45 + 43', '123 + 49']
  