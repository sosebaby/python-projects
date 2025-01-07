
days = int(input("Enter the number of days you walked: "))
def calculateTotalSteps():
    totalSteps = 0
    for day in range(1, days + 1):
        steps1 = int(input(f"Enter steps for day {day}: "))
        totalSteps += steps1
    print(f"Total steps in {days} days: {totalSteps}")
calculateTotalSteps()

goal= int(input("Please what is your step goal: "))
steps=int(input("How many steps did you acheive: "))
def checkSteps(steps, goal):
    if steps>=goal:
        print("Goal met!") 
    else:
        print("Goal not met")
checkSteps(steps,goal)

print("Drinking water is an important step in staying healthy, set a reminder for drinking water!")
def waterReminder():
    reminders = int(input("Enter the number of reminders to drink water needed: "))
    while reminders > 0:
        print(f"Drink water!\n{reminders} reminder(s) left.")
        reminders -= 1
waterReminder()