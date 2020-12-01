# Setup

## macOS

Check what version of Python is default on you're system. Open terminal and type "python". If you have not messed with python at all, the default should be 2.7.x

### Python 2.7.X

Since Python 2.7 is a depricated version of python, there is a few packages we would need to install first in order for the apple script to work properly. Run these commands in terminal to setup python for the apple script.

```
pip install pandas

pip install xlrd

pip install openpyxl
```

### Python 3.X.X

If you are using the most up-to-date python version, you should only need to install one python package. Run this command in terminal to setup python for the apple script.

`pip install pandas`

Once you have python setup, clone/install the repo with a CLI (If you have github CLI installed) or install the zip file directly from the website. Place the contents of the repo into a folder on the desktop (**the folder must be in the desktop in order for the apple script to work**).

## Usage

Run the apple script and you should be prompted with a window that is asking you for the location of the excel file you want to process through the python script. An example location could look something like this (the location of the excel file does not have to be in the same folder as the application):

<img src="https://i.gyazo.com/26b086b935e784e9375137b398d1881f.png" width=500>

If everything goes well, when you click "Ok" it should create a new excel file in the application folder called "AVGUTIL <today's date>"
