# Forensic

## Down the Wormhole

An explosive chase with a UFO led us to a wormhole!

Make sure you have your bases covered before you head in and find the secrets hiding inside!

File: https://media.discordapp.net/attachments/758115188796162088/1168429828236656661/wormhole.jpg?ex=6551bc13&is=653f4713&hm=4a42ac51a17d11d63b1617e0bf92b85589407ba48a5533184dba3785bc3efaf2&=&width=1898&height=1068

---

### Solution

Exiftool give us `Comment                         : cGFzc3dvcmQ6IGRpZ2dpbmdkZWVwZXI=`, base64 decode is `password: diggingdeeper`.

```bash
$ steghide extract -sf wormhole.jpg
Enter passphrase: diggingdeeper
wrote extracted data to "next.txt".

$ cat next.txt 
After diving through the wormhole, you find yourself in front of a rabbit hole. What secrets lie inside?

https://niccgetsspooky.xyz/r/a/b/b/i/t/h/o/l/e/rabbit-hole.svg
```

Inspect element of website, there is long comment


Decode the weird comment by base32 give us .gz file. Let .gz name is download.gz

```bash
$ gzip -d download.gz
$ bzip2 -d download
$ unzip download.out                                                                    
Archive:  download.out
  inflating: secrets665.zip.bz2.gz
```

Lets work with the Wormhole!

```bash
#!/bin/bash
for ((i=665 ; i>-1 ; i--));
do
    filename="secrets$i.zip"
    gzip -d ${filename}.bz2.gz
    bzip2 -d ${filename}.bz2
    unzip $filename
    rm $filename
done
```

```bash
$ cat flag.txt     
NICC{TH3-UF0S-4R3-UP-N0T-D0WN-50-WHY-4R3-Y0U-D0WN-H3R3}
```

### NICC{TH3-UF0S-4R3-UP-N0T-D0WN-50-WHY-4R3-Y0U-D0WN-H3R3}