## TODO 
- Implement a snippet generator to generate code snippets for some specialized agent.
- Implement format converteds to convert training sample data to
    - Llama strings
    - Alcapa instruct strings
    - openai strings

for training. These may have different canonical formats. 

## Function Call Finetuner
Makes training data (prompt, function description, and function call sets) to train for llama, alcapa, openai, etc. finetunes.
The data format is generic so as to be able to be reformmated based on need.

`run_generate_description.py` generates the function descriptions in openai's specified format given snippets.
`run_generate_samples.py` generates training samples for functions.

Sample outputs in `outputs/` are from inputs in `test_data/`.

## How to Run
To generate code snippet from tasks:
```
poetry run python run_generate.py --mode snippet --input_file_name "./outputs/tasks/business_tasks.jsonl" --output_file_name "./outputs/snippets/business_snippets.jsonl > ./outputs/snippets/business_snippet.log"
```

To generate open-ai compatible function descriptions from a code snippet:
```
poetry run python run_generate.py --mode description --input_file_name "./outputs/snippets/business_snippets.jsonl" --output_file_name "./outputs/descriptions/business_descriptions.jsonl" > ./outputs/descriptions/business_descriptions.log
```

To generate data for training samples from the function descriptions:
```
poetry run python run_generate.py --mode sample --n_samples 1 --input_file_name "./outputs/descriptions/twitter_descriptions.jsonl" --output_file_name "./outputs/samples/twitter_samples.jsonl" > ./outputs/samples/twitter_samples.log
```

## Why this many steps?
During testing this (task-> code snippet -> json description) was better than trying to go directly from task -> json description.

Going directly to json description resulted in a lot of data with null in the parameters field.


