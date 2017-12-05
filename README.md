# GatorGauge

GatorGauge is a tool made for professors to easily gain information on
abs and practicals completed by their classes. GatorGauge enables professors
to download and analyze the information in student repositories in order to
gain knowledge on how long the projects took, the average number of commits,
where students had the most difficulty. This tool can be used by future
students as well, allowing them to gain the same information about the course
work.

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
it is not supplied in this repository. Before running the program the user must
create a new file in their local root directory called config.ini

Paste the following into this new file:

```
[Token]
; Github access token, KEEP SECRET!!!!
TOKEN =
[Project]
; Project to pull
PROJECT =
[Prefix]
; Prefix to look for to narrow
PREFIX =
[Out]
; default: current directory
OUT = .
```

Once done, paste the token in token section. Must specify a project but PREFIX
is optional, and out defaults to current directory.

### Token

GitHub token allows the program to pull the repositories.

### Project

Name of the project to be pulled down.

### Prefix

Gets every repository in the project that starts with the prefix.

### Out

Folder to place all of the downloaded repositories inside of. Defaults to
current directory and names the repository the project name.

## Execution

### Requirements

To get requirements, use the command

```
pip3 install --user -r requirements.txt
```

### Basic Execution

Type ```python3 gatorGauge.py```, will cause errors if there are no values in
config.ini for Token and Project or if they are not supplied with the command
line arguments.

### Execution Flags

Download the project(named in Config.ini or supplied with the ```--project``` flag)

```
--get
```

Project to download

```
--project
```

Prefix of the repository to download

```
--prefix
```

Token to allow for the program to download the repositories

```
--token
```

Location to place downloaded repositories

```
--out
```

## Usage

GatorGauge analyzes Computer Science students' labs and practicals. Natural language
processing is used in order to create visual displays for professors and future
students to gain information on the work.

### Process

GatorGauge should retrieve the entirety of a specified repository's commit logs,
as well as all current files, and then analyze the comments, code, and commit
logs as follows.

#### Comments

GatorGauge will analyze and return to the viewer a refined list for each single-line
and multi-line comments, as well as count them and calculate the ratios between
lines of each and lines of source code.

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
evaluate the coverage of the test suite.

### Activating Travis-CI

Travis can only be implamented by admin accounts. Admin users can activate Travis
by creating a travis.yml in the project's root
directory.

## Questions or Comments

Any problems or suggestions regarding GatorGauge can be written in the issue
link at the top of the site.
