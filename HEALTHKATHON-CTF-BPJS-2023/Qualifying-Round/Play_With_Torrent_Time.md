# Misc

## Bermain Waktu dengan Torrent

The official torrent files you can find on the site: [https://ubuntu.com/download/alternative-downloads](https://ubuntu.com/download/alternative-downloads)

Extract the information in the following torrent file,
What date was the torrent created (date created)?

Answers use GMT time +0000 with ISO8601 format, answers can also be answered with the prefix **BPJS{}** or not with the prefix **BPJS{}**

Example Answer:
**2001-01-01T01:01:01.00+00:00**

Torrent:
[https://releases.ubuntu.com/22.04/ubuntu-22.04.3-desktop-amd64.iso.torrent](https://releases.ubuntu.com/22.04/ubuntu-22.04.3-desktop-amd64.iso.torrent)

---

### Solution

`$ exiftool ubuntu-22.04.3-desktop-amd64.iso.torrent`

Create Date                     : 2023:08:11 01:30:54+07:00

Since it UTC+07. Substract it with 07 and convert to ISO8601

>BPJS{2023-08-10T18:30:54.00+00:00}