# Miscellaneous

## WPA
<!--CRACK WIFI PASSWORD WPA AIRCRACK-NG WIRESHARK-->

I really need to get on my friends WiFi, but he won't give me the password. I think he think's I'll mess around on his network. I started a packet capture and left it running a while, I think someone connected to the network before I stopped the capture. Can you help me? Flag format: PCTF{password}

File: https://github.com/MasonCompetitiveCyber/PatriotCTF2023/blob/main/misc/wpa/savedcap.cap

---

### Solution

```bash
$ aircrack-ng savedcap.cap -w rockyou.txt

Reading packets, please wait...
Opening savedcap.cap
Read 888 packets.

   #  BSSID              ESSID                     Encryption

   1  52:E2:4D:0A:A6:36  Pctf wifi challenge       WPA (1 handshake)

Choosing first network as target.

Reading packets, please wait...
Opening savedcap.cap
Read 888 packets.

1 potential targets



                               Aircrack-ng 1.7 

      [00:00:01] 2026/10303727 keys tested (2138.91 k/s) 

      Time left: 1 hour, 20 minutes, 16 seconds                  0.02%

                           KEY FOUND! [ qazwsxedc ]
```

### PCTF{qazwsxedc}
