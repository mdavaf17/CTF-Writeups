# Forensic

## Head Jack Sparrow

Captain got an unknown image...Help him out and inspect the file.

File: https://cdn.discordapp.com/attachments/758115188796162088/1168837463712727120/Head_Jack_Sparrow.png?ex=655337b7&is=6540c2b7&hm=6874053e09d1439ef875dab617a57ce63541b097162e29ccfbff7f5e75b82fcd&

---

### Solution

Its corrupted png header, `26 ED AF 21 0D 0A 1A 0A 00 00 00 0D 76 22 E2 52` change to `89 50 4E 47 0D 0A 1A 0A 00 00 00 0D 49 48 44 52`

Look at the right bottom image!

![](https://media.discordapp.net/attachments/758115188796162088/1168839167434838076/flag.png?ex=6553394d&is=6540c44d&hm=6eb02252e432dbd2349a8c90029886c1580f182ac4594e9bca6cdf3f1a022a11&=&width=1068&height=1068)


### QUESTCON{P1RaT3s_Ha13s_PNG_F1l3}