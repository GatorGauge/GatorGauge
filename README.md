# GatorGauge

GatorGauge is a tool made for professors to easily gain information on
abs and practicals completed by their classes. GatorGauge enables professors
to download and analyze the information in student repositories in order to
gain knowledge on how long the projects took, the average number of commits,
where students had the most difficulty. GatorGauge analyzes README files,
commits, source code and source code comments. This tool can be used by
future students as well, allowing them to gain the same information about
the course work.

## Installation

GatorGauge is a python 3 program and, therefore, uses
[pip](https://pip.pypa.io/en/stable/installing/) for installation. Type the
following commands before running the program:

```
pip3 install --upgrade pip
```

```
pip3 install -r requirements.txt
```

## Initial Setup

Ensure that you have installed gspread and oauth2client is installed in the root
directory of the repository. In the terminal use the command:

```shell
python3 -m pip install --user gspread oauth2client
```

## Config.ini

Default Variables. Do not place the variables inside of "".
Since the config.ini file contains sensitive information due to the token,
it is not supplied in this repository. However, the program will automatically
create one for you upon first execution and prompt you to fill in the values.
Token and Project must receive valid inputs in order for the program to download
any repositories. These values can be edited from the command line with the command:

```
config edit
```

### Token

GitHub token allows the program to pull the repositories.
Once done, paste the token in token section. Must specify a project but PREFIX
is optional, and out defaults to current directory.

### Project

Name of the project to be pulled down.

### Keywords

Keywords used to filter for only repositories with the keywords in the name of
the repository.

### Out

Folder to place all of the downloaded repositories inside of. Defaults to
a directory named 'repos' which will be created upon running the get command.

## Execution

### Run GatorGage

Type ```python3 gatorGauge.py --token``` into the terminal with a Github access
token entered into the command line after --token. A token must be entered each
time the program is started for security reasons.

Enter project name? (y/n) ->- y
Enter project name

### Commands

Download the project(named in Config.ini or given with the config command).

```
get
```

Print the values in the config file or temporarily change the config values or if
the second config command is used the user can either edit the values in the config
file or reset the values back to their original state assuming the user does not
save the values after using config edit.

```
config
```

```
config <option>
```

List all repositories if no arguments are given or all files in a given repository.

```
list
```

```
list <repo name>
```

Perform sentiment analysis and gensim on the given target (source, comments, commits,
reflection).

```
analyze <target>
```

Quit the program.

```
quit
```

## Usage

GatorGauge analyzes Computer Science students' labs and practicals. Natural
language processing is used in order to create visual displays for professors
and future students to gain information on the work.

### Process

GatorGauge should retrieve the entirety of a specified repository's commit logs,
as well as all current files, and then analyze the comments, code, and commit
logs as follows.

#### Comments

GatorGauge will, across all downloaded repositories, analyze and return to the
viewer a refined list for each single-line and multi-line comments for all
program files in the given repository, as well as count an average number of
single-line and multi-line comments per file. It will also calculate the average
ratios between lines of each and lines of source code.
Finally, comments analysis will provide Gensim sentiment analysis for
single-line comments and topic analysis for multi-line comments.

#### Code

GatorGauge will calculate the average number of and standard deviation of each
of:

Variables
Methods
Classes
Lines

#### Commit Logs

GatorGauge reads in all commits as text and returns Gensim and LDA analysis for
how often words are repeated and how generally positive and/or negative the
phrasings are.

## Testing

### Functions Tested

### Running the Test Suite

To run the test suite, run the following commands in the rood directory of
GatorGauge:

```
pytest tests
```

Or, depending on the operating system:

```
python3 -m pytest tests
```

### Automatic Linting

The linting automatically checks to ensure code is up to pep8 standards. If
linting errors occur, run the following command to perform automatic linting. If
there are errors that the tool cannot fix, the test suite will tell you where
and what the errors are so that you may go to the location and fix them.

```
autopep8 --in-place --aggressive *.py
```

### Test Coverage

Test coverage is being addressed by Coveralls so that when Travis-CI runs, it can
evaluate the coverage of the test suite. When testing Gensim, the weight of the
topics of related words could not be tested. This is because randomness it built
into Gensim and thus the answers would not be consistant.

### Activating Travis-CI

Travis can only be implamented by admin accounts. Admin users can activate Travis
by creating a travis.yml in the project's root
directory.

## Questions or Comments

Any problems or suggestions regarding GatorGauge can be written in the issue
link at the top of the site.
