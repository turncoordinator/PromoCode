"""
Created on Mon Feb 27 15:52:15 2017
@author: desk243
"""
#stores promocode for final output
promocode = input("Enter Promocode: ")

#opens and reads files into variable 'data'
prod = open('products_file.txt', 'r')
data = prod.read()
prod.close()

#cleans out the nulls (which eventually show up as \x00) which cause problems later 
mynew = open('mynew.txt', 'w')
mynew.write(data.replace('\x00', ''))
mynew.close()

#gives number line count to use later in range
num_lines = sum(1 for line in open('mynew.txt'))

#puts line in myList
with open("mynew.txt") as input:
  myList = [(*(line.strip().split('\t') for line in input))]
  

#prints out id (part number) and promocode with tab between them (if they are not brand Specialized)
for x in range(1,num_lines):
    if (myList[x][2]) != 'Specialized':

#the # lines below were the only thing I could find online that seemed like it would work
#but all it produced was one line of seemingly random characters

             #with open('pf1.txt', 'w') as file:
                 print(myList[x][11],'\t'+promocode)
                 #for a,b in zip(myList[x][11],promocode):
                 #   file.write("{}\t{}".format(a,b))
#print("file saved")
