import re


def emoji_counter(s):

    emoticon1 = re.findall(":smile:",s)
    emoticon2 = re.findall(":rage:",s)
    emoticon3= re.findall(":confused:",s)
    emoticon4 = re.findall(":thumbsdown:",s)
    emoticon5 = re.findall(":hourglass:",s)
    emoticon6 = re.findall(":sob:",s)
    emoticon7 = re.findall(":neutral:",s)
    emoticon8 = re.findall(":sunglasses:",s)
    emoticon9 = re.findall(":raisedHands:",s)
    emoticon10 = re.findall(":smilingImp:",s)

    print("emojies: "+str(emoticon1)+str(emoticon2)+str(emoticon4))
    print("SmileyFaces: ", len(emoticon1))
    print("RageFaces: ", len(emoticon2))
    print("Confused: ", len(emoticon3))
    print("thumbsdown: ", len(emoticon4))
    print("TimeConsuming: ", len(emoticon5))
    print("Sad: ", len(emoticon6))
    print("Neutral: ", len(emoticon7))
    print("Cool: ", len(emoticon8))
    print("RaisedHands: ", len(emoticon9))
    print("SmilingImp: ", len(emoticon10))

if __name__ == "__main__":
    emoji_counter()
