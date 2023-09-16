# Web

## What Is Cookie?

Please open [this website](http://178.128.112.149/11_medium)

You are given access to a system that uses cookies for user authentication. Your task is to bypass such authentication systems by modifying user authentication cookies. How can you do this?

Hint:You can use browser developer tools or cookie editing extensions to modify cookie values. Can you add the authenticated cookie value to 'true' to exploit this vulnerability? And if the authenticated value has been added to the cookie, you can redirect to index.php in the URL.

---

### Solution

Add cookies: {authenticated : true} and go to index.php

>BPJS{30922d20db0c3ce3e9e3cce7c0ec6a83}