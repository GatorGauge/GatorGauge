# Expanding gkapfham's gatorgrader/gatorgrader_comments.py
# References:
# https://stackoverflow.com/questions/15423658/regular-expression-for-single-line-comments
# https://blog.ostermiller.org/find-comment
"""Parse comments from a Java source code file."""
import re


FILE_SEPARATOR = "/"

MULTILINECOMMENT_RE = r'\/\*+([\s\S]*?)\*+\/'  # new regex
SINGLELINECOMMENT_RE_JAVA = r'^(?:[^"/\\]|\"(?:[^\"\\]|\\.)*\"|/(?:[^/"\\]|\\.)|/\"(?:[^\"\\]|\\.)*\"|\\.)*//(.*)$'


def list_singleline_java_comments(java_string):
    """Return list of singleline Java comments in the java_string."""
    pattern = re.compile(SINGLELINECOMMENT_RE_JAVA, re.MULTILINE)
    singleline_comments = pattern.findall(java_string)
    for comment in singleline_comments:
        comment = comment.strip()
    return singleline_comments


def list_multiline_java_comments(java_string):
    """Count the number of multiline Java comments in the java_string."""
    pattern = re.compile(MULTILINECOMMENT_RE, re.MULTILINE)
    multiline_comments = pattern.findall(java_string)
    for comment in multiline_comments:
        comment = comment.strip()
    return multiline_comments


def count_singleline_java_comments(java_string):
    """Count the number of singleline Java comments in the java_string."""
    pattern = re.compile(SINGLELINECOMMENT_RE_JAVA, re.MULTILINE)
    singleline_comments = pattern.findall(java_string)
    for comment in singleline_comments:
        comment = comment.strip()
    return len(singleline_comments)


def count_multiline_java_comments(java_string):
    """Count the number of multiline Java comments in the java_string."""
    pattern = re.compile(MULTILINECOMMENT_RE, re.MULTILINE)
    multiline_comments = pattern.findall(java_string)
    for comment in multiline_comments:
        comment = comment.strip()
    return len(multiline_comments)
