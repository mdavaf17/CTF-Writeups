# Forensic

## What's the Wallet

Ransomware was recently discovered on a system within De Monne’s network courtesy of a DEADFACE member. Luckily, they were able to restore from backups. You have been tasked with finding the Bitcoin wallet address from the provided sample so that it can be reported to the authorities. Locate the wallet address in the code sample and submit the flag as flag{wallet_address}.

File: https://cdn.discordapp.com/attachments/758115188796162088/1165891522114367498/Bitcoin.txt?ex=65488018&is=65360b18&hm=12a45e337d07aa734bd41474922cfda10124c99886f01658b6a4fb84331bcd03&


---

### Solution

Look at the Store-BtcWalletAddress function

```shell
function Store-BtcWalletAddress {
    `$global:BtcWalletAddress = [System.Convert]::FromBase64String([System.Text.Encoding]::UTF8.GetBytes('bjMzaGE1bm96aXhlNnJyZzcxa2d3eWlubWt1c3gy'))
}
```

Decoding base64 of `bjMzaGE1bm96aXhlNnJyZzcxa2d3eWlubWt1c3gy` will produces `n33ha5nozixe6rrg71kgwyinmkusx2`

### flag{n33ha5nozixe6rrg71kgwyinmkusx2}