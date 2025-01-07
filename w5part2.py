#Write a program to print two strings in alphabetical order.
# Ask the user to enter y to repeat or n to quit.

def twoString():
    string1 = input("Please write your sentence:\n")
    string2 = input("Please write another sentence:\n")
    if string1>string2:
        print("Your sentences in an alpabetical order\n", string1,"\n", string2)
    else:
        print("Your sentences in an alpabetical order\n",string2,"\n", string1)
def loop():
    while True:
        twoString()
        anotherSentence=input("Do you want to input another sentence?(y/n)\n ")
        if anotherSentence != "y":
            print("Goodbye!")
            break
loop()