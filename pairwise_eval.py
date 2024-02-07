from gpt_eval import eval_model_on_dataset

task_names = ["addition", "subtraction"]
model_names = ["ft:davinci-002:personal:addition-ft:8pjPH2DU", "ft:davinci-002:personal:subtraction-ft:8pij0waY"]

for task_name in task_names:
    for model_name in model_names:
        correct, incorrect = eval_model_on_dataset(model_name, task_name)

        print(f"Performance of {task_names[model_names.index(model_name)]}-finetuned model on {task_name} dataset: {correct / (correct + incorrect)}")
