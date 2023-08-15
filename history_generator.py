import random
from datetime import datetime, timedelta
from dateutil.parser import parse

def create_commit_date_list(commits_per_day, gradient, workdays_only, no_commit_percentage, working_hours_range, start_date, end_date):
    commit_date_list = []
    current_date = start_date
    date_difference = (end_date - start_date).days
    day_count = 0

    while current_date <= end_date:
        day_count += 1
        # print("LOOPING ")  
        # print(current_date)
        # if workdays_only and current_date.weekday() >= 5:
        #     # print("SKIPPED A DAY")
        #     # print(current_date.weekday())
        #     current_date += timedelta(days=1)
        if random.random() <= no_commit_percentage:
            current_date += timedelta(days=1)
        lower_bound = round(commits_per_day[0] + (round(sum(commits_per_day) / len(commits_per_day)) - commits_per_day[0]) * (day_count/date_difference))
        commits_range = random.randint(lower_bound, commits_per_day[1])
        for commit in range(commits_range):
            date_with_hours = current_date.replace(
                hour=random.randint(working_hours_range[0], working_hours_range[1])
            )
            date_with_hours_and_minutes = date_with_hours.replace(
                minute=random.randint(0, 59)
            )
            commit_date = date_with_hours_and_minutes.replace(
                second=random.randint(0, 59)
            )

            commit_date_list.append(commit_date)
        current_date += timedelta(days=1)

    return commit_date_list
