import random
import os

# List of AI-generated writing prompts related to software engineering
prompts = [
    "Describe a challenging bug you encountered and how you fixed it.",
    "What is your favorite programming language and why?",
    "Discuss a project you're proud of and what you learned from it.",
    "How do you stay updated with new technologies?",
    "Write about a time when you had to learn a new framework quickly.",
]

# Define the file name for storing journal entries
journal_file = "journal.txt"
# Maximum number of entries
MAX_ENTRIES = 10

def display_menu():
    """Display the menu options to the user."""
    print("\nJournal Program for Software Engineers")
    print("1. Write a journal entry")
    print("2. Get a writing prompt")
    print("3. View past entries")
    print("4. Exit")

def get_user_choice():
    """Get the user's choice from the menu."""
    choice = input("Enter your choice (1, 2, 3, or 4): ")
    return choice

def load_entries():
    """Load journal entries from the file."""
    try:
        with open(journal_file, "r") as file:
            entries = file.readlines()
        return [entry.strip() for entry in entries]
    except OSError:
        return []

def write_journal_entry():
    """Allow the user to write a journal entry and save it to the flash memory."""
    entries = load_entries()
    entry = input("Write your journal entry (include tags if needed):\n")
    
    # Use circular buffering for wear leveling
    if len(entries) >= MAX_ENTRIES:
        # Remove the oldest entry
        entries.pop(0)
    entries.append(entry)
    
    # Write all entries back to the file
    with open(journal_file, "w") as file:
        for entry in entries:
            file.write(entry + "\n")
    print("Your entry has been saved!")

def get_prompt():
    """Generate and display a random writing prompt."""
    prompt = random.choice(prompts)
    print(f"Here's a writing prompt for you: {prompt}")

def view_entries():
    """Display past journal entries."""
    entries = load_entries()
    if entries:
        print("\nPast Journal Entries:")
        for i, entry in enumerate(entries, 1):
            print(f"{i}: {entry}")
    else:
        print("No entries found.")

def main():
    """Main function to run the journal program."""
    while True:
        display_menu()
        choice = get_user_choice()
        
        if choice == '1':
            write_journal_entry()
        elif choice == '2':
            get_prompt()
        elif choice == '3':
            view_entries()
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

# Run the main function to start the program
if __name__ == "__main__":
    main()
