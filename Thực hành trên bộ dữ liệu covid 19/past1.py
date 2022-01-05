import pandas as pd
import matplotlib.pyplot as plt

data_frame = pd.read_csv("D:\Data Analytics\Thực hành trên bộ dữ liệu covid 19\subset-covid-data.csv")
#print(data_frame.info())
#data_frame.info()
#print(data_frame.date.value_counts())
cleaded_data = data_frame[data_frame.date == "2020-04-12"]
#print(cleaded_data)
print(str(cleaded_data.cases.mean())) #trung bình số ca mắc mới(cases)
print(str(cleaded_data.cases.median())) #trung vị số ca mắc mới
print(data_frame.describe())
plt.hist(x=data_frame["cases"],bins=200)
plt.title("Phân bố số ca mắc mới")
plt.xlabel("Số ca mắc mới")
plt.ylabel("Số lượng quốc gia")
plt.show() 