def read_file_line_by_line(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            print(line.strip())

# Example usage:
file_path = 'your_file.txt'  # Replace 'your_file.txt' with the path to your file
read_file_line_by_line(file_path)
