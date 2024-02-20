import json

from openai import OpenAI
import tqdm

from secret import API_KEYS


def eval_model_on_dataset(model, dataset, exemplars, id=0):
    client = OpenAI(api_key=API_KEYS[id])
    # client = OpenAI()

    correct = 0
    incorrect = 0

    with open(f'data/{dataset}_validate.jsonl', 'r') as file:
        lines = file.readlines()

    few_shot_stub = "\n".join([str(exemplar[0]) + str(exemplar[1]) for exemplar in exemplars])
    for line in tqdm.tqdm(lines):
        json_line = json.loads(line)
        prompt = json_line["prompt"]
        completion = json_line["completion"]

        full_prompt = few_shot_stub + '\n' + prompt
        response = client.completions.create(
            model=model,
            prompt=full_prompt,
            max_tokens=7,
            temperature=0
        )

        result = response.choices[0].text.strip().replace(",", "")

        # Get the first n characters of the result
        result = result[:len(completion)]

        if result != completion:
            print(f"{full_prompt}{result}")

        if result == completion:
            correct += 1
        else:
            incorrect += 1

    return correct, incorrect


x=eval_model_on_dataset("davinci-002", "addy", exemplars=[("23+48=","71"), ("125+7=","132"), ("251+633=","784")])

84")])

print(x)
