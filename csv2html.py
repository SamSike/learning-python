import csv

# read the data in the given CSV file

table_fp = open("testdata.csv")

data = csv.reader(table_fp)

table = []

for line in data:
    print(line)
    table.append(line)

table_fp.close()

# data in CSV file now stored in table

print(table)

# write an HTML file containing the data as a table

html_table = open("mytable.html", "w")

html_table.write("<table border='10'>\n")

html_table.write("   <tr>\n")
for field in table[0]:
    html_table.write(f"   <th> {field} </th>\n")
html_table.write("   </tr>\n")


for line in table[1:]:
    html_table.write("   <tr>\n")
    for field in line:
        html_table.write(f"   <td> {field} </td>\n")
    html_table.write("   </tr>\n")

html_table.write("</table>\n")

html_table.close()
