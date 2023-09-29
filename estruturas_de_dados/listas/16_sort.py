linguagens = ["Python", "js", "c", "java", "csharp"]
linguagens.sort()  # ["Python', 'c', 'csharp', 'java', 'js']
print(linguagens)

linguagens = ["Python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True)  # ['js', 'java', 'csharp', 'c', 'Python']
print(linguagens)

linguagens = ["Python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x))  # ['c', 'js', 'java', 'Python', 'csharp']
print(linguagens)

linguagens = ["Python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True)  # ['Python', 'csharp', 'java', 'js', 'c']
print(linguagens)