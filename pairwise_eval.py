from gpt_eval import eval_model_on_dataset
from utils import get_model_name, get_joint_model_name

task_names = ["addition", "subtraction"]

for first_task_name in task_names:
    for second_task_name in task_names:
        # First, calculate how a model finetuned on the 1st task performs on the 2nd task

        model_finetuned_on_first_task_name = get_model_name(first_task_name)

        correct, incorrect = eval_model_on_dataset(model_finetuned_on_first_task_name, second_task_name)

        print(f"Performance of {first_task_name}-finetuned model on {second_task_name} dataset: {correct / (correct + incorrect)}")


        # If the two tasks are different, calculate how a model finetuned on the 1st task and then slightly
        # finetuned on the 2nd task performs on the 2nd task
        if first_task_name != second_task_name:
            model_finetuned_on_first_task_and_a_bit_on_second_task = get_joint_model_name(first_task_name, second_task_name)

            correct, incorrect = eval_model_on_dataset(model_finetuned_on_first_task_and_a_bit_on_second_task, second_task_name)

            print(f"Performance of {first_task_name}-finetuned model (plus 10 examples on {second_task_name}) model on {second_task_name} dataset: {correct / (correct + incorrect)}")