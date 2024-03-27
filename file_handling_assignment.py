'''
Demonstrate your understanding of Python file handling by completing the following tasks.

Tasks:

File Creation:
Create a Python script (file_handling_assignment.py) that does the following:
Creates a new text file named "my_file.txt" in write mode ('w').
Write at least three lines of text to the file, including a mix of strings and numbers.


File Reading and Display:
Enhance your script to read the contents of "my_file.txt" and display them on the console.


File Appending:
Modify the script to open "my_file.txt" in append mode ('a').
Append three additional lines of text to the existing content.


Error Handling:
Implement error handling using try, except, and finally blocks to manage potential file-related exceptions (e.g., FileNotFoundError, PermissionError).
'''
#File creation
try:
    with open("my_file.txt", "w") as file:
        file.write("This is my first program.\n")
        file.write("I hope it works, lets see!.\n")
        file.write("Do it buddy!\n")
except IOError:
    print("Error: could not create file my_file.txt")

 #File reading and display.
try:
    with open("my_file.txt", "r") as file:
        contents = file.read()
        print(contents)
except IOError:
    print("Error: could not read file my_file.txt")

#File appending
try:
    with open("my_file.txt", "a") as file:
        file.write("This is my second program.\n")
        file.write("You ready!\n")
        file.write("lets go!.\n")
except IOError:
    print("Error: could not append to file my_file.txt")

#Error handling
try:
    with open("my_file.txt", "a") as file:
        file.write("This is my third paragraph.\n")
        file.write("I hope you dont doubt this.\n")
        file.write("come on!.\n")
except FileNotFoundError:
    print("Error: File not found")
except PermissionError:
    print("Error: Permission denied")
except IOError:
    print("Error: An I/O error occurred")
finally:
    print("File operations completed.")
      
