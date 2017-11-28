import java_to_string.py
import re


def test_remove_comments(javaString):
    """Test if the functions removes all commensts
    from the Java source code"""
     assert javaString = re.sub(re.compile("(?<=/\*).*?(?=\*/)",re.DOTALL ) ,"" ,javaString)
     assert javaString = re.sub(re.compile("//.*?\n" ) ,"" ,javaString)
     assert javaString = javaString.replace("\n", "")
     assert javaString = javaString.replace("/**/","")
