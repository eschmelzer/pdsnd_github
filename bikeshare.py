import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    #"""
    #Asks user to specify a city, month, and day to analyze.

    #Returns:
    #    (str) city - name of the city to analyze
    #    (str) month - name of the month to filter by, or "all" to apply no month filter
    #    (str) day - name of the day of week to filter by, or "all" to apply no day filter
    #"""
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city = input("What city are you interested in? Your options are Chicago, New York City, and Washington. \nCity: ").lower()
    while city not in  ['chicago','new york city','washington']:
        print('Invalid selection. Please restart.')
        exit()   
    else:
        print('Nice Choice!')
        
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("What month are you interested in? Please enter the month by name, or \'all\' to view all months. \nMonth: ").lower()
    while month not in ['january','february','march','april','may','june','all']:
        print('Invalid selection. Please restart.')
        exit()  
    else:
        print('Nice Choice!')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("And lastly, what day of the week are you interested in? Please enter the day by name, or \'all\' to view all months. \nDay: ").lower()

    while day not in ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']:
        print('Invalid selection. Please restart.')
        exit()  
    else:
        print('Nice Choice!')
          
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month 
    df['day'] = df['Start Time'].dt.weekday_name
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # TO DO: display the most common month  
    df['month'] = df['Start Time'].dt.month      
    popular_month = df['month'].mode()[0]
    print('Most Common Month:', popular_month)

    # TO DO: display the most common day of week    
    df['day'] = df['Start Time'].dt.weekday_name
    popular_day = df['day'].mode()[0]
    print('Most Common Day of Week:', popular_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Common Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Common Start Station:', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Common End Station:', popular_end_station)    

    # TO DO: display most frequent combination of start station and end station trip
    df['start end combo'] = df['Start Station'].astype(str).str.cat(df['End Station'].astype(str), sep = ' to ')
    popular_station_combo = df['start end combo'].mode()[0]
    print('Most Common Trip by Start and End Station:', popular_station_combo)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = sum(df['Trip Duration'])
    #print(('All trips for {day}s in {month} took a combined:',  total_travel_time).format(day,month))
    print('All trips took a combined', total_travel_time, 'seconds, or', total_travel_time/60, 'minutes, or', total_travel_time/60/60, 'hours.')
          
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The average trip took', mean_travel_time, 'seconds, or', mean_travel_time/60, 'minutes.')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    if 'Gender' not in df.columns:
        print('Gender Statistics Unavailable')
    else: 
        print(df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' not in df.columns:
        print('Birth Year/Age Statistics Unavailable')
    else: 
        print('The earliest birth year is', int(df['Birth Year'].min()))
        print('The most recent birth year is', int(df['Birth Year'].max()))
        print('The most common birth year is', int(df['Birth Year'].mode()[0]))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        answer = input('Would you like to view 5 lines of raw data from the dataframe? Enter yes or no.')
        if answer == 'yes':
            i = 0
            while True:
                print(df.iloc[i:i+5])
                i += 5
                continue_prompt = input('Would you like to see the next 5 lines of raw data from the dataframe? Enter yes or no.')
                if continue_prompt not in 'yes':
                    break
                elif IndexError:
                    break
            while False:
                break
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
