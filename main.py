def menuDisplay():
  print("Please choose from the following options: ")
  print("1) Placeholder Question 1")
  print("2) Placeholder Question 2")
  print("3) Placeholder Question 3")
  print("4) Exit Program")
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
  if(option == "1"):
    print("\nOption 1 reached\n")
  elif(option == "2"):
    print("\nOption 2 reached\n")
  elif(option == "3"):
    print("\nOption 3 reached\n")
  elif(option == "4"):
    print()
    print(f"Thank you for using our service, {name}!")
    print("Goodbye!")
    ifInLoop = False
  else:
    print("\nPlease enter a number from 1 to 4.\n")
    continue