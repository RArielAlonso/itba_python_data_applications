import pandas as pd
import time
import numpy as np
import os


def generate_random_csv(size):
    df = pd.DataFrame()
    df['name'] = np.random.choice(['Ariel', 'Miguel', 'Nicolas', 'Florencia', 'Ana'], size)
    df['last_name'] = np.random.choice(['Alonso', 'Sanchez', 'Fernandez', 'Martinez', 'Peruzzi'], size)
    df['age'] = np.random.randint(1, 100, size)
    df['liter_water_per_day'] = np.random.uniform(0, 4, size)
    df['needs_more_water'] = np.random.choice([True, False], size)
    df.to_csv(f"random-person-{size}-rows.csv")


def read_csv(size):
    data_csv = pd.read_csv(f'random-person-{size}-rows.csv')
    return data_csv


def to_parquet(df, size, compression):
    df.to_parquet(f'random-person-{size}-rows-{compression}-compression.parquet', compression=compression)


def main():
    number_of_records = [10000, 100000, 1000000, 5000000, 10_000_000]
    compression = ["snappy", "gzip", "brotli", "lz4", "zstd"]
    results_dict_csv = {}
    for i in number_of_records:
        start_generating_csv_time = time.time()
        generate_random_csv(i)
        end_generating_csv_time = time.time()
        start_reading_time = time.time()
        data_csv = read_csv(i)
        finished_reading_time = time.time()
        for j in compression:
            start_compression_time = time.time()
            to_parquet(data_csv, i, compression=j)
            end_compression_time = time.time()
            delta_generation_csv = end_generating_csv_time-start_generating_csv_time
            delta_reading_time = finished_reading_time-start_reading_time
            delta_compression_time = end_compression_time-start_compression_time
            results_dict_csv[i, j] = {
                "rows": int(i),
                "compression": j,
                "time_generation_csv": round(delta_generation_csv, 2),
                "time_reading_csv": round(delta_reading_time, 2),
                "compression_time": round(delta_compression_time, 2),
                "parquet_size_kb": round(os.path.getsize(f'random-person-{i}-rows-{j}-compression.parquet')/1024**1),
                "csv_size_kb": round(os.path.getsize(f'random-person-{i}-rows.csv')/1024**1)
            }        
    pd.DataFrame(results_dict_csv).to_excel("Results.xlsx")


if __name__ == "__main__":
    main()
