'''
Utility program
Takes as input the POS tagged test data from tagger.py and the gold standard
data from pos-test-key.txt. It prints the overall accuracy of my tagging and 
writes a confusion matrix to the designated output file

The base accuracy without rules is 57.149%
'''
from sys import argv
from sys import stdout
#import pandas as pd

testfile = argv[1]
keyfile = argv[2]

test = ''
with open(testfile, "rb") as f:
    content = f.read()
    test = content.decode("utf-16")

testList = test.split()

#list of tags predicted
testTags = []
for phrase in testList:
     phraseList = phrase.split('/')
     testTags.append(phraseList[1])

#dictionary with tag as key and count of tag as value
test_freq = {}
for tag in testTags:
    if tag in test_freq:
        test_freq[tag]+=1
    else:
        test_freq[tag] = 1


key = ''
with open(keyfile, "r") as f:
    key += f.read()
#remove brackets
key = ''.join(key.split('['))
key = ''.join(key.split(']'))

keyList = key.split()
keyTags = []
for phrase in keyList:
    phraseList = phrase.split('/')
    keyTags.append(phraseList[1])

key_freq = {}
for tag in keyTags:
    if tag in key_freq:
        key_freq[tag]+=1
    else:
        key_freq[tag] = 1

#determine accuracy
accuracies = []
for tag in key_freq:
    if tag not in test_freq:
        continue
    if test_freq[tag] > key_freq[tag]:
        acc = key_freq[tag]/test_freq[tag]
    elif test_freq[tag] < key_freq[tag]:
        acc = test_freq[tag]/key_freq[tag]
    accuracies.append(acc)
accuracy = sum(accuracies)/len(accuracies) * 100
print("Accuracy is: "+str(accuracy))

#confusion matrix - doesn't work
# confusion_matrix = pd.crosstab(keyTags, testTags, rownames=['Actual'], colnames=['Predicted'])
# print (confusion_matrix)
