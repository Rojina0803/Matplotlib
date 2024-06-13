import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# plt.plot([1,2,3,4])
# plt.ylabel("NUMBERS")
# plt.xlabel("VALUES")
# plt.show()

#sample data
# x=[1,2,3,4]
# y=[1,4,9,16]
# plt.plot(x,y,'ro')
# plt.ylabel("Y-axis")
# plt.xlabel("X-axis")
# plt.title("PLOTTING")
# plt.axis([0,7,0,7])
# plt.show()

# x=[1,2,3,4,5]
# y1=[2,4,6,8,10]
# y2=[1,2,5,7,9]

# plt.plot(x,y1,label="Line1",linestyle="--") #color
# plt.plot(x,y2,label="Line2",linestyle="-")
# plt.ylabel("Y-axis")
# plt.xlabel("X-axis")
# plt.title("PLOTTING")
# plt.legend()
# plt.show()

#HOMEWORK
df = pd.read_csv('company_sales_data.csv')
#print(df)

#Exercise 1: Read Total profit of all months and show it using a line plot
plt.plot(df['month_number'], df['total_profit'])
plt.xlabel('month_number')
plt.ylabel('Total Profit')
plt.title('Total Profit of All Months')
plt.show()


#Exercise 2: Read all product sales data and show it  using a multiline plot

plt.plot(df['month_number'], df['facecream'], label='Face Cream')
plt.plot(df['month_number'], df['facewash'], label='Face Wash')
plt.plot(df['month_number'], df['toothpaste'], label='Toothpaste')
plt.plot(df['month_number'], df['bathingsoap'], label='Bathing Soap')
plt.plot(df['month_number'], df['shampoo'], label='Shampoo')
plt.plot(df['month_number'], df['moisturizer'], label='Moisturizer')

plt.xlabel('Month Number')
plt.ylabel('Units Sold')
plt.title('Product Sales Data')
plt.legend()
plt.show()

#Exercise 3: Read face cream and facewash product sales data and show it using the bar chart

plt.bar(df['month_number'], df['facecream'], label='Face Cream')
plt.bar(df['month_number'], df['facewash'], label='Face Wash')

plt.xlabel('Month Number')
plt.ylabel('Units Sold')
plt.title('Face Cream and Face Wash Sales Data')
plt.legend()
plt.show()



#Exercise 4: Calculate total sale data for last year for each product and show it using a Pie chart

total_facecream = sum(df['facecream'])
total_facewash = sum(df['facewash'])
total_toothpaste = sum(df['toothpaste'])
total_bathingsoap = sum(df['bathingsoap'])
total_shampoo = sum(df['shampoo'])
total_moisturizer = sum(df['moisturizer'])

labels = ['Face Cream', 'Face Wash', 'Toothpaste', 'Bathing Soap', 'Shampoo', 'Moisturizer']
sizes = [total_facecream, total_facewash, total_toothpaste, total_bathingsoap, total_shampoo, total_moisturizer]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'ed', 'purple']
plt.title('Total Sales Data for Last Year')
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.show()



