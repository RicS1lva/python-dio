linguagens = ["Python", "js", "c", "java", "csharp"]

sorted(linguagens, key=lambda x: len(x)) # ["c", "js", "java", "Python", 
# "csharp"]

sorted(linguagens, key=lambda x: len(x), reverse=True)  # ["Python, "csharp",
# "java", "js", "c"]

print(sorted(linguagens))