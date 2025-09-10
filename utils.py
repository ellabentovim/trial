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
