time = input("What time should I get out of bed? 5 or 10? ")


if(time == "5"):
    print("time to go to the bathroom")
elif(time == "10"):
    print("time to go to the kitchen")

bathroom = input("Brush teeth or bath?" )
if(bathroom == "Brush teeth"):
    print("minty fresh! time to go to the kitchen")
elif(bathroom == "bath"):
    print("I'm clean now, time to go to the kitchen!")

kitchen = input("fruit or muffin?" )
if( kitchen == "muffin"):
    print("yummmmmm")
elif(kitchen == "fruit"):
    print("yummm")

clothes = input("what type of sunglasses should I put on, hearts or stars?")
if(clothes == "hearts" or "stars"):
    print("time to go to school")
