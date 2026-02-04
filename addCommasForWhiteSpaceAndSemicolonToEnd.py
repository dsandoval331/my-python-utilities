import re

input_file_name = 'input.txt'
output_file_name = 'output.txt'

try:
    with open(input_file_name, 'r') as f_read, open(output_file_name, 'w') as f_write:
        for line in f_read:
            # Strip leading/trailing whitespace, replace sequences of one or more whitespace with a comma
            modified_line = re.sub(r'\s+', ',', line.strip())
            # Append a semicolon and a newline character to the end of the line
            f_write.write(modified_line + ';\n')
    print(f"File successfully processed and saved to {output_file_name}")
except FileNotFoundError:
    print(f"Error: {input_file_name} not found.")
except Exception as e:
    print(f"An error occurred: {e}")


