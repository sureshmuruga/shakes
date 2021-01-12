# importing csv module 
import csv
import os, codecs
import fileinput
from re import search
import time
import psutil
start=time.time()
dict={}
count={}

with open('french_dictionary.csv') as File:
    reader = csv.reader(File, delimiter=',', quotechar=',',
                        quoting=csv.QUOTE_MINIMAL)
    for row in reader:
        #dict.add(row[0],row[1])
        dict[row[0]]=row[1]
        count[row[0]]=0
    #print(dict)
        


jok="ram"
#input file
#fin = open("t8.shakespeare.txt", "rt")
fin=open("lol.txt","rt")
#output file to write the result to
fout = open("out.txt", "wt")
#for each line in the input file
for line in fin:
    #st=str(line.strip())
    #print(line)
    line = line.rstrip()
    for i in dict:
        if(line=="" or line==" "):
            break
        elif (i in line):
            line=line.replace(i,dict[i])
            count[i]=count[i]+1
    #print(line)
    fout.write(line)
    fout.write("\n")
    #print(i," ", line)
   
#close input and output files
fin.close()
fout.close()
rav=jok.replace("ram","ravi")
for i in count:
    print(i," ",count[i])
record=[]
field=['ENGLISH','FRENCH','OCCURENCE']
'''
for i in dict:
    record.append([i,dict[i],count[i]])
'''
with open("occurence.csv","w") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(field)
    for i in dict:
        csvwriter.writerow([i,dict[i],count[i]])
    #csvwriter.writerows(record)
end=time.time()
print("\nRuntime of the program is: %.2f"%((end-start)/60),"min")
print("Memory useage of program: ","%.2f"%(((psutil.virtual_memory().used/1024)/1024)/1024),"mb")
print("...end....")

'''
# csv file name 
filename = "french_dictionary.csv"

# initializing the titles and rows list 
fields = [] 
rows = [] 

# reading csv file 
with open(filename, 'r') as csvfile: 
    csvreader = csv.reader(csvfile)
    #fields = csvreader.next()
    for row in csvreader:
        rows.append(row)

# Reading an excel file using Python
import xlrd

# Give the location of the file
loc = ("")


wb = xlrd.open_workbook("french_dictionary.csv")
sheet = wb.sheet_by_index(0)


print(sheet.cell_value(0, 0))


'''
