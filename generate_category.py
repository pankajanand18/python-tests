__author__ = 'pankaj'

import csv
import json

file_path = '/home/pankaj/Documents/STS_Final_Categories-v1.csv'
def toTitleWord(words):
    words_array=words.split(' ')
    new_array=[]
    for word in words_array:
        word=word.title()
        new_array.append(word)
    return " ".join(new_array)

def chopArray(array):
    new_array=[]
    for item in array:
        item=item.strip()
        item=toTitleWord(item)
        new_array.append(item)
    return  new_array

def getSortedArray(array):
    list=chopArray(array.split(','))
    list.sort()
    return list

def generateJson(filepath):
    with open(filepath, "rb") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        count = 0
        sts_categories = []
        subcategories = {}
        brands = {}
        keywords = {}

        for row in csvreader:
            if count < 2:
                count = count + 1
                continue
            category = row[0]
            sts_categories.append(category)
            if len(row[2]) > 0:
                subcategories.update({category: getSortedArray(row[2])})
            if len(row[3]) > 3:
                brands.update({category: getSortedArray(row[3])})
            if len(row[4]) > 0:
                keywords.update({category: getSortedArray(row[4])})
                #print row


        # print sts_categories
        # print subcategories
        # print brands
        # print keywords
        final_json={}
        final_json.update({'categories':sts_categories})
        final_json.update({'subCategories':subcategories})
        final_json.update({'brands':brands})
        final_json.update({'keywords':keywords})
        print json.dumps(final_json)


generateJson(file_path)
#print getSortedArray("pankaj,anand,Karol,Bagh")

