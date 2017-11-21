import sys

import github_clone_all
import parse_args
import defaults
from parse_comments import CommentParser

if __name__ == "__main__":
    args = parse_args.parse_args(sys.argv[1:])
    print(args)
    if args.get is True and defaults.PROJECT == "" and args.project == "":
        print("\tERROR: '--get' requires either a default project name or a supplied '--project' flag")
        quit()
    if args.get is True:
        github_clone_all.get_repositories(args.project, args.prefix, args.token, args.out)

    with open('./java/HelloWorld.java', 'r') as java_file:
        java_string = java_file.read()

    comments = CommentParser.list_singleline_java_comments(java_string)
    print("\nSingleline comments\n-------------------")
    for comment in comments:
        print(comment)
    print("Number of singleline comments: " + str(CommentParser.count_singleline_java_comments(java_string)))

    comments = CommentParser.list_multiline_java_comments(java_string)
    print("\nMultiline comments\n------------------")
    for comment in comments:
        print(comment)
    print("Number of multiline comments: " + str(CommentParser.count_multiline_java_comments(java_string)))
