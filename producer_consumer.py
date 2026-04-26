buffer = 0
max_size = 5

while True:
    print("\n1. Produce\n2. Consume\n3. Exit")
    choice = int(input())

    if choice == 1:
        if buffer == max_size:
            print("Buffer Full!")
        else:
            buffer += 1
            print(f"Produced, Buffer = {buffer}")

    elif choice == 2:
        if buffer == 0:
            print("Buffer Empty!")
        else:
            buffer -= 1
            print(f"Consumed, Buffer = {buffer}")

    else:
        break