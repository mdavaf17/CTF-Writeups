# Forensics

## Capybara

What a cute picture of a capybara!

File: ![Capy](https://github.com/MasonCompetitiveCyber/PatriotCTF2023/blob/main/Forensics/Capybara/capybara.jpeg?raw=true)

---

### Solution

```bash
$ binwalk capybara.jpeg  

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             JPEG image data, JFIF standard 1.01
151174        0x24E86         Zip archive data, at least v2.0 to extract, compressed size: 6902, uncompressed size: 919160, name: audio.wav
158170        0x269DA         End of Zip archive, footer length: 22
```

Extract the embedded file.

`$ binwalk -e capybara.jpeg`

We got the audio.wav. Its morse audio, decode with https://morsecode.world/international/decoder/audio-decoder-adaptive.html.

`5 0 4 3 5 4 4 6 7 B 6 4 3 0 5 F 7 9 3 0 5 5 5 F 6 B 4 E 3 0 5 7 5 F 6 8 3 0 5 7 5 F 7 4 3 0 5 F 5 2 3 3 3 4 4 4 5 F 6 D 3 0 7 2 3 5 3 3 5 F 4 3 3 0 6 4 3 3 3 F 7 D`

Remove the whitespace and convert from hex to ascii.

### PCTF{d0_y0U_kN0W_h0W_t0_R34D_m0r53_C0d3?}
