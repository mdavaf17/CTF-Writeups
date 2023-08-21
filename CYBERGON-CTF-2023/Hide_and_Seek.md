# Forensic


## Hide and Seek


Our SOC team detected a data exfiltration case where an employee from the sales department uploaded some files to his personal cloud storage every day this week. After checking all the files, we have suspected one file is Secret_File.docx. Can you help us find the secret data in this file?

https://cdn.discordapp.com/attachments/758115188796162088/1142436267569725451/Secret_File.docx

---

### Solution

Extract any file using binwalk

`$ binwalk -e Secret_File.docx`

go to the /word and check the content

`document.xml  endnotes.xml  fontTable.xml  footnotes.xml  header1.xml  _rels  settings.xml  styles.xml  theme  webSettings.xml`

The header1.xml name look weird, right?

Let see the content!

```xml
<w:t>
++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>---.>+++++++++++++++++++++.-----------------------.+++.+++++++++++++.<++++.>---.-.<----.+++++++++++++++++.--------------.>+++++++++++++.<-----------------.--.>------------------------.-----------------.<.++++.>+++++++++++++.<+++++++++++++.----------------.+++.---.>.<---.>+++++++++++++++.---------------.<+++++++++++++++++++++++.<+++++++++++++++++++++.+.>>+++++.<<-.>++++++++++.>+++++++++++++++++++++++++.
</w:t>
```

Its a brainfuck, interpret it!

CyberGonCTF{53cR37_D474_1n_H34d3R}