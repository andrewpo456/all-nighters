import sys
import getopt
import operator
import datetime
import academic_date
from feit_building import sensor
from feit_building import retrieve
from resources import test


def __filter_overnight_logins(data_set):
    """Filter the data_set and returns only the login information for overnight stays."""
    overnight_data = list(filter(lambda x: academic_date.AcademicDate.is_all_nighter(x[0], '%Y-%m-%d %H:%M:%S'), data_set))

    overnight_data.sort()   # Sort the data before returning
    return overnight_data


def __calculate_all_nighters(data_set):
    """
    Using the data_set obtained from __get_login_data, this method calculates the number of all night study sessions students have undertaken.This is done through examining the login data for each computer in each lab of B11 UTS.

    The data_set is expected to be in the format:
    [['2017-02-20 12:29:01', 0], [...], ...]]
    """
    total = 0
    # We need to keep track of the current night as we progress through the data set
    current_night = datetime.datetime.strptime(data_set[0][0], '%Y-%m-%d %H:%M:%S')
    students_in_lab = data_set[0][1]
    total += students_in_lab

    for date_data, logins in data_set:
        date = datetime.datetime.strptime(date_data, '%Y-%m-%d %H:%M:%S')

        # If we are now looking at the next night, we need to reset the tracking of logins and the current night
        if date.date() > current_night.date():
            current_night = date
            students_in_lab = logins
            total += students_in_lab
            continue

        # Otherwise we check if the number of students_in_lab has increased since the last data point
        if logins > students_in_lab:
            total += (logins - students_in_lab)

        # Update the running total of students in a lab for this night
        students_in_lab = logins

    return total


def __get_login_data(startDate, endDate):
    """
    Will get the login data for each lab in the engineering building between two dates.

    startDate, endDate - AcademicDate objects
    startDate must be > endDate

    returns data_set - Data contating information about the logins in each lab
    """
    if(startDate.date > endDate.date):
        raise RuntimeError('startDate was greater than endDate')

    data = dict()
    for l in sensor.LabUnit:
        (rc, json) = retrieve.Data.retrieve(startDate.date_str(), endDate.date_str(), 'logins', l.value)
        # If the query was sucessfull append to data set
        if rc:
            data[l.value] = json

    return data


def main(devmode):
    """Main method."""
    startDate = academic_date.AUTUMN_START
    endDate = academic_date.AcademicDate(datetime.datetime.now())

    print("Calculating all nighters between: ")
    print("(AUTUMN COMMENCMENT) " + startDate.date_str('%d-%b-%Y %H:%M:%S'))
    print("(NOW) " + endDate.date_str('%d-%b-%Y %H:%M:%S'))

    data_set = dict()
    if not devmode:
        data_set = __get_login_data(startDate, endDate)
    else:
        data_set = test.TEST_LAB_DATA

    # For each lab, filter its lab data_set for overnight logins only
    for k, v in data_set.items():
        data_set[k] = __filter_overnight_logins(v)

    # For each lab find out how many over night lab sessions have occurred
    num_all_nighters = dict()
    for lab, data in data_set.items():
        num_all_nighters[lab] = __calculate_all_nighters(data)

    # Calculate total of all nighters occurred and then sort labs by number of all night sessions
    total = 0
    for lab, all_nighters in num_all_nighters.items():
        total += all_nighters

    print(str.format("\n\nTotal number of all night sessions pulled = {0}", total))
    print("Breakdown per lab:")
    for lab, all_nighters in sorted(num_all_nighters.items(), key=operator.itemgetter(1), reverse=True):
        print(str.format("{0} : {1} ", lab, all_nighters))


if __name__ == "__main__":
    devmode = False
    try:
        opts, args = getopt.getopt(sys.argv[1:], "d", ["dev"])
    except getopt.GetoptError:
        devmode = False

    for opt, arg in opts:
        if opt in ("-d", "--dev"):
            devmode = True

    main(devmode)
