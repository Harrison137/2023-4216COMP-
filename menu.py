import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Sample - Superstore.csv', encoding='windows-1252')

populations = {
    'California': 39538223,
    'New York': 19530351,
    'Texas': 29145505,
    'Washington': 7693612,
    'Pennsylvania': 13002700,
    'Florida': 21538187,
    'Illinois': 12812508,
    'Ohio': 11799448,
    'Michigan': 10077331,
    'Virginia': 8626207,
    'North Carolina': 10611862,
    'Indiana': 6745354,
    'Georgia': 10711908,
    'Kentucky': 4499692,
    'New Jersey': 9288994,
    'Arizona': 7278717,
    'Wisconsin': 5851754,
    'Colorado': 5845526,
    'Tennessee': 6910840,
    'Minnesota': 5706494,
    'Massachusetts': 7029917,
    'Delaware': 989948,
    'Maryland': 6177224,
    'Rhode Island': 1098164,
    'Missouri': 6154913,
    'Oklahoma': 3980783,
    'Alabama': 5024279,
    'Oregon': 4217737,
    'Nevada': 3104614,
    'Connecticut': 3605944,
    'Arkansas': 3011524,
    'Utah': 3271616,
    'Mississippi': 2961279,
    'Louisiana': 4648794,
    'Vermont': 643077,
    'South Carolina': 5118425,
    'Nebraska': 1961504,
    'New Hampshire': 1377529,
    'Montana': 1085407,
    'New Mexico': 2117522,
    'Iowa': 3192406,
    'Idaho': 1826156,
    'Kansas': 2937880,
    'District of Columbia': 689545,
    'Wyoming': 576851,
    'South Dakota': 886667,
    'Maine': 1362359,
    'West Virginia': 1793716,
    'North Dakota': 779094
}

def option1():
    #bar chart to display average sales per region
    df = pd.read_csv('Sample - Superstore.csv', encoding='windows-1252')
    #calculate the average sales per region
    avg_sales = df.groupby('Region')['Quantity'].mean()

    #plot the results as a bar chart
    avg_sales.plot(kind='bar')
    plt.title('Average Sales per Region')
    plt.xlabel('Region')
    plt.ylabel('Average Sales')
    plt.show()

def option2():
    #the average profit per segment
    df = pd.read_csv('Sample - Superstore.csv', encoding='windows-1252')
    #calculate the average profit per segment
    avgSegmentProfit = df.groupby('Segment')['Profit'].mean()
    avgSegProfit = pd.DataFrame(avgSegmentProfit)
    print (avgSegProfit)

def option3():
    # Top 5 products by sales
    top_sales = df.groupby('Product Name').agg({'Sales': 'sum', 'Profit': 'sum'}).sort_values('Sales', ascending=False).head(5)
    print("\nTop 5 products by sales:")
    for index, row in top_sales.iterrows():
        print(f"{index}, Total sales = ${row['Sales']:.2f}, Total Profit = ${row['Profit']:.2f}")
    print()

    # Bottom 5 products by sales
    bottom_sales = df.groupby('Product Name').agg({'Sales': 'sum', 'Profit': 'sum'}).sort_values('Sales').head(5)
    print("Bottom 5 products by sales:")
    for index, row in bottom_sales.iterrows():
        print(f"{index}, Total sales = ${row['Sales']:.2f}, Total Profit = ${row['Profit']:.2f}")
    print()

    # Top 5 products by profit
    top_profit = df.groupby('Product Name').agg({'Sales': 'sum', 'Profit': 'sum'}).sort_values('Profit', ascending=False).head(5)
    print("Top 5 products by profit:")
    for index, row in top_profit.iterrows():
        print(f"{index}, Total sales = ${row['Sales']:.2f}, Total Profit = ${row['Profit']:.2f}")
    print()

    # Bottom 5 products by profit
    bottom_profit = df.groupby('Product Name').agg({'Sales': 'sum', 'Profit': 'sum'}).sort_values('Profit').head(5)
    print("Bottom 5 products by profit:")
    for index, row in bottom_profit.iterrows():
        print(f"{index}, Total sales = ${row['Sales']:.2f}, Total Profit = ${row['Profit']:.2f}")
    print()
    
def option4():
    # Calculate the number of products available
    num_products = df['Product ID'].nunique()

    # Calculate the average sale price and profit per product
    avg_sale_price = df['Sales'].mean()
    avg_profit = df['Profit'].mean()

    # Print the results
    print("\nAverage Product Sales Information:")
    print("Number of Products Available:", num_products)
    print("Average Sale price per Product: ${:.2f}".format(avg_sale_price))
    print("Average Profit per Product: ${:.2f}\n".format(avg_profit))

