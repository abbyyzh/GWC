# --- Define your functions below! ---
from random import *
def welcome():
    print("Hello, welcome to chatbox")
    user = input("What is your name? ")
    print("Nice to meet you " + user)
def isvalid(userinput, thelist):
    if userinput in thelist:
        print("True")
        return
    else:
        print("False")
        return
def mathvalid(userguess, possibleanswers):
    if userguess in possibleanswers:
        print("True")
        return
    else:
        print("False")
        return
def breakfast(food):
    print("I also like to eat " + food)
def travel(place):
    print("I just came back from " + place + "!, it was very fun")
def joke():
    input("What do you call a train carrying bubblegum?")
    print("a chew-chew train! hahaHAHAHhahaHahaha")
# --- Put your main program below! ---
def main():
    welcome()
    useranswer = input("What day is it today? ")
    possibledays = ["thursday", "Thursday", "July 11", "July 11, 2019" "7/11", "july 11", "july 11, 2019", "7/11/19"]
    isvalid(useranswer, possibledays)
    useranswer = input("What is 5 + 5? ")
    correctanswers = ["10", "ten", "TEN"]
    mathvalid(useranswer, correctanswers)
    favorite = input("What did you eat for breakfast today? ")
    breakfast(favorite)
    favplace = input("Where is your favorite place to travel to? ")
    travel(favplace)
    joke()


# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
