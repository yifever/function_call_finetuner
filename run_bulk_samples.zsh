#!/usr/bin/env sh

input="descriptions"
output="samples"

# Directory where task files are located
task_dir="./outputs/${input}/"

# Loop through each .jsonl file in the task directory
for input_file in "${task_dir}"*.jsonl; do
  # Extract the filename without the directory and extension
  file_name=$(basename "${input_file}")
  task_type="${file_name%_${input}.jsonl}"

  echo "Processing $task_type..."

  # Run the command with the current task_type
  poetry run python run_generate.py \
    --mode ${output} \
    --input_file_name "${input_file}" \
    --output_file_name "./outputs/${output}/${task_type}_${output}.jsonl" \
    > "./outputs/${output}/${task_type}_${output}.log"

  echo "Completed processing for $task_type."
done

# Notify user that all tasks have been processed
echo "All tasks have been processed."
