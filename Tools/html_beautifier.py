from yattag import indent
with open("E:/python/Tools/index.html", "r") as file:
    data = file.read()

result = indent(
    data,
    indentation='    ',
    newline='\r\n',
    indent_text=True
)
print(result)
