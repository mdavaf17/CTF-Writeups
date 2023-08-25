# Forensic


## Malfunction File

Can you fix the file and extract the secret data?

https://media.discordapp.net/attachments/758115188796162088/1142977520078168156/Cybergon.jpg?width=634&height=628

---

### Solution

Extract the file content

`$ binwalk -e Cybergon.jpg`

We got the corrupted flag.png file.

Fix the .png header

`89 50 3E 37 0D 0A to 89 50 4E 47 0D 0A`

Waittt! The file still corrupt.

Check it out,

```bash
$ pngcheck flag.png
zlib warning:  different version (expected 1.2.13, using 1.2.11)

flag.png  CRC error in chunk IHDR (computed 9ce9173e, expected e5b6965f)
ERROR: flag.png
```

Edit the `e5 b6 96 5f ---> 9c e9 17 3e`, at the offset 0x1D with your hex editor.

Now, the file isn't corrupt right? We can display it. However, the image is just blank.

Check the hint at the first file (Cybergon.jpg), there is the "Love Dimension" words.

I think, we must modify the dimension size, width or height.

I modify the dimension with [TweakPNG](https://entropymine.com/jason/tweakpng/).

I guess and type manually and finally, got the flag on the 1500x972 px.

![](https://media.discordapp.net/attachments/758115188796162088/1142981027065774251/newflag.png?width=1648&height=1068)


CyberGonCTF{D1m3N510N_c0rRuP73d}