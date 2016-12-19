# open file called list.txt in write mode
file = open('list.txt','w')

x = 0
# add user input to the file
while x < 10:
    file.write(input("What fruits would you like to add to the file? ") + ' \n')
    x += 1

file.close()
file = open('list.txt','r')
file.seek(0)
print(file.read())