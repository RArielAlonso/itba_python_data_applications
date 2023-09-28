import pandas as pd
import gcsfs
import cfg as ce
from google.cloud import bigquery


FILEPATH = 'bucket_itba_ariel/generic-food.parquet'


def read_csv():
    df = pd.read_csv('generic-food.csv')
    return df


def load_df_file_into_gcs(df):
    fs = gcsfs.GCSFileSystem(project=ce.PROJECT_ID)

    # Make sure that the "gs://" prefix is removed for the FILEPATH in to_parquet.
    with fs.open(FILEPATH, 'wb') as f:
        df.to_parquet(f)


def load_parquet_into_bq():
    # Initialize a BigQuery client
    bq_client = bigquery.Client()

    # Construct a BigQuery job configuration object
    job_config = bigquery.LoadJobConfig()
    job_config.source_format = bigquery.SourceFormat.PARQUET

    uri = 'gs://' + FILEPATH
    # Make an API request to start the BigQuery job
    load_job = bq_client.load_table_from_uri(uri, ce.DATASET_ID+"."+ce.TABLE_ID, job_config=job_config)
    load_job.result()  # Wait for the job to complete

    destination_table = bq_client.get_table(ce.PROJECT_ID+"."+ce.DATASET_ID+"."+ce.TABLE_ID)  # Make an API request.
    print("Loaded {} rows.".format(destination_table.num_rows))


if __name__ == "__main__":
    df = read_csv()
    print("csv ok")
    load_df_file_into_gcs(df)
    print("load ok")
    load_parquet_into_bq()
