import csv
from faker import Faker
import pandas as pd
import time

fake = Faker()


def generate_random_csv(row_list):
    for i in row_list:
        with open(f'random-person-{i}-rows.csv', mode='w') as file:
            file_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            file_writer.writerow(['first_name', 'last_name', 'age'])
            for _ in range(i):
                file_writer.writerow([fake.first_name(), fake.last_name(), fake.numerify("@#")])


def to_parquet_to_compression(row_list, compression):
    for i in row_list:
        print(i)
        start_reading_time = time.time()
        data_csv = pd.read_csv(f'random-person-{i}-rows.csv')
        finished_reading_time = time.time()
        delta_reading_time = finished_reading_time-start_reading_time
        print("--------------------------")
        print(f"For {i} numbers of rows, reading time was {delta_reading_time}")
        print("--------------------------")
        for j in compression:
            start_compression_time = time.time()
            print(start_compression_time)
            data_csv.to_parquet(f'random-person-{i}-rows-{j}-compression.parquet', compression=j)
            end_compression_time = time.time()
            delta_compression_time = end_compression_time-start_compression_time
            print("--------------------------")
            print(f"For {i} numbers of rows and compression {j}, compression time was {delta_compression_time}")
            print("--------------------------")


def main():
    number_of_records = [10, 1000, 10000, 100000, 1000000, 5000000]
    # generate_random_csv(number_of_records)
    compression = ["snappy", "gzip", "brotli", "lz4", "zstd"]
    to_parquet_to_compression(number_of_records, compression)


if __name__ == "__main__":
    main()
