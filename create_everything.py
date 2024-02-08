from fine_tune import fine_tune_full
from fine_tune_only_tiny import fine_tune_only_tiny
from fine_tune_tiny import fine_tune_tiny
from utils import get_model_name

# task_names = ["addy", "div", "mex", "mult2x1", "spain", "sub"]
task_names = [["addy", "sub", "spain"],
              ["div", "mex", "mult2x1"],
              ["faith", "science"]]

# fine_tune_full("mult2x2", 2)
# fine_tune_full("faith", 2)
# fine_tune_full("science", 2)

# fine_tune_only_tiny("div", 1)
# fine_tune_only_tiny("mex", 1)
# fine_tune_only_tiny("mult2x1", 1)

# fine_tune_only_tiny("faith", 2)
# fine_tune_only_tiny("science", 2)


# model_finetuned_on_first_task_name = get_model_name("spain", 0)
# fine_tune_tiny("science", model_finetuned_on_first_task_name, 0)
#
# model_finetuned_on_first_task_name = get_model_name("spain", 0)
# fine_tune_tiny("mult2x1", model_finetuned_on_first_task_name, 0)
#
# model_finetuned_on_first_task_name = get_model_name("spain", 0)
# fine_tune_tiny("faith", model_finetuned_on_first_task_name, 0)

# model_finetuned_on_first_task_name = get_model_name("mult2x1", 1)
# fine_tune_tiny("mex", model_finetuned_on_first_task_name, 1)
#
# model_finetuned_on_first_task_name = get_model_name("mult2x1", 1)
# fine_tune_tiny("faith", model_finetuned_on_first_task_name, 1)
#
# model_finetuned_on_first_task_name = get_model_name("mult2x1", 1)
# fine_tune_tiny("science", model_finetuned_on_first_task_name, 1)

# model_finetuned_on_first_task_name = get_model_name("science", 2)
# fine_tune_tiny("mex", model_finetuned_on_first_task_name, 2)
#
# model_finetuned_on_first_task_name = get_model_name("science", 2)
# fine_tune_tiny("mult2x1", model_finetuned_on_first_task_name, 2)
#
# model_finetuned_on_first_task_name = get_model_name("science", 2)
# fine_tune_tiny("faith", model_finetuned_on_first_task_name, 2)

# fine_tune_only_tiny("spain")

# for task_name in ["sub", "spain"]:
#     print(f"Fine-tuning on {task_name}...")
#     fine_tune_full(task_name)
#     print(f"Fine-tuning on {task_name} (tiny)...")
#     fine_tune_only_tiny(task_name)

# for first_task_name in task_names:
#     for second_task_name in task_names:
#         if first_task_name != second_task_name:
#             print(f"Fine-tuning {first_task_name} model on {second_task_name} (tiny)...")
#             model_finetuned_on_first_task_name = get_model_name(first_task_name)
#             fine_tune_tiny(second_task_name, model_finetuned_on_first_task_name)
