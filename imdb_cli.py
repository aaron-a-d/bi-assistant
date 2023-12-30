import os
import sqlite3
import pandas as pd
from tqdm import tqdm
import argparse
from langchain.llms import OpenAI
from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain

# Global constant for the download folder
DOWNLOAD_FOLDER = "imdb_datasets"
os.environ["OPENAI_API_KEY"] = "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"

def initialize():
    if not os.path.exists(DOWNLOAD_FOLDER):
        os.makedirs(DOWNLOAD_FOLDER)

    urls = [
        "https://datasets.imdbws.com/name.basics.tsv.gz",
        "https://datasets.imdbws.com/title.akas.tsv.gz",
        "https://datasets.imdbws.com/title.basics.tsv.gz",
        "https://datasets.imdbws.com/title.crew.tsv.gz",
        "https://datasets.imdbws.com/title.episode.tsv.gz",
        "https://datasets.imdbws.com/title.principals.tsv.gz",
        "https://datasets.imdbws.com/title.ratings.tsv.gz",
    ]

    for url in urls:
        os.system(f"curl -o {DOWNLOAD_FOLDER}/{os.path.basename(url)} {url}")

    # Create a SQLite database connection
    conn = sqlite3.connect('imdb_database.db')
    chunksize = 1000000

    # Iterate through each dataset and load into the database
    for url in urls:
        print(f"Processing `{url}`")
        file_name = os.path.basename(url)
        table_name = file_name.replace(".tsv.gz", "").replace(".", "_")
        full_path = os.path.join(DOWNLOAD_FOLDER, file_name)
        for chunk in tqdm(pd.read_csv(full_path, sep='\t', na_values='\\N', chunksize=chunksize, low_memory=False)):
            chunk.to_sql(name=table_name, con=conn, if_exists='append')

    conn.close()


def query_database(question):
    db = SQLDatabase.from_uri("sqlite:///imdb_database.db")
    llm = OpenAI(temperature=0, verbose=False)
    db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=False)
    answer = db_chain.run(question)
    return answer


def main():
    parser = argparse.ArgumentParser(description="BI Assistant")
    parser.add_argument("--init", help="Download, decompress, process and store IMDb datasets", action="store_true")
    parser.add_argument("--query", help="Query the IMDb database", type=str)

    args = parser.parse_args()

    if args.init:
        initialize()
    if args.query:
        answer = query_database(args.query)
        print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
