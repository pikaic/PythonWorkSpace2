import os

# dealing with data file
test_file=open("test.txt","wb")
print(test_file.mode)
print(test_file.name)
test_file.write(bytes("Writing this text on to the data file...","UTF-8"))
test_file.close()

test_file = open("test.txt","r+")
text_in_file = test_file.read()
print("So the file content -> ",text_in_file)
test_file.close()

os.remove("test.txt")