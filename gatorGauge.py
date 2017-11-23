import sys

import github_clone_all
import parse_args
import defaults
import file_list
if __name__ == "__main__":
    args = parse_args.parse_args(sys.argv[1:])
    if args.get is True and defaults.PROJECT == "" and args.project == "":
        print("\tERROR: '--get' requires either a default project name or a supplied '--project' flag")
        quit()
    if args.get is True:
        github_clone_all.get_repositories(args.project, args.prefix, args.token, args.out)
    
    if "--list" in sys.argv[1:]: # checks if --list was used in command line
        files = file_list.list_files(args.list, args.out) # list of files returned
        for file in files:
            print(file)