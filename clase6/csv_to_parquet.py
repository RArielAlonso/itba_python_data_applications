import pandas as pd


def read_food_csv():
    data = pd.read_csv("generic-food.csv")
    return data


def to_parquet(df, name):
    df.to_parquet(name)


if __name__ == "__main__":
    print('--------READING CSV--------')
    df = read_food_csv()
    print('--------CONVERTIN CSV TO PARQUET--------')
    to_parquet(df, "generic-food.parquet")
    print('--------PROCESS END--------')
