from openai import OpenAI

from secret import API_KEY

client = OpenAI(api_key=API_KEY)


def get_all_model_names():
    r = client.fine_tuning.jobs.list(limit=1000)

    all_model_names = []

    for i in range(len(r.data)):
        if r.data[i].fine_tuned_model is not None:
            all_model_names.append(r.data[i].fine_tuned_model)

    return all_model_names


def get_model_name(dataset):
    model_names = get_all_model_names()

    for model_name in model_names:
        if f"{dataset}-ft" in model_name:
            return model_name

def get_onlytiny_model_name(dataset):
    model_names = get_all_model_names()

    for model_name in model_names:
        if f"{dataset}-tiny-ft" in model_name:
            return model_name


def get_joint_model_name(dataset1, dataset2):
    model_names = get_all_model_names()

    for model_name in model_names:
        if dataset1[:3] + "-smft-" + dataset2[:3] in model_name:
            return model_name


# print(get_joint_model_name("addition", "subtraction"))
