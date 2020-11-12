import pathlib


p = pathlib.Path("")
txt_files = p.glob("exercise-91/*.txt")

print(f"*.txt: {list(txt_files)}")
print(f"**/*.txt: {list(p.glob('exercise-91/**/*.txt'))}")
print(f"*/*: {list(p.glob('exercise-91/*/*'))}")
print(f"Files in */*: {[f for f in p.glob('exercise-91/*/*') if f.is_file()]}")
