print("Hello! I'm your chatbot.")

# Collect the user's name and age
name = input("What's your name? ")
age = input("How old are you? ")

# Ask the user how it can help them
print(f"Nice to meet you, {name}! How can I help you today?")

while True:
  # Display the menu/list of options
  print("\nMenu:")
  print("1. option 1")
  print("2. option 2")
  print("3. option 3")
  print("4. Exit")

  # Allow the user to choose an option
  choice = input("Select an option (1-4): ")

  if choice == '1':
    print("You selected Option 1.")
  elif choice == '2':
    print("You selected Option 2.")
  elif choice == '3':
    print("You selected Option 3.")
  elif choice == '4':
    # Exit the conversation
    print("Goodbye! Have a great day.")
    break
  else:
    print("Invalid choice. Please select a valid option (1-4).")