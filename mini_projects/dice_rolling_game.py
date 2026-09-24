import random

print()
print("---------Random Number Generator----------")
print()

while True:
    
    choose = input("Roll the dice? (y/n): ")

    if choose == 'y' or choose == 'Y':
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)

        print(f"Generated Numbers:{dice_1},{dice_2}")
        total = dice_1 + dice_2
        print(f"Total:{total}")

        if total%2==0:
            print("even")
        else:
            print("odd")

    elif choose == 'n' or choose == 'N':

        print("Thanks for Playing")
        break

      
    else:

        print("Invalid choice")
  




