#This method is used to print @ in format
def for_range_example(width,height):
    print("*"*width)
    """print a box made up of asterisks.

    width: width of box in characters, must be at least 2
    height: height of box in lines, must be at least 2
    """


    # print sides of box
    for _ in range(height-2):
        print("*" + " " * (width-2) + "*")


    print("*" * width)



for_range_example(4,7)
