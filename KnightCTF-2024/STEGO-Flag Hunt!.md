# Steganography

## Flag Hunt!

Hunt your way through the challenge and Capture The hidden Flag!!!

[Attachment 1](https://drive.google.com/file/d/1BXotCFeXqNuVC_vo_8uLss9OobIKHXnl/view)

Flag Format: KCTF{S0m3th1ng_h3re}

---

### Solution

```bash
$ fcrackzip -u -D -p ~/CTF/rockyou.txt chall.zip
PASSWORD FOUND!!!!: pw == zippo123

$ unzip -P zippo123 chall.zip 
Archive:  chall.zip
   creating: challenge/
  inflating: challenge/img...jpg

$ echo "Its extract 1000 jpg files and other file"

$ ls -1
img1000.jpg
...
img9.jpg
key.wav
n0t3.txt
nooope_not_here_gotta_try_harder.txt
```

![give-up](https://media.discordapp.net/attachments/758115188796162088/1198910790112124978/image.png?ex=65c09faf&is=65ae2aaf&hm=831bd17057c1f459ea61c601d5b73844c6edf14dc5ce73069370c20de0324a3e&=&format=webp&quality=lossless&width=1142&height=1056)

Imagine 1000 images are the same. However, there has to be an Easter egg in one of them. Okay, ignore the `.img` file.


```
$ cat nooope_not_here_gotta_try_harder.txt n0t3.txt 
KCTF{f4k3_fl46}
The flag is here somewhere. Keep Searching..

Tip: Use lowercase only
```

The `key.wav` is a morse audio. Decode it with [this], results `MORSECODETOTHERESCUE!!`.

Now, analyze the `.img` file.  Check the sample file size.

```bash
$ du -h img{1..5}.jpg 
136K	img1.jpg
136K	img2.jpg
136K	img3.jpg
136K	img4.jpg
136K	img5.jpg

$ du -h * | sort -r
4.0K	nooope_not_here_gotta_try_harder.txt
4.0K	n0t3.txt
3.0M	key.wav
140K	img725.jpg
136K	img9.jpg
136K	img99.jpg
136K	img999.jpg
136K	img998.jpg
```

Yup, the `img725.jpg` is the **impostor!**.


```bash
$ steghide --info -p "MORSECODETOTHERESCUE\!\!" img725.jpg
"img725.jpg":
  format: jpeg
  capacity: 8.0 KB
steghide: could not extract any data with that passphrase!
                                                      
$ steghide --info -p "morsecodetotherescue\!\!" img725.jpg
"img725.jpg":
  format: jpeg
  capacity: 8.0 KB
  embedded file "flag.txt":
    size: 47.0 Byte
    encrypted: rijndael-128, cbc
    compressed: yes

$ steghide extract -p "morsecodetotherescue\!\!" -sf img725.jpg 
wrote extracted data to "flag.txt".

$ cat flag.txt                                     
KCTF{3mb3d_53cr37_4nd_z1pp17_4ll_up_ba6df32ce}
```
### KCTF{3mb3d_53cr37_4nd_z1pp17_4ll_up_ba6df32ce}