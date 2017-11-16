(Basic README do not judge)
# GatorGauge

Downloads and analyzes the information in student repositories (currently only downloads).

## Config.ini

Default Variables. DO not place the variables inside of "".

### Token

Github token allows the program to pull the repositories.

### Project

Name of the project to be pulled down.

### Prefix

Gets every repository in the project that starts with the prefix.

### Out

Folder to place all of the downloaded repositories inside of. Defaults to current directory and names the 
repository the project name.

# Execution

## requirements

To get requirements, use the command 
```
pip install --user -r requirements.txt
```
## Basic Execution

Type ```python3 gatorGauge.py```, will cause errors if there are no values in config.ini for Token and Project 
or if they are not supplied with the command line arguments.

## Execution Flags

```
--get
```
Download the project (named in Config.ini or supplied with the ```--project``` flag)

```
--project
```
Project to download

```
--prefix

```
Prefix of the repository to download

```
--token
```
Token to allow for the program to download the repositories

```
--out
```
Location to place downloaded repositories


















