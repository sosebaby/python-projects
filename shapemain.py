import shape2d
def main():
    shape = shape2d.Shape2D(10, 15)
    print("The shape has the follwing dimension:")
    shape.setLength(25)
    print("New area:", shape.getArea())
    print(shape)
if __name__ == "__main__":
    main()