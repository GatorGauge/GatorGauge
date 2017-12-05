import re

def emoji_counter():

    teststr = ["Lorem ipsum dolor sit amet, :smile:  :smile:  :rage:  consectetur :thumbsdown: adipiscing elit"]

    emoticon1 = enumerate(re.findall(":smile:"))
    smileFace = sum(1 for _ in teststr)

    

    emoticon2 = re.finditer(ru[:rage:], s)
    rageFace = sum(1 for _ in teststr)

    emoticon3 = re.finditer(ru[:confused:], s)
    confusedFace = sum(1 for _ in teststr)

    emoticon4 = re.finditer(ru[:thumbsdown:], s)
    thumbsdown = sum(1 for _ in teststr)

    emoticon5 = re.finditer(ru[:hourglass:], s)
    hourglass = sum(1 for _ in teststr)

    emoticon6 = re.finditer(ru[:sob:], s)
    sobFace = sum(1 for _ in teststr)

    emoticon7 = re.finditer(ru[:neutral_face:], s)
    neutralFace = sum(1 for _ in teststr)

    emoticon8 = re.finditer(ru[:sunglasses:], s)
    sunglassesFace = sum(1 for _ in teststr)

    emoticon9 = re.finditer(ru[:raised_hands:], s)
    raisedHands = sum(1 for _ in teststr)

    emoticon10 = re.finditer(ru[:smiling_imp:], s)
    smilingImp = sum(1 for _ in teststr)

    emojiData = [smileFace, "rageFace", "confusedFace", "thumbsdown", "hourglass", "sobFace", "neutralFace", "sunglassesFace", "raisedHands", "smilingImp" ]

    print (emoticon1)
    print (smileFace)
    return emojiData
