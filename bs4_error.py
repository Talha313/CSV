from web import bsobj

try:
    badContent=bsobj.nonExistingTag.anotherTag
except AttributeError as e:
    print("attribute not found")
else:
    if (badContent==None):
        print("attribute not found")
    else:
        print(badContent)