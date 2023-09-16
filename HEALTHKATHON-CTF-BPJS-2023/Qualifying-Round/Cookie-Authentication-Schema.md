# Web

## Cookie Authentication Schema

Please open [this site](http://178.128.112.149/15_medium)

A website implements a cookie-based authentication scheme that appears to use encryption available on the web. This encryption uses the following custom key: BPJSHealthkhaton2023. You get this token for decryption: EDDGxGCNH1NdNOaeAbEb2g==.

Your task is to decrypt the token to gain access to the flag.

Hint: Try decrypting the given token. Most likely, this website uses a popular encryption scheme.

---

### Solution

Decrypt EDDGxGCNH1NdNOaeAbEb2g== with key BPJSHealthkhaton2023 on [this site](https://www.devglan.com/online-tools/text-encryption-decryption) produces "getflagbpjs".

Login with username = `admin` and password = `admin`

Edit the `access` cookie value to `getflagbpjs`

Refresh!

>BPJS{0438179c9227e4a6b47980b7deb174d8}