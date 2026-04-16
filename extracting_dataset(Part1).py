import csv

# easier to go though files
input_files = [
    './data/daily_sales_data_0.csv',
    './data/daily_sales_data_1.csv',
    './data/daily_sales_data_2.csv'
]

with open('./data/pink_morsel.csv', 'w', newline='') as pink_morsel:
    writer = csv.writer(pink_morsel)
    writer.writerow(["sales", "date", "region"])

    for path in input_files:
        with open(path, newline='') as f:
            reader = csv.reader(f, delimiter=',')

            next(reader)  # skips the header

            for row in reader:
                # row structure: product, price, quantity, date, region
                # pink morsel is in row[0]
                if "pink morsel" not in row[0].lower():
                    continue
                else:
                    print(', '.join(row)) # check takes

                price = float(row[1].replace("$", ""))
                quantity = int(row[2])
                date = row[3]
                region = row[4]

                sales = price * quantity

                writer.writerow([sales, date, region])



# Testing stuff

# with open('./data/daily_sales_data_0.csv', newline='') as csvf0, \
#      open('./data/daily_sales_data_1.csv', newline='') as csvf2, \
#      open('./data/daily_sales_data_2.csv', newline='') as csvf3, \
#      open('./data/pink_morsel.csv', "w", newline='') as combined_csv:
#
#     files = [csvf0, csvf2, csvf3]
#     writer = csv.writer(combined_csv)
#
#     for file in files:
#         reader = csv.reader(file, delimiter=',', quotechar='|')
#         for row in reader:
#             if row[0] == "pink" and "morsel" in row[1]:
#                 writer.writerow(row)
#                 print(', '.join(row))
#                 # pink_morsel.append(row)
#
# with open('./data/pink_morsel.csv', newline='') as f:
#     for row in f:
#         print(', '.join(row))

# with open('./data/daily_sales_data_0.csv', newline='') as csvf0, \
#      open('./data/daily_sales_data_1.csv', newline='') as csvf2, \
#      open('./data/daily_sales_data_2.csv', newline='') as csvf3, \
#      open('./data/pink_morsel.csv', newline='') as combined_csv:
#      wrtier = csv.writer(combined_csv)
#      for row in pink_morsel:
#          wrtier.writerow(row)



# for row in pink_morsel:
#     print(', '.join(row))
#
# print(', '.join(pink_morsel[0]))
