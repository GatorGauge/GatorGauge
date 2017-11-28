"""Test parse_comments functions."""
import parse_comments


def test_get_ratio_of_singleline_comments_to_source_code_with_one_comment():
    java_string = """/**
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

    expected_ratio = 0.2
    actual_ratio = parse_comments.get_ratio_of_singleline_comments_to_source_code(java_string)
    assert actual_ratio == expected_ratio


def test_get_ratio_of_multiline_comments_to_source_code_with_two_comments():
    java_string = """/**
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

    expected_ratio = 0.4
    actual_ratio = parse_comments.get_ratio_of_multiline_comments_to_source_code(java_string)
    assert actual_ratio == expected_ratio
