#File Objects

# f = open('test.txt') #The open command allows us to specify whether we want to open this file for reading, writing, appending or reading and writing. If we don't specify anything then it defaults the file to reading
# f = open('test.txt', 'r')   #This is only for reading
# print(f.name)
# print(f.mode)
# f.close()


#Opening files with context manager and why this is the preferred way
#If we open a file like we did above then we need to explicitly close the file as well. If we don't close the file then we may end up with leaks that cause you to run over the maximum allowed file descriptors in the system and application keeps throwing error
# with open('test.txt', 'r') as f:    #Context manager allows us to work with the files within blocks and once we exit the block the file is close automatically. It will also close the file if any exceptions are thrown.
#     pass

# We have access to the file object variable after we have exit the context manager. But the file will just be closed.
# print(f.closed)     #This will print True. Although we have access to the file object variable, it is closed and we cannot read from it


with open('test.txt', 'r') as f:
    # f_contents = f.read()     #This reads the entire file as it is
    # f_contents = f.readlines()  # We get a list of all the lines in the file. We have a newline character at the end of each line
    # f_contents = f.readline()     #Reads the first line in the file. IF we run this again, then the next line is read.
    # print(f_contents, end='')     #Print statements end with a new line by default and so we pass the empty string

    #Reading data from an extremely large file
    # for line in f:              #This approach does not read the entire content of the file all at once and hence we do not have to run into any memory issue
    #     print(line,end="")

    # f_contents = f.read(100)        #Reads the first 100 characters of our file
    # print(f_contents, end='')
    # f_contents = f.read(100)        #This starts where it left off above and prints the next 100 chars
    # print(f_contents, end='')


    # size_to_read = 10
    # f_contents = f.read(size_to_read)
    # while len(f_contents) > 0:
    #     print(f_contents, end='*')
    #     f_contents = f.read(size_to_read)

    # print(f.tell())         #This prints the current position of the file

    # size_to_read = 10
    # f_contents = f.read(size_to_read)
    # print(f_contents, end='')
    # f.seek(0)           #This method manipulates our current position. This sets our position back to the beginning of the file
    # f_contents = f.read(size_to_read)
    # print(f_contents)


#Writing files
14:41
