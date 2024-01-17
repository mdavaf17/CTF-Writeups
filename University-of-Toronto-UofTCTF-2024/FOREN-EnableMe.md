# Forensics

## Secret Message 1

You've received a confidential document! Follow the instructions to unlock it.

Note: This is not malware

File: https://cdn.discordapp.com/attachments/758115188796162088/1196745649069236304/invoice.docm?ex=65b8bf3d&is=65a64a3d&hm=c45bd3224129f26eb23f281c0f938ada2d618dbeb21a087ad9f73b0571a68bce&

---

### Solution

```bash
$ binwalk -e invoice.docm       

$ olevba word/vbaProject.bin
olevba 0.60.1 on Python 3.11.5 - http://decalage.info/python/oletools
===============================================================================
FILE: word/vbaProject.bin
Type: OLE
-------------------------------------------------------------------------------
VBA MACRO ThisDocument.cls 
in file: word/vbaProject.bin - OLE stream: 'VBA/ThisDocument'
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
Sub AutoOpen()
    Dim v6 As Variant, v7 As Variant
    v6 = Array(98, 120, 113, 99, 116, 99, 113, 108, 115, 39, 116, 111, 72, 113, 38, 123, 36, 34, 72, 116, 35, 121, 72, 101, 98, 121, 72, 116, 39, 115, 114, 72, 99, 39, 39, 39, 106)
    v7 = Array(44, 32, 51, 84, 43, 53, 48, 62, 68, 114, 38, 61, 17, 70, 121, 45, 112, 126, 26, 39, 21, 78, 21, 7, 6, 26, 127, 8, 89, 0, 1, 54, 26, 87, 16, 10, 84)
    
    Dim v8 As Integer: v8 = 23

    Dim v9 As String, v10 As String, v4 As String, i As Integer
    v9 = ""
    For i = 0 To UBound(v6)
        v9 = v9 & Chr(v6(i) Xor Asc(Mid(Chr(v8), (i Mod Len(Chr(v8))) + 1, 1)))
    Next i

    v10 = ""
    For i = 0 To UBound(v7)
        v10 = v10 & Chr(v7(i) Xor Asc(Mid(v9, (i Mod Len(v9)) + 1, 1)))
    Next i

    MsgBox v10
End Sub
```


Convert the above code into python code

```python
def auto_open():
    v6 = [98, 120, 113, 99, 116, 99, 113, 108, 115, 39, 116, 111, 72, 113, 38, 123, 36, 34, 72, 116, 35, 121, 72, 101, 98, 121, 72, 116, 39, 115, 114, 72, 99, 39, 39, 39, 106]
    v7 = [44, 32, 51, 84, 43, 53, 48, 62, 68, 114, 38, 61, 17, 70, 121, 45, 112, 126, 26, 39, 21, 78, 21, 7, 6, 26, 127, 8, 89, 0, 1, 54, 26, 87, 16, 10, 84]
    v8 = 23

    v9 = ""
    for i in range(len(v6)):
        v9 += chr(v6[i] ^ ord(chr(v8)[i % len(chr(v8))]))

    v10 = ""
    for i in range(len(v7)):
        v10 += chr(v7[i] ^ ord(v9[i % len(v9)]))

    print(v10)

# Call the function to decode the message
auto_open()
```

If the code is executed it will produce `YOU HAVE BEEN HACKED! Just kidding :)`. However, if I change to `print(v9)` instead of `print(v10)` it will produce a flag.

### uoftctf{d0cx_f1l35_c4n_run_c0de_t000}