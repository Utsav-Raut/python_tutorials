# try: 
#     f = open('testfile.txt')
#     # var = bad_var
# # except FileNotFoundError:
# #     print('Sorry! This file does not exist')
# # except Exception:
# #     print('Sorry! Something went wrong.')
# except FileNotFoundError as e:
#     print(e)
# except Exception as e:
#     print(e)
# else:
#     print(f.read())
#     f.close()
# finally:
#     print("Executing finally")


# CUSTOM EXCEPTIONS
try: 
    f = open('corrupt_file.txt')
    if f.name == 'corrupt_file.txt':
        raise Exception
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print('Error!')
else:
    print(f.read())
    f.close()
finally:
    print("Executing finally")
