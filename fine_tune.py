import json
import os

from openai import OpenAI
client = OpenAI()

dataset = "addition"

response = client.files.create(
  file=open(f"data/{dataset}_train.jsonl", "rb"),
  purpose="fine-tune"
)
print(response)
client.files.create(
  file=open(f"data/{dataset}_validate.jsonl", "rb"),
  purpose="fine-tune"
)

client.fine_tuning.jobs.create(
  training_file=f"{dataset}_train",
  validation_file=f"{dataset}_validate",
  suffix=f"{dataset}-finetuned",
  model="davinci-002"
)
