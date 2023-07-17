# ASSIGNMENT 7

## Installation
Run this command in terminal.
```
pip install -r requirements.txt
```

## Usage
### section_1.py
Apply different 2D filters on an image. The results will be saved in the `output/section_1` directory:

`if1`: Edge detection filter

`if2`: Sharpening filter in vertical and horizontal directions

`if3`: Emboss filter in horizontal direction

`if4`: Identity filter
`if5`: Emboss filter in vertical direction

`if6`: Sharpening filter in 8 directions

`if7`: Blur filter with 8*8 kernel size
### section_2.py
Apply different weighted sum to show hidden things in an image. The result will be saved in the `output/section_2` directory. from left to right:

`1) ` original image

`2) ` convolution with kernel size 5 and weights 0.04

`3) ` convolution with kernel size 5 and weights 1

`4) ` convolution with kernel size 5 and weights 5

`5) ` convolution with kernel size 3 and weights 0.04

`6) ` convolution with kernel size 3 and weights 1

`7) ` convolution with kernel size 3 and weights 5

### section_3.py
Apply median filter to reduce salt and pepper noise in images. The results will be saved in the `output/section_3` directory.

### section_4_a.py
Apply histogram equalization for low contrast images. The results will be saved in the `output/section_4_a` directory.

### section_4_b.py
Apply clahe algorithm for adaptive histogram equalization. we compared histogram equalization and adaptive histogram equalization results and saved them in `output/section_4_b` directory.