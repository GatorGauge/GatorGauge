import emoji_library


def test_get_emojis_counter_with_one_of_each():
    """Check that one of each emoji is counted."""
    list_of_commits = [":smile: :rage: :confused: :thumbsdown: :hourglass:",
                       ":sob: :neutral: :sunglasses: :raisedHands: :smilingImp:"]

    emoji_count = emoji_library.get_emojis_count(list_of_commits)

    assert all(count == 1 for count in emoji_count.values())
