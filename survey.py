import json
survey = {}

masterlist = []

p = open("surveyanswers.json", "w")

while True: 

    survey = {}
    nameanswer = input("What is your name? ")
    coloranswer = input("What is your favorie color? ")
    foodanswer = input("What is your favorite food? ")
    animalanswer = input("What is your favorite animal? ")
    ageanswer = input("How old are you? ")
    sportsanswer = input("What is your favorite sport? ")

    survey["What is your name? "] = nameanswer
    survey["What is your favorite color? "] = coloranswer
    survey["What is your favorite food? "] = foodanswer
    survey["What is your favorite animal? "] = animalanswer
    survey["How old are you? "] = ageanswer
    survey["What is your favorite sport? "] = sportsanswer
    
    masterlist.append(survey)

    dictionaryToJson = json.dumps(survey)
    json.dump(dictionaryToJson,p)
    print(dictionaryToJson)

    answer = input("Is there another person? ")
    if answer == "no"  or answer == "No" :
        break

print(masterlist)
p.close()




  





 

