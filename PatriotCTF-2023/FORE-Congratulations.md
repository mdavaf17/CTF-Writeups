# Forensics

## Congratulations
<!--VBA-->

Congratulations, here's an email attatchment.

File: https://github.com/MasonCompetitiveCyber/PatriotCTF2023/blob/main/Forensics/congratulations/Congratulations.docm

---

### Solution

Extract the embedded files. `$ binwalk -e Congratulations.docm`

Decompiled the VBA binary using [pcode2code](https://pypi.org/project/pcode2code/).

```
$ pcode2code word/vbaProject.bin 
stream : VBA/ThisDocument - 938 bytes
########################################


stream : VBA/NewMacros - 4527 bytes
########################################

Dim x51 As String
Dim x49 As String

x51 = "C:\Program Files\Internet Explorer\iexplore.exe"

Dim x50 As Integer
Dim x47 As Double
For x50 = 1 To 100
  x47 = Sqr(x50) * 2 + 5 / x50
Next x50

MsgBox "cYvSGF9cFrrEmfYFW8Yo", vbInformation, "aThg"

 x49 = [char]0x50 + [char]0x43 + [char]0x54 + [char]0x46 + [char]0x7B + [char]0x33 + [char]0x6E + [char]0x34 + [char]0x62 + [char]0x6C + [char]0x33 + [char]0x5F + [char]0x6D + [char]0x34 + [char]0x63 + [char]0x72 + [char]0x30 + [char]0x35 + [char]0x5F + [char]0x70 + [char]0x6C + [char]0x7A + [char]0x5F + [char]0x32 + [char]0x37 + [char]0x33 + [char]0x31 + [char]0x35 + [char]0x36 + [char]0x37 + [char]0x30 + [char]0x7D

...
omitted
...
```

Decode the x49 variable values would result the flag.

### PCTF{3n4bl3_m4cr05_plz_27315670}
