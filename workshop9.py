import random
f = open("integers.txt", 'w')
for count in range(10):
    number = random.randint(1, 100)
    f.write(str(number) + "\n")
f.close()
with open("integers.txt", "r") as x:
    num = [int(line.strip())for line in x]
    average = sum(num) / len(num)
with open("result.txt", "w") as i:
    i.write(f"The average is {average}")
f = open("mywords.txt", "w")
for i in range(5):
    listofwords = input(f"Enter word {1+i}: ")
    f.write(listofwords + "\n")
f.close()
f = open("mywords.txt", "r")
newtxt = f.read()
numwords = len(newtxt.split())
print(f"There are {numwords} in this file")
    
