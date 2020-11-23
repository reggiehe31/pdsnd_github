import time
import pandas as pd
import numpy as np

#Assign dictionary of cities name and related csv. file
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

#Assign month list and day of week list
months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    # Use variable judge0 as a criteria to check if the city name is valid or not. If not, break the while loop
    i = 0
    while i < 1:
        city = input('\nPlease input the city name you want to analyze: ').lower()
        if city in CITY_DATA:
            i = 1
            break
        else:
            print('\nPlease input valid city name\n')

    # TO DO: get user input for month (all, january, february, ... , june)
    # Use variable judge1 as a criteria to check if the month name is valid or not. If not, break the while loop
    j = 0
    while j < 1:
        month = input('\nPlease input the name of month you want to analyze: ').lower()
        if month in months:
            j = 1
            break
        else:
            print('\nPlease input valid month name!\n')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    # Use variable judge2 as a criteria to check if the day of week name is valid or not. If not, break the while loop
    k = 0
    while k < 1:
        day = input('\nPlease input the name of the day of week you want to analyze: ').lower()
        if day in days:
            k = 1
            break
        else:
            print('\nPlease input valid day of week name!\n')

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
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        months = ['january','february','march','april','may','june']
        month = months.index(month)+1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]



    print('\n')
    print('-'*40)
    print('\n')
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # Convert the date information from object to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # TO DO: display the most common month
    # Extract month information from the datetime data
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print("\nThe most popular month is: ",popular_month)

    # TO DO: display the most common day of week
    # Extract day_of_week information from the datetime data
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    popular_day = df['day_of_week'].mode()[0]
    print('\nThe most popular day is: ',popular_day)

    # TO DO: display the most common start hour
    # Extract hour information from the datetime data
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('\nThe most popular start hour is: ',popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_start_station = df['Start Station'].mode()[0]
    print('The most popular start station is: ',most_start_station)

    # TO DO: display most commonly used end station
    most_end_station = df['End Station'].mode()[0]
    print('The most popular end station is: ',most_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    # Create a new column for the combination of start stations and end stations
    df['start_and_end'] = 'From '+df['Start Station']+' to '+df['End Station']
    most_freq_combo = df['start_and_end'].mode()[0]
    print('The most frequent combination of start and end station trip is: ',most_freq_combo)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    # Add up the travel time from the trip duration column
    total_time = df['Trip Duration'].sum()
    print('The total travel time is (unit: seconds): ',total_travel_time)

    # TO DO: display mean travel time
    # Calculate the average travel time from the trip duation column
    mean_time = df['Trip Duration'].mean()
    print('The mean travel time is (unit: seconds): ',mean_travel_time)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    # Use value_counts function to record the numbers of different user types
    user_type = df['User Type'].value_counts()
    print('\n',user_type)

    # TO DO: Display counts of gender
    # Use value_counts function to record the numbers of different gender
    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts()
        print('\n',gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        # The minimum value of the column would be the earliest birth year
        earliest_year = df['Birth Year'].min()
        print('\nThe earliest birth year is: ',int(earliest_year))

        # The maximum value of the column would be the most recent birth year
        most_recent_year = df['Birth Year'].max()
        print('\nThe most recent year is: ',int(most_recent_year))

        # The mode of the column would be the most common birth year
        most_common_year = df['Birth Year'].mode()[0]
        print('\nThe most common year is: ',int(most_common_year))

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

        #A while loop which could view consecutive five rows of the csv. file. The loop will end if the user say no
        l = 0
        m = 0
        while l < 1:
            answer = input('\nDo you want to see the raw data of your chosen city?(yes/no): ').lower()
            if answer == 'yes':
                print(df.iloc[i:i+5])
            else:
                l = 1
                break
            m += 5

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
