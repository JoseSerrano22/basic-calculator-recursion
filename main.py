import art

print(art.logo)


def add(n1,n2):
  result = n1+n2
  return result

def substract(n1,n2):
  result = n1-n2
  return result

def mult(n1,n2):
  result = n1*n2
  return result

def div(n1,n2):
  result = n1/n2
  return result

operations = { #dictionary of funcions
  "+": add,
  "-": substract,
  "*": mult,
  "/": div
} 

def calculator():
  num1 = float(input("What is your first number?: "))

  for key in operations: #print operations
    print(key)

  symbol = input("Which operation you gonna use from above?: ")

  num2 = float(input("What is your second number?: "))



  function = operations[symbol]
  result = function(num1,num2) #result of the user's operation

  print(f"{num1} {symbol} {num2} = {result}")


  again = input(f"Type 'y' to continue with calculating {result}, or 'n' to have new slate: ")

  if again == "y": #if true repeat with the result 
    while True:
      for key in operations:
        print(key)

      symbol = input("Which operation you gonna use from above?: ")

      num2 = float(input("What is your second number?: "))

      function = operations[symbol]
      result = function(result,num2)

      print(f"{result} {symbol} {num2} = {result}")

      again = input(f"Type 'y' to continue with calculating {result}, or 'n' to have a new slate: ")

      if(again == "n"): #if no repeat the calculator again from zero
        calculator() # recursion for a new slate
  elif again == "n":
    calculator()

calculator()