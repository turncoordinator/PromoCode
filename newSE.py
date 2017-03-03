"""
Created on Mon Feb 27 15:52:15 2017
@author: desk243
"""

promocode = input("Enter Promocode: ")
#opens and reads files into variable 'data'

prod = open('products_file.txt', 'r')
data = prod.read()
prod.close()

#cleans out the nulls (\x00) which cause problems later 
mynew = open('mynew.txt', 'w')
mynew.write(data.replace('\x00', ''))
mynew.close()

#gives number line count to use later in range
num_lines = sum(1 for line in open('mynew.txt'))

#puts line in myList
with open("mynew.txt") as input:
  myList = [(*(line.strip().split('\t') for line in input))]
  

#prints out brand name (for use when removing them later  )
for x in range(1,num_lines):
    if (myList[x][2]) != 'Specialized': 
             #with open('gpf1.txt', 'w') as file:
                 print(myList[x][11],'\t'+promocode)
                 #for a,b in zip(myList[x][11],promocode):
                  #   file.write("{}\t{}".format(a,b))
#print("file saved")