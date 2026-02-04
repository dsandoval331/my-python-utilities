def add_ascending_numbers_to_file(input_filename, output_filename="numbered_output.txt"):
    """
    Reads lines from an input file, prepends ascending line numbers (1: Line Content),
    and writes the result to a specified output file.

    Args:
        input_filename (str): The path to the file you want to read from.
        output_filename (str): The path where you want to save the numbered output.
                               Defaults to 'numbered_output.txt' in the current directory.
    """
    try:
        # Open the input file in read mode ('r')
        with open(input_filename, 'r') as infile:
            lines = infile.readlines()

        numbered_lines = []
        # Use enumerate to get both the index (line number) and the line content
        # Start the index count at 1
        for index, line in enumerate(lines, 1):
            # Strip existing newlines to ensure consistent formatting, then add our own
            formatted_line = f"{index} {line.rstrip()}\n"
            numbered_lines.append(formatted_line)

        # Open the output file in write mode ('w'). This will create the file if it doesn't exist
        # or overwrite it if it does.
        with open(output_filename, 'w') as outfile:
            outfile.writelines(numbered_lines)

        print(f"Successfully numbered lines from '{input_filename}' and saved to '{output_filename}'.")
        print(f"Total lines processed: {len(lines)}")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found. Please check the file path.")
    except IOError as e:
        print(f"An I/O error occurred: {e}")

# --- How to use the script ---
if __name__ == "__main__":
    # 1. Ensure you have an 'input_file.txt' in the same directory as this script.
    #    You can replace 'input_file.txt' with the full path to your file.
    # 2. Run the function:
    add_ascending_numbers_to_file("input_file.txt", "final_output.txt")
