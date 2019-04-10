 find /mnt -type f -mtime -1 2>/dev/null | grep -v "/var/" | grep -v "/proc/" | grep -v "/dev/" | grep -v "/sys/" | grep -v "/run/" | less
