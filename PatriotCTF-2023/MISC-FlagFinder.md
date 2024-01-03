# Miscellaneous

## WPA

All you have to do is find the flag.

File: https://github.com/MasonCompetitiveCyber/PatriotCTF2023/blob/main/misc/FlagFinder/flagfinder

---

### Solution

Decompile with Ghidra.

```c
undefined8 main(void)

{
  size_t sVar1;
  size_t sVar2;
  ulong uVar3;
  undefined8 local_a8;
  undefined8 local_a0;
  undefined4 local_98;
  char userInput [108];
  int local_1c;
  
  printf("What is the password: ");
  __isoc99_scanf(&DAT_0010201f,userInput);
  local_a8 = 0x6d69547b66746370;
  local_a0 = 0x334e3849676e6933;
  local_98 = 0x7d7461;
  sVar1 = strlen(userInput);
  sVar2 = strlen((char *)&local_a8);
  if (sVar1 < sVar2) {
    printf("%s is not long enough",userInput);
  }
  else {
    ...
    omitted
    ...
}
```

Just look at local_a8, local_a0, local_98 value. https://gchq.github.io/CyberChef/#recipe=Swap_endianness('Hex',8,false)From_Hex('Auto')&input=NmQ2OTU0N2I2Njc0NjM3MDMzNGUzODQ5Njc2ZTY5MzM3ZDc0NjE


### pctf{Tim3ingI8N3at}
