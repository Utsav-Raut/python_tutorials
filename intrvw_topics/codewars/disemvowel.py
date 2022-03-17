#REMOVE THE VOWELS OF A STRING

def disemvowel(s):
    return "".join(c for c in s if c.lower() not in 'aeiou')

str = "This website is for fools, LOL!"
reply = disemvowel(str)
print(reply)