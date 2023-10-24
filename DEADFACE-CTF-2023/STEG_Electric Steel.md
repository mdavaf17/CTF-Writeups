# Steganography

## Electric Steel


Check out this image DEADFACE left on one of their victims' machines. We tried a couple tools and they didn’t reveal anything. Take a look and see what you can find.

Submit the flag as flag{flag_text}.

File: https://media.discordapp.net/attachments/758115188796162088/1165915933827665950/electric-steel.png?ex=654896d4&is=653621d4&hm=36a68770b279a6f6f6ff2762acd73e19d3fa646ad83e6bb439e78f72cb7112ff&=&width=1418&height=1068

---

### Solution

```bash
$ binwalk -e electric-steel.png
...
$ ls
1664FA  ACF  ACF.zlib

$ strings 1664FA        
flag.txt
...
...
flag{3L3ctr1c_5t33L_b1G_H41R}
```


### flag{3L3ctr1c_5t33L_b1G_H41R}