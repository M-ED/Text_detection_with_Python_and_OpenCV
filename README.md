
# Text Detection with Python, OpenCV, and EasyOCR

This mini-project demonstrates how to perform text detection and recognition on images using Python, OpenCV, and EasyOCR. The python script reads an image detects the text within an image, draws bounding box around the detected text, and displays the recognized text on the image.






## Prerequisites
- Python 3.9.0 or higher 
- OpenCV
- EasyOCR
- Matplotlib

## Installation

1. Clone the repository:

```bash
  git clone https://github.com/M-ED/Text_detection_with_Python_and_Opencv_OCR_using_EasyOCR.git
```

2. Create virtual environment using following commands:
```bash
  conda create -n projects_CV python==3.9.0
  conda activate projects_CV
```

3. Install the necessary libraries in requirements file
```bash
   pip install -r requirements.txt
```

4. Run the script
```bash
  python main.py
```


## Demo

![Output_Image](https://drive.google.com/file/d/1LEf4HMJAUtz8mIO-HDmtmdXanzDBXb2r/view?usp=drive_link)
## Features

Following are the key features:
- images: There are 3, 4 images for detecting text on number plate.
- main.py: The main script that handles image reading, drawing bounding boxes, text display, and finally resulting image is displayed using Matplotlib.

## Example Output

```bash
([[166, 126], [448, 126], [448, 182], [166, 182]], 'ROAD CLOSED', 0.9994066640174729)
([[167, 181], [447, 181], [447, 221], [167, 221]], 'TO ALL PEDESTRIAN', 0.9704423461894937)
([[209, 220], [409, 220], [409, 258], [209, 258]], 'AND BIKE USE', 0.9281838718124332)
```

## Future Work

- Experiment with different different threshold values for text detection.
- Explore the use of GPU for faster text detection usig EasyOCR.
- Extend the project to handle video streams for real-time detection.





## Acknowledgements

- OpenCV: [https://opencv.org/](https://opencv.org/)
- Scikit-Learn: [hhttps://scikit-learn.org/stable//](https://scikit-learn.org/stable/)



## License

[MIT](https://choosealicense.com/licenses/mit/)


## Badges

Add badges from somewhere like: [shields.io](https://shields.io/)

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)


## Author

- [@mohtadia_naqvi](https://github.com/M-ED)

