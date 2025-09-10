from utils import show_users, ask_name

def main():
    ask_name()
    show_users()

if __name__ == '__main__':
    main()

def ask_name():
    name = input("what is your name? ")
    print(f"nice to meet you, {name}!")

def show_users():
    try:
        with open("users.txt", "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]
            print("\nregistered users:")
            for line in lines:
                print("-", line)

    except FileNotFoundError:
        print("User file not found.")
