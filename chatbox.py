# Function to start the chatbot
def chatbot():

    # Display the Welcome message
    print("===== Basic Chatbot =====")
    print("Type 'bye' to exit.\n")

    # Keep the chatbot running,get input from the user & convert into lowercase.
    while True:
        message = input("You : ").lower()

        if message ==( "hello"):
            print("Bot : Hi! I'm here to help.")

        elif message == ("how are you"):
            print("Bot : I'm Fine. Thanks for asking!,How are you doing Today..?")

        elif message ==( "thank you"):
            print("Bot : You're welcome!")

        elif message == ("bye"):
            print("Bot : Goodbye! Have a nice day.")
            break

        # Handle any unknown input
        else:
            print("Bot : Sorry, I don't understand. Try saying 'hello'.")
# Call the Function to start the program
chatbot()