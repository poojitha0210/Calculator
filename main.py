from art import logo
from replit import clear


def add(n1,n2):
  return n1+n2

def sub(n1,n2):
  return n1-n2

def mul(n1,n2):
  return n1*n2

def div(n1,n2):
  return n1/n2

operation={
  "+":add,
  "-":sub,
  "*":mul,
  "/":div
}

def calculator():
  n1=float(input("enter number 1:"))
  for i in operation:
    print(i)
  flag=True
  while flag:
    n2=float(input("enter number :"))
    op=input("enter the operation from above: ")
    t=operation[op]
    output=t(n1,n2)
    print(f"{n1} {op} {n2} = {output}")
    
    if input("type Y to continue or N to stop")== "Y":
      n1=output
    else:
      flag=False
      calculator()
      
calculator()


