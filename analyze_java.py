import file_list

def analyze_java(out):
    print("Analyzing java files:")
    java_files = file_list.list_files("java", out, True)
    for java_file in java_files:
        print(java_file)
