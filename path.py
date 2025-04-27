import os

current_dir = os.path.dirname(os.path.abspath(__file__))

os.chdir(current_dir)

print("the currnet working directory:", os.getcwd())
