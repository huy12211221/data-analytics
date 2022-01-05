import pandas as pd

data_frame = pd.read_csv("D:\Data Analytics\Thực hành trên bộ dữ liệu Online Retail\OnlineRetail.csv", encoding="ISO-8859-1")

#data_frame.info()
#print(data_frame.Country.value_counts())
country = data_frame.Country.unique()
print(str(country.size))
