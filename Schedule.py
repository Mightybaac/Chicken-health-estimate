import schedule
import time
import subprocess
import os

# Set the interval at which to run the chicken.py program (in minutes)
interval_minutes = 30

# Set the filename for the CSV file containing the health scores and ages of the chicken
csv_filename = "chicken_health.csv"

# Define a function to run the chicken.py program and save the output to a CSV file
def log_chicken_health():
    output = subprocess.check_output(["python", "chicken.py"])
    with open(csv_filename, "a") as f:
        f.write(output.decode("utf-8"))

# Define a function to generate a line chart of the chicken's health over time
def generate_health_chart():
    os.system("python data_visualizer.py")

# Schedule the log_chicken_health function to run at regular intervals
schedule.every(interval_minutes).minutes.do(log_chicken_health)

# Schedule the generate_health_chart function to run once per day
schedule.every().day.at("00:00").do(generate_health_chart)

# Main loop to run the scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(1)
