#!/usr/bin/env sh

sudo apt-get install apt-transport-https

### Install SDKman for Java and Gradle build
echo "Install SDKMAN https://sdkman.io/install, or wait 2 secs to automatically do it"
curl -s "https://get.sdkman.io" > /tmp/sdkman.sh
less /tmp/sdkman.sh
echo "Wait 5 seconds if you want to run the downloaded shell script automatically"
sleep 5
bash /tmp/sdkman.sh

$ source "$HOME/.sdkman/bin/sdkman-init.sh"
### Install gradle
echo "Installing gradle"
sdk install gradle 5.4

### Threat Modeling
mkvirtualenv ThreatModeling
workon ThreatModeling
pip install pytm
sudo apt-get install graphviz


### Oh my zsh
sudo apt install zsh curl
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

### exfat for Windows large disks
sudo add-apt-repository universe
sudo apt install exfat-fuse exfat-utils

