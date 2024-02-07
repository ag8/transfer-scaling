import json
import os

from openai import OpenAI

from secret import API_KEY

client = OpenAI(api_key=API_KEY)

correct = 0
incorrect = 0

# Read in all the lines of output.jsonl into a file
with open('data/subtraction_validate.jsonl', 'r') as file:
    lines = file.readlines()

for line in lines:
    # The format of each line is {"prompt": "4471+305", "completion": "4776"}
    json_line = json.loads(line)
    prompt = json_line["prompt"]
    completion = json_line["completion"]

    response = client.completions.create(
        # model="ft:davinci-002:personal:subtraction-ft:8pij0waY",
        model="davinci-002",
        prompt=prompt,
        max_tokens=7,
        temperature=0
    )

    result = response.choices[0].text.strip().replace(",", "")

    # Get the first `n` characters of the result
    result = result[:len(completion)]

    print(f"{prompt}{result}")

    if result == completion:
        correct += 1
    else:
        incorrect += 1

print(f"Correct: {correct}, Incorrect: {incorrect} (Total accuracy: {correct / (correct + incorrect)})")
