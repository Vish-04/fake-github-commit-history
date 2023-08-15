from commit_generator import generate_commits

if __name__ == "__main__":
    workdaysOnly = False
    commitsPerDay = "1,5"
    startDate = "2023-01-01"
    endDate = "2023-12-31"
    gradient = "linear"
    noCommitPercentage = 0
    workingHours = "9-18"

    generate_commits(startDate, endDate, gradient, workingHours, workdaysOnly=True, noCommitPercentage=0.3,commitsPerDay="1,20")
