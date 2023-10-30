# Miscellaneous

## Insecure Protocols

I just spun up my first website with a login page and everything! My friend tells me my page isn't secure and I'm not sure why.

File: https://cdn.discordapp.com/attachments/758115188796162088/1168438471115943996/insecure.pcapng?ex=6551c420&is=653f4f20&hm=c13369b47e206f045f276d83de517867d9e981bcf1c50c8336746eca67fd3c71&

---

### Solution

Open with Wireshark, filter only HTTP (text/html) with `data-text-lines`. One of packet results there is strings "You must login".

Follow TCP Stream that packet. 


```bash
POST /userinfo.php HTTP/1.1
Host: testphp.vulnweb.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 46
Origin: http://testphp.vulnweb.com
Connection: keep-alive
Referer: http://testphp.vulnweb.com/login.php
Upgrade-Insecure-Requests: 1

uname=NICC%7Bh77p_15_1n53cur3%7D&pass=passwordHTTP/1.1 302 Found
Server: nginx/1.19.0
Date: Mon, 23 Oct 2023 04:16:17 GMT
Content-Type: text/html; charset=UTF-8
Transfer-Encoding: chunked
Connection: keep-alive
X-Powered-By: PHP/5.6.40-38+ubuntu20.04.1+deb.sury.org+1
Location: login.php

e
you must login
0
```

### NICC{h77p_15_1n53cur3}