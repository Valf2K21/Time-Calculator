'''
    The Time Calculator is a Python application written as partial requirement of freeCodeCamp's Scientific Computing with Python Certification.
    Written November 2023 by Valfrid Galinato
'''

# create a function to calculate date and time
def add_time(start, duration, start_day = ''):
    # initialize lists to store start and duration hours and minutes, meridiem, and days
    hrs = []
    mins= []
    meridiem = ['AM', 'PM']
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

    # split user-provided data
    split_whole = start.split()
    split_start = split_whole[0].split(':')
    split_duration = duration.split(':')

    # append data in their respective lists and variables
    merid = split_whole[1]
    hrs.append(split_start[0])
    hrs.append(split_duration[0])
    mins.append(split_start[1])
    mins.append(split_duration[1])

    # if-statements to determine if user provided valid time
    if int(hrs[0]) < 1 or int(hrs[0]) > 12:
        # return error message
        return 'Error: Start time must be in 12-hour format only'
    
    if int(mins[0]) < 0 or int(mins[0]) > 59:
        # return error message
        return 'Error: Start minutes must be within 0-59 only'
    
    if int(mins[1]) < 0 or int(mins[1]) > 59:
        # return error message
        return 'Error: Duration minutes must be within 0-59 only'
    
    # add start and duration minutes, divide by 60, and set remainder as final_mins, and whole number as add_hrs
    sum_mins = int(mins[0]) + int(mins[1])
    final_mins = sum_mins % 60
    add_hrs = sum_mins // 60

    # if-elif-else statement to determine whether to add 12 more hours depending on meridiem
    if merid == 'AM':
        # set start_hrs as its default value
        start_hrs = int(hrs[0])

        # set merid_index to 0
        merid_index = 0

    elif merid == 'PM':
        # add 12 to start's default hour value
        start_hrs = int(hrs[0]) + 12

        # set merid_index to 1
        merid_index = 1

    else:
        # return error message
        return 'Error: Meridiem must be AM or PM only'
    
    # add start and duration hours, divide by 12, and set whole number as add_merid, and remainder as final_hrs
    sum_hrs = start_hrs + int(hrs[1]) + add_hrs
    final_hrs = sum_hrs % 12
    add_merid = sum_hrs // 12

    # add merid_index and add_merid, and save a copy of merid_index to another variable for the while-loop
    count = add_merid
    counter = merid_index
    
    # initialize final_merid variable
    final_merid = merid

    # while-loop to loop through contents of meridiem list until it gets final_merid
    while counter != count:
        # if-else statement to determine whether to add or subtract 1 to merid_index based on its current value
        if merid_index == 1:
            # subtract 1 to current value of merid_index
            merid_index = merid_index - 1

        else:
            # add 1 to current value of merid_index
            merid_index = merid_index + 1

        # use merid_index with meridiem list to set final_merid
        final_merid = meridiem[merid_index]

        # increment current value of counter
        counter = counter + 1

    # initialize days_passed variable
    days_passed = 0

    # while-loop that runs continuously until sum_hrs is less than 24
    while sum_hrs >= 24:
        # subtract sum_hrs with 24, then divide sub_hrs by 24
        sub_hrs = sum_hrs - 24
        div_hrs = sub_hrs // 24

        # if-else statement to check if div_hrs is already 0
        if div_hrs != 0:
            # add 1 to days_passed
            days_passed = days_passed + 1
        
        else:
            # add 1 to days_passed then end the loop
            days_passed = days_passed + 1
            break

        # set sub_hrs as new value of sum_hrs
        sum_hrs = sub_hrs
    
    # if-statement to check if user passed an optional start_day
    if start_day:
        # use .index() function to store start_day's index in a variable
        day_index = days.index(start_day.lower().capitalize())

        # initialize days_count variable
        days_count = 0

        # while-loop to loop through contents of days list until it gets result_day
        while days_count != days_passed + 1:
            # use day_index with days list to set result_day
            result_day = days[day_index]

            # if-else statement to determine whether to reset day_index back to 0 depending on its current value
            if day_index == 6:
                # reset day_index to 0
                day_index = 0

            else:
                # add 1 to day_index
                day_index = day_index + 1

            # increment current value of days_count
            days_count = days_count + 1

    # if-statement to check if final_hrs' value is 0
    if final_hrs == 0:
        # set final_hrs to 12
        final_hrs = 12

    # if-statement to check if final_mins' value is less than 10
    if final_mins < 10:
        # add a 0 before said value
        final_mins = '0' + str(final_mins)
        
    # use days_passed to set days_notif
    days_notif = f'({str(days_passed)} days later)'

    # if-elif statements to determine what calculate time result format to return
    if not start_day and days_passed == 0:
        # return result in a specific format
        return f'{final_hrs}:{final_mins} {final_merid}'
    
    elif not start_day and days_passed == 1:
        # return result in a specific format
        return f'{final_hrs}:{final_mins} {final_merid} (next day)'
    
    elif not start_day and days_passed > 1:
        # return result in a specific format
        return f'{final_hrs}:{final_mins} {final_merid} {days_notif}'
    
    elif start_day and days_passed == 0:
        # return result in a specific format
        return f'{final_hrs}:{final_mins} {final_merid}, {result_day}'
    
    elif start_day and days_passed == 1:
        # return result in a specific format
        return f'{final_hrs}:{final_mins} {final_merid}, {result_day} (next day)'
    
    elif start_day and days_passed > 1:
        # return result in a specific format
        return f'{final_hrs}:{final_mins} {final_merid}, {result_day} {days_notif}'