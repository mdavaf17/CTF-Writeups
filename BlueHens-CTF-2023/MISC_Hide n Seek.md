# Miscellaneous

## Hide n Seek

LET HIM COOOOK!! read everything you can carefully

![](https://media.discordapp.net/attachments/758115188796162088/1168452631765725224/STEG_O_SAURS.jpeg?ex=6551d150&is=653f5c50&hm=992c7647da8151fb3119fa2d0a70a592c5a3c355d9a2afed546c4e1e5cd74c17&=&width=448&height=224)

File: [LOLisCapatlized.wav](https://cdn.discordapp.com/attachments/758115188796162088/1168452632113844284/LOLisCapatlized.wav?ex=6551d150&is=653f5c50&hm=39c6f8e394bacc0778e3720fd552ac3ce9363e807759c389499110fd00e94abe&) []()

---

### Solution

Upload the image to [aperisolve](aperisolve.com). There is information of common password:

Common password(s): GIVEMETHEFLAGLOL, givemetheflaglol, givemetheflagLOL.

With the clue of .wav filename, we decide the password is `givemetheflagLOL`.



```bash
$ steghide extract -sf STEG_O_SAURS.jpeg 
Enter passphrase: givemetheflagLOL
wrote extracted data to "flaglol.txt".

$ cat flaglol.txt
UDCTF{01111001 01000000 01010101 01011111 01100011 01000001 01011110 01101110 01011111 01101000 00100001 01100100 00110011 00111111 01011111 01101100 01001111 01101100 01011111 01110011 01010100 00110011 01000111 01101111}
```


### UDCTF{y@U_cA^n_h!d3?_lOl_sT3Go}