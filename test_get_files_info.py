from functions.get_files_info import get_files_info

result1 = get_files_info("calculator", ".")
result2 = get_files_info("calculator", "pkg")
result3 = get_files_info("calculator", "/bin")
result4 = get_files_info("calculator", "../")

print("Result for current directory:")
print(result1)
print("Result for 'pkg' directory:")
print(result2)
print("Result for '/bin' directory:")
print(f"  {result3}")
print("Result for '../' directory:")
print(f"  {result4}")
