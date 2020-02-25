greeting = {"How do you do?": "Fine",
                "What are you doing?": "Trying Python."
                }
def ask_user():
    ask_user = input("Ask me something ")
    while True:
        try:
            if greeting.get(ask_user) is None:
                print("I'll ask you something else")
            else:
                print(greeting[ask_user])
                break
        except KeyboardInterrupt:
            print("Bye-bye")
            break

ask_user()