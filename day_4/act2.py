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
                self.file = open(file_name, "r")
                self.contents = self.file.readlines()
                break
            except FileNotFoundError:
                print("File not found. Please enter a valid file name.")
                file_name = input(
                    "Please enter the name of the file you would like to read: "
                )
            except IOError:
                print("Error reading file. Please enter a valid file name.")
                file_name = input(
                    "Please enter the name of the file you would like to read: "
                )
            except Exception as e:
                print("An error occurred:", str(e))
                file_name = input(
                    "Please enter the name of the file you would like to read: "
                )

    def reverse(self, new_file_name):
        try:
            with open(new_file_name, "w") as new_file:
                for line in self.contents:
                    reversed_line = line.strip()[::-1]
                    new_file.write(reversed_line + "\n")
            print(
                "File successfully reversed and written to", new_file_name
            )
        except Exception as e:
            print("An error occurred while reversing the file:", str(e))

    def upper(self, new_file_name):
        try:
            with open(new_file_name, "w") as new_file:
                for line in self.contents:
                    upper_line = line.upper()
                    new_file.write(upper_line)
            print(
                "File successfully capitalized and written to", new_file_name
            )
        except Exception as e:
            print("An error occurred while upping the file:", str(e))


if __name__ == "__main__":
    f = FileManipulator("tmp.txt")
    print(f.contents)
    f.reverse("tmp2.txt")
    f.upper("tmp3.txt")
