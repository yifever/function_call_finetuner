#!/usr/bin/env zsh

# Directory where task files are located
task_dir="./outputs/snippets/"

# Loop through each .jsonl file in the task directory
for input_file in "${task_dir}"*.jsonl; do
  # Extract the filename without the directory and extension
  file_name=$(basename "${input_file}")
  task_type="${file_name%_snippets.jsonl}"

  echo "Processing $task_type..."

  out_type="descriptions"
  # Run the command with the current task_type
  poetry run python run_generate.py \
    --mode description \
    --input_file_name "${input_file}" \
    --output_file_name "./outputs/${out_type}/${task_type}_${out_type}.jsonl" \
    > "./outputs/${out_type}/${task_type}_${out_type}.log"

  echo "Completed processing for $task_type."
done

# Notify user that all tasks have been processed
echo "All tasks have been processed."
