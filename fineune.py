import jsonlines
import itertools
import pandas as pd
from pprint import pprint

import datasets
from datasets import load_dataset

# pretrained_dataset = load_dataset("c4", "en", split="train", streaming=True)
# n = 5
# print("Pretrained dataset:")
# top_n = itertools.islice(pretrained_dataset, n)
# for i in top_n:
#   print(i)

filename = "lamini_docs.jsonl"
instruction_dataset_df = pd.read_json(filename, lines=True)
# print(instruction_dataset_df)

examples = instruction_dataset_df.to_dict()
text = examples["question"][0] + f"\n"+ examples["answer"][0]
print(text)
