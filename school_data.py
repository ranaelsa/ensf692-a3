# school_data.py
# AUTHOR NAME: Rana Elsadig
#
# A terminal-based application for computing and printing statistics based on given input.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc. 
# You may import any modules from the standard Python library.
# Remember to include docstrings and comments.


import numpy as np
from given_data import year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022

# Declare any global variables needed to store the data here
FILE_LOC = "Assignment3Data.csv"

schools_dict = {}
grades = [10, 11, 12]
years = [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
given_data_array = [year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022]

with open(FILE_LOC) as file:
    lines = file.read().splitlines()

for i, line in enumerate(lines):
    if i > 0:
        if i % 10 == 0:
            line = line.split(",")
            schools_dict[line[1]] = line[2]


enrollment_data = np.dstack([year.reshape(20,3) for year in given_data_array])

# You may add your own additional classes, functions, variables, etc.

class SchoolStats:
    def __init__(self, school_index):
        self.school_index = school_index
        self.school_subarray = enrollment_data[school_index]

    def mean_enrollment(self):
        for index, grade in enumerate(grades):
            mean_enrollment = np.nanmean(self.school_subarray[index, :])
            print(f"Mean enrollment for Grade {grade}: {int(mean_enrollment)}")
    
    def min_max_enrollment(self):
        min_enrollment = np.nanmin(self.school_subarray)
        max_enrollment = np.nanmax(self.school_subarray)
        print(f"Highest enrollment for a single grade: {int(max_enrollment)}")
        print(f"Lowest enrollment for a single grade: {int(min_enrollment)}")

    def total_enrollment(self):
        for index, year in enumerate(years):
            print(f"Total enrollment for {year}: {int(np.nansum(self.school_subarray[:, index]) // 1)}")
        print(f"Total ten year enrollment: {int(np.nansum(self.school_subarray))}")

    def total_mean_enrollment(self):
        print(f"Mean total enrollment over 10 years: {int(np.nansum(self.school_subarray) / len(years))}")

    def enrollment_over_500(self):
        if np.any(self.school_subarray > 500):
            over_500 = (self.school_subarray > 500)
            mean_over_500 = np.nanmedian(self.school_subarray[over_500])
            print(f"For all enrollments over 500, the median value was: {int(mean_over_500)}")
        else:
            print("No enrollments over 500.")

class GeneralStats:
    def mean_enrollment(self):
        for index, year in enumerate(years):
            if ((index == 0) or (index == years.index(2022))):
                mean_enrollment = np.nanmean(enrollment_data[:,:, index])
                print(f"Mean enrollment in {year}: {int(mean_enrollment)}")
    
    def total_graduating_class(self):
        total_graduating_2022 = np.nansum(enrollment_data[:, grades.index(12), years.index(2022)])
        print(f"Total graduating class of 2022: {int(total_graduating_2022)}")

    def min_max_enrollment(self):
        min_enrollment = np.nanmin(enrollment_data)
        max_enrollment = np.nanmax(enrollment_data)
        print(f"Highest enrollment for a single grade: {int(max_enrollment)}")
        print(f"Lowest enrollment for a single grade: {int(min_enrollment)}")


def main():
    print("ENSF 692 School Enrollment Statistics")

    # Print Stage 1 requirements here
    print("Shape of full data array: ", enrollment_data.shape)
    print("Dimensions of full data array: ", enrollment_data.ndim)

    # Prompt for user input
    while(True):
        try:
            user_input = input("Please enter the high school name or school code: ")
            if (user_input not in schools_dict) and (user_input not in schools_dict.values()) and (user_input not in [school.lower() for school in schools_dict]):
                raise ValueError
        except ValueError:
            print("You must enter a valid school name or code.")
        else:
            # Print Stage 2 requirements here
            print("\n***Requested School Statistics***\n")
            school_index = 0
            for index, (key, value) in enumerate(schools_dict.items()):
                if user_input == key or user_input == key.lower() or user_input == value:
                    school_index = index
                    print(f"School Name: {key}, School Code: {value}")

            school_stats = SchoolStats(school_index)
            school_stats.mean_enrollment()
            school_stats.min_max_enrollment()
            school_stats.total_enrollment()
            school_stats.total_mean_enrollment()
            school_stats.enrollment_over_500()

            # Print Stage 3 requirements here
            print("\n***General Statistics for All schools_dict***\n")
            general_stats = GeneralStats()
            general_stats.mean_enrollment()
            general_stats.total_graduating_class()
            general_stats.min_max_enrollment()
            break


if __name__ == '__main__':
    main()

