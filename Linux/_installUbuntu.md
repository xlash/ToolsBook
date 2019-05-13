#!/usr/bin/env sh
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
