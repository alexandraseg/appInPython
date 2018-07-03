#Read the file
f=open('unsorted_fruits.txt','r')
#Create an empty list
fruit_list=[]
#For every line in file
for fruit in f.readlines():
    #Remove whitespace from the begin or end of the string
    fruit=fruit.strip()
    if len(fruit)==0:
        continue
    #Append to the list
    fruit_list.append(fruit)
#Sort the list
fruit_list.sort()
#Close the file
f.close()
#Open the output files in write mode
output_file=open("sorted_fruits.txt","w")
#Iterate fruits in ascending order
for fruit in fruit_list:
    #Write to the file
    output_file.write(fruit+"\n")
#Close the file
output_file.close()
