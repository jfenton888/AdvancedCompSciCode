firstName= [" stinky", " lumpy", " buttercup", " gidget", " crusty", " greasy", " fluffy", " cheeseball", " chim-chim", " poopsie", " flunky", " booger", " pinky", " zippy", " goober", " doofus", " slimy", " loopy", " snotty", " falafel", " dorkey", " squeezit", " oprah", " skipper", " dinky", " zsa-zsa"]
lastNameF= [" diaper", " toilet", " giggle", " bubble", " girdle", " barf", " lizard", " waffle", " cootie", " monkey", " potty", " liver", " banana", " rhino", " burger", " hamster", " toad", " gizzard", " pizza", " gerbil", " chicken", " pickle", " chuckle", " tofu", " gorilla", " stinker"]
lastNameL= ["head", "mouth", "face", "nose", "tush", "breath", "pants", "shorts", "lips", "honker", "butt", "brain", "tushie", "chunks", "hiney", "biscuits", "toes", "buns", "fanny", "sniffer", "sprinkles", "kisser", "squirt", "humperdinck", "brains", "juice"]
oldName= ((input('what name do you want to make better?').lower()).split(' '))
def letter_to_int(letter):
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    return alphabet.index(letter) + 1
print (oldName)
oldName[0] = list(oldName[0])
oldName[1] = list(oldName[1])
newFName = (firstName(letter_to_int(oldName[1:0])))
newLFName = (lastNameF(letter_to_int(oldName[2:0])))
newLLName = (lastNameL(letter_to_int(oldName[2:(len(oldName[2]))])))
print(oldName)
print(str(newFName) +" "+ str(newFName) + str(newLLName))