import json
import os
from subprocess import Popen, PIPE
import shutil
import sys
import shutil

path_to_pandoc = 'pandoc'
try:
    path_to_pandoc = sys.argv[1]
except:
    print('Trying installed pandoc at PATH')

profile = {}
blogs = []
contacts = []

mailSVG = '''<svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none"
                stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
                class="feather feather-mail">
                <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path>
                <polyline points="22,6 12,13 2,6"></polyline>
            </svg>'''
twitterSVG = '''<svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none"
                stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
                class="feather feather-twitter">
                <path d="M23 3a10.9 10.9 0 0 1-3.14 1.53 4.48 4.48 0 0 0-7.86 3v1A10.66 10.66 0 0 1 3 4s-4 9 5 13a11.64 11.64 0 0 1-7 2c9 5 20 0 20-11.5a4.5 4.5 0 0 0-.08-.83A7.72 7.72 0 0 0 23 3z">
                </path>
            </svg>'''
githubSVG = '''<svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none"
                stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
                class="feather feather-github">
                <path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22">
                </path>
            </svg>'''

js = '''
<script>
        const stylesheet = document.documentElement.style;
        const darkThemeMq = window.matchMedia("(prefers-color-scheme: dark)");
        if(!localStorage.getItem("theme")){
            localStorage.setItem("theme", "system");
        }
        setButtonText();

        function setDarkTheme(){
            const darkBg = getComputedStyle(document.documentElement).getPropertyValue("--dark-bg");
            const darkAccent = getComputedStyle(document.documentElement).getPropertyValue("--dark-accent");
            const darkAccent2 = getComputedStyle(document.documentElement).getPropertyValue("--dark-accent-2");
            const darkAccent3 = getComputedStyle(document.documentElement).getPropertyValue("--dark-accent-3");
            stylesheet.setProperty("--theme-bg", darkBg);
            stylesheet.setProperty("--theme-accent", darkAccent);
            stylesheet.setProperty("--theme-accent-2", darkAccent2);
            stylesheet.setProperty("--theme-accent-3", darkAccent3);
        }
        function setLightTheme(){
            const lightBg = getComputedStyle(document.documentElement).getPropertyValue("--light-bg");
            const lightAccent = getComputedStyle(document.documentElement).getPropertyValue("--light-accent");
            const lightAccent2 = getComputedStyle(document.documentElement).getPropertyValue("--light-accent-2");
            const lightAccent3 = getComputedStyle(document.documentElement).getPropertyValue("--light-accent-3");
            stylesheet.setProperty("--theme-bg", lightBg);
            stylesheet.setProperty("--theme-accent", lightAccent);
            stylesheet.setProperty("--theme-accent-2", lightAccent2);
            stylesheet.setProperty("--theme-accent-3", lightAccent3);
        }
        function setButtonText(){
            const theme = localStorage.getItem("theme");
            var text = theme.toUpperCase() +' THEME';
            document.getElementById("btn").innerHTML = text;
        }
        darkThemeMq.addListener(e => {
            if (e.matches) {
                if(localStorage.getItem("theme") == "system"){
                    setButtonText();
                    setDarkTheme();
                }
            } else {
                if(localStorage.getItem("theme") == "system"){
                    setButtonText();
                    setLightTheme();
                }
            }
        });
        function setTheme(){
            if(localStorage.getItem("theme") == "system"){
                localStorage.setItem("theme", "light");
                setLightTheme();
                setButtonText();
            }else if(localStorage.getItem("theme") == "light"){
                localStorage.setItem("theme", "dark");
                setDarkTheme();
                setButtonText();
            }else{
                localStorage.setItem("theme", "system");
                setButtonText();
            }
        }
</script>
'''

with open('profile.json', 'r') as file:
    profile = json.loads(''.join(file.readlines()))

for blog in profile["blogs"]:
    isSeries = False
    try:
        series = blog["series"]
        isSeries = True
        blogs.append("<details>")
        blogs.append("<summary>"+blog["name"]+"</summary>")
        for chapter in series:
            name = chapter["name"]
            link = chapter["link"]
            isDisabled = False
            try:
                isDisabled = chapter["disabled"]
            except:
                x = 0
            if isDisabled == True:
                blogs.append("<a class='disabled' href='"+link+".html"+"'> <li>"+"<s>"+name+"</s>"+"</li></a>")
            else:
                blogs.append("<a href='"+link+".html"+"'> <li>"+name+"</li></a>")
        blogs.append("</details>")
    except:
        x = 0

    if isSeries == False:
        name = blog["name"]
        link = blog["link"]
        blogs.append("<a href='"+link+".html"+"'> <li>"+name+"</li></a>")



