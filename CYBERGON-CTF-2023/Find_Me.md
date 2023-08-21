# Misc

## Find Me

Find, spot and grab the flag.

Flag Format : CybergonCTF{XXX_XXX_XXX}

Attachment: https://cdn.discordapp.com/attachments/758115188796162088/1142616504135847936/Find_me.xlsx

---

### Solution

No Clue?

Look the strings in file

`$ strings Find_me.xlsx `

```xml
...
w2>y}
xl/sharedStrings.xml4O
"1sg
docProps/core.xml 
&9'O
...
```

The sharedStrings file look weird, right?

Unzip the content

`$ unzip Find_me.xlsx `

Then,

`$ cat xl/sharedStrings.xml`

```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<sst xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" count="1" uniqueCount="1"><si><t xml:space="preserve">C
y
b
e
r
g
o
n
C
T
F
{
H
i
d
d
e
n
_
W
o
r
d
s
_
4
_
U
}
</t></si></sst>
```


CybergonCTF{Hidden_Words_4_U}