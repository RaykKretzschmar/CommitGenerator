from datetime import datetime, timedelta
import os
import random

# Set your GitHub email
email = "YOUR_EMAIL_HERE"

# Set the start date to 3 years ago from today
start_date = datetime.now() - timedelta(days=3*365)
current_date = start_date

commit_messages = ["updated", "removed unnecessary code", "bugfix", "refactor", "fix", "add feature"]

while current_date < datetime.now():
    # Create a fake commit for each day with a random commit message
    date = current_date.strftime('%m/%d/%Y %H:%M:%S')
    commit_message = random.choice(commit_messages)
    with open('fake.txt', 'a') as file:
        file.write(date + '\n')
    os.system('git add .')
    os.system(f'git commit --date="{date}" -m "{commit_message}"')
    
    # Push the commit to GitHub
    os.system('git push origin main')
    
    # Increment the current date by one day
    current_date += timedelta(days=1)

# Set your Git config email back to your original email
os.system(f'git config --global user.email "{email}"')