# Reverse Engineering

## Patchwork

This program should just give the flag, but I set the wrong value in the code and now it refuses to jump to the correct function. Could you patch it for me?

File: https://github.com/MasonCompetitiveCyber/PatriotCTF2023/blob/main/Rev/patchwork/patchwork

---

### Solution

```
$ ./patchwork 
Trampolines are quite fun!; I love to jump! 
You should try jumping too! It'll sure be more fun than reversing the flag manually.
```

The default program is not calling `give_flag` func.


```bash
$ gdb -q ./patchwork
Reading symbols from ./patchwork...
gdb-peda$ i functions 
All defined functions:

Non-debugging symbols:
0x0000000000001000  _init
0x0000000000001030  puts@plt
0x0000000000001040  __cxa_finalize@plt
0x0000000000001050  _start
0x0000000000001080  deregister_tm_clones
0x00000000000010b0  register_tm_clones
0x00000000000010f0  __do_global_dtors_aux
0x0000000000001130  frame_dummy
0x0000000000001139  main
0x000000000000117d  give_flag
0x000000000000121c  _fini
gdb-peda$ pdisass main
Dump of assembler code for function main:
   0x0000000000001139 <+0>:	push   rbp
   0x000000000000113a <+1>:	mov    rbp,rsp
   0x000000000000113d <+4>:	sub    rsp,0x10
   0x0000000000001141 <+8>:	mov    DWORD PTR [rbp-0x4],0x0
   0x0000000000001148 <+15>:	lea    rax,[rip+0xeb9]        # 0x2008
   0x000000000000114f <+22>:	mov    rdi,rax
   0x0000000000001152 <+25>:	call   0x1030 <puts@plt>
   0x0000000000001157 <+30>:	lea    rax,[rip+0xeda]        # 0x2038
   0x000000000000115e <+37>:	mov    rdi,rax
   0x0000000000001161 <+40>:	call   0x1030 <puts@plt>
   0x0000000000001166 <+45>:	cmp    DWORD PTR [rbp-0x4],0x0
   0x000000000000116a <+49>:	je     0x1176 <main+61>
   0x000000000000116c <+51>:	mov    eax,0x0
   0x0000000000001171 <+56>:	call   0x117d <give_flag>
   0x0000000000001176 <+61>:	mov    eax,0x0
   0x000000000000117b <+66>:	leave
   0x000000000000117c <+67>:	ret
End of assembler dump.
```


```bash
gdb-peda$ b *main+66
gdb-peda$ echo breakpoint before leave\n
gdb-peda$ r
gdb-peda$ jump give_flag
Continuing at 0x555555555181.
PCTF{JuMp_uP_4nd_g3t_d0Wn}
[Inferior 1 (process 7803) exited normally]
```

### PCTF{JuMp_uP_4nd_g3t_d0Wn}