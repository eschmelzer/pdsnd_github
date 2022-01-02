Hello. Welcome to the README file for the "bikeshare data project" from Udacity; my project was created in December 2021. 

Essentially, this project allows the user to recieve statistics about bikeshare usage in 3 cities - New York City, Chicago, and Washington, D.C. - during a sixth-month time period from January through June 2017. Users can recieve statistics for the specified city for some combination of a certain weekday and a certain month, or select "all" for either of these options. Statistics pertain to the most frequent travel times, the most popular bike stations, trip duration, and user demographics. 

For this project there are three data files, one each containing the data for New York City, Chicago, and Washington, D.C. There is also a python file entitled bikeshare.py. The user runs this file via the command line, where their input is taken, and the requested statistics are displayed.

Please note that I used the following sources outside of the Udacity course itself for ideas of how to complete certain portions of the project:

    combine the start and end station columns in order to find the most common combination:
    https://stackoverflow.com/questions/19377969/combine-two-columns-of-text-in-pandas-dataframe

    skip the Gender and Birth Year statistics due to missing columns in Washington:
    http://net-informations.com/ds/pd/exists.htm

    iterate through the next five rows of the dataframe:
    https://knowledge.udacity.com/questions/26261 (answer from Ronak M.)

    breaking the loop once the index is out of range of the dataframe:
    https://stackoverflow.com/questions/11902458/i-want-to-exception-handle-list-index-out-of-range/11902480


