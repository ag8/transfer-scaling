from gpt_eval import eval_model_on_dataset
from utils import get_model_name, get_joint_model_name, get_onlytiny_model_name


def get_id_by_task_name(task_name):
    if task_name in ["addy", "sub", "spain"]:
        return 3
    elif task_name in ["div", "mex", "mult2x1"]:
        return 4
    elif task_name in ["faith", "science"]:
        return 5
    else:
        raise ValueError("Invalid task name")


task_names = ["addy", "sub", "spain", "div", "mex", "mult2x1", "faith", "science"]

for first_task_name in task_names:
    model_finetuned_on_first_task_name = get_onlytiny_model_name(first_task_name, get_id_by_task_name(first_task_name))

    correct, incorrect = eval_model_on_dataset(model_finetuned_on_first_task_name, first_task_name)

    print(
        f"Performance of {first_task_name}-tiny-finetuned model on {first_task_name} dataset: {correct / (correct + incorrect)}")

