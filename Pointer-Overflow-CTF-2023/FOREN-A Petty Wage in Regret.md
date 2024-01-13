# Forensics

## A Petty Wage in Regret

[Here](https://uwspedu-my.sharepoint.com/:i:/g/personal/cjohnson_uwsp_edu/EUU6XEnKsk1BopS8Iz0JAD8B1yHWrVJZXYnmbCqhIPYVHw?e=sLK92J) is a very interesting image. The flag has been broken up into several parts and embedded within it, so it will take a variety of skills to assemble it.


---

### Solution

```bash
$ exiftool DF2.jpg        
ExifTool Version Number         : 12.67
File Name                       : DF2.jpg
...
User Comment                    : 3A3A50312F323A3A20706F6374667B757773705F3768335F7730726C645F683464
...

$ echo 3A3A50312F323A3A20706F6374667B757773705F3768335F7730726C645F683464 | perl -ne 's/([0-9a-f]{2})/print chr hex $1/gie' && echo ''
::P1/2:: poctf{uwsp_7h3_w0rld_h4d
```

Part 2:

![flag 2/2](https://media.discordapp.net/attachments/758115188796162088/1195177497860526160/image_rgb_6.png?ex=65b30ac8&is=65a095c8&hm=ad9f86a1cecfc76116138b738d55aa7578df65f0fd92ba7d405133a181b2f6ec&=&format=webp&quality=lossless&width=1168&height=1168)

That's hard to read. I can take

```
P2/2
27
f1257
```

but it makes sense if 27 -> 17 = "iT". After trial & error, I got the flag.

### poctf{uwsp_7h3_w0rld_h4d_17_f1257}