import analyze_java as aj


def test_get_file_paths():
    """Testing to ensure that the get_file_paths function returns the correct list of file paths"""
    path_list = aj.get_file_paths(".java", "test_repos")
    correct_path = ['test_repos/test-repo-1/src/test.java', 'test_repos/test-repo-2/src/test.java', 'test_repos/test-repo-3/src/test.java']
    assert correct_path == path_list


def test_get_java_strings():
    """Testing to ensure that the get_java_strings function returns java source code as a string"""
    java_string = aj.get_java_strings("simple_test_repo")
    correct_string = ['public class simple {\n    public static void main(String[] args) {\n        int x = 3;\n        System.out.println(x);\n    }\n}']
    assert java_string == correct_string
