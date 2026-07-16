from random import randint

winning_number = randint(1, 10)

lives = 5

print("Welcome to the Number Guessing Game!")
print("When you start the game, you have:", "❤️" * lives)
print("If you run out of ❤️, you lose the game.")

while True:
    try:
        prediction = int(input("Enter a number from 1 to 10: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if prediction < 1 or prediction > 10:
        print("Choose a number between 1 and 10.")
        continue

    if prediction == winning_number:
        print("🎉 Congratulations! You guessed it!")
        break

    difference = abs(winning_number - prediction)

    if difference == 1:
        print("🔥 Burning!!!!")
    elif difference == 2:
        print("🥵 Hot!")
    elif difference == 3:
        print("🙂 Warm!")
    else:
        print("🥶 Freezing!!!!")

    lives -=  1

    print("Lives left: ", "❤️" * lives)

    if lives == 0:
        print(f"You lose! The number was {winning_number}")
        break
