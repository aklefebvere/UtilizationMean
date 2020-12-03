# Setup

## macOS

Check what version of Python is default on you're system. Open terminal and type "python". If you have not messed with python at all, the default should be 2.7.x

Before we install the required packages for Python, we need to install the package installer pip. To do this run the following commands in order:
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

python get-pip.py
```
This downloads the ```get-pip.py``` module and it runs the module with python to download the pip package installer. You could also install pip using ```sudo easy_install pip```. This may work for you but I do not recommend this method as this method has been deprecated since 2019, the first solution is the up-to-date way to install pip.

### Python 2.7.X

Since Python 2.7 is a deprecated version of python, there is a few packages we would need to install first. Run these commands in terminal:

```
pip install pandas

pip install xlrd

pip install openpyxl
```

### Python 3.X.X

If you are using the most up-to-date python version, you should only need to install one python package. Run this command in terminal.

`pip install pandas`

Once you have python setup, clone/install the repo with a CLI (If you have github CLI installed) or install the zip file directly from the website. Place the contents of the repo into a folder.

## Usage

In a CLI, CD into the directory of where the .py module is located. To run the script, run the following command:
```
python ciscoutil.py
```
You will be prompted with a message asking for the location of the excel filel, paste the location of the excel file wrapped in quotes (ex: "/Users/adriann/Desktop/CiscoUtil/Delivery-sheet.xlsx") and press enter. If you are returned with the message "Done!" then it should have created an excel file in the same directory as the py module named "AVGUTIL <today's date>".




