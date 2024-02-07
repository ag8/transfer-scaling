import openai
from openai import OpenAI

from secret import API_KEY
from utils import get_all_model_names

client = OpenAI(api_key=API_KEY)

dataset = "subtraction"

r = client.fine_tuning.jobs.list(limit=10)

k = client.models.list()

for model_name in get_all_model_names():
    client.models.delete(model_name)
