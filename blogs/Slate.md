# Slate, a static site generator

Now that I am in college and soon was going to be out in the industry, I thought I should start putting myself out there, that is, have some platform for myself in general. The first thing that came to my mind was to make a personal website, which would have technical write-ups, blogs, etc. My original plan was to grab some HUGO or Jekyll static site generator templates and use them and tweak them for myself. But then there arose 3 problems:

1. Maintaining the site: Static site generators like HUGO and Jekyll use different technologies (Golang and Ruby) that I know nothing about. The problem here was that I didn't have enough time and motivation to learn them. Web dev isn't something that I want to aspire to. All these made tweaking and maintaining the whole codebase unnecessarily harder.
2. Site's theme: Not many of the themes I saw looked attractive or felt like `me` to me. Even If I found one, it gives me itches to tweak it again, which lead us to point 1 `¯\_(ツ)_/¯`.
3. Downloads: I didn't want to download different things when I only have < 256 Gb of space `(╥﹏╥)`.
 
So, to solve this problem, my only choice was to write my own site. I know you are probably `(－‸ლ)`, but this looks like an altogether better option to me `¯\_(ツ)_/¯`. I would not have to spend days learning things because I can just use HTML, CSS and some JS. Making a simple site with those in just a few hours of google searching.

There was a new problem. If I wanted to write blogs, I would have to do it in HTML and not markdown. To avoid this painful scenario, I used the pandoc CLI tool to convert. To convert the blog in bulk,  I had to write a script to do the conversion. Then I thought, why not just write a simple static site generator?`( ﾟｰﾟ)`

So, I thought, why not just do it? I maybe learn a thing or two and have something new to showcase? While creating it, I had some goals for it.

1. Simple: No need for hundreds of features. It should just get the work done. This also makes it easier to maintain.
2. Minimal: Keep stuff to download to a minimum. This can be done with Python + HTML + CSS + JS, which is included in all major systems by default, and a small CLI tool (pandoc) to download, no more than that.
3. Extensible: Since it is simple, it should be easy to add features you like if you know Python + HTML + CSS (easy to learn and get started).
4. Structure: Since it is simple, we just use JSON for config, some folders for CSS, js and blogs and call it a day.

And so we are done. Was it any brainer to get it done? No! I just hacked and dumped it together <code>↶（`∇´）</code>.

Here, this is how it look like `¬‿¬`

---

# Heading 1
## Heading 2
### Heading 3
#### Heading 4
##### Heading 5

---

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

**BOLD**

*Italic*

***Italic***

> Blockquote like this!
>
>> Nested blockquotes!


1. First
    1. Sub-First
        1. Sub-Sub-First
        2. Sub-Sub-Second
2. Second
    1. Sub-Second
    2. Sub-Second Second
3. Third

- First
    - Sub-First
    - Sub-Second
        - Sub-Sub-First

`Single backtick code look like this!`

```py
print("Hello World")
for i in range(0, 100):
    print("Your code look like this!")
```

[Link look like this!](https://github.com/BlackGoku36/BG36Portfolio)

![](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimages.fineartamerica.com%2Fimages%2Fartworkimages%2Fmediumlarge%2F2%2Fcloseup-of-an-indian-ring-necked-parakeet-jill-nightingale.jpg&f=1&nofb=1)

Dark and light mode is also supported.