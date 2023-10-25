# OSINT

## Dark_Web_Dump

Welcome to challenge 1 in the Track the Hacker Series, a multi-step challenge. You are simulating an attack path as the hacker to take over GlitterCo!

For this challenge, d34th dumped some data onto GhostTown in a thread about Dark Web Dumps. Use this information to track down the person’s username and password that he left out on the public web! This will require a bit of social media and other websites to track these credentials down, think you can hack it?

Submit the flag as flag{username:password} (case sensitive).

---

### Solution

Try to search 'Dark Web Dumps' at https://ghosttown.deadface.io/. You will found [Hacked Stuff - Google Drive](https://drive.google.com/drive/folders/1tVdSeNgvGCLjhS-nbjhI0-uL3HAtacVY?usp=drive_link).

Open the google drive link, there is `Dear Lucy.pdf`. I got the sender's name is 'OpticSeltzer69' and the **Twitter** word.

The twitter account is https://twitter.com/OpticSeltzer69. The account post a [github repo](https://github.com/OpticSeltzer/Tictactoeeee). That's wrong repository! Change to another repo, namely [BrownGlitter](https://github.com/OpticSeltzer/BrownGlitter).

Look at `BrownGlitter.py`, we got username and password on the 2nd line.

`if username == "jakeg" and password == "MakeitChocolateRain"`

### flag{jakeg:MakeitChocolateRain}