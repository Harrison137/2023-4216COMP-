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
    #creates pie chart for the data
    avgSegProfit.plot(kind='pie', subplots = True, colors=['r', 'g', 'b'], autopct='%.2f', fontsize=20)
    plt.title('Average Profit Per Segment')
    plt.ylabel('Profit')
    plt.show()

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
    ax1.set_title('Average Discount by Country')
    #The following 2 lines adjust the code so that the names of the states are flipped
    ax1.set_xticks(range(len(avg_discount)))
    ax1.set_xticklabels(avg_discount.index, rotation=90)
    ax2.plot(avg_sales)
    ax2.set_title('Average Quantity by Country')
    ax2.set_xticks(range(len(avg_sales)))
    ax2.set_xticklabels(avg_sales.index, rotation=90)
    plt.show()
    
    
def option11():
    # Group the data by region and calculate the total profit for each region
    region_profit = df.groupby('Region')['Profit'].sum()
    print("\n", region_profit, "\n")
    print("")


    


def options():
    print("[0] To leave")
    print("[1] Option 1")
    print("[2] Option 2")
    print("[3] Option 3: Top and Bottom performing Products")
    print("[4] Option 4: Average Product Sales Information")
    print("[5] Option 5: Total Sales and Profits by Category")
    print("[6] Option 6: Total Sales by State")
    print("[7] Option 7: Total Profits by State")
    print("[8] Option 8: Total Sales by State with Populations")
    print("[9] Option 9: Average sales per region compared to average discount per region")
    print("[10] Option 10: Average sales per state compared to average discount per state")
    print("[11] option 11: Total profits by region")


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