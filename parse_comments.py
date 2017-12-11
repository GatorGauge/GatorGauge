# Expanding gkapfham's gatorgrader/gatorgrader_comments.py
# References:
# https://stackoverflow.com/questions/15423658/regular-expression-for-single-line-comments
# https://blog.ostermiller.org/find-comment


"""Parse comments from a Java source code file."""
import re
import java_parser


FILE_SEPARATOR = "/"
MULTILINECOMMENT_RE = r'\/\*+([\s\S]*?)\*+\/'
SINGLELINECOMMENT_RE_JAVA = \
    r'^(?:[^"/\\]|\"(?:[^\"\\]|\\.)*\"|/(?:[^/"\\]|\\.)|/\"(?:[^\"\\]|\\.)*\"|\\.)*//(.*)$'


def nix_javadoc_tags(java_string):
    """Removes javadoc tags such as @author from the source comments"""
    post_nix = re.sub('.@.*? ', ' ', java_string)
    return post_nix


def list_singleline_java_comments(java_string):
    """Return list of singleline Java comments in the java_string."""
    pattern = re.compile(SINGLELINECOMMENT_RE_JAVA, re.MULTILINE)
    singleline_comments = pattern.findall(java_string)
    trimmed_comments = []
    for comment in singleline_comments:
        trimmed_comments.append(comment.strip().strip('* '))
    return trimmed_comments


def list_multiline_java_comments(java_string):
    """Count the number of multiline Java comments in the java_string."""
    pattern = re.compile(MULTILINECOMMENT_RE, re.MULTILINE)
    multiline_comments = pattern.findall(java_string)
    trimmed_comments = []
    for comment in multiline_comments:
        trimmed_comments.append(comment.strip().strip('* '))
    return trimmed_comments


def count_singleline_java_comments(java_string):
    """Count the number of singleline Java comments in the java_string."""
    pattern = re.compile(SINGLELINECOMMENT_RE_JAVA, re.MULTILINE)
    singleline_comments = pattern.findall(java_string)
    return len(singleline_comments)


def count_multiline_java_comments(java_string):
    """Count the number of multiline Java comments in the java_string."""
    pattern = re.compile(MULTILINECOMMENT_RE, re.MULTILINE)
    multiline_comments = pattern.findall(java_string)
    return len(multiline_comments)


def get_ratio_of_singleline_comments_to_source_code(java_string):
    """Get the ratio of singleline comments to the
        number of lines in the Java source code."""
    total_number_of_lines = java_parser.get_number_of_lines(java_string)
    number_of_singleline_comments = count_singleline_java_comments(java_string)
    return float(number_of_singleline_comments / total_number_of_lines)


def get_ratio_of_multiline_comments_to_source_code(java_string):
    """Get the ratio of multiline comments to the
        number of lines in the Java source code."""
    total_number_of_lines = java_parser.get_number_of_lines(java_string)
    number_of_multiline_comments = count_multiline_java_comments(java_string)
    return float(number_of_multiline_comments / total_number_of_lines)


if __name__ == "__main__":

    with open('./java/HelloWorld.java', 'r') as java_file:
        JAVA_STRING = java_file.read()

    comment = nix_javadoc_tags(JAVA_STRING)
    print("\nComments w/out Javadoc tags\n-------------------")
    print(repr(comment))
    str(nix_javadoc_tags(JAVA_STRING))

    COMMENTS = list_singleline_java_comments(JAVA_STRING)
    print("\nSingleline comments\n-------------------")
    for comment in COMMENTS:
        print(repr(comment))
    print("Number of singleline comments: " +
          str(count_singleline_java_comments(JAVA_STRING)))

    print("Ratio of singleline comments to total Java source code lines: " +
          str(get_ratio_of_singleline_comments_to_source_code(JAVA_STRING)))

    COMMENTS = list_multiline_java_comments(JAVA_STRING)
    print("\nMultiline comments\n------------------")
    for comment in COMMENTS:
        print(repr(comment))
    print("Number of multiline comments: " +
          str(count_multiline_java_comments(JAVA_STRING)))

    print("Ratio of multiline comments to total Java source code lines: " +
          str(get_ratio_of_multiline_comments_to_source_code(JAVA_STRING)))
