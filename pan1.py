import numpy as np

import matplotlib.pyplot as plt

barwidth= 0.25

fig=plt.subplots(figsize=(12,8))

IT=[20,30,40,50,60]

ECE=[25,35,45,55,65]

CSE=[30,40,50,60,70]

br1= np.arange(len(IT))

br2=[x + barwidth for x in br1]

br3=[x + barwidth for x in br2]

plt.bar(br1,IT, color="r",width=barwidth,edgecolor="grey",label="IT")

plt.bar(br2,ECE, color="b",width=barwidth,edgecolor="grey",label="ECE")

plt.bar(br3,CSE, color="g",width=barwidth,edgecolor="grey",label="CSE")

plt.xlabel("Branch",fontweight="bold",fontsize=15)

plt.ylabel('Students passed', fontweight="bold", fontsize=15)

plt.xticks([r + barwidth for r in range(len(IT))],["2016","2017","2018","2019","2020"])

plt.title("Bar graph", fontweight="bold", fontsize=15)

plt.legend()

plt.show()