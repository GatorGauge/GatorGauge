""" main file in the GatorGauge system """
import sys
# local imports
import github_clone_all
import parse_args
import defaults
import read_markdown

if __name__ == "__main__":
    args = parse_args.parse_args(sys.argv[1:])
    # checks if the required information is entered
    if args.token == "" and defaults.TOKEN == "" and args.get is True and defaults.PROJECT == "" and args.project == "":
        print("\tERROR: A Github token is required for the system to run. Please enter one in either config.ini or in the command line with the --token flag")
        print("\tERROR: '--get' requires either a default project name (in config.ini) or a supplied '--project' flag")
        quit()
        
    elif args.token == "" and defaults.TOKEN == "":
        print("\tERROR: A Github token is required for the system to run. Please enter one in either config.ini or in the command line with the --token flag")
        quit()
        
    elif args.get is True and defaults.PROJECT == "" and args.project == "":
        print("\tERROR: '--get' requires either a default project name in config.ini or supplied with the '--project' flag")
        quit()
        
    if args.get is True:
        github_clone_all.get_repositories(args.project, args.prefix, args.token, args.out)
    markdown = read_markdown.read_markdown("test.md")
    for line in markdown:
        print(line)
