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

## HOW TO RUN
To generate data for training samples from the function descriptions:
```
poetry run python run_generate_samples.py --n_samples 1 --input_file_name "./test_data/test_function_descriptions.jsonl" --output_file_name "./outputs/test_generate_samples.jsonl"
```

To generate open-ai compatible function descriptions from a code snippet:
```
poetry run python run_generate_description.py --input_file_name "./test_data/test_function_snippets.jsonl" --output_file_name "./outputs/test_generate_snippets.jsonl"
```
