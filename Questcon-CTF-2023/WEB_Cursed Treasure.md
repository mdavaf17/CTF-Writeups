# Web Exploitation

## Cursed Treasure

Ahoy, matey! a bottle of code! Captain Jack Sparrow has hidden his secret pirate flag using the ancient JavaScript Cipher. It's your duty to decipher the code and uncover the hidden treasure, savvy?

https://web-explorer.netlify.app

---

### Solution

There are 3 Maps (page). Each page bring `id` argumen. 


First map: https://questcon-cursed-treasure.chals.io/maps.php?id=e25388fde8290dc286a6164fa2d97e551b53498dcbf7bc378eb1f178.

We notice that the argument is `SHA224` of 1. 

Second map: https://questcon-cursed-treasure.chals.io/maps.php?id=58b2aaa0bfae7acc021b3260e941117b529b2e69de878fd7d45c61a9, `SHA224` of 2.

Third map: https://questcon-cursed-treasure.chals.io/maps.php?id=271f93f45e9b4067327ed5c8cd30a034730aaace4382803c3e1d6c2f, `SHA224` of 4.

Thats skip `id = 3`. Try to send id of 3.

3 = 4cfc3a1811fe40afa401b25ef7fa0379f1f7c1930a04f8755d678474

After send id of 3, we get Username verification form. Verified with Barbossa.

https://questcon-cursed-treasure.chals.io/maps.php?id=4cfc3a1811fe40afa401b25ef7fa0379f1f7c1930a04f8755d678474&username=Barbossa


### QUESTCON{Th3_Pir4t3s_0f_Th3_Car1bb34n_Arr_Th3_B3st!}