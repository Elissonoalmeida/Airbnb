#Libraries used

import pandas as pd #Imports the Pandas library, commonly used for data manipulation and analysis.
from tabulate import tabulate #Imports the tabulate function, which helps in displaying data in a tabular form.
import matplotlib.pyplot as plt #Imports the pyplot module from Matplotlib, a library used for data visualization in Python.
import numpy as np #Imports the NumPy library, primarily used for numerical operations and arrays in Python

# Read the CSV file into a DataFrame
df = pd.read_csv('airbnb_listings.csv')
#Data cleaning

df['review_scores_cleanliness'] = df['review_scores_cleanliness'].replace('nan', 0).astype(float) # replace nan to 0 to fill the missing values.
df = df.dropna(subset=['host_response_rate', 'host_response_time','price','listing_url',]) # this rows were removed because if the host does not answer or there are no score it means that you are losing your time independently how good it is.
df['host_response_rate'] = df['host_response_rate'].str.replace('%', '').astype(float) # Replace '%' with ' ' (space) and convert 'host_response_rate' to numerical values
df['price'] = df['price'].str.replace('$', '').str.replace(',', '').astype(float) # Replace '$' for '' and ',' for '' to fix the price column

#Code
while True:
    def top10(): # Function to help in select the best top 10 of accomodations
        Customize = 'host_acceptance_rate' # First list of  Top 10 is sorted by host_acceptance_rate
        loop_end = False
        Customized2 = False
        search = df['maximum_nights'] >= guest_inf_1 # select the amount of nights that the user need
        nights_df = df[search]
        nights_df['Total_expenses'] = nights_df['price'] * guest_inf_1
        search2 = nights_df['instant_bookable'] == "t"
        while loop_end == False:
            filtered_bookable = nights_df[search2] 
            select = filtered_bookable.sort_values(by=Customize,ascending=Customized2).head(10)  # select top 10     
            # Select columns and convert DataFrame to a list of lists for tabulate
            table_data = select[['listing_url', 'host_is_superhost', 'room_type', 'price','host_response_rate','host_response_time','Total_expenses']].values.tolist() # head of the most interest features
            headers = ['Listing URL','Host is Superhost','Room Type','price','host_response_rate','host_response_time','Total_expenses']
            # Print the formatted table
            print(tabulate(table_data, headers=headers, tablefmt='grid'))
            print("\n0 = Return from the begining\n1 = print the graph from rate of response of this top 10\n2 = print the table again sorted by less 'price'\n3 = print the table again sorted by the best 'host_response_rate'\n4 = filter 'Host is Superhost' t=true only\n5 = filter a Room Type")
            try:
                question = int(input('Please select above writting the number from what do you want: '))
                if question == 0:
                    print('Thank you, good bye')
                    loop_end = True
                elif question == 1: 
                    # Map 'host_response_time' categories to numerical labels
                    time_categories = select['host_response_time'].unique()
                    time_labels = np.arange(len(time_categories))
                    time_mapping = dict(zip(time_categories, time_labels))
                    # Create a new numerical column for 'host_response_time'
                    select['time_label'] = select['host_response_time'].map(time_mapping)
                    # Create the scatter plot
                    plt.scatter(select['time_label'], select['host_response_rate'])
                    # Customize the plot
                    plt.title('Host Response Rate with top 10 vs. Response Time with top 10')
                    plt.xlabel('Host Response Time (Category)')
                    plt.ylabel('Host Response Rate (Percentage)')
                    plt.xticks(time_labels, time_categories, rotation=45)  # Set x-axis labels
                    plt.tight_layout()
                    plt.show()
                elif question == 2:
                    Customize = 'price'
                    Customized2 = True
                elif question == 3:
                    Customize = 'host_response_rate'
                    Customized2 = False
                elif question == 4:                    
                    search2 = nights_df['host_is_superhost'] == 't'# t = true
                    Customized2 = False
                elif question == 5:
                    print('\n0 = End the research\n1 = Entire home/apt\n2 = Hotel room\n3 = Private room\n4 = Shared room')
                    sub_question = int(input('Enter with number from options of the Room type above:'))
                    if sub_question == 0:
                        loop_end = True
                    elif sub_question == 1:
                        search2 = nights_df['room_type'] == 'Entire home/apt'
                    elif sub_question == 2:
                        search2 = nights_df['room_type'] == 'Hotel room'
                    elif sub_question == 3:
                        search2 = nights_df['room_type'] == 'Private room'
                    elif sub_question == 4:
                        search2 = nights_df['room_type'] == 'Shared room'   
                    else:
                        print('insert the correct parameter')
                else:
                    print('wrong input try again')
            except:
                print("Error, please enter with the correct option")

    def cleanliness(): # function created to show the overview of all data available in Airbnb site
        end_loop = False
        Customized = 'host_acceptance_rate'
        Customized2 = False
        while end_loop == False:
            count_cleanliness = df['review_scores_cleanliness'] >= 4 # selectiong the scores higher than 4
            overview = df[count_cleanliness]
            top_clean = df[count_cleanliness].sort_values(by=Customized, ascending=Customized2).head(10) # select top 10
            table_cleanliness = top_clean[['listing_url', 'host_is_superhost', 'room_type', 'price','host_response_rate','host_response_time','review_scores_cleanliness']].values.tolist()
            headers_cleanliness = ['Listing URL','Host is Superhost','Room Type','price','host_response_rate','host_response_time','review_scores_cleanliness']
            # Print the formatted table
            print(tabulate(table_cleanliness, headers=headers_cleanliness, tablefmt='grid'))
            print(f'The number of {count_cleanliness.sum()} accomodations were found which has scores from 4 to more\n')
            try:
                print('Would you like to explore more?')
                print('\n0 = Return from the begining\n1 = sort per less Price\n2 = Sort per host_response_rate\n3 = Sort per review_scores_cleanliness\n4 = Do you want to see a overview graph between host_response_rate vs host_response_time  ')
                request = int(input('Please select some numeral option above: '))
                if request == 0:
                    print('Thank you, good bye')
                    end_loop = True
                elif request == 1:
                    Customized = 'price'
                    Customized2 = True
                elif request == 2:
                    Customized = 'host_response_rate'
                    Customized2 = False
                elif request == 3:
                    Customized = 'review_scores_cleanliness'
                    Customized2 = False
                elif request == 4:
                    time_categories = overview['host_response_time'].unique()
                    time_labels = np.arange(len(time_categories))
                    time_mapping = dict(zip(time_categories, time_labels))
                # Create a new numerical column for 'host_response_time'
                    overview['time_label'] = overview['host_response_time'].map(time_mapping)
                # Create the scatter plot
                    plt.scatter(overview['time_label'], overview['host_response_rate'])
                # Customize the plot
                    plt.title('Host Response Rate over all vs. Response Time with over all')
                    plt.xlabel('Host Response Time (Category)')
                    plt.ylabel('Host Response Rate (Percentage)')
                    plt.xticks(time_labels, time_categories, rotation=45)  # Set x-axis labels
                    plt.tight_layout()
                    plt.show()
                else:
                    print('wrong input try again')
            except:
                print("Error, please enter with the correct option")
    try:
        print('Hi How are you? \nDo you need assist to find some accomodation?\n\nPlease select one option')
        print('\n0 = End the Programm\n1 = Let me to Find top 10 accomodations for you with instant bookable\n2 = Just want to see an over view in the amount of Airbnb´s in Dublin relating the rating of cleanliness')
        guest_inf_0 = int(input("\nplease tell me one option: "))
        if guest_inf_0 == 0:
            print('End of the programm')
            break
        elif guest_inf_0 == 1:
            print('perfect, I am doing the reserch for you, I will provide the top 10 accomodations')
            guest_inf_1 = int(input("Now I will help you to find your accomodation, please tell me how many days you want to stay in Ireland: "))
            top10()
        elif guest_inf_0 == 2:
            cleanliness()
        else:
            print('try again') 
    except:
        print("Error, please enter with the correct option")