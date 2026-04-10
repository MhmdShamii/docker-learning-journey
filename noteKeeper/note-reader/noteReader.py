import os

app_name = os.environ.get("APP_NAME", "DefaultName")
print(f"Welcome to {app_name}!")
print("=== Your Notes ===")

try:
    with open("/data/notes.txt", "r") as file:
        notes = file.readlines()
        for note in notes:
            print(note.strip())
except FileNotFoundError:
    print("No notes found.")