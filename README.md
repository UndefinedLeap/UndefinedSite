Personal site generator I made for myself. But you can fork and use it for yourself :).

## Usages

* Create and configure your landing page with `profile.json`. Example:
```json
{
    "name": "Your name",
    "description": "Your blogpost now belong to me",
    "blogs": [
        {
            "name": "Test",
            "link": "Test.html"
        },
    ],
    "github": "https://github.com/lala",
    "twitter": "https://twitter.com/lalal",
    "mail": "lalala@lololo.com",
    "copyright": "© 2021-2022 lalala"
}
```
* Create `pfp.png` (obv, your profile pic).
* Create `blogs` directory and put your markdown blogs there. Code can be included with backticks syntax and raw inlined html works. In case, your preferred programming language is not highlighted, then replace `highlight.min.js` (in `js` folder) with your [own](https://highlightjs.org).
* In `blogs` directory, create `assets` folder and dump all your images and videos there.

## Run

* Make sure you have pandoc installed

If pandoc is installed and $PATH var point to it then simply run:
```
python3 generator.py
```
else:
```
python3 generator.py <path/to/pandoc_bin>
```

* Generated output will be in `docs` folder.

## License

This is licensed under zlib. Check `License.md` for more info.
