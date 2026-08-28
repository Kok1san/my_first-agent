from functions.get_file_content import get_file_content

result = get_file_content("calculator", "lorem.txt")
print(f"lorem.txt length: {len(result)}")
print(f"lorem.txt truncated: {'truncated' in result}")

result_2 = get_file_content("calculator", "main.py")
print(result_2)
print(f"main.py length: {len(result_2)}")
print(f"main.py truncated: {'truncated' in result_2}")

result_3 = get_file_content("calculator", "pkg/calculator.py")
print(result_3)
print(f"pkg/calculator.py length: {len(result_3)}")
print(f"pkg/calculator.py truncated: {'truncated' in result_3}")

result_4 = get_file_content("calculator", "/bin/cat")
print(result_4)
result_5 = get_file_content("calculator", "pkg/does_not_exist.py")
print(result_5)
