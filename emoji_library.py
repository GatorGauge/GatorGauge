import re


def get_emojis_count(list_of_commits):
    """Count emojis within a list of commits."""

    smile = rage = confused = thumbsdown = hourglass = sob = \
        neutral = sunglasses = raisedHands = smilingImp = 0

    for commit in list_of_commits:
        smile += len(re.findall(":smile:", commit))
        rage += len(re.findall(":rage:", commit))
        confused += len(re.findall(":confused:", commit))
        thumbsdown += len(re.findall(":thumbsdown:", commit))
        hourglass += len(re.findall(":hourglass:", commit))
        sob += len(re.findall(":sob:", commit))
        neutral += len(re.findall(":neutral:", commit))
        sunglasses += len(re.findall(":sunglasses:", commit))
        raisedHands += len(re.findall(":raisedHands:", commit))
        smilingImp += len(re.findall(":smilingImp:", commit))

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
