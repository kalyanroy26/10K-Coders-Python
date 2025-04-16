import random 

count = 0
while True:
    choice = input("want to roll the dice? y/n: ")

    if choice == 'y':
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        print(f"{dice1}, {dice2}")
        count+=1
    elif choice == 'n':
        print("GAME COMPLETED")
        break
    else:
        print("invalid choice")
    
    print(count,"times dice rolled")
