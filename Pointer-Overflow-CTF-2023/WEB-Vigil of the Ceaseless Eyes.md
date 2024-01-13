# Web Exploitation

## We Rest Upon a Single Hope

Hey, contestants! Allow me to take this opportunity to debut the hottest new social media platform on the planet. I call it [ManyKins](https://nvstgt.com/ManyKin/index.html)! There is also ZERO chance it has ANY vulnerabilities that might allow one to find the flag (under /secret/flag.pdf)!

---

### Solution

Go to `https://nvstgt.com/ManyKin/secret/flag.pdf`, and download the file.

```bash
$ wget https://nvstgt.com/ManyKin/secret/flag.pdf
Saving to: ‘flag.pdf’
flag.pdf                                    100%[========================================================================================>]      31  --.-KB/s    in 0s      
                                              
$ cat flag.pdf 
poctf{uwsp_71m3_15_4n_1llu510n} 
```

### poctf{uwsp_71m3_15_4n_1llu510n} 