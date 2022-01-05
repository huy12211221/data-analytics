import pandas as pd
from pandas.core.indexes.base import Index 

data_frame = pd.read_csv("D:\Data Analytics\Thực hành trên bộ dữ liệu Online Retail\OnlineRetail.csv",encoding= "ISO-8859-1")

#1
data_frame["total"] = data_frame["Quantity"] * data_frame["UnitPrice"]
print("Tổng số lượng đơn hàng bán ra: "+ str(data_frame["total"].size))
print("Tổng doanh thu: " + str(data_frame["total"].sum()))

#2
print("""--------------------------------------------------------
#Top 10 mặt hàng có số lương bán ra lớn nhất: """)
grounp_by = data_frame.groupby(['StockCode', 'Description'])
data = grounp_by["Quantity"].sum().sort_values(ascending=False)
print(data.head(10))

#3
data_frame["total"] = data_frame["Quantity"] * data_frame["UnitPrice"]
grouped = data_frame.groupby(["StockCode","Description"])["total"].sum().sort_values(ascending=False)
print(grouped.head(10))