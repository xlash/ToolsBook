# Will extract the data field only, for example in ICMP
tshark -r ~/<FILENAME.pcap> -T fields -e data

