import pyjokes

def tellJokes():
    print(f"\n\n{pyjokes.get_joke()}\n\n")

while True:
    print("==========Welcome to the Programmer's Hub==========")
    print("""
        What do you want?
        1.) Completely Random Programming Jokes
        2.) Help With your code
        3.) Nothing but want to exit
    """)
    choice = input()
    if choice == '1':
        tellJokes()
    elif choice == '2':
        print("DEVELOPER PARADISE -> https://stackoverflow.com/")
    elif choice == '3':
        print("Have a nice day banging your heads into editors and terminals")
        quit()
    else:
        print("Invalid choice!")
