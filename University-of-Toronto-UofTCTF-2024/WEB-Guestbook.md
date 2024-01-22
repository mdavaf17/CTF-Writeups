# Web Exploitation

## Guestbook
<!-- Spreadsheet, Macro, Sheet, sheetId -->

I made this cool guestbook for the CTF. Please sign it.

---

### Solution

```html
<!-- file: index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My Guestbook</title>
    <script async=false defer=false>
        fetch("https://script.google.com/macros/s/AKfycbyX5Y5MkBLDO4JrB67pTTx7A6JI_ajT-3aBXC1UvnurQjbLYmDJjUfPTne-cyGsKxY8/exec?sheetId=1PGFh37vMWFrdOnIoItnxiGAkIqSxlJDiDyklp9OVtoQ").then(x=>x.json()).then(x=>{
            x.slice(x.length-11).forEach(entry =>{
                const el = document.createElement("li");
                el.innerText = entry.Name + " - " + entry.Message
                document.getElementById("entries").appendChild(el)
            })
            document.getElementById("loading")?.remove();
        })
    </script>
</head>
<body>
<h1>
    Hi! I made this guestbook for my site, please sign it.
</h1>
<iframe name="dummyframe" id="dummyframe" style="display: none;"></iframe>
<h3 style="margin: 0">Last 10 user entries in the guestbook:</h3>
<p id="loading" style="margin: 0">Loading...</p>
<ul id="entries" style="margin: 0">
</ul>

<h3>Sign the guestbook:</h3>
<form method="POST" action="https://script.google.com/macros/s/AKfycbyX5Y5MkBLDO4JrB67pTTx7A6JI_ajT-3aBXC1UvnurQjbLYmDJjUfPTne-cyGsKxY8/exec?sheetId=1PGFh37vMWFrdOnIoItnxiGAkIqSxlJDiDyklp9OVtoQ">
  <input id="name" name="name" type="text" placeholder="Name" required>
  <input id="message" name="message" type="text" placeholder="Message" required>
  <button type="submit">Send</button>
</form>
</body>
</html>
```

The form post the data with google app script (macro). It seems like, the script write the data to a google spreadsheet (look at the `sheetId` parameter). 

Now, I got
https://docs.google.com/spreadsheets/d/1PGFh37vMWFrdOnIoItnxiGAkIqSxlJDiDyklp9OVtoQ/edit#gid=1015185525.

There is a hidden sheet!

![flag](https://media.discordapp.net/attachments/758115188796162088/1196950098639327305/image.png?ex=65b97da5&is=65a708a5&hm=66ed0afa707572fa40446ec4598b8c10341e414d64e6975f38ee304a936ba531&=&format=webp&quality=lossless&width=550&height=1056)


### uoftctf{@PP 5cRIP7 !5 s0 coOL}