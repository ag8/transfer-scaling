import random
import json


def generate_prompt_completion_pair():
    # Generate random numbers
    num1 = random.randint(10, 99)
    num2 = random.randint(10, 99)

    # Calculate the sum
    sum = num1 + num2

    # Format the output as a dictionary
    output_dict = {
        "prompt": f"{num1}+{num2}=",
        "completion": str(sum)
    }

    # Convert dictionary to JSON string
    return json.dumps(output_dict)


# Open a file in write mode
with open('data/addition_tiny.jsonl', 'w') as file:
    # Generate and write 3 pairs to the file
    for _ in range(10):
        json_line = generate_prompt_completion_pair()
        file.write(json_line + '\n')  # Write the JSON line with a newline character
