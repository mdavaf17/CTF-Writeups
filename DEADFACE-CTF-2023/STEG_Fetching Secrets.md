# Steganography

## Fetching Secrets

This image was found on Ghost Town. Looks like one of DEADFACE’s newest members is new to steganography. See if you can find any hidden information in this image. Knowing information about the image may help to reveal the flag.

Submit the flag as: flag{flag_text}.

File: https://media.discordapp.net/attachments/758115188796162088/1165910898976759909/cyberdog.jpg?ex=65489223&is=65361d23&hm=c7c52b6f867f626c631bb7a23fa0023d105a376d1541332e97d6cd8cb63ea800&=&width=1070&height=1066

---

### Solution

```bash
$ stegseek cyberdog.jpg -wl rockyou.txt
[i] Found passphrase: "kira"           

[i] Extracting to "cyberdog.jpg.out".
```

![](https://media.discordapp.net/attachments/758115188796162088/1165913579162185738/image.png?ex=654894a2&is=65361fa2&hm=44aa01a51df0fc126932ef0578e887e3cee068fd8f1b0cc41268bb0bf86d476b&=&width=2160&height=414)


### flag{g00d_dawg_woofw00f}