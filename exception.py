while True:
     
    try:   
        a = int(input("Enter a number:"))
        b = int(input("enter a second number:"))
        print(f"the division of both is: {a/b}")

    except ZeroDivisionError:
        print ("dont divide by zero")    
    
    except Exception as e:
        print("there's an error occuring", e)

    
