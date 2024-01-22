# Steganography

## Flag Hunt!

The ocean's beauty is in its clear waters, but its strength lies in its dark depths.

[Attachment 1](https://drive.google.com/file/d/1AUkb75vryU1bMce4i3dvm1fLM8ZPjnH6/view?usp=sharing)

Flag Format: KCTF{S0m3th1ng_h3re}

---

### Solution

```bash
$ ls
clue.jpg  peaceful.wav

$ exiftool clue.jpg    
ExifTool Version Number         : 12.67
File Name                       : clue.jpg
...
Comment                         : 8qQd3iMYmtsyto7aXUuw1KVRpQFCRxqRtJiRgP85e36y
```

Decode the comment by base58 result "theoceanisactuallyreallydeeeepp'. Ohh, maybe this is about [**Deepsound**](https://github.com/Jpinsoft/DeepSound), I was found this chall before.

1. Select `peaceful.wav` as carrier file
2. Enter the decoded comment as password
3. Extract the secret files (flag.png)

![flag](https://media.discordapp.net/attachments/758115188796162088/1198923768886739045/image.png?ex=65c0abc5&is=65ae36c5&hm=51c9f898c0976b0ffb5a07e4623d63c370e5feecb76d5e3cf901a41c6c18b38e&=&format=webp&quality=lossless&width=1414&height=1056)

```bash
$ binwalk -e flag.png   

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             JPEG image data, JFIF standard 1.01
4435          0x1153          Zip archive data, at least v1.0 to extract, name: flag/
4498          0x1192          Zip archive data, at least v1.0 to extract, compressed size: 35, uncompressed size: 35, name: flag/flag.txt
4762          0x129A          End of Zip archive, footer length: 22

$ cat _flag.png.extracted/flag/flag.txt 
KCTF{mul71_l4y3r3d_57360_ec4dacb5}
```


### KCTF{mul71_l4y3r3d_57360_ec4dacb5}