# from langchain_ollama import ChatOllama
# from langchain_core.messages import (AIMessage, HumanMessage, SystemMessage)
# from dotenv import load_dotenv
# import os
# load_dotenv()

# api_key = os.getenv("")


# client = ChatOllama(
#    model="deepseek-v3.1:671b",
#     base_url="https://ollama.com",
#     api_key="de7b94d28aee4ab1af4acc608111310c.3vdp0F6SswPB42NqUWtP7CXI"
# )


# chat_history = []

# system_message = SystemMessage(content="You are a helpful AI Assistant.")
# chat_history.append(system_message)

# while True:
#     user_input = input("You: ")
#     if user_input.lower() in ["exit", "quit"]:
#         print("Exiting the chat. Goodbye!")
#         break

#     human_message = HumanMessage(content=user_input)
#     chat_history.append(human_message)

#     response = client.invoke(chat_history)
#     ai_message = AIMessage(content=response.content)
#     chat_history.append(ai_message)

#     print(f"AI: {response.content}\n")

















#     import json
# import os

print("🏦 Welcome to ABDU-RAFEEQ Banking System 😇🤝")
print("————————————————————————————————————————————")

# File to store user data
DATA_FILE = "accounts.json"

# Load existing data
if window.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        accounts = json.load(f)
else:
    accounts = {}

# Ask for user name
username = input("Please enter your name: ").strip().title()

# Initialize balance if user is new
if username not in accounts:
    accounts[username] = {"balance": 0}

def save_data():
    with open(DATA_FILE, "w") as f:
        json.dump(accounts, f, indent=4)

while True:
    print("\nMenu:")("1️⃣  Deposit")
    print("2️⃣  Withdraw")
    print("3️⃣  Check Balance")
    print("4️⃣  View All Savings")
    print("5️⃣  Exit")

    choice = input("Please enter your choice (1-5): ")

    # Deposit
    if choice == "1":
        amount = float(input("Enter amount to deposit: "))
        if amount <= 0:
            print("❌ Invalid amount! Please enter a positive number.")
        else:
            accounts[username]["balance"] += amount
            save_data()
            print(f"✅ You deposited ₦{amount:.2f}. New balance: ₦{accounts[username]['balance']:.2f}")

    # Withdraw
    elif choice == "2":
        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("❌ Invalid amount! Please enter a positive number.")
        elif amount > accounts[username]["balance"]:
            print("❌ Insufficient funds!")
        else:
            accounts[username]["balance"] -= amount
            save_data()
            print(f"✅ You withdrew ₦{amount:.2f}. Remaining balance: ₦{accounts[username]['balance']:.2f}")

    # Check balance
    elif choice == "3":
        print(f"💰 {username}, your current balance is ₦{accounts[username]['balance']:.2f}")

    # View all users’ balances
    elif choice == "4":
        print("\n📊 All Savings Info:")
        for user, data in accounts.items():
            print(f"👤 {user}: ₦{data['balance']:.2f}")

    # Exit
    elif choice == "5":
        print("👋🏽 Thank you for using ABDU-RAFEEQ Banking System! Goodbye.")
        break

    else:
        print("⚠️ Invalid choice, please try again.")
