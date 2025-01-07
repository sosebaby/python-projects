def greetChina(name):
    print("Ni hao! ", name)
def greetFrance(name):
    print("Bonjour! ", name)
def greetIndia(name):
    print("Namaste! ",name)
def greetSpain(name):
    print("Hola!", name)
def quitProgram():
    print("Successfully exited")
def error():
    print("Error, please input a valid answer")
print("Select a country:\n 1.China\n 2.France\n 3.India\n 4.Spain\n 5.Quit\n")
name = input("Type in your name: ")
def main():
    while True:
        choice=int(input("Your choice: "))
        if choice==1:
            greetChina(name)

        elif choice==2:
            greetFrance(name)

        elif choice==3:
            greetIndia(name)

        elif choice==4:
            greetSpain(name)

        elif choice==5:
            quitProgram()
            break
        else:
            error()
main()

def areaOfRectangle():
    length=int(input("Enter the length of the rectangle: "))
    breadth=int(input("Enter the breadth of the rectangle: "))
    theAreaOfRectangle=float( length*breadth)
    print("The area of the rectangle is" ,theAreaOfRectangle)
def areaOfSquare():
    side=int(input("Enter the value of the side of the square: "))
    theAreaOfSquare=float( side*side)
    print("The area of the square is" ,theAreaOfSquare)
def areaOfTriangle():
    base=int(input("Enter the value of the base: "))
    height=int(input("Enter the value of the height: "))
    theAreaOfTriangle=float(0.5*base*height)
    print("The area of the triangle is ",theAreaOfTriangle)
def areaOfCircle():
    radius=int(input("Enter the value of the radius: "))
    theAreaOfCircle=float(3.14*radius*radius)
    print("The area of a circle is: ", theAreaOfCircle)
def notAvailable():
    print("Sorry! We cannot find this shape.")
print("Calculate the area of:\na)Rectangle\nb)Square\nc)Triangle\nd)Circle")
def main():
    choice = input("Pick from the list a shape you want to find the area of: ")
    if choice=="a":
        areaOfRectangle()
    elif choice=="b":
        areaOfSquare()
    elif choice=="c":
        areaOfTriangle()
    elif choice=="d":
        areaOfCircle()
    else:
        notAvailable()
main()