def option5():
    # group the data by category and calculate total sales and profit
    category_group = df.groupby('Category').agg({'Sales': 'sum', 'Profit': 'sum'})

    # print the total sales and profit for each category
    print('\nTotal sales and profit for each product category:')
    for index, row in category_group.iterrows():
        category_name = index
        total_sales = '${:,.2f}'.format(row['Sales'])
        total_profit = '${:,.2f}'.format(row['Profit'])
        print(f'{category_name}: Total sales = {total_sales}, Total profit = {total_profit}')
    print("")

def option6():
    # group sales by state
    salesByState = df.groupby('State').sum()['Sales']

    # sort sales by state in descending order
    salesByState = salesByState.sort_values(ascending=False)

    # print sales by state with formatting
    print("Sales by state:")
    for i, (state, sales) in enumerate(salesByState.items(), start=1):
        print(f"{i}. {state:<20s} ${sales:,.2f}")

    # determine which state sells the most
    stateWithMostSales = salesByState.index[0]
    stateWithLeastSales = salesByState.index[-1]
    print(f"\nThe state with the most sales is {stateWithMostSales} with sales of ${salesByState.iloc[0]:,.2f}")
    print(f"The state with the least sales is {stateWithLeastSales} with sales of ${salesByState.iloc[-1]:,.2f}\n")

def option7():
    # group profit by state
    profitByState = df.groupby('State').sum()['Profit']

    # sort profit by state in descending order
    profitByState = profitByState.sort_values(ascending=False)

    # print profit by state with formatting
    print("\nProfit by state:")
    for i, (state, profit) in enumerate(profitByState.iteritems(), start=1):
        print(f"{i}. {state:<20s} ${profit:,.2f}")

    # determine which state makes the most profit
    stateWithMostProfit = profitByState.index[0]
    stateWithLeastProfit = profitByState.index[-1]
    print(f"\nThe state with the most profit is {stateWithMostProfit} with a profit of ${profitByState.iloc[0]:,.2f}")
    print(f"The state with the least profit is {stateWithLeastProfit} with a profit of ${profitByState.iloc[-1]:,.2f}\n")

def option8():
    sales_by_state = df.groupby('State')['Sales'].sum()

    # Add the population data to the sales_by_state dataframe
    sales_by_state = sales_by_state.to_frame().reset_index()
    sales_by_state['Population'] = sales_by_state['State'].map(populations)

    # Calculate sales per capita
    sales_by_state['Sales per Capita'] = sales_by_state['Sales'] / sales_by_state['Population']

    # Format the Sales column as currency
    sales_by_state['Sales'] = sales_by_state['Sales'].apply(lambda x: f'${x:.2f}')

    # Sort the data by sales per capita
    sales_by_state = sales_by_state.sort_values(by='Sales per Capita', ascending=False)

    # Print the data
    print(sales_by_state.to_string(index=False))

def option9():
    #Average discount rate compared to average sales
    avg_discount = df.groupby('Region')['Discount'].mean()
    avg_sales = df.groupby('Region')['Quantity'].mean()
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
    ax1.plot(avg_discount)
    ax1.set_title('Average Discount by Region')
    ax2.plot(avg_sales)
    ax2.set_title('Average Quantity by Region')
    plt.show()

def option10():
    #Average discount rate compared to average sales
    avg_discount = df.groupby('State')['Discount'].mean()
    avg_sales = df.groupby('State')['Quantity'].mean()
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    ax1.plot(avg_discount)
    ax1.set_title('Average Discount by State')
    #The following 2 lines adjust the code so that the names of the states are flipped
    ax1.set_xticks(range(len(avg_discount)))
    ax1.set_xticklabels(avg_discount.index, rotation=90)
    ax2.plot(avg_sales)
    ax2.set_title('Average Sales by State')
    ax2.set_xticks(range(len(avg_sales)))
    ax2.set_xticklabels(avg_sales.index, rotation=90)
    plt.show()
    
    
def option11():
    regionProfit = df.groupby('Region')['Profit'].sum()
    print("\n Region profit($): \n", regionProfit, "\n")
    
    #This Calculates the profit margin for each region
def option12():
    regionData = df.groupby('Region').agg({'Profit': 'sum', 'Sales': 'sum'})
    regionData['Profit Margin'] = (regionData['Profit'] / regionData['Sales']) * 100

    #Sort the data by profit margin in descending order and print results
    regionData = regionData.sort_values('Profit Margin', ascending=False)
    print("\nProfit Margin by Region(%):\n")
    print(regionData[['Profit Margin']])

def option13():
    #Print profit margin per sub category
    #find profit margin for each row
    pm = (df['Profit'] / df['Sales']) * 100
    #create new column for pm in the dataframe
    df['Profit margin'] = pm
    #Match sub cat to profit margin
    subcat_pm = df.groupby('Sub-Category')['Profit margin'].mean()
    print(subcat_pm)
    

