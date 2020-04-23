import sys
import math

ifile = ""

if len(sys.argv) >= 2:
  ifile = sys.argv[1]
else:
  ifile = input("File to interpret? ")

ifile = open(ifile, "r")
script = ifile.read()
ifile.close()

stack = []

i=0
while i < len(script):
  char = script[i]
  charnum = 0
  try:
    charnum = int(char)
    if charnum >= 0 and charnum <= 9:
      stack.append(charnum)
  except:
    pass
    if char.lower() == "n":
      try:
        uin = int(input("? "))
        stack.append(uin)
      except:
        print("ERROR: User input is not a valid number!", file=sys.stderr)
        sys.exit()
    elif char == "+":
      stack.append(stack.pop()+stack.pop())
    elif char == "-":
      stack.append(stack.pop()-stack.pop())
    elif char == "*":
      stack.append(stack.pop()*stack.pop())
    elif char == "/":
      stack.append(math.floor(stack.pop()/stack.pop()))
    elif char == "?":
      if stack.pop() != 0:
        i = stack.pop()-1
    elif char == "!":
      if stack.pop(0) != 0:
        i = stack.pop(0)-1
    elif char == "&":
      stack[len(stack)] = stack[len(stack)-1]
    elif char == "%":
      stack = [stack[0]] + stack
  finally:
    i += 1

print(stack)