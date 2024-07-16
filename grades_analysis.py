import numpy as np

# Create numpy array called "grades"
grades = np.array([85, 90, 88, 92, 95, 80, 75, 98, 89, 83])

# Calculate mean, median, and standard deviation
mean_grade = np.mean(grades)
median_grade = np.median(grades)
std_deviation = np.std(grades)

# Find maximum and minimum grades
max_grade = np.max(grades)
min_grade = np.min(grades)

# Sort grades in ascending order
sorted_grades = np.sort(grades)

# Find the index of the highest grade
index_highest_grade = np.argmax(grades)

# Count number of students who scored above 90
above_90_count = np.sum(grades > 90)

# Calculate percentage of students who scored above 90
percentage_above_90 = np.mean(grades > 90) * 100

# Calculate percentage of students who scored below 75
percentage_below_75 = np.mean(grades < 75) * 100

# Extract all grades above 90 into new array "high_performers"
high_performers = grades[grades > 90]

# Create array "passing_grades" with grades above 75
passing_grades = grades[grades > 75]

# Print the results
print("Mean Grade:", mean_grade)
print("Median Grade:", median_grade)
print("Standard Deviation:", std_deviation)
print("Maximum Grade:", max_grade)
print("Minimum Grade:", min_grade)
print("Sorted Grades:", sorted_grades)
print("Index of Highest Grade:", index_highest_grade)
print("Number of Students above 90:", above_90_count)
print("Percentage of Students above 90:", percentage_above_90)
print("Percentage of Students below 75:", percentage_below_75)
print("High Performers:", high_performers)
print("Passing Grades:", passing_grades)
