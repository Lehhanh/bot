from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

# List all vector stores
vector_stores = client.vector_stores.list()
print("Vector stores: ", len(vector_stores.data))
# for v in vector_stores.data:
#   deleted_vector_store = client.vector_stores.delete(
#     vector_store_id=v.id
#   )
#   print(deleted_vector_store)


# Delete all file in OpenAI
# all_files = client.files.list()
# for file in all_files:
#     client.files.delete(file.id)
#     print(f"Successfully deleted: {file.id}")

vector_store_id = "vs_6a51d364dac0819195d0afd65913e13b"

# files = client.vector_stores.files.list(
#     vector_store_id=vector_store_id
# )
# i = 0
# for file in files.data:
#     i += 1
#     print(file.id)
#     print(file.status)
#     print(file.created_at)
#     print("-" * 30)
    
# print(i)
# vector_files = client.vector_stores.files.list(
#     vector_store_id="vs_6a51d364dac0819195d0afd65913e13b"
# )

# print(f"Vector Store contains {len(vector_files.data)} files")
# print(vector_files.has_more)
# uploaded_files = client.files.list()
# i = 0
# for file in uploaded_files:
#     i += 1
#     print(f"File ID: {file.id}")
#     print(f"File Name: {file.filename}")
#     print(f"Purpose: {file.purpose}")
#     print(f"Size: {file.bytes} bytes")
#     print(f"Created At: {file.created_at}")
#     print("-" * 40)
# print(i)