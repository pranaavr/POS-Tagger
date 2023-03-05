'''
Programming Assignment 3 - POS Tagging
Class: CMSC416 Natural Language Processing
Author: Pranaav Rao
Date: 5/13/2022

This program will take as input a training file containing part of speech tagged text, and a file 
containing text to be part of speech tagged. Each word in the training data is recorded along with
its tag and how many times that tag occured. Each word in the test data is subsequently tagged based
on the training data. If the word exists in the training data, the word is tagged with the highest
occuring tag from the training data. If the word doesn't exist in the training data, it is tagged
with NN. The output is written into the designated output file

'''
from sys import argv
from sys import stdout
import re
import os.path

#get file names
trainfile = argv[1]
testfile = argv[2]

#open training file and convert to string
train = ''
with open(trainfile, encoding="utf8") as f:
    train += f.read().replace('\n', ' ')
#remove brackets
train = ''.join(train.split('['))
train = ''.join(train.split(']'))

# list of words and their tag
groups = train.split()

# for each word, its value is a dictionary with its tag and how many times that tag occurred
posdict = {}
for group in groups:
    groupList = group.split('/')
    word = groupList[0]
    tag = groupList[1]
    if word in posdict:
        if tag in posdict[word]:
            posdict[word][tag] += 1
        else:
            posdict[word][tag] = 1
    else:
        posdict[word] = {tag : 1}

#open test file and convert to string
test = ''
with open(testfile, encoding="utf8") as f:
    test += f.read().replace('\n', '')
#remove brackets
test = ''.join(test.split('['))
test = ''.join(test.split(']'))

testList = test.split(' ')

output = ''

for word in testList:
    if word in posdict:
        # assign the POS tag that maximizes P(tag|word)
        output += word+'/'+ max(posdict[word])+ ' '
    elif word.isalnum():
        if word[-1] == 's':
        #rule 1: if word ends with s, tag is NNS
            output += word+'/NNS '
        #rule 2: unknown is a number, tag is CD
        elif word.isdigit():
            output += word+'/CD '
        #rule 3: if word is there, tag is EX
        elif word == 'there':
            output += word+'/EX '
        #rule 4: if word ends w 'ed', tag is VBD
        elif len(word)>4 and word[-2] == 'ed':
            output += word+'/VBD '
        #rule 5: if unknown, tag is NN
        output += word+'/NN '    
    else:
        continue

#output to file
print(output)
