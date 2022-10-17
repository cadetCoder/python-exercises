print("A standard sized egg box holds 6 eggs")

numeggs=int(input("How many eggs do you need to pack?:\t"))

if numeggs<1:
    print("Please enter the value of 1 or more")
    
else:
    spaces = 0
    boxes = int(numeggs/6)
    remainder = numeggs % 6

    if remainder>0:
        boxes=boxes+1
        spaces=6-remainder

    if boxes==1:
        b=str("box")
    else:
        b=str("boxes")

    print("You will need",boxes, b)
    
    if spaces!=0:
        print("The last boxes will have", spaces,"empty spaces")
