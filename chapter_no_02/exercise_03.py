# name = input ("Enter your name: ")
# ch = input ("Enter a character: ")
name, ch = input ("Enter name and a chacracter: ").split(",")
print (f"length of your name: {len(name)}")
print (f"The character's of {ch} in your  name: {((name.lower()).count(ch))}")