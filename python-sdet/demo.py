
pancard_list=["AABGT6715H", "UFFAC4352T", "IFSBD9163K", "JOOEC1225H","RWXAFE187B"]


print(pancard_list[3][6], end=" ")
print(pancard_list[4][3:])

import re
word="New Airlines4"
if(re.search(r"^N",word) and re.search(r"e$",word)):
    print(re.sub(r"New",r"Old",word))
else:
    print(re.sub(r"s(\d{1})",r"S\1",word))

song="JINGLE Bells jingle Bells Jingle All The Way"
song.upper()
print(song)
song_words=song.split()
count=0
for word in song_words:
    if(word.startswith("jingle")):
        count=count+1
print(count)


FHW=open("data2.txt","w")
FHW.write("written some thing")
print(FHW.tell())
print("closed?",FHW.closed)
FHW.close()
print("after closing the file closed?",FHW.closed)