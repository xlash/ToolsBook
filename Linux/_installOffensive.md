# Set up Java path
export JAVA_HOME=$(dirname $(dirname $(readlink $(readlink $(which javac)))))
export PATH=$PATH:$JAVA_HOME/bin
export CLASSPATH=.:$JAVA_HOME/jre/lib:$JAVA_HOME/lib:$JAVA_HOME/lib/tools.jar

# Aliases
alias chrome_burp_proxy='chromium --proxy-server="https=127.0.0.1:8080;http=127.0.0.1:8080"'


# Install searchsploit
sudo apt update && sudo apt -y install exploitdb



# Manual install for Burp
Install BurpSmartScanner (dirbuster replacement)
sudo apt -y install jython
echo ('configure manuall jython in burp extender options')
