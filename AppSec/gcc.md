## FLAG fstart-protector (Type of Canary for certain function with buffer 8bytes or with malloc)
1.30 -fstack-protector, -fstack-protector-all, -fstack-protector-strong, -fno-stack-protector
Inserts a guard variable onto the stack frame for each vulnerable function or for all functions.

The prologue of a function stores a guard variable onto the stack frame. Before returning from the function, the function epilogue checks the guard variable to make sure that it has not been overwritten. A guard variable that is overwritten indicates a buffer overflow, and the checking code alerts the run-time environment.

## FLAG -W[all] -Wall
Show all warnings

## FLAG -O3
optimisation level of o3 (not zero)
uncertain about risks introduce. Supposedly it generates faster code

##FLAG -fPIE

PIE is to support address space layout randomization (ASLR) in executable files.
https://stackoverflow.com/questions/2463150/what-is-the-fpie-option-for-position-independent-executables-in-gcc-and-ld
