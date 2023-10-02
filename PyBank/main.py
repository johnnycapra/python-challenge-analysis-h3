import os 
import csv

budget_data_csv = os.path.join("Resources", "budget_data.csv")

total_months = []
total_amount = []
financial_average = []

with open(budget_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)

    for row in csvreader:
        total_months.append(row[0])
        total_amount.append(int(row[1]))
        # print(f'{len(total_amount)}')
    for i in range(len(total_amount)-1):
        financial_average.append(total_amount[i+1]-total_amount[i])
        # print(f'{financial_average}')

greatest_increase = max(financial_average)
greatest_decrease = min(financial_average)
greatest_month_increase = financial_average.index(max(financial_average)) + 1
greatest_month_decrease = financial_average.index(min(financial_average)) + 1
# print(f'{total_months[greatest_month_increase]}')
# print(f'{total_months[greatest_month_decrease]}')
text_output = ("Financial Analysis\n"
                "-------------------------\n"
                f'Total Months: ${len(total_months)}\n'
                f'Total: ${sum(total_amount)}\n'
                f'Average Change: ${round(sum(financial_average)/len(financial_average),2)}\n'
                f'Greatest Increase in Profits: {total_months[greatest_month_increase]}\n'
                f'Greatest Decrease in Profits: {total_months[greatest_month_decrease]}\n'
)

print(text_output)

financial_analysis = os.path.join("analysis", "financial_analysis.txt")
with open(financial_analysis, "w") as file:
  
    file.write(text_output)








    

