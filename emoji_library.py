import emoji
from emoji_data_python import emoji_data
from .emoji_char import EmojiChar

def emoji_counter(commit_str):
    emoticon1 = re.finditer(ru'[:smile:]', s)
    smileFace = sum(1 for _ in commit_str)

    emoticon2 = re.finditer(ru'[:rage:]', s)
    rageFace = sum(1 for _ in commit_str)

    emoticon3 = re.finditer(ru'[:confused:]', s)
    confusedFace = sum(1 for _ in commit_str)

    emoticon4 = re.finditer(ru'[:thumbsdown:]', s)
    thumbsdown = sum(1 for _ in commit_str)

    emoticon5 = re.finditer(ru'[:hourglass:]', s)
    hourglass = sum(1 for _ in commit_str)

    emoticon6 = re.finditer(ru'[:sob:]', s)
    sobFace = sum(1 for _ in commit_str)

    emoticon7 = re.finditer(ru'[:neutral_face:]', s)
    neutralFace = sum(1 for _ in commit_str)

    emoticon8 = re.finditer(ru'[:sunglasses:]', s)
    sunglassesFace = sum(1 for _ in commit_str)

    emoticon9 = re.finditer(ru'[:raised_hands:]', s)
    raisedHands = sum(1 for _ in commit_str)

    emoticon10 = re.finditer(ru'[:smiling_imp:]', s)
    smilingImp = sum(1 for _ in commit_str)

    emojiData = [smileFace, rageFace, confusedFace, thumbsdown, hourglass, sobFace, neutralFace, sunglassesFace, raisedHands, smilingImp ]

    return emojiData
