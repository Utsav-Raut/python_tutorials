fhr=open("data1.txt","r")
data =fhr.read()
print("Before writing:")
print(data)
fhr.close()
fhw=open("data1.txt","a")
num=fhw.write("this new first line written\n")
num1=fhw.write("this new second line written\n")
print("num:",num)
print("num1:",num1)
fhw.close()
fhr=open("data1.txt","r")
data =fhr.read()
print("After writing:")
print(data)
fhr.close()

# showing the tell() method which tells the current position pointed by the file object within the file
print("Using the tell() method")
fhr=open("data1.txt","r")
cur_pos=fhr.tell()
print(cur_pos)
data =fhr.readline()
print(data)
cur_pos=fhr.tell()
print(cur_pos)
data =fhr.readline()
print(data)
fhr.close()

#Using seek()
print("Using seek method")
fhr=open("data1.txt","rb+")
print(fhr.tell())
fhr.seek(12) #navigates to 12th position from beginning of the file
print(fhr.tell())
fhr.seek(3,1) #navigates to 3rd position from current position of the file object position
print(fhr.tell())
fhr.seek(-3,2)#navigates to 3rd position from end of the file in backward direction
print(fhr.tell())
fhr.close()

#File modes
fhr=open("data1.txt","rb+")
print("file name:",fhr.name)
print("access mode:",fhr.mode)
print("closed?",fhr.closed)
fhr.close()
print("after closing the file closed?",fhr.closed)



