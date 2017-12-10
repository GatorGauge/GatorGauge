"""Test parse_comments functions."""
import parse_comments as pc


JAVA_STRING = """/**
* A class to print out "Hello, world!"
* Another line
*@user, a tag for removal
*@blahfenshtele, another tag for removal
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
        pc.get_ratio_of_singleline_comments_to_source_code(JAVA_STRING)
    assert actual_ratio == 0.2


def test_get_ratio_of_multiline_comments_to_source_code_with_two_comments():
    actual_ratio = \
        pc.get_ratio_of_multiline_comments_to_source_code(JAVA_STRING)
    assert actual_ratio == 0.4


def test_get_javadoc_tag_nixed_code_comments():
    final_form = pc.nix_javadoc_tags(JAVA_STRING)
    assert "@user," not in final_form
    assert "@blahfenshtele," not in final_form
