# OSINT

## Bad Documentation

I heard that this security researcher accidentally leaked his password in his documentation, but he deleted all the files in his repository so now we don't have access to it anymore! I'm pretty sure it's hopeless, but if you think you can find it here's the link to the repo: https://github.com/Th3Burn1nat0r/vuln.

---

### Solution

Look at the "Add files via upload" commit.

![](https://raw.githubusercontent.com/Th3Burn1nat0r/vuln/52552b52ac8ad993d150ff83a8e12bfeee6e74e6/J-Link/JLE25006.png)

Decoding base64 of "YWRtaW46UENURntOMF9jMEQzJ3NfMlZlUnlfUjNhTGxZX0cwbjN9" would result "admin:PCTF{N0_c0D3's_2VeRy_R3aLlY_G0n3}".

### PCTF{N0_c0D3's_2VeRy_R3aLlY_G0n3}
