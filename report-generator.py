import os
import pyperclip

def collect_notes(item_name):
    print(f"Enter notes for {item_name} (type 'done' on a new line to finish):")
    notes = []
    while True:
        note = input()
        if note.lower() == 'done':
            break
        notes.append(f"- {note}")
    return "\n".join(notes)

def write_message_to_file():
    location = input("Enter the location you are in: ")
    sitenum = input("Enter the site number: ")
    date = input("Enter the date (e.g., MM/DD/YYYY): ")
    shift_time = input("Enter shift time (e.g., 00am - 00pm): ")

    num_items = int(input("Enter the number of items: "))
    item_data = []

    for i in range(num_items):
        item_name = input(f"Enter the name for item {i+1} (will be appended with 'ID'): ")
        item_name_with_ID = f"ID{item_name}"
        item_tasks = input(f"Enter the number of tasks for {item_name_with_ID}: ")
        item_notes = collect_notes(item_name_with_ID)
        item_data.append((item_name_with_ID, item_tasks, item_notes))

    content = f"{location} / Site {sitenum} || Date: {date} || Shift Time: ({shift_time})\nitems:\n"
    for item_name_with_ID, item_tasks, item_notes in item_data:
        content += f" {item_name_with_ID} - {item_tasks} Task(s) completed\n{item_notes}\n"

    #Change directory location to appropriate directory
    directory = os.path.expanduser("~/Documents")
    os.makedirs(directory, exist_ok=True)
    #Filetype is not generated automatically
    filename = input("Enter the filename (typically date_shift.txt): ")
    file_path = os.path.join(directory, filename)

    with open(file_path, "w") as file:
        file.write(content)

    with open(file_path, "r") as file:
        file_content = file.read()
        print("\nFile content:\n")
        print(file_content)

    print(f"\nReport written to {file_path}")
    pyperclip.copy(file_content)
    print("\nThe file content has been copied to the clipboard.")

write_message_to_file()
