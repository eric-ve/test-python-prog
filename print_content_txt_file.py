# Open the file
with open('messages.txt', 'r') as file:

    # Read the contents of the file
    contents = file.readline()

    # Display the contents on the screen
    print(contents)
