# Pico-Journal-App
Journal
Explanation of the Code:

1. Prompts List:
• Contains writing prompts relevant to software engineering.
2. Load Entries:
• The load_entries() function reads journal entries from the file and returns them as a list. It handles the case where the file may not exist.
3. Write Journal Entry:
• The write_journal_entry() function allows the user to input an entry. It checks the number of entries and implements a circular buffer mechanism:
• If the maximum number of entries (MAX_ENTRIES) is reached, it removes the oldest entry.
• It then appends the new entry and rewrites all entries back to the file.
4. View Entries:
• The view_entries() function displays all the journal entries loaded from the file.
5. Main Function:
• The main() function provides the menu interface for the user to interact with the journal program.

Wear Leveling Approach:

• Circular Buffer: By limiting the number of entries stored (in this case, 10), the program reduces write cycles on the same locations in the flash memory. When the limit is reached, it overwrites the oldest entry, helping distribute writes over time.

Usage:

• Upload this script to your Raspberry Pi Pico and run it. Follow the menu prompts to write entries, receive prompts, or view past entries. All entries will be saved in journal.txt in the flash memory of the Pico.
