# Steganography

## Mystery

Another mystery!

File: ![](https://media.discordapp.net/attachments/758115188796162088/1169175927620640768/pirate.jpg?ex=655472ef&is=6541fdef&hm=4465d7880a46172fba302e334ada7d8a3980e16ddb604b33d7cfcc7d6e812f67&=&width=1898&height=1068)

---

### Solution

LSB encoded.

```bash
─$ zsteg another_mystery.png
b1,g,lsb,xy         .. file: OpenPGP Public Key
b1,abgr,msb,xy      .. text: "}wwwwwww;"
b2,r,lsb,xy         .. text: "Y?*[*LkB"
b2,g,lsb,xy         .. text: "EAUUUUUUUU"
b2,b,msb,xy         .. text: "jUUv}VU}%c"
b2,rgba,lsb,xy      .. text: "QUESTCON{P1raT3s_Ar3_M7s!3rY}\n"
```


### QUESTCON{P1raT3s_Ar3_M7s!3rY}