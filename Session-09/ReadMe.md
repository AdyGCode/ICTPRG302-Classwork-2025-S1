# Working with Version Control

If you want a base to work with for a project in ICTPRG302, or any other 
Python based programming cluster, then you may use these instructions.

## Setting Up

Create a `Source/Repos` folder, change into the `Source/Repos` folder.

```shell
cd ~
mkdir -p Source/Repos
cd Source/Repos
```

> ### 🛑 Important: 
> 
> When working in Room 3-06 at TAFE, we need to use:
> 
> ```shell
> cd /c/Users/YOUR_USER_NAME
> mkdir -p Source/Repos
> cd Source/Repos
> ```
> 
> Remember to replace YOUR_USER_NAME with the username you logged into the 
> PC with.


### Clone the Base Repo

Clone the Base Project Repository, replacing the `XXX` with **YOUR** initials.

```shell
git clone https://github.com/AdyGCode/AJG-ICTPRG302-Project-2025-s1.git XXX-ICTPRG302-Project-2025-s1
```

### Move into the Repo, and Activate Python Virtual Environment

Change into the new folder, add & activate Python virtual environment:

```shell
cd XXX-ICTPRG302-Project-2025-s1
python -m venv .venv
source .venv/Scripts/activate
```

> ### Note:
> Mac and Linux users will need to use `source .venv/bin/activate` instead 
> of `source .venv/Scripts/activate` for Windows users.

## Running the Application

To execute the program on the command line use:

```shell
python PYTHON_FILENAME.py
```

> ### Students TODO
> 
> Replace the `PYTHON_FILENAME` with the name of your python
> then delete this TODO.


---

## JetBrains PyCharm Hints

- Use the `.ignore` plugin to help add commonly ignored files in version control
- Make the default folder a `Source/Repos` folder

### Installing the _.ignore_ Plugin

- Open PyCharm
- Press <kbd>CTRL</kbd>+<kbd>ALT</kbd>+<kbd>S</kbd> (PC)<br> 
  or <kbd>CTRL</kbd>+<kbd>,</kbd> (MacOS) to open settings
- Click on Plugins option
- Click on Marketplace
- Locate **.ignore** in list, and click install
- Click OK to save the settings

You may have to restart the IDE at this point.

### Create a root .gitignore file

- Click on the project name in Pycharm
- Right mouse click the project name
- Select New...
- Select **.ignore** File (bottom of menu)
- Select & Click on **.gitignore** (top of menu)
- Tick the following options to add to the `.gitignore` file
  - [x] Backup
  - [x] Csharp
  - [x] Linux
  - [x] MicrosoftOffice
  - [x] OSX
  - [x] MacOS
  - [x] Python
  - [x] VirtualEnv
  - [x] VisualStudioCode
  - [x] Windows
- Tick "Generate without duplicates"
- Click Generate

### Allow Zoom of Editor

- Open PyCharm
- Press <kbd>CTRL</kbd>+<kbd>ALT</kbd>+<kbd>S</kbd> (PC)<br> 
  or <kbd>CTRL</kbd>+<kbd>,</kbd> (MacOS) to open settings
- Click on `>` next to Editor
- Click on General
- Tick "Change font size with CTRL+Mouse Wheel"
- Optionally select "All Editors"
- Click OK to save the settings

You will now be able to <kbd>CTRL</kbd>+Mouse Wheel to change editor font 
sizes.







# File Exercises Continued


These exercises are for you to use as practice.

Make mistakes, correct them and enjoy the success as you complete each one.

If you are stuck, then ask for assistance from your lecturer, or from the
lecturer who is holding a Workshop Lab.

## Text files and other assets

The text files and other assets (for example, images) are saved in an 
`assets` folder within this session's folder.

Sometimes files will be linked to from previous session folders to reduce 
duplication and errors from said duplication. 


## Filename: exercise-01.py

## Filename: exercise-02.py

## Filename: exercise-03.py

## Filename: exercise-04.py

## Filename: exercise-05.py

## Filename: exercise-06.py


# Acknowledgement

Some of these exercises are based on the resources from
[ncce.io/tcc](ncce.io/tcc). They are licensed under the Open Government
Licence, version 3. For more information on this licence,
see [ncce.io/ogl](ncce.io/ogl).

More exercises will be available in [Session-08](../Session-08).
