# Web Exploitation

## Web Explorer's Journey

Ahoy, matey! a bottle of code! Captain Jack Sparrow has hidden his secret pirate flag using the ancient JavaScript Cipher. It's your duty to decipher the code and uncover the hidden treasure, savvy?

https://web-explorer.netlify.app

---

### Solution

Inspect .html file

`Your flag is: 1856983846779781238751669551888076488251829549839552875183487751125`

Look at .js file.

```javascript
let flag = "flag{Test_Flag}";
let encryptedFlag = "";
function encodeFlag() {
  for (let i = 0; i < flag.length; i++) {
    encryptedFlag += flag.charCodeAt(i);
  }
}

encodeFlag();
document.getElementById("flag").innerHTML = encryptedFlag;
```

[Decode](https://onlinetools.com/ascii/convert-decimal-to-ascii) from Decimal to ASCII.

### QUESTCON{W3B_3XPL0R3R_1S_4W3S0M3}