try:
    contacts.append("<a href='"+profile["github"]+"'>"+githubSVG+"</a>")
except:
    print("-> Github account skipped")

try:
    contacts.append("<a href='"+profile["twitter"]+"'>"+twitterSVG+"</a>")
except:
    print("-> Twitter account skipped")

try:
    contacts.append("<a href='mailto: "+profile["mail"]+"'>"+mailSVG+"</a>")
except:
    print("-> Mail skipped")

contact = ""
if(len(contacts)!=0):
    contact = '<br><h2>CONTACTS</h2><hr><div class="contact">'+''.join(contacts) + '</div>'

copyright = ""
try:
    copyright = "<footer>"+profile["copyright"]+"</footer>"
except:
    print("-> copyright skipped")

switchThemeBTN = '''
<button id="btn" onclick="setTheme()">THEME</button>
'''

indexHTML = [
    '''<!DOCTYPE html><html><head><meta charset="utf-8">
    <link rel="stylesheet" href="index.css"><meta name="viewport" content="width=device-width, initial-scale=1">
    <title>''', profile["name"], '''</title></head>
    <body>
    <div class="contents">
    <h1 style="display: inline-block; padding-right: 20px;">''', profile["name"], '''</h1>''',
    switchThemeBTN,
    '''<hr>
    <div class="profile">
        <img src="pfp.png"
            width="150" height="150" style="float:left; margin-right: 15px; margin-top: 5px;">
        <p>''',profile["description"],'''</p>
        <br>
    </div>
    <br><br><br>
    <h2>BLOGS</h2><hr>
    <div class="project">
        <ul>''', ''.join(blogs), '''</ul>
    </div>''', 
    contact, 
    '''</div>''', 
    copyright, js,'''
    </body>
    </html>
    '''
]

try:
    shutil.rmtree('docs')
except:
    x = 0
try:
    os.mkdir("docs")
except:
    x = 0

with open('docs/index.html', 'w') as file:
    file.writelines(indexHTML)

# Blogs


blogBtns = '''<a class="home" href="index.html">HOME</a>'''+switchThemeBTN+'''

---

'''

shutil.copy('pfp.png', 'docs/pfp.png')
shutil.copy('css/blog.css', 'docs/blog.css')
shutil.copy('css/index.css', 'docs/index.css')
shutil.copy('js/highlight.min.js', 'docs/highlight.min.js')

try:
    shutil.rmtree('docs/assets')
except:
    x = 0
try:
    os.mkdir("docs/assets")
except:
    x = 0

with os.scandir('blogs/assets/') as entries:
    for entry in entries:
        if (".png" or ".jpeg" or ".mp4" or ".mov") in entry.name:
            shutil.copy('blogs/assets/'+entry.name, 'docs/assets/'+entry.name)


def createBlogs():
    with os.scandir('blogs/') as entries:
        for entry in entries:
            if ".md" in entry.name:
                blogContents = []
                blogContents.append('<h1>'+profile["name"]+"</h1>")
                blogContents.append('<div class="contents">')
                blogContents.append(blogBtns)
                with open('blogs/'+entry.name, 'r') as file:
                    blogContents.append(''.join(file.readlines()))
                blogContents.append("\n")
                blogContents.append('\n<script src="highlight.min.js"></script><script>hljs.highlightAll();</script>')
                blogContents.append(js)
                blogContents.append('</div>')
                blogContents.append(copyright)
                with open('docs/'+entry.name, 'w') as file:
                    file.writelines(blogContents)
                md_to_html(entry.name)
                os.remove('docs/'+entry.name)

def md_to_html(entry):
    process = Popen([
            path_to_pandoc, 
            '--metadata', 'title='+entry[:-3],
            '-s', '--no-highlight', 
            '-c', 'blog.css', 
            'docs/'+entry, 
            '-o', 'docs/'+entry[:-3]+'.html'
        ], stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    error = bytes.decode(stderr)
    if(error == ""):
        print('\033[32m '+entry+' successfully translated to html'+' \033[0m')
    else:
        print("\033[31m '"+error+"' \033[0m")

createBlogs()