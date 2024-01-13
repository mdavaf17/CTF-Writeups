# Forensics

## If You Don't, Remember Me

Here is a PDF file that seems to have some problems. I'm not sure what it used to be, but that's not important. I know it contains the flag, but I'm sure you can find it and drag it out of the file somehow. This is a two-step flag as you will find it partially encoded.

File: https://cdn.discordapp.com/attachments/758115188796162088/1195169562702917632/DF1.pdf?ex=65b30364&is=65a08e64&hm=87decc98a69f9f7bf4e4ef5bfe9f674f9284ac73dac39297ce88ec79a1604373&

---

### Solution

```bash
$  strings DF1.pdf | grep "poctf"
poctf(uwsp_77333163306D335F37305F3768335F39346D33}

$ echo 77333163306D335F37305F3768335F39346D33 | perl -ne 's/([0-9a-f]{2})/print chr hex $1/gie' && echo ''
w31c0m3_70_7h3_94m3
```

### poctf{uwsp_w31c0m3_70_7h3_94m3}