#This is the program for CCC question 1
#The question asks you to find the area of a fence with peices of wood with very different lengths and widths


#These are the inputs 
fences = int(input("")) #number of fences
height = input("")#The height of the fences
base = input ("")#The length of the base of the fences
total = 0.0#The variable will be used later as the final output number so it will start at 0

heights = [fences + 1] #The value of the heights array is the length of fences
bases = [fences] #The value of bases array is the length of fences

h = height.split() #This will set the value of h to be all the values of the heights array as a string
b = base.split() #This will set the value of h to be all the values of the base array as a string

#This is the loop that will add all the areas of the pieces of wood together
for x in range(fences):
  if x + 1 > fences:# If the value of x+1 is greater than fences, it will end the code. X is the position of the element in the array.
    break
  else:
    total = total + (float(b[x]) * (float(h[x]) + float(h[x+1])))/2 #This will find the area of the each of the woods (using (b*h+h)/2) and add it to total. It will keep looping for each piece of wood

print (total)#This will print the total
