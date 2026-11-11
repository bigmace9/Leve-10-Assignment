import pandas as pd

file = pd.read_csv("cfb.csv")

season = int(input("Enter a season to analyze: "))
season_file = file[file["Season"] == season]

if season_file.empty:
    print("Season not found.")
else:
    categories = {
    "10 or more wins": [],
    "8-9 wins": [],
    "6-7 wins": [],
    "Fewer than 6 wins": []
        }
    for index, row in season_file.iterrows():
        team = row["Team"].rsplit(" (", 1)[0]
        wins = row["Win"]

        if wins >= 10:
            categories["10 or more wins"].append(team)
        elif wins >= 8:
            categories["8-9 wins"].append(team)
        elif wins >= 6:
            categories["6-7 wins"].append(team)
        else:
            categories["Fewer than 6 wins"].append(team)
    print("College Football Results for", season)
    for category, teams in categories.items():
        print(category + ":")
        for team in teams:
            print("   ", team)


