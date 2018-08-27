#Helpful pip Commands
pip help
pip help install

pip search package_name     This will show info about the package
pip search Pympler

pip install Pympler         This will install the package Pympler

pip list                    This will list all the installed packages

pip uninstall Pympler       This will uninstall Pympler package

Usually all the packages that get listed with 'pip list' shows the package name along with the versions.
To check out if the package is outdated or not, we type:
pip list --outdated
OR
pip list --o            This will list the packages which are outdated along with the current version and the latest available version

To update the outdated version with the latest version, type:
pip install -U package_name


In case we want someone to work on a same project as ours and we want them to get those packages installed as present on our machine we can send them the list of packages as:
pip freeze > requirements.txt     This command will output  all our packages and version numbers and the requirement format within the requirements.txt file which we can send over
cat requirements.txt                This will show the output of the file

when someone wants to install the packages mentioned in the requirements file, then that person can do:
cat requirements.txt        This will show the package list
pip install -r requirements.txt     Here -r denotes that we want to read a requirements file. This command will install the packages
