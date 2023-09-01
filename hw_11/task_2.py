# 1. Create file with some content. As example you can take this one
#     ```
#         Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
#     ```
#     2. Create second file and copy content of the first file to the second file in upper case.

with open("some_content.txt", "w") as file:
    file.write("Lorem ipsum dolor sit amet,\n consectetur adipiscing elit,\n sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\n Ut enim ad minim veniam,\n quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.\n Duis aute irure dolor in reprehenderit in voluptate velit\n esse cillum dolore eu fugiat nulla pariatur.\n Excepteur sint occaecat cupidatat non proident,\n sunt in culpa qui officia deserunt mollit anim id est laborum.")

with open("some_content.txt", "r") as file:
    content = file.read()


with open("copy_some_content.txt", "w") as file2:
    file2.write(content.upper())
