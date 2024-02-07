import json
import os

from openai import OpenAI
client = OpenAI()

dataset = "addition"

client.files.create(
  file=open(f"data/{dataset}_train.jsonl", "rb"),
  purpose="fine-tune"
)
client.files.create(
  file=open(f"data/{dataset}_validate.jsonl", "rb"),
  purpose="fine-tune"
)

