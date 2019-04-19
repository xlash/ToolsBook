#!/user/bin/env bash
workon OffensiveSec_v3
cd ~/
git clone https://github.com/RhinoSecurityLabs/pacu.git
mv pacu pacu_aws_exploitation_framework
cd pacu_aws_exploitation_framework
bash install.sh
