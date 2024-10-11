#this program gets the total sales for a month and displays the new total, adding both sales and county tax.

#function for finding and adding sales and county tax
def tax(total_sales):
	#sales tax
	sales_tax = total_sales * 0.05
	#county tax
	county_tax = total_sales * 0.025
	#add tax
	total_tax = sales_tax + county_tax
	#total amount
	return total_tax

#get total sales for the month
total_sales = int(input("Enter the total sales amount for this month: "))
#use tax function to calculate tax
total_tax = tax(total_sales)
#calculate sales plus tax
total_amount = total_tax + total_sales
#display new amount
print(f"Your new total, including sales and county tax, is {total_amount:.2f}")is program