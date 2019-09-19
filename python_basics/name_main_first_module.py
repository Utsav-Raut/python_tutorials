import name_main_53 # whenever we import a file, it runs that code
#The above line prints: First module's name: name_main_53
# The reason for printing this is because the first file is no longer being run directly, it is being imported

print("Second module's name: {}".format(__name__))
# Now the above two statement prints:
# First module's name: name_main_53
# Second module's name: __main__

#After writing as __name__ ==  __main__ in the other file, this program prints: Second module's name: __main__
# The reason why it didn't print the first modules name is because now we have the check in place: if __name__main:
# Due to the check, whenever it came through and ran the code this second module saw that __name__ == name_main_53, and not __main__, so it never made it to the internal main() method


# After adding the below steps in the other file and running this file we get
# if __name__ == '__main__':
#     print("Run directly")
# else:
#     print("Run from import")

# Now the output is:
# Run from import
# Second module's name: __main__


# We can run the main() method of the other file by simply writing modulename.methodname()
