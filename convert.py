import markdown
import sys

scaffold = """
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>The Dump</title>
        <link rel="stylesheet" href="../style/index.css">
    </head>
    <body>
    {}
    </body>
    <script src="../script/index.js"></script>
</html>
"""

snippet = """
<div class="snippet">
    <h3><a href="{}">{}</a></h3>
    <div class="date">{}</div>
    <div class="preview">
        {}
    </div>
</div>
"""



if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python3 convert.py post_md/filename.md")

    markdown_filepath = sys.argv[1]
    html_filepath = "posts/" + markdown_filepath.split('/')[-1].split('.')[0] + ".html"

    with open(markdown_filepath, 'r') as f:
        text = f.read()
        html = markdown.markdown(text)

    title = html.split('</h1>')[0][4:]
    time = html.split('<em>')[1].split('</em>')[0]
    preview = html.split('<p>')[2].split('</p>')[0]

    with open(html_filepath, 'w') as f:
        f.write(scaffold.format(html))

    print(snippet.format(html_filepath,title,time,preview))
    


