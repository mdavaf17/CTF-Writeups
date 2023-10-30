# Forensic

## Don't stick me there!

I woke up after a night out and I'm hurting uh... everywhere... I think I left my phone at one of the bars we were at last night. Thankfully, I was able to see the last photo I took through the cloud.

Can you help me find my phone? I need to know the name of the bar and when the photo was taken.

flagformat: NICC{Bar_Name-HH:MM:SS}

File: https://media.discordapp.net/attachments/758115188796162088/1168427672775434310/lastphoto.png?ex=6551ba11&is=653f4511&hm=3ca418ef6351a334386305d058963f6901df5d399f11ef545c1c440c8ba2baca&=&width=800&height=1068

---

### Solution

Exiftool give us

```bash
GPS Position    : 40 deg 42' 33.02" N, 73 deg 56' 14.04" W
Create Date     : 2023:08:13 03:47:12
```


### NICC{The_Anchored_Inn-03:47:12}