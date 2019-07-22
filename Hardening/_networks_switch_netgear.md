# DHCP Snooping
	(https://kb.netgear.com/21814/How-do-I-configure-Dynamic-Host-Configuration-Protocol-DHCP-snooping-using-CLI-commands-on-my-managed-switch)

	ip dhcp snooping

	Enable DHCP snooping in a VLAN.

	(Netgear Switch) (Config)# ip dhcp snooping vlan 1

	Configure the port through which the DHCP server is reached as trusted.

	(Netgear Switch) (Config)# interface 1/0/1
	(Netgear Switch) (Interface 1/0/1)# ip dhcp snooping trust

	==> Does not seem applicable to all switches but :
		Managed - Volume (8)
		M4100-26-POE (FSM7226Pv1h1)
		M4100-26G (GSM7224v2h2)
		M4100-26G-POE (GSM7226LPv1h1)
		M4100-50-POE (FSM7250Pv1h1)
		M4100-50G (GSM7248v2h2)
		M4100-50G-POE+ (GSM7248Pv1h1)
		M4100-D10-POE (FSM5210Pv1h1)
		M4100-D12G (GSM5212v1h1)
		Managed - Premium (20)
		M4200-10MG-PoE+ (GSM4210P)
		M4300-12X12F (XSM4324S)
		M4300-24X (XSM4324CS)
		M4300-28G (GSM4328S)
		M4300-28G-PoE+ (GSM4328PA)
		M4300-28G-PoE+ (GSM4328PB)
		M4300-48X (XSM4348CS)
		M4300-52G (GSM4352S)
		M4300-52G-PoE+ (GSM4352PA)
		M4300-52G-PoE+ (GSM4352PB)
		M4300-8X8F (XSM4316S)
		M5300-28G (GSM7228S)
		M5300-28G-POE+ (GSM7228PSv1h2)
		M5300-28G3 (GSM7328Sv2h2)
		M5300-28GF3 (GSM7328FSv2)
		M5300-52G (GSM7252S)
		M5300-52G-POE+ (GSM7252PSv1h2)
		M5300-52G3 (GSM7352Sv2h2)
		M7100-24X (XSM7224)
		M7300-24XF (XSM7224S)

# Dynamic ARP Inspection
	(https://kb.netgear.com/21809/How-do-I-configure-Dynamic-ARP-inspection-DAI-using-CLI-commands-on-my-managed-switch)


	Enable ARP inspection in VLAN 1.

	(Netgear Switch) (Config)# ip arp inspection vlan 1

	Now all ARP packets received on ports that are members of the VLAN are copied to the CPU for ARP inspection. If there are trusted ports, you can configure them as trusted in the next step. ARP packets received on trusted ports are not copied to the CPU.

	Configure port 1/0/1 as trusted.

	(Netgear Switch) (Config)# interface 1/0/1
	(Netgear Switch) (Interface 1/0/1)# ip arp inspection trust

	Now ARP packets from the DHCP client go through because there is a DHCP snooping entry; however ARP packets from the static client are dropped. It can be overcome by static configuration.

	==> Does not seem applicable to all switches but :
		Managed - Volume (8)
		M4100-26-POE (FSM7226Pv1h1)
		M4100-26G (GSM7224v2h2)
		M4100-26G-POE (GSM7226LPv1h1)
		M4100-50-POE (FSM7250Pv1h1)
		M4100-50G (GSM7248v2h2)
		M4100-50G-POE+ (GSM7248Pv1h1)
		M4100-D10-POE (FSM5210Pv1h1)
		M4100-D12G (GSM5212v1h1)
		Managed - Premium (20)
		M4200-10MG-PoE+ (GSM4210P)
		M4300-12X12F (XSM4324S)
		M4300-24X (XSM4324CS)
		M4300-28G (GSM4328S)
		M4300-28G-PoE+ (GSM4328PA)
		M4300-28G-PoE+ (GSM4328PB)
		M4300-48X (XSM4348CS)
		M4300-52G (GSM4352S)
		M4300-52G-PoE+ (GSM4352PA)
		M4300-52G-PoE+ (GSM4352PB)
		M4300-8X8F (XSM4316S)
		M5300-28G (GSM7228S)
		M5300-28G-POE+ (GSM7228PSv1h2)
		M5300-28G3 (GSM7328Sv2h2)
		M5300-28GF3 (GSM7328FSv2)
		M5300-52G (GSM7252S)
		M5300-52G-POE+ (GSM7252PSv1h2)
		M5300-52G3 (GSM7352Sv2h2)
		M7100-24X (XSM7224)
		M7300-24XF (XSM7224S)
