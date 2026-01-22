from Hasan.age_calculator import run_age_calculator
from mark.greeting import greet_user
from rubeen.favorite_color import ask_color
from Peter.lucky_number import zodiac_main

def main():
    print("\n===== TEAM APPLICATION =====")
    print("1. Calculate Age (Hasan)")
    print("2. Greeting (Mark)")
    print("3. Favorite Color (Rubeen)")
    print("4. Lucky Number (Peter)")
    print("5. Exit")
    print("============================")

choice = input("Select option (1-5): ")

if choice == "1":
    run_age_calculator()
elif choice == "2":
    greet_user()
elif choice == "3":
    ask_color()
elif choice == "4":
    zodiac_main()
elif choice == "5":
    print("Goodbye!")
else:
    print("Invalid option.")

if __name__ == "main":
    main()