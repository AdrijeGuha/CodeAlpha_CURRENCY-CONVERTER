# Currency Converter Python Program

![preview](https://github.com/AdrijeGuha/CodeAlpha_CURRENCY-CONVERTER/blob/647441a4826d689599c6b94034cbc375def49e8d/img/preview.png)

## Overview

This Python project aims to provide a user-friendly Graphical User Interface (GUI) for converting currency from one currency to any other currency in real-time. The program utilizes the `customtkiter` library for GUI development and the `forex-python` library for currency conversion.

## Features

- Real-time currency conversion with a single button click.
- User-friendly interface for input and output currency values.
- Supports conversion between a wide range of currencies.

## Prerequisites

Before running the program, ensure you have the following libraries installed:

- [customtkinter](https://github.com/TomSchimansky/CustomTkinter)
- [forex-python](https://github.com/MicroPyramid/forex-python)
- [pandas](https://pandas.pydata.org/)
- [pillow](https://pillow.readthedocs.io/en/stable/)

You can install the required libraries using the following command:

```bash
pip install -r requirements.txt
```

The requirements.txt file is present in this repo itself.

## How to Use

1. Clone this repository to your local machine.
2. Install the required libraries as mentioned in the "Prerequisites" section.
3. Run the `CurrencyConverter.py` script to launch the GUI application.

## Getting Started

1. Import the necessary modules from `customtkiter` and `forex_python`.
2. Create a GUI window with input and output currency value fields, along with a "Convert" button.
3. Implement the currency conversion function using the `forex_python` library.
4. Link the "Convert" button to call the conversion function and update the output currency value field accordingly.

## Limitations

- The program requires an active internet connection to access real-time currency conversion rates.
- Currency conversion rates may vary based on the API used.
- Due to the limitations of the Google Translate API, extensive usage may be rate-limited.
- The GUI library has set limitations, demining the applications' user-friendly aspect.

## Contributions

Contributions to improve the project, adding new features, fixing bugs, or enhancing the GUI are welcome. Just create a pull request, and we'll review it together.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/AdrijeGuha/CodeAlpha_CURRENCY-CONVERTER/blob/f973aa1b0d3ab40af9b72d665eabba9bb37b3f2f/LICENSE) file for details.
