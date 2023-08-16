import sys
import os
import subprocess
from datetime import datetime, timedelta
from dateutil.parser import parse
from history_generator import create_commit_date_list


def validate_boolean(value, name):
    if not isinstance(value, bool):
        raise ValueError(f"{name} must be a boolean value.")


def validate_percentage(value, name):
    if not (0 <= value <= 1):
        raise ValueError(
            f"{name} must be a floating-point number between 0 and 1 (inclusive).")


def validate_working_hours(value, name):
    if not isinstance(value, list) or len(value) != 2 or not all(isinstance(item, int) or (0 <= item <= 23) for item in value):
        raise ValueError(
            f"{name} must be in the format 'int-int' of values between 0-23 in military hours.")
    elif value[0] > value[1]:
        raise ValueError(f"{name} must have a valid ascending range")


def validate_commit_ranges(value, name):
    if not isinstance(value, list) or len(value) != 2 or not all(isinstance(item, int) or (item >= 0) for item in value):
        raise ValueError(
            f"{name} must be in the format 'int-int' of values 0 and above.")
    elif value[0] > value[1]:
        raise ValueError(f"{name} must have a valid ascending range")


def validate_gradient(value):
    if value not in ['linear', 'exponential', 'bursts']:
        raise TypeError(
            "gradient must be either 'linear', 'exponential', or 'bursts'.")


def generate_commits(workdays_only=False, weekend_behavior=False, commits_per_day="0-3", start_date=None, end_date=None, gradient=None, no_commit_percentage=0, working_hours="9-17"):
    try:
        try:
            commits_per_day = list(map(int, commits_per_day.split("-")))
            validate_commit_ranges(commits_per_day, "commits_per_day")
        except:
            print(
                "Error: commits_per_day must be in the format 'int-int' of values 0 and above of valid ascending ranges.")
            return
        try:
            working_hours_range = list(map(int, working_hours.split("-")))
            validate_working_hours(working_hours_range, "working_hours")
        except:
            print(
                "Error: working_hours must be in the format 'int-int' of values between 0-23 in military hours of valid ascending ranges.")
            return
        try:
            start_date = parse(
                start_date) if start_date else datetime.now() - timedelta(days=365)
        except:
            print("Error: must be in a valid date in the format MM/DD/YYYY.")
            return
        try:
            end_date = parse(end_date) if end_date else datetime.now()
        except:
            print("Error: end_date must be in a valid date in the format MM/DD/YYYY.")
            return
        if(start_date >= end_date):
            raise ValueError("start_date cannot be later than the end_date")
        print(weekend_behavior)
        validate_boolean(weekend_behavior, "weekend_behavior")
        print(gradient)
        validate_gradient(gradient)
        print(workdays_only)
        validate_boolean(workdays_only, "workdays_only")
        print(no_commit_percentage)
        validate_percentage(no_commit_percentage, "no_commit_percentage")

        commit_date_list = create_commit_date_list(
            commits_per_day=commits_per_day, gradient=gradient, workdays_only=workdays_only, no_commit_percentage=no_commit_percentage, working_hours_range=working_hours_range, start_date=start_date, end_date=end_date, weekend_behavior=weekend_behavior
        )
        print("Generating your GitHub commit history")

        history_folder = "github-history"

        # Remove git history folder if it already exists.
        if os.path.exists(history_folder):
            subprocess.run(
                [sys.executable, "-c",
                    f"import shutil; shutil.rmtree('{history_folder}')"],
                shell=True,
            )

        os.makedirs(history_folder, exist_ok=True)
        os.chdir(history_folder)
        subprocess.run(["git", "init"])

        for commit_date in commit_date_list:
            print(
                f"Generating GitHub commit history... ({commit_date.strftime('%Y-%m-%d %H:%M:%S')})")
            with open("fake-history.txt", "w") as file:
                file.write(commit_date.strftime('%Y-%m-%d %H:%M:%S'))
            subprocess.run(["git", "add", "."])
            subprocess.run(
                ["git", "commit", "--quiet", "--date",
                    commit_date.strftime('%Y-%m-%d %H:%M:%S'), "-m", "fake commit"]
            )
        print(f"{len(commit_date_list)} commits have been created.")
    except Exception as e:
        print(f"Error: {str(e)}")
