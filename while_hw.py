greeting = {"How do you do?": "I'm fine, thanks.",
                "What are you doing?": "Trying Python."
                }
def ask_user():
    while True:
        ask_user = input("Ask me something ")
        if greeting.get(ask_user) != None:
            print(greeting[ask_user])
            break
        else:
            print("I'll ask you something else")

ask_user()