import os

def scan_directory(path):
    print(f"Scanning directory: {path}\n")
    for root, dirs, files in os.walk(path):
        for file in files:
            filepath = os.path.join(root, file)
            size = os.path.getsize(filepath)
            ext = os.path.splitext(file)[1]
            print(f"{filepath} | {size} bytes | {ext}")

if __name__ == "__main__":
    folder = "."   # current directory
    scan_directory(folder)
