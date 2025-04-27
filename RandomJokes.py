import requests
import random

def get_joke():
    try:
        response = requests.get("https://official-joke-api.appspot.com/jokes/random")
        data = response.json()
        print("\n Joke:")
        print(data['setup'])
        print(data['punchline'])
    except:
        print("Error fetching joke.")

def main():
    while True:
        print("\n=== Random Jokes ===")
        print("1. Get a joke")
        print("2. Exit")
        choice = input("Enter your choice (1/2): ")

        if choice == '1':
            get_joke()
        elif choice == '2':
            print("Bye! Have a nice day")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
