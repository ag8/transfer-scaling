
import json
import random

def select_random_rows(input_file, output_file, num_rows=10):
    # Read all lines from the input file
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    # Select num_rows random lines from the list
    random_lines = random.sample(lines, min(num_rows, len(lines)))
    
    # Write the selected lines to the output file
    with open(output_file, 'w', encoding='utf-8') as file:
        for line in random_lines:
            file.write(line)

# Specify the input and output file names
input_file = 'translation_train.jsonl'
output_file = 'translation_train_small.jsonl'

# Call the function
select_random_rows(input_file, output_file)