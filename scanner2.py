import os

SUSPICIOUS = ["eval(", "exec(", "os.system", "subprocess"]

def scan_files(path):
    print(f"Scanning for suspicious code in: {path}\n")
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".py"):
                filepath = os.path.join(root, file)
                with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                    for keyword in SUSPICIOUS:
                        if keyword in content:
                            print(f"[!] Found '{keyword}' in {filepath}")

if __name__ == "__main__":
    folder = "."   # current directory
    scan_files(folder)
