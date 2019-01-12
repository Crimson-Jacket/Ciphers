def letterFrequency(text):
    frequency = {}
    for x in "".join(text.split(" ")):
        try:
            frequency[x] += 1
        except:
            frequency[x] = 1
    while True:
        print("Display \n1. Alphabetically \n2. Most to Least \n3. Least to Most")
        choice = input("Option number: ")
        if choice == "1":
            for key in sorted(frequency.items(), key=lambda x: x[0]):
                print("{}: {} instances.".format(key[0], key[1]))
            break
        elif choice == "2":
            for key in sorted(frequency, reverse=True):
                print("{}: {} instances.".format(key, frequency[key]))
            break
        elif choice == "3":
            for key in sorted(frequency):
                print("{}: {} instances.".format(key, frequency[key]))
                break
        else:
            print("Please choose a valid option.")