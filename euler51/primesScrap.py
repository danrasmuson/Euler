import pickle
import os
path = "C:\\Users\\Daniel\\Desktop\\euler51\\primes"
allNums = set()
for fileName in os.listdir(path):
    textFile = open(path+"\\"+fileName,"r")
    fullText = textFile.read()
    textFile.close()
    for num in fullText.split("\n"):
        allNums.add(num)
pickle.dump( allNums, open( "save.p", "wb" ) )




