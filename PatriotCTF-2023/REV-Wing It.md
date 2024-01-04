# Reverse Engineering

## Wing It

I'm just gonna wing it

File: https://github.com/MasonCompetitiveCyber/PatriotCTF2023/blob/main/Rev/wing_it/wing_it

---

### Solution

Decompiled with Ghidra.

```c
undefined8 main(void)

{
  int iVar1;
  size_t sVar2;
  long in_FS_OFFSET;
  int input4;
  char input1 [256];
  char input2 [256];
  char input3 [264];
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  puts("Welcome everyone to............ (drum roll please)......... airplane trivia!");
  puts("Answers correctly and you\'ll get a special prize");
  puts("------------------------------------------------");
  puts("What\'s the worlds fastest non-military plane?");
  fgets(input1,0x100,stdin);
  sVar2 = strcspn(input1,"\n");
  input1[sVar2] = '\0';
  iVar1 = strcmp(input1,"the Concorde!");
  if (iVar1 == 0) {
    puts("What plane first went coast-to-coast across the US?");
    fgets(input2,0x100,stdin);
    sVar2 = strcspn(input2,"\n");
    input2[sVar2] = '\0';
    iVar1 = strcmp(input2,"duh it\'s the Vin Fiz Flyer");
    if (iVar1 == 0) {
      puts("What private company owns the most airplanes in the world?");
      fgets(input3,0x100,stdin);
      sVar2 = strcspn(input3,"\n");
      input3[sVar2] = '\0';
      iVar1 = strcmp(input3,"AMeriCan aiRLiNEs");
      if (iVar1 == 0) {
        puts(&DAT_001022a0);
        __isoc99_scanf(&DAT_001022bf,&input4);
        if (input4 - 100298U < 517) {
          puts("Dang, you really know your stuff!");
          puts("Have you ever considered a career as a pilot?");
          outputFlag();
        }
        else {
          puts(":( so close...");
        }
      }
      else {
        puts("Can we pretend that airplanes in the night sky are like shootin\' stars");
        puts(&DAT_00102287);
      }
    }
    else {
      puts("ERR! Wrong! Try again buddy...");
      puts("people really need to learn their plane facts...");
    }
  }
  else {
    puts("ERR! Wrong!");
  }
  if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return 0;
}
```

```bash
$ ./wing_it  
Welcome everyone to............ (drum roll please)......... airplane trivia!
Answers correctly and you'll get a special prize
------------------------------------------------
What's the worlds fastest non-military plane?
the Concorde!
What plane first went coast-to-coast across the US?
duh it's the Vin Fiz Flyer
What private company owns the most airplanes in the world?
AMeriCan aiRLiNEs
What date did ��� crash?
100298
Dang, you really know your stuff!
Have you ever considered a career as a pilot?
PCTF{1_10v3_p1ane5_9656734785}
```

### PCTF{1_10v3_p1ane5_9656734785}