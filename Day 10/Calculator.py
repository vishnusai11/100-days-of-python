from art import logo
print(logo)
#add
def add(n1,n2):
  return n1+n2
#subtract
def subtract(n1,n2):
  return n1-n2
#multiply
def multiply(n1,n2):
  return n1*n2
#divide
def divide(n1,n2):
  return n1/n2
operations={
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":divide
}
def calc(operation_symbol,num1,num2):
  operation=operations[operation_symbol]
  answer=operation(num1,num2)
  return answer
  #print(f"{num1}{operation_symbol}{num2}={answer}")
choice=True
while choice:
  num1=int(input('Enter your first number'))
  for operation in operations:
    print(operation)
  operation_symbol=input('Enter the operation that you want to do')
  num2=int(input('Enter your second number'))
  ans=calc(operation_symbol,num1,num2)
  print(f"{num1}{operation_symbol}{num2}={ans}")
  choice_qn=input('Do you want to continue calculations by entering a new number\nEnter "yes" or "no"')
  while choice_qn=='yes':
    for operation in operations:
      print(operation)
    operation_symbol=input('Enter the operation that you want to do')
    num3=int(input('Enter your next number'))
    ans_1=calc(operation_symbol,ans,num3)
    print(f"{ans}{operation_symbol}{num3}={ans_1}")
    choice_qn=input('Do you want to continue calculations by entering a new number\nEnter "yes" or "no"')
  if choice_qn=='no':
    choice=False


