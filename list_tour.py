from bs4 import BeautifulSoup
import urllib
import json

r = urllib.urlopen("https://en.wikipedia.org/wiki/List_of_Tour_de_France_general_classification_winners").read()
soup = BeautifulSoup(r)

table = soup.find('table', attrs={'class':'wikitable plainrowheaders sortable'})

header = []
for row in table.find_all('tr'):
	header.append(row.find_all('th')[0].text);
	header.append(row.find_all('th')[1].text);
	header.append(row.find_all('th')[2].text);  
	header.append(row.find_all('th')[3].text);  
	header.append(row.find_all('th')[4].text);  
	header.append(row.find_all('th')[5].text);  
	header.append(row.find_all('th')[6].text);
	header.append(row.find_all('th')[7].text);  
	header.append(row.find_all('th')[8].text);     
	break

print header;

records = []
i=0
for row in table.find_all('tr')[1:]:
	print i
	print row.find_all('td')[0].text
	record = {}
	# WWI and WWII
	if (i >= 12 and i <= 15) or (i >= 37 and i <= 43):
		print i
		print row.find_all('td')[0].text
		reason = ''
		record[header[0]] = row.find_all('td')[0].text

		if(i < 17):
			reason = 'World War I'
		else:
			reason = 'World War II'

		record[header[1]] = reason 		# Country
		record[header[2]] = reason 		# Cyclist
		record[header[3]] = reason 		# Sponsor/Team
		record[header[4]] = reason 		# Distance
		record[header[5]] = reason 		# Time/Points
		record[header[6]] = reason 		# Margin
		record[header[7]] = reason 		# Stage wins
		record[header[8]] = reason 		# Yellow jerseys
	
	# Doping	
	elif (i >= 96 and i <= 102):
		reason = 'Results voided (doping)'
		record[header[0]] = row.find_all('td')[0].text
		record[header[1]] = reason 							# Country
		record[header[2]] = reason 							# Cyclist
		record[header[3]] = reason 							# Sponsor/Team
		record[header[4]] = row.find_all('td')[1].text 		# Distance
		record[header[5]] = reason 							# Time/Points
		record[header[6]] = reason 							# Margin
		record[header[7]] = reason 							# Stage wins
		record[header[8]] = reason 							# Yellow jerseys

	# +2016
	elif i >= 114:
		break
	
	else:
		record[header[0]] = row.find_all('td')[0].text 			# Year
		record[header[1]] = row.find_all('td')[1].text 			# Country
		if i == 113:
			record[header[2]] = row.find_all('td')[0].a.text
		else: 
			record[header[2]] = row.find_all('th')[0].a.text 	# Cyclist
		record[header[3]] = row.find_all('td')[2].text 			# Sponsor/Team
		record[header[4]] = row.find_all('td')[3].text 			# Distance
		record[header[5]] = row.find_all('td')[4].text 			# Time/Points
		record[header[6]] = row.find_all('td')[5].text 			# Margin
		record[header[7]] = row.find_all('td')[6].text 			# Stage wins
		record[header[8]] = row.find_all('td')[7].text 			# Yellow jerseys

	records.append(record)
	i+=1
	
json_result = json.dumps(records)
json_result.encode('UTF-8')
print json_result

with open('data.json', 'w') as outfile:
    outfile.write(json_result)
