import random
import json

# Set a maximum depth for recursion
MAX_DEPTH = 3

# Generate a random integer
def generate_integer():
    return str(random.randint(1, 10))

# Generate an expression based on the M rule, with depth control
def generate_M(depth=0):
    if depth >= MAX_DEPTH:
        return generate_integer()
    choice = random.random()
    if choice < 0.5 and depth > 0:
        return generate_integer()
    elif choice < 0.75:
        return generate_M(depth + 1) + '*' + generate_M(depth + 1)
    else:
        return '(' + generate_E(depth + 1) + '+' + generate_E(depth + 1) + ')'

# Generate an expression based on the E rule, with depth control
def generate_E(depth=0):
    if depth >= MAX_DEPTH:
        return generate_integer()
    choice = random.random()
    if choice < 0.25 and depth > 0:
        return generate_integer()
    elif choice < 0.35:
        return generate_M(depth + 1) + '*' + generate_M(depth + 1)
    else:
        return generate_E(depth + 1) + '+' + generate_E(depth + 1)

# Generate and evaluate expressions
def generate_expressions(num_expressions):
    expressions = []
    for _ in range(num_expressions):
        expr = generate_E()
        eval_expr = eval(expr)
        expressions.append({"prompt": expr + "=", "completion": str(eval_expr)})
    return expressions

# Generate 10 random expressions
num_expressions = 200
generated_expressions = generate_expressions(num_expressions)

# Open a file in write mode
with open('data/mex_validate.jsonl', 'w') as file:
    # Print the expressions in JSON format
    for expr in generated_expressions:
        file.write(json.dumps(expr) + '\n')
