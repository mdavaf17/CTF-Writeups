# Forensics

## Better to Burn in the Light

[This](https://uwspedu-my.sharepoint.com/:u:/g/personal/cjohnson_uwsp_edu/Efkglq1V9PtAqZxOU5IEoFABx3eLJ2x383ume8dllMiSqQ?e=LOhNdP) is an image of a disk that once contained several files. They were deleted prior to imaging, unfortunately. To find the flag, we're going to need to bring some of them back from the dead. The flag is actually broken up between two of them. Carve the files out of the image and restore any missing file headers to find the pieces to reassemble.

---

### Solution

`$ binwalk --dd=".*" DF3.001 `

We got the thumbnail image.

![part 1](https://media.discordapp.net/attachments/758115188796162088/1195362965499695124/image.png?ex=65b3b783&is=65a14283&hm=91c96dd0f9989c202f12ee738a716e554f4a7f0e0e398b4be2b2a42e320745d0&=&format=webp&quality=lossless&width=2160&height=492)![part2](https://media.discordapp.net/attachments/758115188796162088/1195363074161524767/image.png?ex=65b3b79d&is=65a1429d&hm=aacbd2666dac684295fd37eefa28231344a210aaea174d1f17ea52a1c21a3810&=&format=webp&quality=lossless&width=2160&height=432)

### poctf{uwsp_5h1v3r_m3_71mb3r5}