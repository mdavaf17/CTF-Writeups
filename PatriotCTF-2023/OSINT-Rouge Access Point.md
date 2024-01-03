# OSINT

## Rouge Access Point
<!--SSID WIFI-->

We've received a notice from our companies EDR software that a laptop was attacked while they were on WFH. The employee says they were at home when it happened, but we suspect they were using public wifi. Our EDR software managed to capture the BSSID of the wifi (46:D1:FA:63:BC:66) network before it got disconnected, but not the SSID. Can you still find the network they were connected to? You're flag should be in the format PCTF{SSID}

---

### Solution

https://wigle.net/search?netid=46%3AD1%3AFA%3A63%3ABC%3A66

### PCTF{Red's Table Free Wifi}
