# BI Assistant

This tool enables you to interact with IMDb datasets using a command-line interface. It facilitates downloading, processing IMDb datasets, and querying a database created from these datasets.

## Prerequisites

Before you begin, ensure you have Python installed on your system. This application is tested with Python 3.10 and above.

## Installation

### Step 1: Clone or Download the Repository

Start by cloning this repository to your local machine, or download the `imdb_cli.py` script directly.

### Step 2: Install Dependencies

Install the required dependencies by running the following command in your terminal:

```bash
pip install -r requirements.txt
```
This command will install all necessary Python packages listed in requirements.txt.

### Step 3: Set Up OpenAI API Key
You need to have an OpenAI API key to use this application. Set your OpenAI API key in the `imdb_cli.py` file.
Replace your_api_key_here with your actual OpenAI API key.

## Usage
### Initialize IMDb Datasets
To download the IMDb datasets, run:

```bash
python imdb_cli.py --init
```
This will download, decompress and store the required datasets. This step can take some time depending on your system's performance and internet speed.


### Querying the Database
To query the IMDb database, use:

```bash
python imdb_cli.py --query "Your query here"
```
Replace "Your query here" with your actual query.

## Examples
Here are some example commands:

- Initialize datasets: `python imdb_cli.py --init`
- Query database: `python imdb_cli.py --query 'What is the language of the movie "Pulp Fiction"?'`

## Notes
Ensure you have sufficient disk space for downloading and processing the datasets.
The initial setup, especially the processing step, might take a considerable amount of time.
Always ensure your OpenAI API key is set correctly before running queries.
