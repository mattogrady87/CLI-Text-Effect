import time
from random import uniform
from os import get_terminal_size
def cooltextinator(c):
    """
    This will make all your text dreams come true!
    """
    #c = input("Type something to have is put in cooler!: ") 
    b = ""
    ts = get_terminal_size()

    #Using carriage return with more than one line will break the intended output:
    #Thats why we use get_terminal_size to limit the input.
    #My GF broke it the first time she tried it lol :(

    for letter in c:
        if len(b) < ts.columns:
            b += letter
            continue
        else:
            print("We had to cut it short, we only go as wide as your screen!")
            break


    answer = input("Do you want 13375p34|< y or n?: ")
    if answer == "y":
        leetVar = True
    else:
        leetVar = False

    cstr = ""
    astr=""
    bstr=""
    #Those commas look like that because I used vim visual-block and thats what
    #happened
    leet = { "a" : "4",
             "b" : "B",
             "c" : "(",
             "e" : "€",
             "f" : "ƒ",
             "g" : "9",
             "i" : "1"   ,
             "l" : "£"   ,
             "o" : "0"   ,
             "p" : "¶"   ,
             "q" : "q"   ,
             "r" : "®"   ,
             "s" : "$"   ,
             "t" : "┱",
             "u" : "µ"   ,
             "y" : "¥"   ,
             }

    while 1:

        for x in (range(0, len(b))):

            #if you comment out this line you get a very different but cool
            #effect when using the 'y' leetspeak option
            print(b, end="\r")

            cstr = b[x].upper()

            astr = b[0:x]

            print(astr+cstr, end="\r")

            if cstr.isalpha():
                time.sleep(uniform(0.2,0.3))

        #reversed is a cool function!
        for x in reversed((range(0, len(b)))):

            astr = b[0:x]

            if leetVar:
                cstr = b[x].lower()
                for char in cstr:
                    if char in leet:
                        cstr = leet[char]
                print(astr+cstr, end="\r")

                #skip the spaces, we use b[x] not cstr because cstr is leet
                #chars now, not alphabet chars
                if b[x].isalpha():
                    time.sleep(uniform(0.2, 0.3))

            else:

                #Allows string to go back to lowercase each iteration
                print(b, end="\r")

                cstr = b[x].upper()
                #Stop it from pausing on spaces and punctuation:
                if cstr.isalpha():
                    print(astr+cstr, end="\r")
                    time.sleep(uniform(0.2,0.3))
                elif cstr.isnumeric():
                    cstr = "0"
                    print(astr+cstr, end="\r")
                    time.sleep(uniform(0.2,0.3))
                else:
                    print(astr+cstr, end="\r")

if __name__ == '__main__':
    c = input("Type something to get changed up: ")
    cooltextinator(c)

