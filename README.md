# pyhtml
pyhtml is a little toolbox which allows you to write html content within your
python script into a variable. This variable then can be saved to a .html file
and be opened with any standard browser.

## Where to get it
```sh
# PyPI
pip install pyhtmlgen
```

## supported html objects
* h1, h2, h3
* paragraphs
* line breaks
* tables
* start and end

## supported python objects
* strings
* numpy matrices
* plotly figures

## How to use
* create a variable to store a string within your script
* use generators.start('Title of your page') to add the html head
* add content as you wish
* use generators.end() to close the html file correctly
* write the variable to a file

Have a look at the example.py script for more information
