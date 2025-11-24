import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

FILE_NAME = "sleepdata.csv"
#funct to create sample data
def create_samplesleepdata(filename=FILE_NAME, days =30):
  #this will generate a sample CSV file  id does not exists"
  try:
    pd.read_csv(filename)
    return
  except FileNotFoundError:
    pass

  print(f"Sample data file '{filename}' not found. Creating a new one")
  dates = pd.date_range(end=datetime.now().date(), periods=days, freq='D')

  #simulate slightly inconsistent sleep around 7.5 hours
  np.random.seed(42)
  hours_slept = np.random.normal(loc=7.5 , scale=0.8, size=days).clip(min=5, max=10).round(2)

  data = pd.DataFrame({
    'Date': dates.strftime('%Y-%m-%d'),
    'Hours' : hours_slept
  })
  data.to_csv(filename, index=False)
  print(f"Sample data created with {days} days of records.")
try:
  create_samplesleepdata(FILE_NAME)
  df = pd.read_csv(FILE_NAME)
  if "Hours" not in df.columns:
    raise ValueError("CSV must contain a column named 'Hours'.")
  hours = df["Hours"]
  
  #Use the index (row no.) for plotting if no date or day column is specified
  x_axis_data = df.index
  x_label = "Day Number"
  if "Date" in df.colums:
    df['Date'] = pd.to_datetime(df['Date'])
    x_axis_data = df['Date']
    x_label = "Date"

except Exception as e :
  print(f"AN error occurred during data loading: {e}")
  exit()

avg_sleep = hours.mean()
max_sleep = hours.max()
min_sleep = hours.min()
deviations = hours.diff().abs().dropna()
consistency_score = round(10-min(10, (deviations.mean() *2)),2)

#SUMMARY
if 7<= avg_sleep <= 9:
  quality = "Healthy Sleep Duration"
elif avg_sleep <6:
  quality = "Sleep Derived"
elif avg_sleep >9:
  quality = "Oversleeping"
else:
  quality = "Slightly Below Ideal "

print("\n----Sleep Pattern Analysis ----")
print(f"Total Records: {len(hours)}")
print(f"Average Sleep: **{avg_sleep:.2f} hours**")
print(f"Maximum Sleep: {max_sleep} hours")
print(f"Minimum Sleep: {min_sleep} hours")
print(f"Consistency Score (0-10): **{consistency_score}**")
print(f"Sleep Quality: **{quality}**")
print("--------------------------------------\n")

#1. Sleep Hours Trend
plt.figure(figsize=(10,5))
plt.plot(x_axis_data, hours, marker="o" , linestyle='-' , color= 'indigo')
plt.xlabel(x_label)
plt.ylabel("Hours Slept")
plt.title("1. Daily Sleep Hours Trend")
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

#2. Histogram of Sleep Hours
plt.figure(figsize=(8,5))
plt.hist(hours, bins=8, edgecolor= 'black', color='seagreen')
plt.xlabel("Hours Slept")
plt.ylabel("Frequency(Days)")
plt.title("2. Distribution of Sleep Hours")
plt.axvline(avg_sleep, color='red', linestyle='dashed',linewidth=1, label=f'Average: {avg_sleep:.2f}h')
plt.legend()
plt.tight_layout()
plt.show()
    
    
    
    

   
  


                      
                      
                      
                      
                      
