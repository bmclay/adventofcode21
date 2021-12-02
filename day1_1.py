#open a text file with the list of numbers in it
txtfile=open('sonarSweepReport.txt')

#create an empty list to load each value into from the text file
depths=[]
for line in txtfile:
    depths.append(int(line.rstrip()))
txtfile.close()

#using the list compare each index value to its prededing value.
#dump the occurances of "True" into a list called res and then show how many times this happened.
res = []
for idx in range(1, len(depths)):
    if depths[idx - 1] < depths[idx]:
       res.append(True)
print(len(res))
