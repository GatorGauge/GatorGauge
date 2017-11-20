import sys

import github_clone_all
import parse_args
import defaults
import read_markdown
if __name__ == "__main__":
    args = parse_args.parse_args(sys.argv[1:])
    print(args)
    if args.get is True and defaults.PROJECT == "" and args.project == "":
        print("\tERROR: '--get' requires either a default project name or a supplied '--project' flag")
        quit()
    if args.get is True:
        github_clone_all.get_repositories(args.project, args.prefix, args.token, args.out)
    print(read_markdown.read_markdown("test.md"))
