# Web Exploitation

## We Rest Upon a Single Hope

I am Vinz, Vinz Clortho, Keymaster of Gozer. Volguus Zildrohar, Lord of the Sebouillia. Are you the Gatekeeper?

[Are you the Keymaster?](https://nvstgt.com/Hope2/index.html)

---

### Solution

Looking to the source code.

```html
<HEAD>
    <TITLE>I dreamed a dream the other night...</TITLE>
    <LINK rel="stylesheet" type="text/css" href="./static/style.css">
    <SCRIPT>
        function Gozer(key) {
            var hash = 0, i, chr;
            for (i = 0; i < key.length; i++) {
                chr   = key.charCodeAt(i);
                hash  = ((hash << 5) - hash) + chr;
                hash |= 0;
            }
            return hash;
        }
        function conv(s)	{
            var a = [];
            for (var n = 0, l = s.length; n < l; n ++) {
                var hex = Number(s.charCodeAt(n)).toString(16);
                a.push(hex);
            }
            return a.join('');
        }
        function Zuul(key) {
            if (key == v) {
                var Gatekeeper = [];
                var y = [];
                var z = [];
                Gatekeeper[0] = "706f6374667b75777370";
                Gatekeeper[1] = "formal";
                Gatekeeper[2] = "88410";
                for (var i = 0, l = Gatekeeper[0].length; i < l; i ++) {
                    if (i == 0 || i % 2 == 0) {
                        y += String.fromCharCode(parseInt((Gatekeeper[0].substring(i, i+2)), 16));
                    }
                }
                z[0] = y;
                z[1] = Gatekeeper[2][3];
                z[2] = Gatekeeper[2][2] + Gatekeeper[1][3];
                z[3] = z[2][0] + Gatekeeper[1][5] + Gatekeeper[1][5];
                z[4] = (Gatekeeper[2]/12630) + "h" + z[2][0] + (Gatekeeper[2][0]-1);
                z[5] = z[4][0] + z[4][1] + '3' + Gatekeeper[1][2] + '3';
                z[6] = (Gatekeeper[2]/Gatekeeper[2]) + '5';
                z[7] = (Gatekeeper[2]*0) + Gatekeeper[1][0];
                z[8] = (Gatekeeper[2]/12630) + "h" + '3';
                z[9] = Gatekeeper[1][3] + (Gatekeeper[2]*0) + '5' + (Gatekeeper[2][0]-1);
                z[10] = 'r' + '3' + z[2][0] + Gatekeeper[1][5] + '}';
                console.log(z.join("_"));
            } else {
                console.log("Gozer the Traveler. He will come in one of the pre-chosen forms. During the rectification of the Vuldrini, the traveler came as a large and moving Torg! Then, during the third reconciliation of the last of the McKetrick supplicants, they chose a new form for him: that of a giant Slor! Many Shuvs and Zuuls knew what it was to be roasted in the depths of the Slor that day, I can tell you!");
            }
        }
        var p = navigator.mimeTypes+navigator.doNotTrack;
        var o = navigator.deviceMemory;
        var c = navigator.vendor+navigator.userAgent;
        var t = navigator.product+p;
        var f = o+c+p;
        var v = Gozer(p/((o+c)*t)+f);
    </SCRIPT>
</HEAD>
```

`<INPUT id="login" type="submit" value="Submit" onclick="return Zuul(key.value)">`

We have to make `key.value == v`. Leaks `v` from the console.

![solve](https://media.discordapp.net/attachments/758115188796162088/1195545315588182036/image.png?ex=65b46157&is=65a1ec57&hm=5704ff00027b9f47d9256fd27bbf47bd4f2269d552628d17ea34c52dfa7a101c&=&format=webp&quality=lossless&width=2160&height=342)

### poctf{uwsp_1_4m_4ll_7h47_7h3r3_15_0f_7h3_m057_r34l}