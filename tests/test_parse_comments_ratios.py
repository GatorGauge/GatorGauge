"""Test parse_comments functions."""
import parse_comments as pc


JAVA_STRING = """/**
* A class to print out "Hello, world!"
* Another line
*@user, a tag for removal
*@blahfenshtele, another tag for removal
*/
class HelloWorld {
    /*
    * Prints out "Hello, world!"
    */
    public static void main(String args[]) {
        System.out.println("Hello, world!");    // print statement
    }

}
"""


def test_ratio_singleline_comments():
    """ verify ratio of single-line comments to source """
    actual_ratio = \
        pc.ratio_of_singleline_comments(JAVA_STRING)
    assert actual_ratio == 0.2


def test_ratio_multiline_comments():
    """ verify ratio of multiline comments to source """
    actual_ratio = \
        pc.ratio_of_multiline_comments(JAVA_STRING)
    assert actual_ratio == 0.2


def test_ratio_javadoc_comments():
    """ verify ratio of javadoc comments to source """
    actual_ratio = \
        pc.ratio_of_javadoc_comments(JAVA_STRING)
    assert actual_ratio == 0.2


def test_javadoc_tag_nixed_comments():
    """ verify javadoc tags are removed """
    final_form = pc.nix_javadoc_tags(JAVA_STRING)
    assert "@user," not in final_form
    assert "@blahfenshtele," not in final_form
