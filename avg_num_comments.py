import java_to_string as j
import java_parser as p
import statistics
import os

def avg_num_comments():
    singleLine = 0
    multiLine = 0
    javadoc = 0

    for eachLine in allLines:
        if eachLine != " " :
                eachLine = eachLine.replace(" ",""); #remove space
                eachLine = self.trim(eachLine);      #remove tabIndent
                if  (iscomment==False):
                    if(eachLine.strip().startswith("//")): #LINECOMMENT 
                        singleLine += 1;
                    if eachLine == "":
                        blankCount += 1;
                    if(eachLine.strip().startswith("/*")):
                        javadoc += 1;
                        if(not eachLine.strip().endswith("*/")):
                            iscomment=True
                else :
                    commentCount += 1;
                    if(eachLine.find("*/")):
                        iscomment=False
