import re

# Opens and creates files for processing
file = open('EXAMPLE.txt', 'r+').read()
analysis_report = open('analysis_report.txt', 'a+', encoding='utf8')

# Locates numbers within the text CDR file
total_numbers = re.findall(r'[0-9]{10}', file)

# Takes numbers from total_numbers list and 
# gets rid of repeat numbers
individual_numbers = []
for i in file.split('\n'):
		z = re.findall(r'[0-9]{10}', i)
		for i in z:
			if i not in individual_numbers:
				individual_numbers.append(i)
			else:
				pass


# Creates a clean line item list and also creates
# a list (totals_list) for sorting purposes. 
running_list = []
totals_list = []
for i in individual_numbers:
	x = total_numbers.count(i)
	line_item = str(x) + '\t\t\t' + str(i)
	running_list.append(line_item)
	totals_list.append(x)
totals_list.sort(reverse=True)

# Sorts the line item list by comparing to the 
# totals list. Also prevents duplicate on numbers
# and appends to list called, "final_list".
final_list =[]
for t in totals_list:
	for r in running_list:
		if r.startswith(str(t)) and r not in final_list:
			final_list.append(r)

# Begins the report generation part of
# the code. Prints header and sorted list
# to, "Analysis Report.txt"

analysis_report.write('\n')
analysis_report.write('██████╗ ██╗  ██╗ ██████╗ ███╗   ██╗███████╗███████╗██████╗ ███████╗ █████╗ ██╗  ██╗\n')
analysis_report.write('██╔══██╗██║  ██║██╔═══██╗████╗  ██║██╔════╝██╔════╝██╔══██╗██╔════╝██╔══██╗██║ ██╔╝\n')
analysis_report.write('██████╔╝███████║██║   ██║██╔██╗ ██║█████╗  █████╗  ██████╔╝█████╗  ███████║█████╔╝ \n')
analysis_report.write('██╔═══╝ ██╔══██║██║   ██║██║╚██╗██║██╔══╝  ██╔══╝  ██╔══██╗██╔══╝  ██╔══██║██╔═██╗ \n')
analysis_report.write('██║     ██║  ██║╚██████╔╝██║ ╚████║███████╗██║     ██║  ██║███████╗██║  ██║██║  ██╗\n')
analysis_report.write('╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝\n')
analysis_report.write('         Frequency Analysis Report Generator by ThatLukeGuy - Version 1.0\n\n\n')
analysis_report.write('Number of calls\t\tNumber Dialed/Recieved\n\n')


for i in final_list:
	analysis_report.write(i + '\n')


analysis_report.write('\n\n\t\tEND OF REPORT')




	





