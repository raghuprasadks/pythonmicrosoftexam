import pandas as pd
from matplotlib import pyplot as plt
df = pd.read_csv("salesdata.csv")
profitlist = df["Profit"].tolist()
monthlist = df["Months"].tolist()
plt.plot(monthlist,profitlist)
plt.xlabel("Month")
plt.ylabel("Profit")
plt.xticks(monthlist)
plt.title("profit per month")
plt.yticks(100000,200000,300000,400000,500000,600000,700000,800000)
plt.show()

'''
a
'''
import pandas as pd
df=pd.read_csv("Automobile_data.csv")
df.head(10)
df.tail(5)


import pandas as pd
import matplotlib.pyplot as plt  

df = pd.read_csv("company_sales_data.csv")
monthList  = df ['month_number'].tolist()
faceCrem= df ['facecream'].tolist()
faceWash= df ['facewash'].tolist()

lst = [a-0.25 for a in monthList]

plt.bar([a-0.25 for a in monthList], faceCrem, width= 0.25, label = 'FaceCream')
plt.bar([a+0.25 for a in monthList], faceWash, width= -0.25, label = 'Face Wash' )
plt.xlabel('Month Number')
plt.ylabel('Sales units in number')
plt.legend(loc='upper left')
plt.title(' Sales data')

plt.xticks(monthList)
plt.grid(True, linewidth= 1, linestyle="--")
plt.title('Facewash and facecream sales data')
plt.show()

