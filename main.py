
import pandas as pd
import matplotlib.pyplot as plt
import re

# Read log file
log_file = "test_logs.txt"

# Extract test case name and status using regex
test_cases = []
statuses = []

with open(log_file, "r") as file:
    for line in file:
        match = re.search(r"Test Case: (.*?) - Status: (\w+)", line)
        if match:
            test_cases.append(match.group(1))
            statuses.append(match.group(2))

# Create a DataFrame
df = pd.DataFrame({"Test Case": test_cases, "Status": statuses})

# Count occurrences of each status
status_counts = df["Status"].value_counts()

# Plot the results
plt.figure(figsize=(6, 4))
status_counts.plot(kind="bar", color=["green", "red"])
plt.xlabel("Test Status")
plt.ylabel("Count")
plt.title("Automation Test Execution Results")
plt.xticks(rotation=0)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()
