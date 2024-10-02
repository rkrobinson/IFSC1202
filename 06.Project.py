def merge_files():
    input_file = "06.Project Input File.txt"
    merge_file = "06.Project Merge File.txt"
    output_file = "06.Project Output File.txt"
    
    input_count = 0
    merge_count = 0
    output_count = 0
    
    with open(output_file, 'w') as out_f:
        with open(input_file, 'r') as in_f:
            for line in in_f:
                input_count += 1
                if line.strip() == "**Insert Merge File Here**":
                    with open(merge_file, 'r') as merge_f:
                        for merge_line in merge_f:
                            merge_count += 1
                            out_f.write(merge_line)
                            output_count += 1
                else:
                    out_f.write(line)
                    output_count += 1
    
    print(f"{input_count} input file records")
    print(f"{merge_count} merge file records")
    print(f"{output_count} output file records")

if __name__ == "__main__":
    merge_files()