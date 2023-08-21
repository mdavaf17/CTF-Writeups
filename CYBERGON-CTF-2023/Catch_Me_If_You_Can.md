# Steg

## Catch Me If You Can

Do not judge until you know all story.

Flag Format : CybergonCTF{XXX_XXX}

Attachment: https://cdn.discordapp.com/attachments/758115188796162088/1142621554262409296/Stegano1.gif

---

### Solution

```bash
$ file Stegano1.gif
Stegano1.gif: data
```

Maybe, it should be .gif according to the extension

Check the file header

```
39 61 F4 01 F4 01 F7 00 03 03 03
```

The .GIF header should be

```
47 49 46 38 39 61 f4 01 |   GIF89a..
```

Just edit with your  hex editor.

Got it!

![](https://media.discordapp.net/attachments/758115188796162088/1142624246338687096/newSteg.gif?width=1000&height=1000)


CybergonCTF{YOU_GOT_ME}