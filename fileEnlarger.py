import partA

def enlarge(file_path):
    print("--- opening file ... ---")
    content = partA.open_file(file_path)
    output = open("file11.txt", "w")
    print("--- writing content ... ---")
    output.write(content)
    output.write(content)
    output.close()
    print("--- Done. ---")

enlarge("file4.txt")
