"""Test parse_comments functions."""
import parse_comments as pc


JAVA_STRING = """/**
* A class to print out "Hello, world!"
* Another line
*/
class HelloWorld {
    /**
    * Prints out "Hello, world!"
    */
    public static void main(String args[]) {
        System.out.println("Hello, world!");    // print statement
    }

}
"""


def test_get_ratio_of_singleline_comments_to_source_code_with_one_comment():
    actual_ratio = \
        pc.ratio_of_singleline_comments(JAVA_STRING)
    assert actual_ratio == 0.2


def test_get_ratio_of_multiline_comments_to_source_code_with_two_comments():
    actual_ratio = \
        pc.ratio_of_multiline_comments(JAVA_STRING)
    assert actual_ratio == 0.4
