# Web Exploitation

## Levi Ackerman

Levi Ackerman is a robot!

N:B: There is no need to do bruteforce.

Target : http://66.228.53.87:5000/

---

### Solution

```bash
$ curl http://66.228.53.87:5000/robots.txt
Disallow : /l3v1_4ck3rm4n.html

$ curl http://66.228.53.87:5000/l3v1_4ck3rm4n.html
KCTF{1m_d01n6_17_b3c4u53_1_h4v3_70}
```

### KCTF{1m_d01n6_17_b3c4u53_1_h4v3_70}