from sre_parse import isident

__author__ = 'pankaj'

import csv
import json

file_path = '/home/pankaj/Documents/Latest_Categories-10.csv'
def toTitleWord(words):
    words_array=words.split(' ')
    new_array=[word.title() for word in words_array]

    # for word in words_array:
    #     word=word.title()
    #     new_array.append(word)
    return " ".join(new_array)

def chopArray(array,titleCase):
    new_array=[]
    if titleCase:
        new_array = [item.strip() for item in array]
    else:
        new_array = [ toTitleWord(item.strip()) for item in array]


    # for item in array:
    #     item=item.strip()
    #     if(titleCase):
    #         item=toTitleWord(item)
    #     new_array.append(item)
    return  new_array

def getSortedArray(array,titlecase=True,sortdata=True):
    data=array
    if type(array) is list:
        data=array
    else:
        data=chopArray(array.split(','),titlecase)
    if(sortdata):
        data.sort()
    return data

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
            if len(row[1]) > 0:
                subcategories.update({category: getSortedArray(row[1].strip(),False)})
            # if len(row[3]) > 3:
            #     brands.update({category: getSortedArray(row[3],False)})
            if len(row[2]) > 0:
                keywords.update({category: getSortedArray(row[2],False,False)})
                #print row


        # print sts_categories
        # print subcategories
        # print brands
        # print keywords
        final_json={}
        sts_categories=getSortedArray(sts_categories)

        final_json.update({'categories':sts_categories})
        final_json.update({'subCategories':subcategories})
        final_json.update({'brands':brands})
        final_json.update({'keywords':keywords})
        print json.dumps(final_json,sort_keys=True,indent=4,separators=(',', ': '))



generateJson(file_path)
#print getSortedArray("pankaj,anand,Karol,Bagh")

