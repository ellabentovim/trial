from menu import show_menu
from utils import show_users,ask_name

def main():
    print("welcome to the program!")
    ask_name()
    while(True):
        show_menu()
        choice = int(input("Enter your choice: "))
        if choice == 1:
            show_users()
        elif choice == 2:
            print("exiting the program. Goodbye!")
            return
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()


