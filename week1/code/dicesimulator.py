import random

def get_user_input():
    try:
        num = int(input("How many dice do you want to roll? [1-6] "))
        if 1 <= num <= 6:
            return num
        else:
            print("Please enter a number between 1 and 6.")
            exit()
    except ValueError:
        print("Invalid input. Please enter a number.")
        exit()
def roll_dice(n):
    results = []
    for _ in range(n):
        results.append(random.randint(1, 6))
    return results
def display_results(results):
    print("\nRolling the dice...")
    for i, value in enumerate(results, 1):
        print(f"Die {i}: {value}")
def main():
    num_dice = get_user_input()
    results = roll_dice(num_dice)
    display_results(results)
main()