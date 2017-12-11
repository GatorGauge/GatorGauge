import get_avg_num_of_comments
JAVA_STRING = """
/**
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

def test_get_avg_num_of_comments():
    avg = get_avg_num_of_comments.get_avg_num_of_comments(JAVA_STRING)
    assert "singleline" in avg
    assert "multiline" in avg
    assert "javadoc" in avg
