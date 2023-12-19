# activity for errors
# fileName = input("Please enter the name of the file you would like to read: ")
# myfile = open(fileName, 'r') # Open a file for reading.
# contents = myfile.readlines() # Read in the content by line.
# myfile.close() # Explicitly close the file
# print(contents) #print the contents of the file
class FileManipulator:
    def __init__(self, file_name):
        while True:
            try:
                self.file = open(file_name, 'r')
                break
            except FileNotFoundError:
                print("File not found. Please enter a valid file name.")
                file_name = input("Please enter the name of the file you would like to read: ")
            except IOError:
                print("Error reading file. Please enter a valid file name.")
                file_name = input("Please enter the name of the file you would like to read: ")
            except Exception as e:
                print("An error occurred:", str(e))
                file_name = input("Please enter the name of the file you would like to read: ")



if __name__ == "--main__":
    f = FileManipulator("tmp.txt")
    print(f.contents)
    f.reverse("tmp2.txt")
