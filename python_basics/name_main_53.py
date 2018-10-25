# print (__name__)
# print("First module's name: {}".format(__name__))       #This prints: First module's name: __main__

# Whenever python runs a file, it first goes through, even before running any code, it sets a few special variables.
# __name__ is one of those special variables.
# When python runs a python file directly it sets the name variable to main.
# We can also import modules. Whenever we import modules we are going to set the "name" variable to the name of the file. So in this case it would be name_main_53.py


# Now if we write as below:
# def main():
#     print("First module's name: {}".format(__name__))
#
# if __name__ == '__main__':      #This line means if this file is being run directly by python or is it being imported
#     main()
    # This prints -> First module's name: __main__




if __name__ == '__main__':
    print("Run directly")
else:
    print("Run from import")

# The idea behind this __name__main concept is that sometime we might just want to run whenever we are running this as a main file, and sometimes there is code that we want to run whenever the code is imported
