import os
import sys
import time

from openai import OpenAI

from secret import API_KEY

client = OpenAI(api_key=API_KEY)

dataset = "subtraction"

r = client.fine_tuning.jobs.list(limit=10)

print(r)

sys.exit(0)

response = client.files.create(
  file=open(f"data/{dataset}_train.jsonl", "rb"),
  purpose="fine-tune"
)

train_id = response.id
train_filename = response.filename

print(response)
print()

response = client.files.create(
  file=open(f"data/{dataset}_validate.jsonl", "rb"),
  purpose="fine-tune"
)

validate_id = response.id
validate_filename = response.filename

print(response)
print()

response = client.fine_tuning.jobs.create(
  training_file=train_id,
  validation_file=validate_id,
  suffix=f"{dataset}-ft",
  model="davinci-002"
)

print(response)
print()

fine_tune_id = response.id

a = client.fine_tuning.jobs.retrieve(fine_tune_id)
print()

status = client.fine_tuning.jobs.retrieve(fine_tune_id).status
while status != "succeeded":
    print(f"Fine-tuning job {fine_tune_id} is currently {status}...")
    time.sleep(10)

print(f"Fine-tuning job {fine_tune_id} has succeeded!")
