# Reverse Engineering

## Easy as it Gets

It doesn't get much easier than this when it comes to reverse engineering. [Here](https://uwspedu-my.sharepoint.com/:u:/g/personal/cjohnson_uwsp_edu/ESssoaM9aGVHkxykqJGKV94Bg_NYCTfq_tLyc5gnwQwjmA?e=0uESL1) we have a "secure" PowerShell script. All you need to do is figure out the super secret passphrase to decrypt the flag.

---

### Solution

```shell
cls  

#### 
# TODO: use strong password
# Canadian_Soap_Opera
### 

$pwd = read-host "(Case Sensitive) Please Enter User Password"  
```

Passwords are commented. Just run the file!

```bash
(Case Sensitive) Please Enter User Password: Canadian_Soap_Opera

Encrypted Password is: TTpgx3Ve2kkHaFNfixbAJfwLqTGQdk9dkmWJ6/t0UCBH2pGyJP/XDrXpFlejfw9d

Testing Decryption of Username / Password...

Decrypted Password is: poctf{uwsp_4d_v1c70r14m_w4573l4nd3r}
```

### poctf{uwsp_4d_v1c70r14m_w4573l4nd3r}