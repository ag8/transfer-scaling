import json

from openai import OpenAI
import tqdm

from secret import API_KEYS

client = OpenAI(api_key=API_KEYS[0])

def eval_model_on_dataset(model, dataset):
    correct = 0
    incorrect = 0

    with open(f'data/{dataset}_validate.jsonl', 'r') as file:
        lines = file.readlines()

    for line in tqdm.tqdm(lines):
        json_line = json.loads(line)
        prompt = json_line["prompt"]
        completion = json_line["completion"]

        response = client.completions.create(
            model=model,
            prompt=prompt,
            max_tokens=7,
            temperature=0
        )

        result = response.choices[0].text.strip().replace(",", "")

        # Get the first `n` characters of the result
        result = result[:len(completion)]

        # print(f"{prompt}{result}")

        if result == completion:
            correct += 1
        else:
            incorrect += 1

    return correct, incorrect
