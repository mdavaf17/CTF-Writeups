# Misc

## Captured

Our intels captured some conversation between Mr.Yit and his friend. Do you find some useful information ?

Flag Format : CybergonCTF{XXXXXXXXX}

Attachment: https://cdn.discordapp.com/attachments/758115188796162088/1142974562515046401/Captured.m4a

---

### Solution

There is phone button sounds in the audio. I try to google: ctf writeup morse audio telephone call.

I found the tool for Detect DTMF Tones.

Then, I convert the .m4a to .wav

```bash
$ python dtmf.py Captured.wav
09007007007
```

CybergonCTF{09007007007}