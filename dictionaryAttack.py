
#Opens a file. You can now look at each line in the file individually with a statement like "for line in f:
f = open("dictionary.txt","r")
file = f.readlines()
f.close()

print("Can your password survive a dictionary attack?")

#Take input from the keyboard, storing in the variable test_password
#NOTE - You will have to use .strip() to strip whitespace and newlines from the file and passwords
test_password = input("Type in a trial password: ")

#Write logic to see if the password is in the dictionary file below here:
if test_password.casefold() in open("dictionary.txt").read():
    print("Choose a better password!")
else:
    print("That's a good password!")

for x in file:
    if x in test_password:
        print("Choose another password!")
    else:
        print("That's a good password!")
