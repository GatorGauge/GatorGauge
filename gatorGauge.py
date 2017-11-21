import sys

import github_clone_all
import parse_args
import defaults
if __name__ == "__main__":
    args = parse_args.parse_args(sys.argv[1:])
    defined_commands = {"get", "project", "prefix", "token", "out", "help", "quit"}
    fSet = frozenset(defined_commands)
    print(args)
    if args.get is True and defaults.PROJECT == "" and args.project == "":
        print("\tERROR: '--get' requires either a default project name or a supplied '--project' flag")
        quit()
    if args.get is True:
        github_clone_all.get_repositories(args.project, args.prefix, args.token, args.out)
