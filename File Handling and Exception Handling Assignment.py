# user input
inputFile = input("Enter the file name to read from: ")
outputFile = input("Enter the file name to write to: ")

#Error handling
try:
    # open file and read content
    with open(inputFile, 'r') as file: content = file.read()

    #change content by converting all text to uppercase
    modifiedText = content.upper()

    #write modified content to a new file
    with open(outputFile, 'w') as outPut: outPut.write(modifiedContent)
    print(f"The file {outputFile} has been updated successfully!")

except FileNotFoundError:
    print(f"The file {inputFile} is inaccessible.")