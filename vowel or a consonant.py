""" determines whether a character entered 
by the user is a vowel or a consonant."""

ch=str(input("enter charecter= "))
vol1= "a"
vol2="e"
vol3="i"
vol4="o"
vol5="u"

if((ch==vol1)or (ch==vol2)or (ch==vol3)or(ch==vol4)or(ch==vol5)):
    print("vowel")
else:
    print("consonant")