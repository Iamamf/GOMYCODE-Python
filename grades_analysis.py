{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "a9a07c03-6f0a-4081-93ed-7189caea2fd4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Mean Grade: 87.5\n",
      "Median Grade: 88.5\n",
      "Standard Deviation: 6.591661399070799\n",
      "Maximum Grade: 98\n",
      "Minimum Grade: 75\n",
      "Sorted Grades: [75 80 83 85 88 89 90 92 95 98]\n",
      "Index of Highest Grade: 7\n",
      "Number of Students above 90: 3\n",
      "Percentage of Students above 90: 30.0\n",
      "Percentage of Students below 75: 0.0\n",
      "High Performers: [92 95 98]\n",
      "Passing Grades: [85 90 88 92 95 80 98 89 83]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "# Create numpy array called \"grades\"\n",
    "grades = np.array([85, 90, 88, 92, 95, 80, 75, 98, 89, 83])\n",
    "\n",
    "# Calculate mean, median, and standard deviation\n",
    "mean_grade = np.mean(grades)\n",
    "median_grade = np.median(grades)\n",
    "std_deviation = np.std(grades)\n",
    "\n",
    "# Find maximum and minimum grades\n",
    "max_grade = np.max(grades)\n",
    "min_grade = np.min(grades)\n",
    "\n",
    "# Sort grades in ascending order\n",
    "sorted_grades = np.sort(grades)\n",
    "\n",
    "# Find the index of the highest grade\n",
    "index_highest_grade = np.argmax(grades)\n",
    "\n",
    "# Count number of students who scored above 90\n",
    "above_90_count = np.sum(grades > 90)\n",
    "\n",
    "# Calculate percentage of students who scored above 90\n",
    "percentage_above_90 = np.mean(grades > 90) * 100\n",
    "\n",
    "# Calculate percentage of students who scored below 75\n",
    "percentage_below_75 = np.mean(grades < 75) * 100\n",
    "\n",
    "# Extract all grades above 90 into new array \"high_performers\"\n",
    "high_performers = grades[grades > 90]\n",
    "\n",
    "# Create array \"passing_grades\" with grades above 75\n",
    "passing_grades = grades[grades > 75]\n",
    "\n",
    "# Print the results\n",
    "print(\"Mean Grade:\", mean_grade)\n",
    "print(\"Median Grade:\", median_grade)\n",
    "print(\"Standard Deviation:\", std_deviation)\n",
    "print(\"Maximum Grade:\", max_grade)\n",
    "print(\"Minimum Grade:\", min_grade)\n",
    "print(\"Sorted Grades:\", sorted_grades)\n",
    "print(\"Index of Highest Grade:\", index_highest_grade)\n",
    "print(\"Number of Students above 90:\", above_90_count)\n",
    "print(\"Percentage of Students above 90:\", percentage_above_90)\n",
    "print(\"Percentage of Students below 75:\", percentage_below_75)\n",
    "print(\"High Performers:\", high_performers)\n",
    "print(\"Passing Grades:\", passing_grades)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7b8943e6-2f7f-4793-bece-c27f1384c35b",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
