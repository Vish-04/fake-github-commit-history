import sys
import os
import subprocess
import random
from datetime import datetime, timedelta
from dateutil.parser import parse
from pathlib import Path
from history_generator import create_commit_date_list

def generate_commits(workdaysOnly=False, commitsPerDay="0,3", startDate=None, endDate=None, gradient=None, noCommitPercentage=0, workingHours="9-17"):
    try:
        commits_per_day = list(map(int, commitsPerDay.split(",")))
        # print("COMMITS_PER DAY: ")
        print(commits_per_day)
        gradient_type = gradient
        # print("GRADIENT RANGE: ")
        print(gradient_type)
        working_hours_range = list(map(int, workingHours.split("-")))
        # print("WORKING HOURS RANGE: ")
        print(working_hours_range)
        start_date = parse(startDate) if startDate else datetime.now() - timedelta(days=365)
        # print("START DATE: ")
        print(start_date)
        end_date = parse(endDate) if endDate else datetime.now()
        # print("END DATE: ")
        print(end_date)

        commit_date_list = create_commit_date_list(
            commits_per_day, gradient_type, workdaysOnly, noCommitPercentage, working_hours_range, start_date, end_date
        )
        # return
        print("Generating your GitHub activity")

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
            print(f"Generating your GitHub activity... ({commit_date.strftime('%Y-%m-%d %H:%M:%S')})")
            with open("foo.txt", "w") as file:
                # file.write("TEST")
                file.write(commit_date.strftime('%Y-%m-%d %H:%M:%S'))
            subprocess.run(["git", "add", "."])
            subprocess.run(
                ["git", "commit", "--quiet", "--date", commit_date.strftime('%Y-%m-%d %H:%M:%S'), "-m", "fake commit"]
            )
        print(f"Success: {len(commit_date_list)} commits have been created.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
