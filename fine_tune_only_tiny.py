import time

from openai import OpenAI

from utils import get_api_key


# dataset = "subtraction"

# r = client.fine_tuning.jobs.list(limit=10)
#
# print(r)
#
# sys.exit(0)

def fine_tune_only_tiny(dataset, id):
    client = OpenAI(api_key=get_api_key(id))

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
        suffix=f"{dataset}-tiny-ft",
        model="davinci-002"
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
