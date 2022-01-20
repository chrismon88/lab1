#creating empty list to store class inputs
classes = []

#ask user for class name until no other classes are entered in while loop
while True:
    print("Enter thes classes you are taking this semester, or don't enter anything to stop program.")
    className = input()
    if className == '':
        break
    classes = classes + [className]
    print("The classes you are taking this semester are:")
    for className in classes:
        print("" + className)