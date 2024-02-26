import random
import time

    # Greeting message
print("Welcome to the PowerBall Number Generator!")

    # Ask the user if they want PowerBall numbers
user_input = input("Would you like some PowerBall numbers? (yes/no): ").lower()

if user_input == "yes":
        # Generate six random numbers for PowerBall
        white_ball_1 = random.randint(1, 69)
        white_ball_2 = random.randint(1, 69)
        white_ball_3 = random.randint(1, 69)
        white_ball_4 = random.randint(1, 69)
        white_ball_5 = random.randint(1, 69)
        red_ball = random.randint(1, 26)

        # Display the PowerBall numbers with proper spacing
        powerball_numbers = f"{white_ball_1}  {white_ball_2}  {white_ball_3}  {white_ball_4}  {white_ball_5}    {red_ball}"
        print("\nHere are your PowerBall numbers:")
        time.sleep(2)
        print(powerball_numbers)

        # Farewell message
        print("Good luck with your PowerBall ticket! Have a great day!")

elif user_input == "no":
        # Farewell message if the user doesn't want PowerBall numbers
        print("Maybe next time! Have a great day!")

else:
        # Handle invalid input
        print("Invalid input. Please enter 'yes' or 'no'.")