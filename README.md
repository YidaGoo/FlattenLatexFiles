This is a python script that flattens multiple .tex files.

Usage:

```
python flatten.py main.tex main_flattened.tex
```

The first argument is your main .tex file. The script recursively looks for "\input{...}" and "\include{...}" latex code and flattens .tex contents accordingly. The final flattened content is written to the .tex file specified as the second argument.

With flattened .tex files, we can now use [latexdiff](https://github.com/ftilmann/latexdiff/) to diff your .tex files and produce nicely notated pdf.

Some helpful articles on the usage of `latexdiff`:
* http://emeryblogger.com/2011/01/14/diff-your-latex-files-with-latexdiff/
* https://www.sharelatex.com/blog/2013/02/16/using-latexdiff-for-marking-changes-to-tex-documents.html
