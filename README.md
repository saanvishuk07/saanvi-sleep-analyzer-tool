# saanvi-sleep-analyzer-tool
PROJECT TITLE :- Sleep Analyzer Tool using Python

#DESCRIPTION :-
The Sleep Analyzer tool is a Python program that analyzes and visualizes daily sleep duration data from a CSV file. It calculates key sleep statistics like average, max, min hours slept, and evaluates sleep consistency and quality. This code also gives us plot of the DISTRIBUTION OF SLEEP HOURS  & DAILY SLEEP HOURS TREND.


#FEATURES :-1. It generates sample sleep data if no data file is found.

2. It reads sleep data from a CSV file with date and hours slept.
  
3. Average sleep duration ,maximum and minimum hours slept is calculated.
   
4.Classification of sleep quality (healthy, deprived, oversleeping, etc).

5.Daily sleep hours trend plot and Histogram of sleep hours distribusion.



#TECHNOLOGIES &  TOOLS USED :-
1. Python 3

2. Pandas for data manipulation and CSV handling

3. NumPy for numerical computations

4. Matplotlib for creating visual plots

5. datetime for date handling



#STEPS TO INSTAL & RUN THE PROJECT :-

1. Make sure Python3 is installed on your system
2. Install all the req library if not alr avlable
   ex :- pip install pandas
         pip install matplotlib

3.   Now, the user has to clone or download the repo.

4.   Run the main Python Script.
     Python sleep_analyzer.py
This code is also capable to create a sample csv file if it does not exist.
5. The code will also analyze the data and display the plots also.



#INSTRUCTIONS FOR TESTING : -
1. Delete or rename the sleep_data.csv file to test the automatic sample data generation.

2. Modify sleep_data.csv to add your own sleep records and rerun the analysis.

3. Ensure the CSV file columns include Date (in YYYY-MM-DD format) and Hours for hours slept.


