import os

if not os.path.exists("/data"):
    os.makedirs("/data")

try:
    with open("/data/count.txt", "r") as file:
        content = file.read()

    if content.strip() == "":
        count = 0
    else:
        count = int(content.strip())
    count += 1

    with open("/data/count.txt", "w") as file:    
        file.write(str(count))

    print(f"Count: {count}")

except FileNotFoundError:
    with open("/data/count.txt", "w") as file:
        file.write("1")
    print("Count: 1")