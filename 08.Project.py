def read_constitution(file_path):
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    return lines

def find_section(lines, search_term):
    found_sections = []
    i = 0
    while i < len(lines):
        if search_term.lower() in lines[i].lower():
            # Find the start of the section (search backwards for a blank line)
            start_index = i
            while start_index > 0 and lines[start_index - 1] != '':
                start_index -= 1
            
            # Find the end of the section (search forwards for a blank line)
            end_index = i
            while end_index < len(lines) - 1 and lines[end_index + 1] != '':
                end_index += 1

            # Avoid printing the same section twice
            if (start_index, end_index) not in found_sections:
                found_sections.append((start_index, end_index))
                
                # Print the section with line numbers
                print(f"Line {start_index + 1}:")
                for j in range(start_index, end_index + 1):
                    print(lines[j])
                print()
                
            # Skip to the end of the section to avoid redundant matches
            i = end_index
        i += 1

def main():
    constitution_file = 'constitution.txt'
    lines = read_constitution(constitution_file)
    
    while True:
        search_term = input("Enter search term (or press Enter to exit): ")
        if not search_term:
            break
        find_section(lines, search_term)

if __name__ == "__main__":
    main()
