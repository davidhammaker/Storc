# Storc | Character Generator

A random character generator that creates a named character to inspire your creativity.

## Purpose

This tool is intended for anyone who is struggling to come up with unique characters, with names and other qualities, for a work of literature or other creative work.

## Dependencies

Requires Python 3.6 or higher to work properly.

Requires "Flask" and "requests".

Character names are fetched from the [Behind the Name](https://www.behindthename.com/) API. For development purposes, the lines of code that fetch a name from Behind the Name are commented out.

If you would like to use the Behind the Name API for character name creation, you must first set the environment variable "BTN_KEY" to your Behind the Name API key. To obtain an API key, follow the instructions found on the Behind the Name website, [here](https://www.behindthename.com/api/). Once you have set "BTN_KEY", open `app.py`, un-comment the lines of code beneath the comment, `# The following lines have been commented out for development:`, and remove or comment out `name = 'John Doe'`.

## Usage

_When using this tool, please be aware that the tool is not yet complete._

To use the application, start by cloning this repository. Use `pip` to install "Flask" and "requests". Run the application with `$ python run.py`. You can then view the application at [localhost:5000](http://localhost:5000/).

## Copyright

© 2018-2019 David J. Hammaker
