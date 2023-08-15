from commit_generator import generate_commits

if __name__ == "__main__":
    workdays_only = False
    commits_per_day = "1-5"
    start_date = "01/02/2023"
    end_date = "12/21/23"
    gradient = "linear"
    no_commit_percentage = 0.25
    working_hours = "9-18"
    weekend_behavior = True

    generate_commits(workdays_only=workdays_only, commits_per_day=commits_per_day, start_date=start_date, end_date=end_date, gradient=gradient, no_commit_percentage=no_commit_percentage, working_hours=working_hours, weekend_behavior=weekend_behavior)
