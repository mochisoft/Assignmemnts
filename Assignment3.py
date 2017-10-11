import operator
import random
import numpy as np
import matplotlib
from matplotlib import pyplot as plt


#Get Number of words
#Count frequency of each word
#Plot a histogram of top frequencies
def Assignment3(strURL,word_limit):
    count=0
    data = open(strURL, 'r')
    text=data.read()
    strWord=text.split()
    count +=len(strWord)
    print "Total Number of Words: %s" % (count)

    max_word_list, word_count_list=genSortedDict(prepareWords(strWord))

    generateChart(max_word_list[:word_limit], [i+1 for i in range(len(max_word_list))][:word_limit], word_count_list[:word_limit])

def prepareWords(strWord):

    unq_word_list=[]
    word_dict={}

    #Generate Unique words
    for x in strWord:
        if x.lower() in unq_word_list:
            continue
        else:
            unq_word_list.append(x.lower())

    print unq_word_list

    #Calculate word counts
    for x in unq_word_list:
        count=0
        for y in strWord:
            if x==y.lower():
                count+=1
        word_dict.update({x:count})

    return word_dict

def genSortedDict(word_dict):

    sorted_x = sorted(word_dict.items(), key=operator.itemgetter(1),reverse=True)
    max_word_list=[x for x,y in sorted_x]
    word_count_list=[y for x,y in sorted_x]
    word_index=[i+1 for i in range(len(max_word_list))]


    return max_word_list, word_count_list

def generateChart(strWord,wordIdx,wordCount):

    #Generating histogram
    #histogram = plt.figure()
    #plt.hist(y, bins, alpha=0.5)
    plt.title('Word Usage Frequency')
    plt.xlabel("Word")
    plt.ylabel("number of Occurence")

    plt.bar(range(len(strWord)), wordCount,width=0.5)
    plt.xticks([i for i in range(len(strWord))], strWord)

    plt.show()

if __name__=="__main__":

    Assignment3("link to text file",20)
    print "------THE END-----------"
