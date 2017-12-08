from get_list_of_commits import get_list_of_commits


def test_get_list_of_commits():
    """Test the functionality of getting_list_of_commits"""
    list = []
    list = (get_list_of_commits("SampleRepo"))
    assert len(list) == 3
    assert "Initial commit" in list
	assert "added lab3" in list