# PhoneFreak
Call Detail Records Frequency Analysis Report Generator


Quick and easy code for generating call frequency reports from call detail records. 

1. Change, "EXAMPLE.txt" on line 4 to your txt file containing your CDR data. Simply convert your PDF or XLSX to a tab delimited text file. 
2. Make sure that your tab delimited text file is in the same directory as your frequency.py
3. You may have to adjust the regex to fit the specific formating of your CDR. Currently the program searched for numbers formatted as follows; "0001112222". Suggested regex for other format (111)222-3333, "([0-9]{3})[0-9]{3}-[0-9]{4}". The regex to be modified can be found on line 14.
