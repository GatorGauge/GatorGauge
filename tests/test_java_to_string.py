import java_to_string
import re


def test_remove_comments_singleLine():
    """Test if the function removes single commensts
    from the Java source code"""

    javaString = '''
    if(x < y) { // begin if block
    x = y;
    y = 0;
    } // end if block

    '''
    actualString = java_to_string.remove_comments(javaString)
    correctString = '    if(x < y) {     x = y;    y = 0;    }     '
    assert actualString == correctString


def test_remove_comments_MultiLines():
    """Test if the function removes multiline comment"""
    javaString = '''
    /**
 * Compares two {@code int} values numerically.
 * The value returned is identical to what would be returned by:
 * <pre>
 *    Integer.valueOf(x).compareTo(Integer.valueOf(y))
 * </pre>
 *
 * @param  x the first {@code int} to compare
 */
public static int compare(int x, int y) {
    return (x < y) ? -1 : ((x == y) ? 0 : 1);
}
    '''
    actualString = java_to_string.remove_comments(javaString)
    correctString = '    public static int compare(int x, int y) {    return (x < y) ? -1 : ((x == y) ? 0 : 1);}    '
    assert actualString == correctString


def test_remove_comments_singleLine_and_MultiLines():
    """Test if the functions removes single line and multiline
    comments"""
    javaString = '''
         /**
      * Compares two {@code int} values numerically.
      * The value returned is identical to what would be returned by:
      * <pre>
      *    Integer.valueOf(x).compareTo(Integer.valueOf(y))
      * </pre>
      *
      * @param  x the first {@code int} to compare
      */
      if(x < y) { // begin if block
      x = y;
      y = 0;
      } // end if block

    '''
    actualString = java_to_string.remove_comments(javaString)
    # print("actual: " , repr(actualString))
    correctString = '               if(x < y) {       x = y;      y = 0;      }     '
    assert actualString == correctString
