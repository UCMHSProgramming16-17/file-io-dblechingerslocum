# In your repository, create csvwriting.py and open the file

# import the csv library
import csv

# open the csv file. YOU DO NOT NEED newline=''
csvfile = open('examplefile.csv', 'w')

# create the csv writer
csvwriter = csv.writer(csvfile, delimiter=',')

# write rows to the file
csvwriter.writerow([1,2,3,4,5,6,7,8,9,10])
csvwriter.writerow(['apple','banana','orange','pineapple','mango','peach','plum','strawberry','kiwi','grape'])

# close the file
csvfile.close()