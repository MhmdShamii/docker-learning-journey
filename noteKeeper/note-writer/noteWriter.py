import os

app_name = os.environ.get("APP_NAME", "DefaultName")
print(f"Welcome to {app_name}!")

with open("/data/notes.txt", "a") as file:
    input_note = input("Enter your note (or 'exit' to quit): ")
    while input_note != "exit":
        file.write(input_note + "\n")
        file.flush()
        print("Note saved to notes.txt")   
        input_note = input("Enter your note (or 'exit' to quit): ")
        
