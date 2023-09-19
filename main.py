commands = ["Placeholder 1", "Placeholder 2", "Placeholder 3"]

def menuDisplay():
  print("Please choose from the following options: ")
  for i in range(0,len(commands)):
    print(f"{i+1}) {commands[i]}")
  
  print(f"{len(commands)+1}) Exit Program")
  option = input("Enter the number of your choice: ")
  return option

print("Welcome to the Elite 101 Chatbot!")
name = input("Please enter your name >>> ")
while(name == ""):
  name = input("Invalid input. Please enter your name >>> ")
  
print(f"Hello {name}! It's nice to meet you. \n")

age = input("Please enter your age >>> ")

while(age.isnumeric() == False or age == ""):
  age = input("Invalid input. Please enter your age >>> ")

print(f"\nOh, to be {age} years old again! It's been {13787000000 - int(age)} years since I've been so young :( \n") 
  

print("How can I help you today?")
print()

ifInLoop = True
while(ifInLoop):
  option = menuDisplay()
  count = 0
  notChosenOption = True
  
  for i in range(0, len(commands)):
    if option.isnumeric(): # if option is number
      if int(option) > 0:
        if int(option)-1 == i: # if option is a number in commands
          print(f"\n{commands[i]} reached!\n")
          notChosenOption = False
        if int(option)-1 == len(commands): #if option is the length of array +1 (which is end sequence) break from loop
          print("\nThank you for shopping with us!")
          notChosenOption = False
          ifInLoop = False
          break
      
      count += 1 #counting if option is over/under possible commands
    else: # reached if value is nonnumeric
      print("\nInvalid input. Please enter a possible command.\n")
      notChosenOption = False
      break
  
  if count == len(commands) and notChosenOption: # if value is above/below possible values
    print("\nInvalid input. Please enter a possible command.\n")  
