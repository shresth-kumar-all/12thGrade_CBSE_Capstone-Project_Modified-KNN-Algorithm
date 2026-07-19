## Overview
This is a class 12 AI capstone project named "Strategic Tagging and Fandom Unifier" aka the STFU project. The project addresses the problem of having too many options for consuming content. It has highly specific user interface letting the user enter what type of content they want to consume and exactly what they want in that media by the utilising the 11 genre inputs.

## Requirements
* **Pandas** `python -m pip install pandas`
* **NumPy** `(installed with pandas)`
* **Tkinter** `(standard module in python installation, but this may not be the case for an OS other than Windows)`
* **CustomTkinter** `pip install customtkinter`
* **Pillow** `pip install Pillow`

> *(the above may or may not work for an OS other than Windows. Please get all the requirements to avoid unexpected errors)*

## Description:
*The KNN algorithm works primarily on the n-dimensional distance formula to check the k no. of data points closest to it and return the mode statistic of their property. Our model modifies this idea by setting k to the number of elements in a dataset to include all the data points for consideration and then instead of showing mode, we tell the model to rank the most relevent (relevence here means the distance from the anchor point created by the user's preferneces) data point highest in order to rank each data point in order of relevence which is then accessed by the user interface to display the data points in decreasing order of relevence.

* **Setup:**
*   -Go to **Data**
*   -add entries in the format provided in the file
*   -add the images of standardized size to the relevent folder in **UI_Assets**

* **For user:**
*   Selecet the type of content on the button pallete on the left
*   Use the sliders to set preferences
*   hit the search button below the last slider
*   use the **prev** and **next** buttons to browse the recommendations
