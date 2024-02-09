from gpt_eval import eval_model_on_dataset
from utils import get_model_name, get_joint_model_name


def get_id_by_task_name(task_name):
    if task_name in ["addy", "sub", "spain"]:
        return 0
    elif task_name in ["div", "mex", "mult2x1"]:
        return 1
    elif task_name in ["faith", "science"]:
        return 2
    else:
        raise ValueError("Invalid task name")


task_names = ["addy", "sub", "spain", "div", "mex", "mult2x1", "faith", "science"]

for first_task_name in task_names:
    for second_task_name in task_names:
        # First, calculate how a model finetuned on the 1st task performs on the 2nd task

        model_finetuned_on_first_task_name = get_model_name(first_task_name, get_id_by_task_name(first_task_name))

        correct, incorrect = eval_model_on_dataset(model_finetuned_on_first_task_name, second_task_name, get_id_by_task_name(first_task_name))

        print(
            f"Performance of {first_task_name}-finetuned model on {second_task_name} dataset: {correct / (correct + incorrect)}")

        # If the two tasks are different, calculate how a model finetuned on the 1st task and then slightly
        # finetuned on the 2nd task performs on the 2nd task
        if first_task_name != second_task_name:
            model_finetuned_on_first_task_and_a_bit_on_second_task = get_joint_model_name(first_task_name,
                                                                                          second_task_name,
                                                                                          get_id_by_task_name(first_task_name))

            correct, incorrect = eval_model_on_dataset(model_finetuned_on_first_task_and_a_bit_on_second_task,
                                                       second_task_name, get_id_by_task_name(first_task_name))

            print(
                f"Performance of {first_task_name}-finetuned model (plus 10 examples on {second_task_name}) model on {second_task_name} dataset: {correct / (correct + incorrect)}")
