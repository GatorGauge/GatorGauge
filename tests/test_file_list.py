import file_list


def test_list_files():
    repo = "all"
    out = "tests/fileListTestFolder"
    folder_list = file_list.list_files(repo, out)
    expected_folder_list = ['testFolder1', 'testFolder2', 'testFolder3']
    expected_folder_size = 3
    assert len(folder_list) == expected_folder_size
    assert all(folder in folder_list for folder in expected_folder_list)

def test_list_files_one():
    repo = "testFolder1"
    out = "tests/fileListTestFolder"
    files_list = file_list.list_files(repo, out)
    expected_files_list = ['testFile1_1.txt', 'testFile1_2.txt']
    expected_files_size = 2
    assert len(files_list) == expected_files_size
    assert files_list == expected_files_list
