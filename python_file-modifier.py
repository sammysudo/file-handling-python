def read_and_modify_file(input_filename, output_filename):
    try:
        # Open the input file in read mode
        with open(input_filename, 'r') as input_file:
            content = input_file.read()

        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()

        # Open the output file in write mode
        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)

        print(f"File '{input_filename}' has been successfully modified and saved as '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")

    except IOError:
        print(f"Error: The file '{input_filename}' cannot be read.")

# Ask the user for the filename
input_filename = input("Enter the filename to read: ")
output_filename = "modified_" + input_filename

# Call the function to read and modify the file
read_and_modify_file(input_filename, output_filename)
