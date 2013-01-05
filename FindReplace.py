'''
Created on 15 Sep 2012

Python script to find a set of words and replace them with a set of words.
  
This is WIP
@author: Alex
'''

'''
done.
1. Works with .txt file.

To do next:
1. Tidy up
2. Get working for excel (multi worksheets).
3. Get working for csv.
4. Better print outs to make it easier to read
'''
import csv
import fileinput

def main():
    readFile();
    
def readFile():
    filenames = open("filenames.csv")
    csvfileNamesParser = csv.reader(filenames)
    for fileToUpdateName in csvfileNamesParser:
        print("looking at " + str(fileToUpdateName[0]))
        fileIn = open(fileToUpdateName[0])
        fileout = open(fileToUpdateName[0] + "out", "wt")
        
        csvFindReplaceParser = csv.reader(open("findreplace.csv"))
        for find, replace in csvFindReplaceParser:
            print find, replace; 
            for line in fileIn: 
                fileout.write(line.replace(find, replace))
        fileout.close();
        fileIn.close();        
    filenames.close();

    
if __name__ == '__main__':
    main()