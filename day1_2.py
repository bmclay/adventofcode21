#open a text file with the list of numbers in it
txtfile=open('sonarSweepReport.txt')

#create an empty list to load each value into from the text file
depths=[]
for line in txtfile:
    depths.append(int(line.rstrip()))
txtfile.close()

#define results variable that contains a list of lists of sets of three numbers.
k=3
sublist = [depths[i:i+k] for i in range(len(depths)-k+1)]
#print(sublist)        #show each individual window of 3 values.

sublistSums=[]                   #empty list to collect all the combined elements from the 3 items in each sublist.

slideTotal=0
for n in sublist[0]:
    slideTotal+=n                #just a way of saying slideTotal=slideTotal+n
sublistSums.append(slideTotal)   #sum of the 3 values in the sliding window.

slideTotal=0
for n in sublist[1]:
    slideTotal+=n
sublistSums.append(slideTotal)

slideTotal=0
for n in sublist[2]:
    slideTotal+=n
sublistSums.append(slideTotal)


#ended confused here... got answer from reddit  
for n in sublist[:]:
    slideTotal+=n               #TypeError: unsupported operand type(s) for +=: 'int' and 'list'
sublistSums.append(slideTotal)


print(sublistSums)
