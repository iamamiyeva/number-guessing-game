import random

random_number = random.randint(1,100)
attempt = 10
score = 100
attempt_count = 0

print("Please guess number between 1-100!")
print(f"Your initial score is {score}.")


while attempt>0:
    guess = int(input("Your guess: "))
    if guess<1 or guess>100:
        print("Please enter numbers between 1-100!!!")
        continue
    attempt_count+=1
    attempt-=1
    if (guess!=random_number):
        score-=10
        if (guess>random_number):
            print(f"Try a smaller number than {guess}!")
        elif(guess<random_number):
            print(f"Try a larger number than {guess}!")
        print(f"Remaining attempts - {attempt}.\n")
    elif (guess==random_number):
        print(f"\nThe answer is {random_number}.\nYou guessed in {attempt_count}th attempt!!!\nYour score is {score}.\n")
        break
if (attempt==0):
    print("You couldn't guess!!!")