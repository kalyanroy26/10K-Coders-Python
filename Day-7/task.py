while True:
    marks = int(input("Enter your marks: "))

    match marks:
        case marks if marks>=90:
            print("top")
        case marks if marks>=70:
            print("first class")
        case marks if marks>=50:
            print("second class")
        case marks if marks>=40:
            print("third class")
        case marks if marks>=1 and marks<40:
            print("failed")
        case _:
            break



while True:
    month = int(input("Enter the number between 1 to 12: "))
    match month:
        case 1:
            print("January")
        case 2:
            print("February")
        case 3:
            print("March")
        case 4:
            print("April")
        case 5:
            print("May")
        case 6:
            print("June")
        case 7:
            print("July")
        case 8:
            print("August")
        case 9:
            print("September")
        case 10:
            print("October")
        case 11:
            print("November")
        case 12:
            print("December")
        case _:
            print("Invalid Input")
            break


