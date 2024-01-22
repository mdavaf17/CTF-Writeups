# Web Exploitation

## Levi Ackerman

Tetanus is a serious, potentially life-threatening infection that can be transmitted by an animal bite.

N:B: There is no need to do bruteforce.

Target : http://45.33.123.243:5020/

---

### Solution

Log in with `username = admin` and `password = password`.

If the login is successful, we go directly to `/dashboard`.

```javascript
if (post_in.startsWith('cat flag.txt')) {
    fetch('/execute', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: `post_input=${encodeURIComponent(post_in)}`
    })
    .then(response => response.text())
    .then(result => {
```

Just post the content of `cat flag.txt` then the resulting content is the flag.

```
Flag Post
KCTF{Fram3S_n3vE9_L1e_4_toGEtH3R}
```

### KCTF{Fram3S_n3vE9_L1e_4_toGEtH3R}