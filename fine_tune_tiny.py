import time

from openai import OpenAI

from utils import get_api_key


def fine_tune_tiny(dataset, current_model, id):
    client = OpenAI(api_key=get_api_key(id))

    # Extract the name of the current model
    current_model_name = current_model.split(":")[3].split("-ft")[0]

    response = client.files.create(
      file=open(f"data/{dataset}_train_small.jsonl", "rb"),
      purpose="fine-tune"
    )

    train_id = response.id
    train_filename = response.filename

    print(response)
    print()

    response = client.files.create(
      file=open(f"data/{dataset}_validate.jsonl", "rb"),
      purpose="fine-tune"
    )

    validate_id = response.id
    validate_filename = response.filename

    print(response)
    print()

    response = client.fine_tuning.jobs.create(
      training_file=train_id,
      validation_file=validate_id,
      suffix=f"{current_model_name[:3]}-smft-{dataset[:3]}",
      model=current_model
    )

    print(response)
    print()

    # fine_tune_id = response.id
    #
    # a = client.fine_tuning.jobs.retrieve(fine_tune_id)
    # print()
    #
    # status = client.fine_tuning.jobs.retrieve(fine_tune_id).status
    # while status != "succeeded":
    #     print(f"Fine-tuning job {fine_tune_id} is currently {status}...")
    #     time.sleep(10)
    #
    # print(f"Fine-tuning job {fine_tune_id} has succeeded!")

# fine_tune_tiny("subtraction", "ft:davinci-002:personal:addition-ft:8pjPH2DU")
