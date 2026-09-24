secret_num = 7

while True:
    try:
        guess_num = int(input("Guess the Number between 1 and 100: "))

        if guess_num != secret_num:

            if secret_num <= guess_num:
                print("Too high")

            else:
                print("Too low")

        else:
            print("Congratulations! You Guessed the Number")
            break

    except ValueError:
           print("Please enter a Vaild number!")