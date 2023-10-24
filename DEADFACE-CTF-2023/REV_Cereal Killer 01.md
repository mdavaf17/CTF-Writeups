# Reverse Engineering

## Cereal Killer 01

How well do you know your DEADFACE hackers? Test your trivia knowledge of our beloved friends at our favorite hactivist collective! We’ll start with bumpyhassan. Even though he grates on TheZeal0t a bit, we find him to be absolutely ADORKABLE!!!

Choose one of the binaries below to test your BH trivia knowlege.

Enter the flag in the format: flag{Ch33ri0z_R_his_FAV}.

File: https://cdn.discordapp.com/attachments/758115188796162088/1166250627035299850/re01?ex=6549ce89&is=65375989&hm=9fc6bc98e1e01d11fbb7105b5806b3f6f8e950784e07a1414b34941ff3cfb3ae&

---

### Solution

![Decompile Main](https://media.discordapp.net/attachments/758115188796162088/1166254333453668402/image.png?ex=6549d1fd&is=65375cfd&hm=d298ca8dd3a240f4c5031556f40031cedc9b1e94f661fbf8daff44f884f9d89d&=&width=1028&height=1068)

There is `memcmp(&favorite,myInput,14);` function that compares the first 14 bytes of memory area &favorite and memory area `myInput`.

The `favorite` data is `4d 79 7c 70 7b 80 47 52 59 5c 4c 4e 4c 59`.

Previously, there is `for loop` that adding our input with '\a', BELL character in C. So, our correct input should substract with '\a' first.

```python
encoded_hex = b'\x4d\x79\x7c\x70\x7b\x80\x47\x52\x59\x5c\x4c\x4e\x4c\x59'
decoded = bytearray()
for byte in encoded_hex:
    decoded_byte = byte - 7
    decoded.append(decoded_byte)

payload = decoded.decode('utf-8')
print(payload)

# Fruity@KRUEGER
```

Input the payload will result the flag.

### flag{I_am_REDDY_for_FREDDY!!!}