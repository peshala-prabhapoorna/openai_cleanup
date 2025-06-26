# Batch Clean OpenAI Storage

Scripts to clean up OpenAI storage in batches.

## How to Use Scripts

1. Create and activate Python virtual environmant

```sh
# venv
python -m venv venv

# virtualenv
virtualenv venv

#activate

source venv/bin/activate
```

2. Install packages

```sh
pip install -r requirements.txt
```

3. Copy the sample env file.

```sh
cp .env.sample .env
```

4. Replace the placeholder in the `.env` file with the OpenAI api key of the project related to the storage to be cleaned up.

5. Run the script associated with the type of resource you want to delete in batches.

```sh
python3 delete_files.py

python3 delete_vector_stores.py
```
