# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 21:02:45 2019

@author: evrozm
"""

import numpy as np
directoryOfElement = r'C:/Users/evrozm/Desktop/'

with open("{}primeNumbers.txt".format(directoryOfElement), "r") as txtfile:
    txtString = txtfile.read()
    txtfile.close()

txtSplitString1 = txtString.split()

primeNumbers = np.asarray(txtSplitString1).astype(int)

primeNumbers = sorted(primeNumbers)

letters = np.array(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"])

myDict = {letters[cnt]:primeNumbers[cnt] for cnt in range(len(letters))}

def word2Prime(word1,myDict):
    base1 = np.int64(1)
    #print(type(base1))
    baseList = []
    cnt = 0
    for letter in word1:
        if cnt == 0:
            baseList.append(myDict[letter])
        elif cnt == len(word1)-1:
            baseList.append(myDict[letter])
        else:
            #print(letter,myDict[letter])
            base1 = base1*myDict[letter]
        cnt = cnt+1
    baseList.append(base1)
    return baseList

def all2lowercase(word):
    for letter in word:
        asciiLetter = ord(letter)
        if asciiLetter>64 and asciiLetter<91:
            asciiLetter = asciiLetter+32
            word = word.replace(letter,chr(asciiLetter))
    return word

def findFactors(x,pnl):
   # This function takes a number and prints the factors
   factors = []
   for i in pnl:
       if x % i == 0 and i<102:
           factors.append(i)
   return factors

def measureSimilary(word1,word2,pnl):
    #print(word1,word2)
    fact1 = findFactors(word1[2],pnl)
    mv = 0
    if word1[0] == word2[0]:
        mv = mv + 0.25
        #print("1",mv)
    #print("22222",word1[1],word2[1])
    if word1[1] == word2[1]:
        mv = mv + 0.25
        #print("2",mv)
    fact2 = findFactors(word2[2],pnl)
    foundFacts = []
    for fact in fact2:
        #print(word1,fact)
        if word1[2]%fact < 1:
            #word1[2] = word1[2]/fact
            #idx = facts.index(fact)
            #print("idx",idx,"fact",fact)
            foundFacts.append(fact)
            #print(fact,"\n")
    mv = mv+((len(foundFacts)+0.01)/(len(fact1)+0.01))*0.50
    #print("3",mv)
    return mv
"""
word1 = "wrod"
word2 = "place"
word3 = "without"
baseList = []
word1 = all2lowercase(word1)
word2 = all2lowercase(word2)
word3 = all2lowercase(word3)
baseList.append(word2Prime(word1,myDict))
baseList.append(word2Prime(word2,myDict))
baseList.append(word2Prime(word3,myDict))
pnl = primeNumbers[0:26]
print("word1:",word1,", word2:",word2,"\n","Matching Result:",measureSimilary(baseList[0],baseList[1],pnl))
print("word2:",word2,", word3:",word3,"\n","Matching Result:",measureSimilary(baseList[1],baseList[2],pnl))
print("word1:",word1,", word3:",word3,"\n","Matching Result:",measureSimilary(baseList[0],baseList[2],pnl))"""

text1 = "Aoccdrnig to a rscheearch and at Cmabrigde Uinervtisy, it deos not mttaer in waht oredr the ltteers in a wrod are, the olny iprmoetnt tihng is taht the frist and lsat ltteer be at the rghit pclae. The rset can be a toatl mses and you can sitll raed it wouthit porbelm. Tihs is bcuseae the huamn mnid deos not raed ervey lteter by istlef, but the wrod as a wlohe."
text2 = "According to a researcher at Cambridge University, it does not matter in what order the letters in a word are, the only important thing is that the first and last letter be at the right place. The rest can be a total mess and you can still read it without problem. This is because the human mind does not read every letter by itself but the word as a whole."
text3 = "Aoccdrnig to a rscheearch and at Cmabrigde Uinervtisy, it deos not mttaer in waht oredr the ltteers in a wrod are, the olny iprmoetnt tihng is taht the frist and lsat ltteer be at the rghit pclae. The rset can be a toatl mses and you can sitll raed it wouthit porbelm. Tihs is bcuseae the huamn mnid deos not raed ervey lteter by istlef, but the wrod as a wlohe."

text1 = text1.replace(",","")
text2 = text2.replace(",","")
text1 = text1.replace(".","")
text2 = text2.replace(".","")

text1S = text1.split()
text2S = text2.split()

pnl = primeNumbers[0:26]
correctionList = []
for elm1 in text1S:
    correctionList.append([])
    for elm2 in text2S:
        #print(elm1, elm2)
        if len(elm1)>3 and len(elm2)>3:
            elm1L = all2lowercase(elm1)
            elm1Prime = word2Prime(elm1L,myDict)
            elm2L = all2lowercase(elm2)
            elm2Prime = word2Prime(elm2L,myDict)
            mv = measureSimilary(elm1Prime,elm2Prime,pnl)
            if mv>0.5:
                print("The word -{}- and -{}- are alike with value {}.".format(elm1,elm2,mv))
            correctionList[-1].append([elm1,elm2,mv])

for cnt in range(len(correctionList)):
    correctionList[cnt] = sorted(correctionList[cnt],key=lambda column:column[2], reverse=True)
    
for cnt in range(len(correctionList)):
    if len(correctionList[cnt])>0:
        text1 = text1.replace(correctionList[cnt][0][0],correctionList[cnt][0][1])