def option14():
    stateData = df.groupby('State')['Quantity'].sum()
    topStates = stateData.sort_values(ascending=False).head(10)
    # Output the top 10 states and their quantity
    print('\n Top 10 States by Quantity of items bought: \n')
    for State, Quantity in topStates.items():
        print(f'{State}: {Quantity} \n')

    
def option15():
    #User input for a state and filter the data to only include this state
    stateInput = input('\nEnter a state: ')
    stateData = df[df['State'] == stateInput]

    #Group the data by product name and sum the profit for each product and then retrieve the name and profit of the most profitable product
    product_data = stateData.groupby('Product Name')['Profit'].sum()
    mostProfitable = product_data.idxmax()
    profit = product_data.max()

    #Print the name of the most profitable product and the profit
    print(f'\nThe most profitable item in {stateInput} is "{mostProfitable}" with a profit of ${profit:.2f}.\n')
        

def option16():
    #Average shipping time per product
    #Set shipping time variable to ship date - order date
    df['shipping time'] = pd.to_datetime(df['Ship Date']) - pd.to_datetime(df['Order Date'])
    #Put it into days
    df['shipping time'] = df['shipping time'].dt.days 
    #Group product name by avg shipping time and print it
    avg_shipping_time = df.groupby('Product Name')['shipping time'].mean()
    print(avg_shipping_time)

def option17():
    #Calculates the total profit for each ship mode and the percentage of total profit for each ship mode
    total_profit = df.groupby('Ship Mode')['Profit'].sum()
    percent_profit = total_profit / total_profit.sum() * 100

    #Prints the percentage of total profit for each ship mode
    print("\nPercentage of Total Profit by Ship Mode:\n")
    for mode, percent in percent_profit.items():
        print(f"{mode}: {percent:.2f}%\n")

def option18():
    # Create a scatter plot with regression line
    sns.lmplot(x='Sales', y='Profit', data=df)

    # Set the title and axis labels
    plt.title('Sales vs. Profit')
    plt.xlabel('Sales')
    plt.ylabel('Profit')

    # Show the plot
    plt.show()

def option19():
    # Create a boxplot of the profit by region and category
    sns.boxplot(x='Region', y='Profit', hue='Category', data=df)

    # Set the title and axis labels
    plt.title('Profit by Region and Category')
    plt.xlabel('Region')
    plt.ylabel('Profit')

    # Show the plot
    plt.show()

def option20():
    # Convert the Order Date column to a datetime object
    df['Order Date'] = pd.to_datetime(df['Order Date'])

    # Group the data by Order Date and sum the sales
    daily_sales = df.groupby('Order Date')['Sales'].sum()

    # Create a line chart of the sales over time
    plt.plot(daily_sales.index, daily_sales.values)

    # Set the title and axis labels
    plt.title('Sales Over Time')
    plt.xlabel('Date')
    plt.ylabel('Sales')

    # Set the x-axis tick frequency and format
    plt.xticks(pd.date_range(daily_sales.index.min(), daily_sales.index.max(), freq='6M'), rotation=45)

    # Show the plot
    plt.show()

def option21():
    # Group the data by category and sub-category and sum the sales
    category_subcategory_sales = df.groupby(['Category', 'Sub-Category'])['Sales'].sum().unstack()

    # Create a heatmap of the sales by category and sub-category
    sns.heatmap(category_subcategory_sales, cmap='Blues')

    # Set the title and axis labels
    plt.title('Sales by Category and Sub-Category')
    plt.xlabel('Sub-Category')
    plt.ylabel('Category')

    # Show the plot
    plt.show()

def option22():
    #Show average discount rate per product
    #Create dataframe with the average discount, and round it to 3 decimal places
     avg_discount = df.groupby('Product Name')['Discount'].mean().round(3)
     print(avg_discount)

def option23():
    #Show shipping mode usage per region
    #Create a dataframe with Region, Ship mode, and a count of how many times it was used
    shipMode = df.groupby('Region')['Ship Mode'].value_counts()
    print(shipMode)

def option24():
        #converts the date into date and time format
    df['Order Date'] = pd.to_datetime(df['Order Date'], format='%m/%d/%Y')
    #gets the year in a data frame
    df['Year'] = df['Order Date'].dt.year
    #gets the month in a data frame
    df['Month'] = df['Order Date'].dt.month
    #groups together the year and month with the sum of the profit
    yearAndMonth = df.groupby(['Month', 'Year'])['Profit'].sum().unstack()
    print(yearAndMonth)
    
def option25():
    #converts order date into a date time format allowing it to be correctly formatted
    df['Order Date'] = pd.to_datetime(df['Order Date'], format='%m/%d/%Y')
    #gets the sum of the total profit per day
    profitPerDay = df.groupby('Order Date') ['Profit'].sum()
    #gets the sum of the total sales per day
    salesPerDay = df.groupby('Order Date') ['Sales'].sum()
    print (salesPerDay)
    print (profitPerDay)

