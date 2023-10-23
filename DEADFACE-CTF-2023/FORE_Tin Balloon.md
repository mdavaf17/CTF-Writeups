# Forensic

## Tin Balloon

We've discovered that DEADFACE was somehow able to extract a fair amount of data from Techno Global Research Industries. We are still working out the details, but we believe they crafted custom malware to gain access to one of TGRI's systems. We intercepted a Word document that we believe mentions the name of the malware, in addition to an audio file that was part of the same conversation. We're not sure what the link is between the two files, but I'm sure you can figure it out!

Submit the flag as: flag{executable_name}. Example: flag{malware.exe}.


File: https://cdn.discordapp.com/attachments/758115188796162088/1165893168034758676/Sequence_01.zip?ex=654881a0&is=65360ca0&hm=235e902341dc6fbd43fa46e008e32174c36c78c1b1b2a4ccbfdd1153c336852e&


---

### Solution


There is weird audio at 3:17 Sequence 01.mp3. Do Spectral Analysis with https://www.dcode.fr/spectral-analysis will produces `Gr33dK1Lzz@11Wh0Per5u3`

Decrypt Untitlednosubject.docx with msoffcrypto-tool

`msoffcrypto-tool Untitlednosubject.docx  decrypted.docx -p Gr33dK1Lzz@11Wh0Per5u3`


Extract .docx file with binwalk

`binwalk -e decrypted.docx `

Look at /word/document.xml, we got "but we are going to use **Wh1t3_N01Z3.exe** to sent out a reverse shell. Be prepared to listen for the signal. "

>flag{Wh1t3_N01Z3.exe}