
import json
import pprint
import os
from collections import defaultdict
import matplotlib.pyplot as plt
import csv


files = ['data/baby_names_2011-2021.json']
all_names = []

for file in files:
    with open(file, encoding='utf8') as fin:
        content = json.load(fin)  
        all_names.extend(content["data"])  

print(f'Total number of names = {len(all_names)}') #69214

# number of names and what their race is 

with open('data/baby_names_2011-2021.json', encoding='utf8') as fin:
    content = json.load(fin)
    baby_data = content["data"]

#kelly 

kelly_counts = defaultdict(int)

for row in baby_data:
    year = row[8]
    gender = row[9]
    ethnicity = row[10]
    name = row[11].upper()  
    count = int(row[12])    

    if name == 'KELLY':
        kelly_counts[ethnicity] += count

print("Number of kids named 'KELLY' by ethnicity:")
for ethnicity, count in kelly_counts.items():
    print(f"{ethnicity}: {count}")


lab_dict = {
    'Hispanic': 12,
    'White non-Hispanic': 167,
    'Black non-Hispanic': 68,
    'Asian and Pacific Islander': 0,
    }


terms = list(lab_dict.keys())
counts = list(lab_dict.values())

sorted_terms = []
sorted_counts = []
for term in sorted(terms):
    sorted_terms.append(term)
    sorted_counts.append(lab_dict[term])

plt.bar(sorted_terms, sorted_counts)

plt.xlabel('Ethnicity', fontweight='bold')
plt.ylabel('Number of Kids Named Kelly', fontweight='bold')
#plt.title('Distribution of the Name "Kelly" by Ethnicity', fontweight='bold')

plt.xticks(rotation=30, ha='right')
plt.tight_layout()  
#plt.show()
plt.savefig('kelly_baby_names.png')



"""
theft_count = 0
battery_count = 0
narcotics_count = 0
total_crimes = 0

total_by_month = defaultdict(int)
theft_by_month = defaultdict(int)
battery_by_month = defaultdict(int)
narcotics_by_month = defaultdict(int)

with open('data/crimes_2024-2025.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    

    raw_headers = next(reader)
    headers = [h.strip() for h in raw_headers]  

    for row in reader:
        row_dict = dict(zip(headers, [val.strip() for val in row]))
        total_crimes += 1

        if row_dict.get('PRIMARY DESCRIPTION', '').upper() == 'THEFT':
            theft_count += 1

        if row_dict.get('PRIMARY DESCRIPTION', '').upper() == 'BATTERY':
            battery_count += 1
        
        if row_dict.get('PRIMARY DESCRIPTION', '').upper() == 'NARCOTICS':
            narcotics_count += 1


print(f"Total Number of Crimes: {total_crimes}")
print(f"Total number of thefts: {theft_count}")
print(f"Total number of Battery crimes: {battery_count}")
print(f"Total number of Narcotic crimes: {narcotics_count}")

"""

total_by_month = defaultdict(int)
theft_by_month = defaultdict(int)
battery_by_month = defaultdict(int)
narcotics_by_month = defaultdict(int)

with open('data/crimes_2024-2025.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)

    raw_headers = next(reader)
    headers = [h.strip() for h in raw_headers]  

    for row in reader:
        row_dict = dict(zip(headers, [val.strip() for val in row]))

        date_str = row_dict.get('DATE  OF OCCURRENCE', '')
        try:
            parts = date_str.split()
            date_only = parts[0]  
            month, day, year = date_only.split('/')
            month_key = f"{year}-{month.zfill(2)}"
        except (IndexError, ValueError):
            continue 

        primary = row_dict.get('PRIMARY DESCRIPTION', '').upper()

        total_by_month[month_key] += 1

        if primary == 'THEFT':
            theft_by_month[month_key] += 1
        elif primary == 'BATTERY':
            battery_by_month[month_key] += 1
        elif primary == 'NARCOTICS':
            narcotics_by_month[month_key] += 1

months = sorted(total_by_month.keys())
totals = [total_by_month[m] for m in months]
thefts = [theft_by_month[m] for m in months]
batteries = [battery_by_month[m] for m in months]
narcotics = [narcotics_by_month[m] for m in months]

print(f"Total Number of Crimes: {sum(totals)}")
print(f"Total number of thefts: {sum(thefts)}")
print(f"Total number of Battery crimes: {sum(batteries)}")
print(f"Total number of Narcotic crimes: {sum(narcotics)}")

plt.figure(figsize=(12, 6))
plt.plot(months, totals, label='Total Crimes', linewidth=2)
plt.plot(months, thefts, label='Theft')
plt.plot(months, batteries, label='Battery')
plt.plot(months, narcotics, label='Narcotics')
plt.xlim(months[0], months[-1])

plt.xlabel('Year-Month', fontweight='bold')
plt.ylabel('Number of Crimes', fontweight='bold')
#plt.title('Monthly Crime Trends (2024–2025)', fontweight='bold')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()
#plt.show()
plt.savefig('Crimes_by_Month.png')





