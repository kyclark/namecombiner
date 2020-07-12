# namecombiner

Python program to create married hybrid names.

My wife's last name is "Kindler," and years ago we tried to create the worst mash-up of her name with "Clark," part of my last name.
We arrived at "Clardler."

Yesterday I learned that friends had unexpectedly wed, so I wanted to find all possible combinations of their names; hence, this program, which uses `itertools.product` to combine all possible beginning and ending strings from the two given names.

```
$ ./namecombiner.py Clark Kindler
C-Kindler
C-dler
C-er
C-indler
C-ler
C-ndler
C-r
Cl-Kindler
Cl-dler
Cl-er
Cl-indler
Cl-ler
Cl-ndler
Cl-r
Cla-Kindler
Cla-dler
Cla-er
Cla-indler
Cla-ler
Cla-ndler
Cla-r
Clar-Kindler
Clar-dler
Clar-er
Clar-indler
Clar-ler
Clar-ndler
Clar-r
Clark-Kindler
Clark-dler
Clark-er
Clark-indler
Clark-ler
Clark-ndler
Clark-r
K-Clark
K-ark
K-k
K-lark
K-rk
Ki-Clark
Ki-ark
Ki-k
Ki-lark
Ki-rk
Kin-Clark
Kin-ark
Kin-k
Kin-lark
Kin-rk
Kind-Clark
Kind-ark
Kind-k
Kind-lark
Kind-rk
Kindl-Clark
Kindl-ark
Kindl-k
Kindl-lark
Kindl-rk
Kindle-Clark
Kindle-ark
Kindle-k
Kindle-lark
Kindle-rk
Kindler-Clark
Kindler-ark
Kindler-k
Kindler-lark
Kindler-rk
```

Source contains both unit and integration tests.

To test:

```
$ pytest -xv namecombiner.py test.py
============================= test session starts ==============================
...

namecombiner.py::test_beginnings PASSED                                  [ 20%]
namecombiner.py::test_endings PASSED                                     [ 40%]
test.py::test_exists PASSED                                              [ 60%]
test.py::test_usage PASSED                                               [ 80%]
test.py::test_clardler PASSED                                            [100%]

============================== 5 passed in 0.16s ===============================
```
