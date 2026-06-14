while True:
    for number in range(1, 11):
        guess = int(input("Make your guess of the number: "))
        if guess != number:
            print("Wrong! Try again.")
        elif guess == number:
            print("Congratulations! You guessed right!")
        break
    

        



        
            

            



