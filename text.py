import os

print("Type 'exit' to quit the coversation")
while True:
    user = input("user: ").strip().lower()  # Normalize input

    if user == "hi":
        print("setoits AI: Hello  How can I help you?")
    elif user == "weather":
        print("setoits AI: According to your location...")
        os.system("start chrome https://www.theweathernetwork.com/en/city/in/maharashtra/aundh/current")
    elif user == "news":
        print("setoits AI: Here are the latest news.....")
        os.system("start chrome https://www.bbc.com/news")
    elif user == "tell me joke" :
        print("setoits AI: What's the smartest insect? A spelling bee!")
 
       
    elif user == "exit":
        print("setoits AI: Goodbye!")
        break
    else:
        print("setoits AI: Sorry, I didn't understand that.")