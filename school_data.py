# school_data.py
# AUTHOR NAME: Rana Elsadig
# A terminal-based application for computing and printing statistics based on given input.

import numpy as np
from given_data import year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022

# CSV file that stores school names, codes and enrollment data
FILE_LOC = "Assignment3Data.csv"

# Dictionary to map school names to their respective codes.
schools_dict = {}

# List of grades
grades = [10, 11, 12]

# List of years 
years = [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]

# List of given data arrays for each year
given_data_array = [year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022]

# Read school data from the file and populate schools_dict
with open(FILE_LOC) as file:
    lines = file.read().splitlines()

for i, line in enumerate(lines):
    if i > 0: # Skip the header
        if i % 10 == 0: # Read every 10th line only
            line = line.split(",")
            schools_dict[line[1]] = line[2]

# Stack enrollment data for all years into a 3D array
enrollment_data = np.dstack([year.reshape(20,3) for year in given_data_array])

class SchoolStats:
    """
    A class used to compute statistics for a specific school.

    Attributes:
        school_index (int): An integer that represents the schools index in the enrollment data array stack.
        school_subarray (numpy.ndarray): A subarray of the enrollment data for the school.
    """

    def __init__(self, school_index):
        self.school_index = school_index
        self.school_subarray = enrollment_data[school_index]

    def mean_enrollment(self):
        """
        Print the mean enrollment for each grade.

        Args:
            None

        Returns:
            None
        """
        for index, grade in enumerate(grades):
            mean_enrollment = np.nanmean(self.school_subarray[index, :])
            print(f"Mean enrollment for Grade {grade}: {int(mean_enrollment)}")
    
    def min_max_enrollment(self):
        """
        Print the highest and lowest enrollment for a single grade within the ten-year period.

        Args:
            None

        Returns:
            None
        """
        min_enrollment = np.nanmin(self.school_subarray)
        max_enrollment = np.nanmax(self.school_subarray)
        print(f"Highest enrollment for a single grade: {int(max_enrollment)}")
        print(f"Lowest enrollment for a single grade: {int(min_enrollment)}")

    def total_enrollment(self):
        """
        Print the total enrollment for each year and the total enrollment for the ten-year period.

        Args:
            None

        Returns:
            None
        """
        for index, year in enumerate(years):
            print(f"Total enrollment for {year}: {int(np.nansum(self.school_subarray[:, index]) // 1)}")
        print(f"Total ten year enrollment: {int(np.nansum(self.school_subarray))}")

    def total_mean_enrollment(self):
        """
        Prints the mean total yearly enrollment over the ten-year period.

        Args:
            None

        Returns:
            None
        """
        print(f"Mean total enrollment over 10 years: {int(np.nansum(self.school_subarray) / len(years))}")

    def enrollment_over_500(self):
        """
        Prints the median value of enrollments over 500, if any exist.

        Args:
            None

        Returns:
            None
        """
        if np.any(self.school_subarray > 500):
            over_500 = (self.school_subarray > 500)
            median_over_500 = np.nanmedian(self.school_subarray[over_500])
            print(f"For all enrollments over 500, the median value was: {int(median_over_500)}")
        else:
            print("No enrollments over 500.")

class GeneralStats:
    """
    A class used to compute general statistics across all schools.
    """

    def mean_enrollment(self):
        """
        Prints the mean enrollment for the first and last year in the dataset.

        Args:
            None

        Returns:
            None
        """
        for index, year in enumerate(years):
            if ((index == 0) or (index == years.index(2022))):
                mean_enrollment = np.nanmean(enrollment_data[:,:, index])
                print(f"Mean enrollment in {year}: {int(mean_enrollment)}")
    
    def total_graduating_class(self):
        """
        Prints the total number of graduates for the class of 2022.

        Args:
            None

        Returns:
            None
        """
        total_graduating_2022 = np.nansum(enrollment_data[:, grades.index(12), years.index(2022)])
        print(f"Total graduating class of 2022: {int(total_graduating_2022)}")

    def min_max_enrollment(self):
        """
        Print the highest and lowest enrollment for a single grade within the ten-year period.

        Args:
            None

        Returns:
            None
        """
        min_enrollment = np.nanmin(enrollment_data)
        max_enrollment = np.nanmax(enrollment_data)
        print(f"Highest enrollment for a single grade: {int(max_enrollment)}")
        print(f"Lowest enrollment for a single grade: {int(min_enrollment)}")


def main():
    """
    Main function to print the enrollment data statistics for each school and across all schools.

    Prompts the user for a school name or code then prints its enrollments statistics as well as general statistics across all schools.
    
    Returns:
        None
    """
    print("ENSF 692 School Enrollment Statistics")

    # Print Stage 1 requirements here
    print("Shape of full data array: ", enrollment_data.shape)
    print("Dimensions of full data array: ", enrollment_data.ndim)

    # Prompt for user input
    while(True):
        try:
            user_input = input("Please enter the high school name or school code: ")
            # Check if the user's input is a valid school name or code, if not, raise a ValueError
            if (user_input not in schools_dict) and (user_input not in schools_dict.values()):
                raise ValueError
        except ValueError:
            print("You must enter a valid school name or code.")
        else:
            # Print Stage 2 requirements here
            print("\n***Requested School Statistics***\n")
            # Find the index for the inputted school in the schools_dict dictionary and print the school name and code
            for index, (key, value) in enumerate(schools_dict.items()):
                if user_input == key or user_input == value:
                    school_index = index
                    print(f"School Name: {key}, School Code: {value}")
            
            # Create a SchoolStats object and print the school statistics
            school_stats = SchoolStats(school_index) # The school index above matches that in the 3D array, therefore pass in as an attribute to SchoolStats
            school_stats.mean_enrollment()
            school_stats.min_max_enrollment()
            school_stats.total_enrollment()
            school_stats.total_mean_enrollment()
            school_stats.enrollment_over_500()

            # Print Stage 3 requirements here
            print("\n***General Statistics for All schools_dict***\n")
            # Create a GeneralStats object and print statistics across all schools
            general_stats = GeneralStats()
            general_stats.mean_enrollment()
            general_stats.total_graduating_class()
            general_stats.min_max_enrollment()
            break


if __name__ == '__main__':
    main()

