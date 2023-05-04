from datetime import datetime, timedelta
import os
import random

# Set your GitHub email
email = input("Please enter your email: ")

# Set the start date to 3 years ago from today
start_date = datetime.now() - timedelta(days=3*365)
current_date = start_date

# popular commit messages
commit_messages = ["updated", "removed unnecessary code",
                   "bugfix", "refactor", "fix", "add feature"]

while current_date < datetime.now() - timedelta(days=3*365):
    # Create a commit for each day with a random commit message
    date = current_date.strftime('%m/%d/%Y %H:%M:%S')
    commit_message = random.choice(commit_messages)
    with open('code.txt', 'a') as file:
        file.write(date + '\n')
    os.system('git add .')
    os.system(f'git commit --date="{date}" -m "{commit_message}"')

    # Push the commit to GitHub
    os.system('git push origin main')

    # Increment the current date by 0 to 3 days randomly
    # This sometimes leads to multiple commits per day
    current_date += timedelta(days=random.randint(0, 3))

os.system(f'git config --global user.email "{email}"')
