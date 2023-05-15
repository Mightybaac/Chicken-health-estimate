import matplotlib.pyplot as plt
import csv

# Get filename of CSV file
filename = input("Enter filename of CSV file: ")

# Get filename to save chart image
chart_filename = input("Enter filename to save chart image: ")

# Initialize lists for ages and health scores
ages = []
health_scores = []

# Read CSV file and extract ages and health scores
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        ages.append(int(row[0]))
        health_scores.append(float(row[1]))

# Create line chart
plt.plot(ages, health_scores)
plt.xlabel('Age (days)')
plt.ylabel('Overall Health Score')
plt.title('Chicken Health Over Time')

# Save chart image to file
plt.savefig(chart_filename)

# Display chart
plt.show()
