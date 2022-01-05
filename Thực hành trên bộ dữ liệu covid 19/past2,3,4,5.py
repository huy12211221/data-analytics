import pandas as pd 
import matplotlib.pyplot as plt

data_frame =  pd.read_csv("D:\Data Analytics\Thực hành trên bộ dữ liệu covid 19\subset-covid-data.csv")

#data_frame.info()
#print(data_frame.continent.value_counts())
print(data_frame.groupby("continent")["cases"].sum()) # Tổng số ca mắc tại mỗi châu lục
data_agg = data_frame.sort_values("cases",ascending=False) # Sắp xếp thứ tự giảm dần
print(data_agg.head(5))
print("|Tổng số lương ca tử cong của từng châu lục|")
print(data_frame.groupby("continent")["deaths"].sum())
data_agg2 = data_frame.sort_values("deaths",ascending=False)# Top năm quóc gia có số lượng ca tử vong lớn nhất 
print(data_agg2.head(5))