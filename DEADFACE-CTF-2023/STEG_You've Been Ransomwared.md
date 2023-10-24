# Steganography

## You've Been Ransomwared

DEADFACE is taunting GlitterCo with their latest ransomware attack. According to our intel, the attackers like to leave a calling card in their attacks. If we can figure out which DEADFACE actor executed this attack, we might be able to figure out a way around paying. Can you find anything in this screenshot that might point to which attacker ran this ransomware attack?

Submit the flag as flag{attacker_name}.

File: https://media.discordapp.net/attachments/758115188796162088/1165906606983233536/ransomwared.png?ex=65488e24&is=65361924&hm=58ba2924a9669b58c1da9c967aff832e6b9dd1b1c81b49ca9c94417026723839&=&width=1502&height=1002

---

### Solution

Check with https://www.aperisolve.com/. There is hidden binary text at the bottom of image.

![](https://media.discordapp.net/attachments/758115188796162088/1165907588995616828/image_b_6.png?ex=65488f0e&is=65361a0e&hm=3db359c904cb0796bca482464f815f85b877e380e034b223f6044b0e07b4f5be&=&width=1502&height=1002)

```
01010100 01101000 01101001 01110011 00100000 01110010 01100001 01101110 01110011 01101111 01101101 01110111 01100001 01110010 01100101 00100000 01100010 01110010 01101111 01110101 01100111 01101000 01110100 00100000 01110100 01101111 00100000 01111001 01101111 01110101 00100000 01100010 01111001 00100000 01101101 01101001 01110010 01110110 01100101 01100001 01101100 00101110
```

Decode the binary will produces **This ransomware brought to you by mirveal**


### flag{mirveal}