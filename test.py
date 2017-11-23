from io import StringIO  # Python3
import sys
 
# Store the reference, in case you want to show things again in standard output
old_stdout = sys.stdout
 
# This variable will store everything that is sent to the standard output
result = StringIO()
 
sys.stdout = result
 
# Here we can call anything we like, like external modules, and everything that they will send to standard output will be stored on "result"
 
sys.stdout.write("WTF IS PYTHON's ISSUE")

 
# Redirect again the std output to screen
 
sys.stdout = old_stdout
 
# Then, get the stdout like a string and process it!
 
result_string = result.getvalue()

print(result_string)