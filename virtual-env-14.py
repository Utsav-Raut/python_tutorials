# virtualenv is a way in which we can separate different python environments for different projects.
# Thus if separate projects have separate dependencies on different versions of a particular module, then upgrading that module globally may break some code. Creating virtualenvs allows us to have separate environments and that we can upgrade the module for a particular environment.
To install virtualenv:
pip install virtualenv

mkdir Environments
cd !$                   Goes into Environments folder
ls                      Shows empty folder

virtualenv project1_env     This creates a new environment. In my machine i had to do a 'sudo apt install virtualenv' as well

source project1_env/bin/activate    This takes us to our new environment

Now we can do:
which python
which pip
pip list
All this shows the contents of the project1_env

deactivate      This takes us out of our virtual environment

rm -rf project1_env/        This deletes a virtual environment
