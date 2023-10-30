# Miscellaneous

## shapeshifter

There's this figure in front of me, but I can't even figure out what it is! What is that thing??

File: https://cdn.discordapp.com/attachments/758115188796162088/1168435340193828964/distant-figure.png?ex=6551c135&is=653f4c35&hm=86c8c24c7499ecc350644b8589b6c1150306b2cb03f813af27f80c22f6d2b72b&

---

### Solution

It's not .png file!

```bash
$ file distant-figure.png 
distant-figure.png: Zip archive data, at least v2.0 to extract, compression method=deflate

$ unzip distant-figure.png  
Archive:  distant-figure.png
  inflating: distant-figure/true-form.exe

$ unrtf --text true-form.exe
###  Translation from RTF performed by UnRTF, version 0.21.10 
...
...
-----------------
There's nothing here&.

NICC{Y0U_F0UND_MY_TRU3_F0RM}
```


<!-- Keyword: \rtf1\adeflang1025\ansi\ansicpg1252\ ANSI-->


### NICC{Y0U_F0UND_MY_TRU3_F0RM}