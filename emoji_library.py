import re


def get_emojis_count(list_of_commits):
    """Count emojis within a list of commits."""

    smile = rage = confused = thumbsdown = hourglass = sob = \
        neutral = sunglasses = raisedHands = smilingImp = 0

    for commit in list_of_commits:
        smile += len(re.findall(":smile:", list_of_commits))
        rage += len(re.findall(":rage:", list_of_commits))
        confused += len(re.findall(":confused:", list_of_commits))
        thumbsdown += len(re.findall(":thumbsdown:", list_of_commits))
        hourglass += len(re.findall(":hourglass:", list_of_commits))
        sob += len(re.findall(":sob:", list_of_commits))
        neutral += len(re.findall(":neutral:", list_of_commits))
        sunglasses += len(re.findall(":sunglasses:", list_of_commits))
        raisedHands += len(re.findall(":raisedHands:", list_of_commits))
        smilingImp += len(re.findall(":smilingImp:", list_of_commits))

    emojis_count = {"smile": smile,
                    "rage": rage,
                    "confused": confused,
                    "thumbsdown": thumbsdown,
                    "hourglass": hourglass,
                    "sob": sob,
                    "neutral": neutral,
                    "sunglasses": sunglasses,
                    "raisedHands": raisedHands,
                    "smilingImp": smilingImp}

    return emojis_count
