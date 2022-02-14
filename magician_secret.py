# Magician & The Secret Code
secret_code = 444

user_input = int(input('Enter The Secret Number : ')) #you have to make the input an integer else it won't work

while user_input != secret_code:
    print("You're Stuck in an Endless loop, Write the correct code to get free")
    user_input = int(input('Enter The Secret Number : '))
  
print("Well Done! You're Free Now")
