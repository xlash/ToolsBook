sudo apt install virtualenv
export WORKON_HOME=~/PyEnvs/
pip install virtualenvwrapper
source /usr/local/bin/virtualenvwrapper.sh

mkvirtualenv PY_3.7 --python=`which python3.7`
pip install bpython ipython
