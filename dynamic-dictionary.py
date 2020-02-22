definition = {}

while True:
    print("1: Add a definition",
          "2: Find a definition",
          "3: Delete the definition",
          "4: Finish the program")

    choice = input("What do you want to do? ")

    if choice == "1":
        key = input("Give the word to add: ")
        explanation = input("Give a definition of this word: ")
        definition[key] = explanation
        print("The definition has been successfully added")

    elif choice == "2":
        key = input("What are you looking for? ")
        if key in definition:
            print("The definition already exists:", definition[key])
        else:
            print("Name definition not found:", key)

    elif choice == "3":
        key = input("What definition do you want to delete? ")
        if key in definition:
            del definition[key]
            print("The definition", key, "is deleted")
        else:
            print("Name definition not found:", key)

    elif choice == "4":
        finish = input("Do you want to finish the program ? [y/n] ")
        if finish == "y":
            break
        else:
            continue

    else:
        print("You didn't choose a function from the range !")






