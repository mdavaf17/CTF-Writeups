# Miscellaneous 

## Out of the Bucket

Check out my flag website!

https://storage.googleapis.com/out-of-the-bucket/src/index.html

---

### Solution

Try to https://storage.googleapis.com/out-of-the-bucket/. 

![bucket](https://media.discordapp.net/attachments/758115188796162088/1196502915163103242/image.png?ex=65b7dd2c&is=65a5682c&hm=cedc5d1eaa3dcc1484fac0838e04b674d0860cc8ee9a6700d9e11fa8a3662802&=&format=webp&quality=lossless&width=1578&height=1168)


There is at file at `secret/dont_show`.

```bash
$ wget https://storage.googleapis.com/out-of-the-bucket/secret/dont_show
--2024-01-16 00:17:54--  https://storage.googleapis.com/out-of-the-bucket/secret/dont_show
Saving to: ‘dont_show’

$ cat dont_show 
uoftctf{allUsers_is_not_safe}
```

### uoftctf{allUsers_is_not_safe}