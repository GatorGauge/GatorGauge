# Expanding gkapfham's gatorgrader/gatorgrader_comments.py
# References:
# https://stackoverflow.com/questions/15423658/regular-expression-for-single-line-comments
# https://blog.ostermiller.org/find-comment
"""Parse comments from a Java source code file."""
import re


class CommentParser:
    FILE_SEPARATOR = "/"

    MULTILINECOMMENT_RE = r'\/\*+([\s\S]*?)\*+\/'  # new regex
    SINGLELINECOMMENT_RE_JAVA = r'^(?:[^"/\\]|\"(?:[^\"\\]|\\.)*\"|/(?:[^/"\\]|\\.)|/\"(?:[^\"\\]|\\.)*\"|\\.)*//(.*)$'

    singleline_comments = None
    multiline_comments = None


    @classmethod
    def list_singleline_java_comments(cls, java_string):
        """Return list of singleline Java comments in the java_string."""
        if cls.singleline_comments is not None:
            return cls.singleline_comments
        else:
            pattern = re.compile(cls.SINGLELINECOMMENT_RE_JAVA, re.MULTILINE)
            cls.singleline_comments = pattern.findall(java_string)
            for comment in cls.singleline_comments:
                comment = comment.strip()
            return cls.singleline_comments


    @classmethod
    def list_multiline_java_comments(cls, java_string):
        """Count the number of multiline Java comments in the java_string."""
        if cls.multiline_comments is not None:
            return cls.multiline_comments
        else:
            pattern = re.compile(cls.MULTILINECOMMENT_RE, re.MULTILINE)
            cls.multiline_comments = pattern.findall(java_string)
            for comment in cls.multiline_comments:
                comment = comment.strip()
            return cls.multiline_comments


    @classmethod
    def count_singleline_java_comments(cls, java_string):
        """Count the number of singleline Java comments in the java_string."""
        if cls.singleline_comments is not None:
            return len(cls.singleline_comments)
        else:
            pattern = re.compile(cls.SINGLELINECOMMENT_RE_JAVA, re.MULTILINE)
            cls.singleline_comments = pattern.findall(java_string)
            for comment in cls.singleline_comments:
                comment = comment.strip()
            return len(cls.singleline_comments)


    @classmethod
    def count_multiline_java_comments(cls, java_string):
        """Count the number of multiline Java comments in the java_string."""
        if cls.multiline_comments is not None:
            return len(cls.multiline_comments)
        else:
            pattern = re.compile(cls.MULTILINECOMMENT_RE, re.MULTILINE)
            cls.multiline_comments = pattern.findall(java_string)
            for comment in cls.multiline_comments:
                comment = comment.strip()
            return len(cls.multiline_comments)
