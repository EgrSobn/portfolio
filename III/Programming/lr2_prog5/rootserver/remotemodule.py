import sys

def myfoo():
    author = "Egor Sobinin"
    print(f"{author}'s module is imported")

sys.path.append("http://localhost:8000")