# Expanding gkapfham's gatorgrader/gatorgrader_comments.py
# References:
# https://stackoverflow.com/questions/15423658/regular-expression-for-single-line-comments
# https://blog.ostermiller.org/find-comment


"""Parse comments from a Java source code file."""
import re
import java_parser


FILE_SEPARATOR = "/"
JAVADOC_COMMENT_RE = r'\/\*\*([\s\S]*?)\*+\/'
MULTILINE_COMMENT_RE = r'\/\*(?!\*)([\s\S]*?)\*+\/'
SINGLELINE_COMMENT_RE_JAVA = \
    r'^(?:[^"/\\]|\"(?:[^\"\\]|\\.)*\"|/(?:[^/"\\]|\\.)|/\"(?:[^\"\\]|\\.)*\"|\\.)*//(.*)$'


def nix_javadoc_tags(java_string):
    """Removes javadoc tags such as @author from the source comments"""
    post_nix = re.sub('.@.*? ', ' ', java_string)
    return post_nix


def list_singleline_java_comments(java_string):
    """Return list of singleline Java comments in the java_string."""
    pattern = re.compile(SINGLELINE_COMMENT_RE_JAVA, re.MULTILINE)
    singleline_comments = pattern.findall(java_string)
    trimmed_comments = []
    for comment in singleline_comments:
        trimmed_comments.append(comment.strip().strip('* '))
    return trimmed_comments


def list_multiline_java_comments(java_string):
    """Count the number of multiline Java comments in the java_string."""
    pattern = re.compile(MULTILINE_COMMENT_RE, re.MULTILINE)
    multiline_comments = pattern.findall(java_string)
    trimmed_comments = []
    for comment in multiline_comments:
        trimmed_comments.append(comment.strip().strip('* '))
    return trimmed_comments


def list_javadoc_comments(java_string):
    """Count the number of javadoc comments in the java_string."""
    pattern = re.compile(JAVADOC_COMMENT_RE, re.MULTILINE)
    tag_nixed_string = nix_javadoc_tags(java_string)
    multiline_comments = pattern.findall(tag_nixed_string)
    trimmed_comments = []
    for comment in multiline_comments:
        trimmed_comments.append(comment.strip().strip('* '))
    return trimmed_comments


def get_all_comments(java_string):
    """Return tuple of all comments in the java_string. """
    return (list_singleline_java_comments(java_string),
            list_multiline_java_comments(java_string),
            list_javadoc_comments(java_string))


def count_singleline_java_comments(java_string):
    """Count the number of singleline Java comments in the java_string."""
    pattern = re.compile(SINGLELINE_COMMENT_RE_JAVA, re.MULTILINE)
    singleline_comments = pattern.findall(java_string)
    return len(singleline_comments)


def count_multiline_java_comments(java_string):
    """Count the number of multiline Java comments in the java_string."""
    pattern = re.compile(MULTILINE_COMMENT_RE, re.MULTILINE)
    multiline_comments = pattern.findall(java_string)
    return len(multiline_comments)


def count_javadoc_java_comments(java_string):
    """Count the number of javadoc Java comments in the java_string."""
    pattern = re.compile(JAVADOC_COMMENT_RE, re.MULTILINE)
    javadoc_comments = pattern.findall(java_string)
    return len(javadoc_comments)


def ratio_of_singleline_comments(java_string):
    """Get the ratio of singleline comments to the
        number of lines in the Java source code."""
    total_number_of_lines = java_parser.get_number_of_lines(java_string)
    number_of_singleline_comments = count_singleline_java_comments(java_string)
    return float(number_of_singleline_comments / total_number_of_lines)


def ratio_of_multiline_comments(java_string):
    """Get the ratio of multiline comments to the
        number of lines in the Java source code."""
    total_number_of_lines = java_parser.get_number_of_lines(java_string)
    number_of_multiline_comments = count_multiline_java_comments(java_string)
    return float(number_of_multiline_comments / total_number_of_lines)
<<<<<<< HEAD
=======


def ratio_of_javadoc_comments(java_string):
    """Get the ratio of javadoc comments to the
        number of lines in the Java source code."""
    total_number_of_lines = java_parser.get_number_of_lines(java_string)
    number_of_javadoc_comments = count_javadoc_java_comments(java_string)
    return float(number_of_javadoc_comments / total_number_of_lines)


def get_ratios_of_comments(java_string):
    """Return dictionary of comment ratios in the java_string."""
    return {
        "singleline": round(ratio_of_singleline_comments(java_string), 2),
        "multiline": round(ratio_of_multiline_comments(java_string), 2),
        "javadoc": round(ratio_of_javadoc_comments(java_string), 2)}
>>>>>>> origin
