#inputs for the charater and the length of the triangle
character = (input("What do you want the triangle to be made out of? "))
length = int(input("Enter the length: "))

for i in range(length + 1): #this for loop runs for the number of rows it will need to create
  output = ""
  for j in range(i): #this for loop creates the rows and runs once each time the main for loop runs
    output += character
  print(output)

