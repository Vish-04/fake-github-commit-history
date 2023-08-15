import sys
import os
import subprocess
import random
from datetime import datetime, timedelta
from dateutil.parser import parse
from pathlib import Path
from history_generator import create_commit_date_list

def generate_commits(workdays_only=False, weekend_behavior=False, commits_each_day="0,3", startDate=None, endDate=None, gradient=None, no_commit_percentage=0, working_hours="9-17"):
    try:
        commits_per_day = list(map(int, commits_each_day.split(",")))
        # print("COMMITS_PER DAY: ")
        print(commits_per_day)
        gradient_type = gradient
        # print("GRADIENT RANGE: ")
        print(gradient_type)
        working_hours_range = list(map(int, working_hours.split("-")))
        # print("WORKING HOURS RANGE: ")
        print(working_hours_range)
        start_date = parse(start_date) if start_date else datetime.now() - timedelta(days=365)
        # print("START DATE: ")
        print(start_date)
        end_date = parse(end_date) if end_date else datetime.now()
        # print("END DATE: ")
        print(end_date)

        commit_date_list = create_commit_date_list(
            commits_per_day, gradient_type, workdays_only, no_commit_percentage, working_hours_range, start_date, end_date
        )
        # return
        print("Generating your GitHub commit history")

        history_folder = "github-history"

        # Remove git history folder if it already exists.
        if os.path.exists(history_folder):
            # print("REMOVED FOLDER")
            subprocess.run(
                [sys.executable, "-c", f"import shutil; shutil.rmtree('{history_folder}')"],
                shell=True,
            )

        os.makedirs(history_folder, exist_ok=True)
        os.chdir(history_folder)
        # print("CHANGED DIRECTORIES")
        subprocess.run(["git", "init"])
        # print("GIT INIT")

        for commit_date in commit_date_list:
            print(f"Generating GitHub commit history... ({commit_date.strftime('%Y-%m-%d %H:%M:%S')})")
            with open("fake-history.txt", "w") as file:
                # file.write("TEST")
                file.write(commit_date.strftime('%Y-%m-%d %H:%M:%S'))
            subprocess.run(["git", "add", "."])
            subprocess.run(
                ["git", "commit", "--quiet", "--date", commit_date.strftime('%Y-%m-%d %H:%M:%S'), "-m", "fake commit"]
            )
        print(f"{len(commit_date_list)} commits have been created.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
