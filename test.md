# Accelegator

Accelegator is an adaptive advising tool written to help advisors help their
students. The program takes information on individual and multiple advisees,
analyzing, compiling, and displaying it for the advisor in a helpful manner.
The user need only send out questionnaires to the advisees and, once submitted,
Accelegator will read in and use the information for the user.

## Installation

Accelegator is a python 3 program and, therefore uses [pip][1] for installation.
Type the following commands before running:

[1]: https://pip.pypa.io/en/stable/installing

```shell
pip3 install --upgrade pip
pip3 install -r requirements.txt
```

## Initial Setup

Create a Google Sheets spreadsheet and a Google Form in Google Drive.  After you
have at least one submission of the Form, you can go to the responses tab and
click on the green icon with the white cross through it.  This will enable you
to link the Sheet to the Form.  You can either create a new Sheet or link to a
preexisting one.  If you need to change the destination, you can click on the
three dot icon menu to the right of the green icon and select "Select response
destination".

Open the `.json` file in the `accelegator` repository and find the `"client-email"`.
Copy the quoted text that looks like an email address.  Return to the Sheet and
open the sharing options.  Paste the address and click send.

Within `defaults.py`, update the `DEFAULT_WORKBOOK` constant to the name of your
Sheet.

------

## Usage

Accelegator analysis advisee questionnaires and uses natural language
processing to compile and sort the information for
advisors.

Along with the NLP, Accelegator uses Latent Dirichlet Allocation (LDA) to
analyze data by specific question, every question, specific person, every
person or all the data with textual results.

How to run:
`` gensim <target> <field> ``

Where target = `person` or `question`
and field = `<email>@allegheny.edu` or `question number` or leave this blank for
analysis for every entry in the target.

In order to run, at minimum, ``<target>`` needs to be declared. This is also
case sensitive.

### Legalities and Privacy

See LegalitiesPrivacy_Accelegator.md file for information.

### Search Queries and Field

Accelegator in an interactive information program. Once the general
information has been compiled, users may search for more specified information
on advisees including groups of similar advisees, skills, and more.

### Commands

Accelegator has command options for a better user experience such as help and
quit.

## Testing

Functions have been tested throughout this system to allow conformation that
the system is working correctly.

### Running the Test Suite

To run the test suite, run the following commands in Accelegator's root
directory:

```shell
pytest tests
```

### Automatic Linting

The linting automatically checks to ensure Accelegator's code is up to pep8
standards. If linting errors occur run the following command to perform
automatic linting:

```shell
autopep8 --in-place --aggressive --aggressive *.py
```

### Test Coverage

Test coverage is being addressed by Coveralls so that when Travis-CI runs, it
can evaluate the overall coverage of the test suite.

### Activating Travis-CI

Travis can only be implemented by admin accounts. Admin users can activate
Travis by creating a .travis.yml file in the project's root directory.

## Questions or Comments

Any problems regarding Accelegator can be written in the issues link at the
top of the site.
