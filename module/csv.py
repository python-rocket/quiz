from pandas import read_csv, DataFrame
from datetime import date

def create_ranking_file():
    ranking_file_path = "data/ranking.csv"
    with open(ranking_file_path, "w") as f:
        True

def read_ranking():
    ranking_file_path = "data/ranking.csv"
    try:
        df = read_csv(ranking_file_path, delimiter=",", names=("name", "points", "date"))
    except:
        create_ranking_file()
        write_ranking("Player", 1)
        df = read_csv(ranking_file_path, delimiter=",", names=("name", "points", "date"))
    df_sorted = df.sort_values(by=['points'], ascending=False)
    print("\nCurrent Ranking:")
    print(df_sorted.to_string(index=False))
    print("\n")

    top_score_index = df["points"].idxmax()
    top_score_name = df.iloc[top_score_index]["name"]
    top_score_points = df.iloc[top_score_index]["points"]
    print(f"The current top score belongs to: {top_score_name} with {top_score_points} points")
    print(f"Try to beat {top_score_name}'s score!")
    print("\n")

def write_ranking(name, points):
    ranking_file_path = "data/ranking.csv"
    date_today = date.today().strftime("%d-%m-%Y")
    data = {"name": [name], "points": [points], "date": [date_today], }
    df = DataFrame(data=data)
    df.to_csv(ranking_file_path, header=False, index=False, mode='a')
