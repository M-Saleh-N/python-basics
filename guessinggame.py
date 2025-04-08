import random

secret_number = random.randint(1, 20)
attempts = 5

print("🎮 Welcome to 'Guessing the Number'!")
print("🤔 I'm thinking of a number between 1 and 20.")
print(f"📝 You have {attempts} to guess it correctly! \n")

while attempts > 0:
    guess = int(input("Enter your guess: "))
    if guess == secret_number:
        print(f"🎉 Congratulations! You guessed the number correctly")
        break
    elif guess < secret_number:
        print("🤔 Your guess is too low. Try again!")
    else:
        print("🤔 Your guess is too high. Try again!")

        attempts -=1
        print(f"😔 Attempts left:  {attempts}\n")

        if attempts == 0:
            print(f"😔 Game over! The number was {secret_number}. Better luck next time!")
