from commit_generator import generate_commits

if __name__ == "__main__":
    workdays_only = False
    commits_per_day = "1,5"
    start_date = "2023-01-01"
    end_date = "2023-12-31"
    gradient = "linear"
    no_commit_percentage = 0
    working_hours = "9-18"
    weekend_behavior = True

    generate_commits(start_date, end_date, gradient, working_hours, weekend_behavior=True, no_commit_percentage=0.3,commits_per_day="1,5")
