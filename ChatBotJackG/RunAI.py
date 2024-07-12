import os
from openai import OpenAI

key = "YOUR API KEY HERE"
assistant_id = "asst_5u7H1dP27dK1TeIwzxzqJ98X"

client = OpenAI(api_key=key)

# Create a Vector Store for AI to access
vector_store = client.beta.vector_stores.create(name="ACME Lab")
print(f"Vector Store Id - {vector_store.id}")

# Upload work from acme files
file_paths = ["ACME.txt", "JackG.txt"]
file_streams = [open(path, "rb") for path in file_paths]

# Add files to vector Store
file_batch = client.beta.vector_stores.file_batches.upload_and_poll(
  vector_store_id = vector_store.id,
  files = file_streams
)

# Print the status and the file counts of the batch to see the result operation
print(file_batch.status)
print(file_batch.file_counts)

# update assistant with files
assistant = client.beta.assistants.update(
  assistant_id=assistant_id,
  tool_resources={"file_search": {"vector_store_ids": [vector_store.id]}},
)

print("Assistant updated with vector store.")

# Create thread
thread = client.beta.threads.create()
print(f"Your thread id is - {thread.id}\n\n")

# Allow the user to query the ChatBot
def getResponse(user_input):
    """
    Given user question then query the AI returning a string response.

    Parameter input: user query.
    Precondition: String.
    """
    text = user_input

    message = client.beta.threads.messages.create(
        thread_id = thread.id,
        role = "user",
        content = text,
    )

    run = client.beta.threads.runs.create_and_poll(
        thread_id = thread.id, assistant_id = assistant.id
    )

    messages = list(client.beta.threads.messages.list(thread_id = thread.id, run_id=run.id))
    message_content = messages[0].content[0].text

    response = f"{message_content.value}"
    return response
