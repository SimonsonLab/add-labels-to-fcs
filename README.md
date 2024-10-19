# add-labels-to-fcs

This repository includes code for adding data labels to FCS files as additional data channels.  It also adds labels a grid that can be gated in standard flow cytometry software.  The package is in active development, and more features will be added here.

## Installation


pip install add-labels-to-fcs


## Basic Usage

To add data columns (unmodified) to an FCS file using command line interface: 

add-labels-to-fcs file.fcs labels.xlsx new_file.fcs


To add data columns in a grid to facilitate gating using command line interface: 

add-labels-as-grid-to-fcs file.fcs labels.xlsx new_file.fcs


To use library functions in your own python scripts, import the following:

from add-labels-to-fcs import add_labels



## See Also

For example R code for adding additional columns to FCS files, see the R studio notebook file at https://github.com/SimonsonLab/2021_Next_Gen_Flow_Lecture.

