# Reverse Engineering

## My Daily Macros


DEADFACE has gotten hold of the HR departments contact list and has been distributing it with a macro in it. There is a phrase the RE team would like for you to pull out of the macro.

Submit the flag as flag{some_text}.

File: https://cdn.discordapp.com/attachments/758115188796162088/1166260573558808637/HR_List.zip?ex=6549d7cc&is=653762cc&hm=6b3f6b4b634aa6db431896abb6dc0ee87d03fdf29017d1229d06c333e8af7a3f&

---

### Solution

Unzip the .xlsm file will result

`'[Content_Types].xml'   docProps  _rels   xl`

Go to /xl and read `vbaProject.bin` file

### flag{youll_never_find_this_}