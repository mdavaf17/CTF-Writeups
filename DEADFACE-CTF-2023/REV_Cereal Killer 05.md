# Reverse Engineering

## Cereal Killer 05

We think Dr. Geschichter of Lytton Labs likes to use his favorite monster cereal as a password for ALL of his accounts! See if you can figure out what it is, and keep it handy! Choose one of the binaries to work with.

Enter the answer as flag{WHATEVER-IT-IS}.

File: https://cdn.discordapp.com/attachments/758115188796162088/1166258283045195776/re05.bin?ex=6549d5aa&is=653760aa&hm=2133372d77d23e030388481a8fa84b4c20de3420b61a3deba3b6e9cbd200ed84&

---

### Solution

![Decompile Main](https://media.discordapp.net/attachments/758115188796162088/1166258910563405824/image.png?ex=6549d640&is=65376140&hm=07de9614c68d187f4e08ec1fe51a57ec06e13f3ad85a6ad12046e496f8c67d5a&=&width=1412&height=1068)

There is `iVar1 = FUN_000110b0(myInput,"Xen0M0rphMell0wz")`. I guess that's just comparison our input with the answer.

Input the `Xen0M0rphMell0wz` will result the flag.

### flag{XENO-DO-DO-DO-DO-DO-DOOOOO}