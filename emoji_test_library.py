import re


def emoji_counter():

    teststr = "Lorem ipsum dolor sit amet, :smile:  :smile:  :rage:  consectetur :thumbsdown: adipiscing elit"
    smileFace = 0

    emoticon1 = re.findall(":smile:",teststr)
    emoticon2 = re.findall(":rage:",teststr)
    emoticon3 = re.findall(":confused:",teststr)
    emoticon4 = re.findall(":thumbsdown:",teststr)
    emoticon5 = re.findall(":hourglass:",teststr)
    emoticon6 = re.findall(":sob:",teststr)
    emoticon7 = re.findall(":neutral:",teststr)
    emoticon8 = re.findall(":sunglasses:",teststr)
    emoticon9 = re.findall(":raisedHands:",teststr)
    emoticon10 = re.findall(":smilingImp:",teststr)

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
