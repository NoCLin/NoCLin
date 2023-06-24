import os
import subprocess
from pathlib import Path

import markdown


def render_to_html():
    for md_file in Path("posts").rglob("*.md"):
        md_content = open(md_file, "rt").read()
        html_file = md_file.parent / (md_file.stem + ".html")

        html = markdown.markdown(md_content)
        html = f"<pre>$ cat {md_file}" + "</pre>" + html
        open(html_file, "wt").write(html)


alias_mapping = {

}

CMD_LIST_POSTS = "ls -l posts/*.html"


def execute(cmd):

    text = f"$ {cmd}" + "\n"
    real_cmd = alias_mapping.get(cmd, cmd)
    output = subprocess.getoutput(real_cmd)

    if cmd == CMD_LIST_POSTS:
        lines = output.splitlines()
        for line_no, line in enumerate(lines):
            parts = line.split(" ")
            if len(parts) != 12:
                continue
            filename = parts[-1]
            file_name_with_link = f'<a href="{filename}">{filename}</a>'
            parts[3] = f'<a href="https://liu.junl.in">Junlin</a>'
            parts[-1] = file_name_with_link
            lines[line_no] = " ".join(parts)
        output = "\n".join(lines)
    text += output + "\n"
    text += "\n"
    return text


if __name__ == '__main__':
    os.chdir("..")
    text = ""

    text += execute("cat welcome.txt")
    text += execute("cat about.html")
    text += execute(CMD_LIST_POSTS)
    text += execute("date")
    text = "<pre>" + text + "</pre>"
    print(text)
    open("content.html", "wt").write(text)
    render_to_html()
