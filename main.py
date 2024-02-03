import re

print("Great calculator")
print("Type 'quit' to exit\n")

previous = 0
run = True

def performMath():
    global run
    global previous
    equation = ""
    if previous == 0:
        equation = input("Enter the equation:")
    else:
        equation = input(str(previous))


    if equation == 'quit':
        print("Goodbye, thanks for using me!")
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:()" "]', '', equation)

        if previous == 0:
            previous = eval(equation)
        else:        
            previous = eval(str(previous) + equation)


while run:
    try:
        performMath()
    except ZeroDivisionError:
        print("Don't try to divide by zero!")
    except SyntaxError:
        print("Something weird happened maybe because of your actions or then it was the universe.")
