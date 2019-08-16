import json
import matplotlib.pyplot as plt
from textblob import TextBlob

import textblob as tb

#pull tweet data out of json file
tweetFile = open("tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

polarity = []
subjectivity = []

for tweet in tweetData:
    tweetTB = TextBlob(tweet["text"])
    polarity.append(tweetTB.polarity)
    subjectivity.append(tweetTB.subjectivity)

polaverage = sum(polarity)/len(polarity)
subaverage = sum(subjectivity)/len(subjectivity)

print(polaverage)
print(subaverage)

plt.hist(polarity, bins = [-1, 0, 1], color = "pink")
plt.title("Polarity Historgram")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()

plt.hist(subjectivity, bins = [-1, 0, 1], color = "blue")
plt.title("Subjectivity Histogram")
plt.show()
