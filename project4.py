while 1:
    a = input()
    b = input()
    for letter in a:
        c = letter.lower()
        if c in "а,е,о,э,я,и,ы,ё,у,ю":
            print(letter, end="")
            print(b, end="")
            print(c, end="")
        else:
            print(letter,end="")
    print("\n")

