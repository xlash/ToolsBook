setuid bit indicates executable will run under owner's privileges.

The setuid bit
When the setuid bit is used, the behavior described above it's modified so that when an executable is launched, it does not run with the privileges of the user who launched it, but with that of the file owner instead. So, for example, if an executable has the setuid bit set on it, and it's owned by root, when launched by a normal user, it will run with root privileges. It should be clear why this represents a potential security risk, if not used correctly.

An example of an executable with the setuid permission set is passwd, the utility we can use to change our login password. We can verify that by using the ls command:
ls -l /bin/passwd
-rwsr-xr-x. 1 root root 27768 Feb 11  2017 /bin/passwd
How to identify the setuid bit? As you surely have noticed looking at the output of the command above, the setuid bit is represented by an s in place of the x of the executable bit. The s implies that the executable bit is set, otherwise you would see a capital S. This happens when the setuid or setgid bits are set, but the executable bit is not, showing the user an inconsistency: the setuid and setgit bits have no effect if the executable bit is not set. The setuid bit has no effect on directories.


