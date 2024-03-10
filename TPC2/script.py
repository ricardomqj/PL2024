import sys 
import re

def convert_md_to_html(md_file):
    html_content = ""
    with open(md_file, 'r') as file:
        for line in file:
            # Headers
            if line.startswith("#"):
                level = line.count("#")
                header_text = line.strip("# \n")
                html_content += f"<h{level}>{header_text}</h{level}>\n"
            #Bold 
            elif "**" in line:
                line = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', line)
                html_content += line
            #Italic 
            elif "*" in line:
                line = re.sub(r'\*(.*?)\*\*', r'<i>\1</i>', line)
                html_content += line
            #Numbered List 
            elif line.strip().isdigit():
                html_content += "<ol>\n"
                while line.strip().isdigit(): # line.strip() remove espaços em branco no inicio e final de uma string
                    html_content += f"<li>{line.strip()}</li>\n"
                    line = next(file)
                html_content += "</ol>\n"
            # Link
            elif "[" in line and "]" in line and "(" in line and ")" in line and not "![" in line:
                link_text = re.search(r'\[(.*?)\]', line).group(1)
                link_url = re.search(r'\((.*?)\)', line).group(1)
                html_content += f'<a href="{link_url}">{link_text}</a>\n'
            # Image 
            elif "![" in line and "]" in line and "(" in line and ")" in line:
                alt_text = re.search(r'\[(.*?)\]', line).group(1)
                image_url = re.search(r'\((.*?)\)', line).group(1)
                html_content += f'<img src="{image_url}" alt="{alt_text}"/>\n'
            else:
                html_content += line
    return html_content

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <file.md>")
        return

    input_md = sys.argv[1]
    output_html = input_md.replace(".md", ".html")
    
    html_content = convert_md_to_html(input_md)
    
    with open(output_html, 'w') as file:
        file.write(html_content)
        
    print(f"Ficheiro em Markdown convertido para HTML e guardado em {output_html}")

if __name__ == "__main__":
    main()