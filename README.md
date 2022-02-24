# Color Revive
## Introduction
This python script is made to revive color from near-colorless images. It works by sensing changes in color pixels and amplifying these changes to their maximum to restore color.

Note that if the changes are null or way too little, the script won't be able to restore the colors.

## prerequisites
* Pillow package in python, you can get it buy running `pip install pillow`

## Installation
```
git clone https://github.com/medanisjbara/Color-revive
install Color-revive/colrev.py $HOME/.local/bin/colrev
```

## Usage
Type `colrev -h` for help.
use `colrev <image-name>` to execute the script on a certain image.

where `<image-name>` is the name of the image.