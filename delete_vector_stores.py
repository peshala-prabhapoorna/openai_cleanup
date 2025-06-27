import os
import sys
from openai import OpenAI

from dotenv import load_dotenv
load_dotenv()

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

# Get all vecotor sotores in OpenAI storage
vector_stores = client.vector_stores.list()

vector_store_count = 0

# Print all vector stores
for vs in vector_stores:
    vector_store_count += 1
    print(f"id: {vs.id} | name: {vs.name}")

print(f"Total number of vector stores: {vector_store_count}")

delete_files = input(f"Delete all {vector_store_count} vector stores? (Y/N): ").strip()

# Exit if user input is not 'Y'
if delete_files != "Y":
    print("No vector stores were deleted")
    sys.exit(0)

# Iterate over vector stores and delete them
for vs in vector_stores:
    client.vector_stores.delete(
        vector_store_id=vs.id
    )
    print(f"Deleted vector store with id: {vs.id}")

print("All vector stores have been deleted")
