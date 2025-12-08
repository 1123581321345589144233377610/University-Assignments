# Дан текстовый файл. Найти количество абзацев в тексте, если абзацы отделяются друг 
# от друга одной или несколькими пустыми строками. 

def count_paragraphs(path_to_file: str) -> int:
    lines = []
    count_lines = 1
    index = 0
    with open(path_to_file, 'r') as file:
        lines = file.readlines()
    if all(line == '\n' for line in lines):
        return 0
    else:
        flag_is_empty_string = False
        while index < len(lines):
            if lines[index] == '\n' and not flag_is_empty_string:
                flag_is_empty_string = True
                count_lines += 1
            elif lines[index] != '\n':
                flag_is_empty_string = False
            index += 1
        return count_lines
        
print(count_paragraphs('data.txt'))