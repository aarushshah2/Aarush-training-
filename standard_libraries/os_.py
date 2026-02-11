import os

# os.getcwd() - Get current directory
print(f"Current Dir: {os.getcwd()}")

# os.path.join(a, b) - Safe path joining
path = os.path.join(os.getcwd(), "test_folder")

# os.mkdir(path) - Create folder
if not os.path.exists(path):
    os.mkdir(path)

# os.listdir(path) - List files
print(f"Files: {os.listdir('.')}")

# os.path.exists(p) - Check existence
print(f"Exists: {os.path.exists('test.txt')}")

# os.rename(a, b) & os.remove(file)
# os.rename("old.txt", "new.txt")
# os.remove("new.txt")