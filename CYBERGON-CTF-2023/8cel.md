# Forensic


## 8cel

Find the flag in this file.

Note: The flag is with Flag Format.

https://cdn.discordapp.com/attachments/758115188796162088/1142499673886691400/8cel.xlsx

---

### Solution

Check the file type

```bash
> $ file 8cel.zip
8cel.xlsx: Microsoft Excel 2007+
```

Open the excel

![](https://media.discordapp.net/attachments/758115188796162088/1142500134899417281/image.png?width=2160&height=882)

There is cell function behind the picture and its protected sheet. So, we cant delete it.

Try to extract xlsx content

`$ binwalk -e 8cel.xlsx `

Look at sheet2.xml content in xl/worksheets folder.

`$ strings sheet2.xml `


```xml
...
...
<c r="B2" t="e" cm="1"><f t="array" aca="1" ref="B2" ca="1">EMBED("Package", "Q3liZXJHb25DVEZ7ZjRrM19GMTRnfQ==")</f><v>#NAME?</v></c><c r="C2" t="e" cm="1"><f t="array" aca="1" ref="C2" ca="1">EMBED("Package", "Q3liZXJHb25DVEZ7RjRrM19GMTRnfQ==")</f><v>#NAME?</v></c><c r="D2" t="e" cm="1"><f t="array" aca="1" ref="D2" ca="1">EMBED("Package", "Q3liZXJHb25DVEZ7RjRrM19GMTRHR30=")</f><v>#NAME?</v></c><c r="E2" t="e" cm="1"><f t="array" aca="1" ref="E2" ca="1">EMBED("Package", "Q3liZXJHb25DVEZ7RjRrM19GMTRHfQ==")
...
```


Then, you will find so many fake flag from base64 encoding.

You will find the True flag at Q3liZXJHb25DVEZ7eTB1X0cwN183aDNfNTNjUjM3XzFOZjB9


CyberGonCTF{y0u_G07_7h3_53cR37_1Nf0}