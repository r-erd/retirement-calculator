# 💸 retirement calculator

Python script that uses simulations to make calculations regarding the retirement rage, takeout rates and savings rates.
One can set a fixed monthly input and output rate, which will be inflation adjusted over time. 
The interest is paid on the accumulated total wealth, during the savings phase and during the takeout phase.

The two main functions are
- `calculateMinimalInvestment` - calculates how much money has to be saved per month to be able to stop working at given age
- `howMuchEarlier` - essentially converts money to time, calculates how much a given amount of money reduces the retirement age

> ⚠️ Tax is not part of this calculation!

> 💡 I wrote this some random afternoon without any careful planning, so if you spot any mistakes or have ideas for improvement, feel free to open an issue or a pull request. Also, this is NOT financial advice.


### Example output

The following is an example for calculating what the minimum monthly investment rate is, 
so that it lasts until (current age) + 60 years, with the savings ending at the desired retirement age.

For the parameters:
- age 23 to 86 (max)
- starting wealth: 0
- desired retirement age: 55
- monthly savings rate: 1000 (starting, will attempt to reduce this)
- monthly takeout rate: 2500 
- inflation: 1.02
- interest: 1.05

Using the function `calculateMinimalInvestment(params, 60)`.


```
Age:       Add (monthly):    Sub (monthly):    Total:  
23 years  |    +847  €     |    -0    €       | 10159   €  
24 years  |    +864  €     |    -0    €       | 21030   €  
25 years  |    +881  €     |    -0    €       | 32651   €  
26 years  |    +898  €     |    -0    €       | 45064   €  
27 years  |    +916  €     |    -0    €       | 58314   €  
28 years  |    +935  €     |    -0    €       | 72446   €  
29 years  |    +953  €     |    -0    €       | 87510   €  
30 years  |    +972  €     |    -0    €       | 103555  €  
31 years  |    +992  €     |    -0    €       | 120636  €  
32 years  |    +1012 €     |    -0    €       | 138809  €  
33 years  |    +1032 €     |    -0    €       | 158133  €  
34 years  |    +1053 €     |    -0    €       | 178671  €  
35 years  |    +1074 €     |    -0    €       | 200489  €  
36 years  |    +1095 €     |    -0    €       | 223656  €  
37 years  |    +1117 €     |    -0    €       | 248243  €  
38 years  |    +1139 €     |    -0    €       | 274328  €  
39 years  |    +1162 €     |    -0    €       | 301991  €  
40 years  |    +1185 €     |    -0    €       | 331316  €  
41 years  |    +1209 €     |    -0    €       | 362392  €  
42 years  |    +1233 €     |    -0    €       | 395312  €  
43 years  |    +1258 €     |    -0    €       | 430173  €  
44 years  |    +1283 €     |    -0    €       | 467080  €  
45 years  |    +1309 €     |    -0    €       | 506140  €  
46 years  |    +1335 €     |    -0    €       | 547467  €  
47 years  |    +1362 €     |    -0    €       | 591180  €  
48 years  |    +1389 €     |    -0    €       | 637407  €  
49 years  |    +1417 €     |    -0    €       | 686278  €  
50 years  |    +1445 €     |    -0    €       | 737932  €  
51 years  |    +1474 €     |    -0    €       | 792516  €  
52 years  |    +1503 €     |    -0    €       | 850183  €  
53 years  |    +1533 €     |    -0    €       | 911094  €  
54 years  |    +1564 €     |    -0    €       | 975419  €  
55 years  |    +1595 €     |    -0    €       | 1043335 €  
56 years  |    +0    €     |    -4902 €       | 1036682 €  
57 years  |    +0    €     |    -5000 €       | 1028519 €  
58 years  |    +0    €     |    -5100 €       | 1018749 €  
59 years  |    +0    €     |    -5202 €       | 1007265 €  
60 years  |    +0    €     |    -5306 €       | 993960  €  
61 years  |    +0    €     |    -5412 €       | 978715  €  
62 years  |    +0    €     |    -5520 €       | 961410  €  
63 years  |    +0    €     |    -5631 €       | 941914  €  
64 years  |    +0    €     |    -5743 €       | 920093  €  
65 years  |    +0    €     |    -5858 €       | 895802  €  
66 years  |    +0    €     |    -5975 €       | 868890  €  
67 years  |    +0    €     |    -6095 €       | 839199  €  
68 years  |    +0    €     |    -6217 €       | 806561  €  
69 years  |    +0    €     |    -6341 €       | 770799  €  
70 years  |    +0    €     |    -6468 €       | 731726  €  
71 years  |    +0    €     |    -6597 €       | 689148  €  
72 years  |    +0    €     |    -6729 €       | 642858  €  
73 years  |    +0    €     |    -6864 €       | 592638  €  
74 years  |    +0    €     |    -7001 €       | 538260  €  
75 years  |    +0    €     |    -7141 €       | 479483  €  
76 years  |    +0    €     |    -7284 €       | 416054  €  
77 years  |    +0    €     |    -7429 €       | 347705  €  
78 years  |    +0    €     |    -7578 €       | 274155  €  
79 years  |    +0    €     |    -7729 €       | 195109  €  
80 years  |    +0    €     |    -7884 €       | 110256  €  
81 years  |    +0    €     |    -8042 €       | 19267   €  
Ran out of money in year: 82 and month: 2
82 years  |    +0    €     |    -8203 €       | -4377   €  
Minimal investment rate is 830€.
It will last for 723 months, which is 60.25 years
```
