# mpFind

This CLI application searches the local area network for either BrightSign or SpinetiX media players

## Start

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install **_python-nmap_**.

```bash
pip install python-nmap
```

##Usage

To run the script, navigate to the main directory of mpFind.py and then run it using:

```bash
py mpFind.py 
```

The script takes a single input argument - **your ip address with the last localization number replaced with a '*'**
Example:
```bash
py mpFind.py 10.423.88.*
```

## License
[MIT](https://choosealicense.com/licenses/mit/)