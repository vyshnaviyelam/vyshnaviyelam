def div():
    try:
        input1=int(input())
        input2=int(input())
        divison=input1/input2
        
    except ZeroDivisionError :
        print("divisor is zero")
    except ValueError:
        print("string is given")
div()