def option26():
     # Convert the Order Date column to datetime format
     df['Order Date'] = pd.to_datetime(df['Order Date'], format='%m/%d/%Y')

     # Create a new column for the month of each order
     df['Month'] = df['Order Date'].dt.month

     # Group the orders by month and count the number of orders in each month
     orders_by_month = df.groupby('Month').size()

     # Print the number of orders in each month
     print(orders_by_month)

def option27():
    # Get user input for state
    state = input("Enter state: ")

    # Filter the DataFrame to only include the specified state
    state_df = df[df['State'] == state]

    # Group the data by Ship Mode, and calculate the count for each group
    totals_by_ship_mode = state_df.groupby('Ship Mode')['Ship Mode'].count()

    # Print the resulting Series
    print(totals_by_ship_mode)

def option28():
    # a bar chart to show total orders per month
    orders_by_month = df.groupby('Month').size()
    print (orders_by_month)    
    orders_by_month.plot(kind='bar')
    plt.title('Total Orders per Month')
    plt.xlabel('Month')
    plt.ylabel('Total Orders')
    plt.show()

def option29():
    # a bar chart to show total shipping methods per state
    # Get user input for state
    state = input("Enter state: ")

    # Filter the DataFrame to only include the specified state
    state_df = df[df['State'] == state]

    # Group the data by Ship Mode, and calculate the count for each group
    totals_by_ship_mode = state_df.groupby('Ship Mode')['Ship Mode'].count()

    totals_by_ship_mode = state_df.groupby('Ship Mode')['Ship Mode'].count()
    print (totals_by_ship_mode)    
    totals_by_ship_mode.plot(kind='pie')
    plt.title('Total Number of Ship Modes per State')
    plt.show()

def options():
    print("[0] To leave")
    print("[1] Option 1: Average sales per region")
    print("[2] Option 2: Average sales per segment")
    print("[3] Option 3: Top and Bottom performing Products")
    print("[4] Option 4: Average Product Sales Information")
    print("[5] Option 5: Total Sales and Profits by Category")
    print("[6] Option 6: Total Sales by State")
    print("[7] Option 7: Total Profits by State")
    print("[8] Option 8: Total Sales by State with Populations")
    print("[9] Option 9: Average sales per region compared to average discount per region")
    print("[10] Option 10: Average sales per state compared to average discount per state")
    print("[11] Option 11: Total profits by region")
    print("[12] Option 12: Profit margin by region")
    print("[13] Option 13: Profit margin per sub category")
    print("[14] Option 14: Show top 10 states by quantity of items bought")
    print("[15] Option 15: Most profitable item in a state")
    print("[16] Option 16: Print average waiting time per product")
    print("[17] Option 17: Show most profitable shipping modes")
    print("[18] Option 18: Show sales vs profit")
    print("[19] Option 19: Profit by region and category")
    print("[20] Option 20: Sales over time")
    print("[21] Option 21: Heatmap of sales by catergory and sub-category")
    print("[22] Option 22: Average discount rate per product.")
    print("[23] Option 23: Show shipping mode usage per region")
    print("[24] Option 24: Profit per month of every year")
    print("[25] Option 25: Total Sales compared to Profit each day")
    print("[26] Option 26: Total Orders per Month")
    print("[27] Option 27: Total Number of Shipping Types in each State")
    print("[28] Option 28: Bar Chart Showing Total Orders per Month")
    print("[29] Option 29: Pie Chart Showing Total Number of Ship Modes per State")

while True:
    options()
    option = int(input())
    if option == 0:
        break
    elif option == 1:
        option1()
    elif option == 2:
        option2()
    elif option == 3:
        option3()
    elif option == 4:
        option4()
    elif option == 5: 
        option5()
    elif option == 6: 
        option6()
    elif option == 7: 
        option7()
    elif option == 8: 
        option8()
    elif option == 9: 
        option9()
    elif option == 10: 
        option10()
    elif option == 11:
        option11()
    elif option == 12:
        option12()
    elif option == 13:
        option13()
    elif option == 14:
        option14()
    elif option == 15:
        option15()
    elif option == 16:
        option16()
    elif option == 17:
        option17()
    elif option == 18:
        option18()    
    elif option == 19:
        option19()    
    elif option == 20:
        option20()    
    elif option == 21:
        option21()
    elif option == 22:
        option22()
    elif option == 23:
        option23()
    elif option == 24:
        option24()
    elif option == 25:
        option25()
    elif option == 26:
        option26()
    elif option == 27:
        option27()
    elif option == 28:
        option28()
    elif option == 29:
        option29()