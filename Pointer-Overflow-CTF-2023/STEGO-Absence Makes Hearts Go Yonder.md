# Steganography

## Absence Makes Hearts Go Yonder

Sometimes the oldest and simplest tricks can be the most fun. Here's an old stego tactic that requires no special software - just a little knowledge and maybe a keen eye.

File: ![gif](https://pointeroverflowctf.com/stego1.gif)

---

### Solution

```bash
$ binwalk -e stego1.gif  
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             GIF image data, version "89a", 210 x 138
561650        0x891F2         Zip archive data, at least v2.0 to extract, compressed size: 37, uncompressed size: 37, name: flag.txt
561779        0x89273         End of Zip archive, footer length: 22

$ cat flag.txt            
poctf{uwsp_h342d_y0u_7h3_f1257_71m3}

```

### poctf{uwsp_h342d_y0u_7h3_f1257_71m3}