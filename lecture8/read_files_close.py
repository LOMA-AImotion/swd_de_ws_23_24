def read_file_lines(file):
    f = open(file, 'r')
    for l in f:
        print(l.strip())
    f.close()
    
# Example usage:
file_path = 'your_file.txt'  
read_file_lines(file_path)
