import random
from datetime import timedelta

def create_commit_date_list(commits_per_day, gradient, workdays_only, no_commit_percentage, working_hours_range, start_date, end_date, weekend_behavior):
    commit_date_list = []
    current_date = start_date
    date_difference = (end_date - start_date).days
    day_count = 0

    while current_date <= end_date:
        day_count += 1
        if workdays_only and current_date.weekday() >= 5:
            current_date += timedelta(days=1)
        else:
            if random.random() <= no_commit_percentage:
                current_date += timedelta(days=1)
            else:
                lower_bound = 0
                commits_range = random.randint(commits_per_day[0], commits_per_day[1])
                if weekend_behavior and current_date.weekday() >= 5:
                    commits_range = random.randint(0,1)
                else:
                    if (gradient == 'linear'):
                        lower_bound = round(commits_per_day[0] + (round(sum(commits_per_day) / len(commits_per_day)) - commits_per_day[0]) * (day_count/date_difference))
                        commits_range = random.randint(lower_bound, commits_per_day[1])
                    elif(gradient == 'exponential'):
                        lower_bound = round(commits_per_day[0] + (sum(commits_per_day) // len(commits_per_day)) * (1 - (2 ** (-day_count / date_difference))))
                        commits_range = random.randint(lower_bound, commits_per_day[1])
                    elif(gradient=='bursts'):
                        period = 21 #Every 3 weeks
                        lower_bound = round(commits_per_day[0] + (commits_per_day[1] - commits_per_day[0]) * (abs(day_count % period - period // 2) / (period // 2)))
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
