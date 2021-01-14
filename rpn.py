stack = []
gamingGamer = True
def isnumber(s):
    try:
        n = float(s)
        return True
    except ValueError:
        return False

while gamingGamer == True:
    inp_str = input("Something something prompt something something")
    someinput = inp_str.split( )
    for i in someinput:
        if isnumber(i):
            stack.append(float(i))
        else:
            if i == "+":
                jeemo = stack.pop()
                meemo = stack.pop()
                print(str(meemo+jeemo))
                stack.append(meemo+jeemo)
            if i == "-":
                jeemo = stack.pop()
                meemo = stack.pop()
                print(str(meemo-jeemo))
                stack.append(meemo-jeemo)

            if i == "*":
                jeemo = stack.pop()
                meemo = stack.pop()
                print(str(meemo*jeemo))
                stack.append(meemo*jeemo)
            if i == "/":
                jeemo = stack.pop()
                meemo = stack.pop()
                print(str(meemo/jeemo))
                stack.append(meemo/jeemo)
            if i == "p": print(stack)
            if i == "i": stack.append(1/stack.pop())
            if i == "n": stack.append(-1*stack.pop())
            if i == "x": gamingGamer = False
