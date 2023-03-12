
#token = ["2","1","+","3","*"]
#token2 = ["4","13","5","/","+"]
token3 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
calc = []

for i in token3:
    print(calc)
    if i.lstrip("-").isdigit():
        calc.append(int(i))
    else:
        num1 = int(calc.pop())
        num2 = int(calc.pop())
        if i == "+":
            calc.append(num2+ num1)
        if i == "-":
            calc.append(num2-num1)        
        if i == "/":
            calc.append(int(num2/num1))
        if i == "*":
            calc.append(num2*num1)
print(calc)                        