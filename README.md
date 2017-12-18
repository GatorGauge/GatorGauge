# GatorGauge

GatorGauge is a tool that allows professors to easily gain information on
practicals and laboratory assignments completed by their students. GatorGauge
does this by enabling professors to download and analyze the information in
student repositories. In doing this information is gained on how long the
projects took, the average number of commits, and where students had the most
difficulty. GatorGauge gains this information by using natural language
processing to analyzes README files, commits, source code, and comments. This
tool can be used by future students as well, allowing them to gain the same
information about the course work.

## Installation

GatorGauge is a python 3 program and, therefore, uses [pip][1] for handling
dependencies. The following commands must be executed in the terminal window
before running the system:

[1]: https://pip.pypa.io/en/stable/installing/

```
pip3 install --upgrade pip
pip3 install --user -r requirements.txt
```

## Config.ini

GatorGauge uses default Variables. Do not wrap variables in quotes as the
program will automatically create one for users upon its first execution and
will prompt users to fill in the necessary values. GatorGauge must receive
valid inputs in order for the program to download repositories. These values
can be edited from the command line with the command:

```
config edit
```

### Project

Name of the project to be pulled down.

### Keywords

Keywords are used as a filter only for repositories with the keywords in the
name of the repository.

### Out

There is a folder in which to place all of the downloaded repositories in.
The folder defaults to a directory named 'repos' which will be created upon
running the get command.

## Execution

### Run GatorGauge

Once everything is properly installed, GatorGauge is ready to run. To begin,
type `python3 gator_gauge.py --token` into the terminal with a GitHub
access token entered into the command line after `--token`. A token must be
entered each time the program is started - for security purposes.

The following warning message may apper when running GatorGauge:

```
UserWarning: The twython library has not been installed. Some functionality
from the twitter package will not be available.
  warnings.warn("The twython library has not been installed. "
```

The package twython is an nltk dependency, but is not necessary for this
program.  You can disregard this warning message or you can install twython
using pip.

When users first run the program and a new config file needs to be generated
these questions will be asked:

```
Enter project name? (y/n)

  If yes, enter the project name

Enter keywords (y/n) --> this is optional, but if key words are entered they
must be separate with a comma.

Enter out directory? (y/n) --> directory where everything will get downloaded
to.

  Enter new directory name (repos is the default)

Save changes (y/n) --> should enter yes for the first run.
```

### Commands

#### REPL Commands

The command `get` downloads the project (named in `Config.ini` or given with
the config command).

The command `config` prints the values in the config file, temporarily
changes the config values, or if the second config command is used,
the user can either edit the values in the config file or reset the
values back to their original state - assuming the user does not save
the values after using config edit.

The `list` command and the `list <repo name>` command lists all
repositories if no arguments are given or all files in the given repository.

The `analyze <target>` command performs sentiment analysis and Gensim on the
given target (source, comments, commits, reflection).

The `quit` command quits the program.

## Features

GatorGauge is a fully featured program. Upon running, a command menu will be
provided for user convenience. GatorGauge allows users to download and
analyze all labs, reflections, and practicals or select sets, including a
specific student's work or specific labs, parcticals, and/or reflections.
The analyzed information is displayed for users in an easy to read visual
graph.

### Command Menu

The commands are listed and explained above - under "REPL commands".

### Repository Selection

Users may select...

### Visual Representation

How to read graphs

## Usage

### Process

GatorGauge retrieves the entirety of a specified repository's commit
logs, as well as all current files. GatorGauge then analyze the comments,
code, and commit logs.

#### Reflections

GatorGauge analyzes student reflections from downloaded repositories. It uses
Gensim analysis on relevant topics within the reflection documents. Sentiment
analysis is also implemented by the system in order to obtain the overall
"feeling" in all the reflections on labs and/or practicals.

#### Comments

GatorGauge will, across all downloaded repositories, analyze and return to the
viewer a refined list for each single-line and multi-line comments. GatorGauge
will do this for all program files in the given repository, as well as count
the average number of single-line and multi-line comments per file. GatorGauge
will also calculate the average ratios between lines of source code. Finally,
comments analysis will provide Gensim sentiment analysis for single-line
comments and topic analysis for multi-line comments.

#### Code

GatorGauge will calculate the average number of and standard deviation of:

* Variables
* Methods
* Classes
* Lines

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

The linting process automatically checks to ensure that the code is up to PEP8
standards. If linting errors occur, run the following command to perform automatic
linting:

```
autopep8 --in-place --aggressive *.py
```

If there are errors that the tool cannot fix, the test suite will tell you
where and what the errors are so that you may go to their location and fix them.

### Test Coverage

Test coverage is being addressed by Coveralls so that when Travis-CI runs, it
can evaluate the coverage of the test suite. When testing Gensim, the weight of
the topics of related words could not be tested. This is because Gensim
intentionally adds some degree of randomness, and thus the results would not be
consistent.

### Activating Travis-CI

Travis can only be implemented by admin accounts. Admin users can activate
Travis by creating a `travis.yml` in the project's root directory.

## Road Map of the system

### Topic Modeling

#### Usage of Topic Modeling

The topic modeling for this project will be maintained by Nicholas Tocci. Topic
modeling for GatorGauge begins when gensim_analysis is given a list of strings.
Once this list is given it is then split of so that the list of strings given is
now a list of lists. Each list in the list of lists contains all of the words in
each specific sentence. This is then sent to the create_tokens function which
then analyzes each word in the lists. If the word contains profanity, is a
number, or is a very common word, the word is left out. If the word has any
special characters in it, the special character is then removed. Next the list
of tokens is made into a dictionary and a corpus using the Gensim library
and visualized using pyLDAvis.

#### Ways to achieve the best anlysis

The best way to get the best analysis is on a larger data set. This means that
the program should not be able to do a single student for a single lab. The LDA
will not provide a strong analysis as the amount of tokens being passes to it is
very small. The program should be outfitted so that the user can select that it
is all students for all labs, or all students for one lab. If all of the
students for one lab is selected, the user will have a very good understanding
of how the lab was perceived by the students and the most important parts of
that specific lab. If the user selects that analysis is done on all of the labs
for every single student, then the user will have a good understanding of how
hard the class is and what the largest topics are for the course.

#### Plans for the future

Plans for the future include instituting Word2Vec and Sense2Vec into the
gensim_anlysis system. This will allow for the ability to visualize how related
the words are. Sense2Vec will be used to help discern what the user means. I
will be researching other systems that could be used to give a better
visualization on the topic models. Lastly the system needs to be enhanced so
that it is easier for the user to complete every lab for every student.

## Questions or Comments

Any problems or suggestions regarding GatorGauge can be written in the issue
link at the top of the site.
