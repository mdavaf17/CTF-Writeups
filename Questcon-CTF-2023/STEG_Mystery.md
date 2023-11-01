# Steganography

## Mystery

Hidden within this image is a concealed message, waiting to be unraveled. The key to unlock the mystery lies in the heart of our theme. Can you discover the hidden treasure without a password?


File: ![](https://media.discordapp.net/attachments/758115188796162088/1169175927620640768/pirate.jpg?ex=655472ef&is=6541fdef&hm=4465d7880a46172fba302e334ada7d8a3980e16ddb604b33d7cfcc7d6e812f67&=&width=1898&height=1068)

---

### Solution

```bash
$ stegseek pirate.jpg -wl ../../wordlist.txt
[i] Found passphrase: ""

[i] Original filename: "mystery".
[i] Extracting to "pirate.jpg.out".

$ exiftool pirate.jpg.out
Image Unique ID                 : UVVFU1RDT057TXk1dDNyeV8xc180dzNzMG1lIX0=

$ echo "UVVFU1RDT057TXk1dDNyeV8xc180dzNzMG1lIX0=" | base64 -d
QUESTCON{My5t3ry_1s_4w3s0me!}
```


### QUESTCON{My5t3ry_1s_4w3s0me!}