import pandas as pd
import numpy as np
import flowkit


def return_FCS_as_compensated_dataframe(fcs_file_path):
    '''
    Read the FCS file, and if there is a SPILL matrix in the metadata, apply the matrix as the compensation matrix.
    '''
    return 0


def write_dataframe_as_FCS_file(dataframe, new_fcs_file_path):
    '''
    TIMESTEP is arbitrarily set to 5 to enable visualization in FACSDiva.
    '''
    return 0
    

def return_xy_nodes_for_visualization(dataframe, nodes_per_row=10, min_x = 10000, max_x = 250000, min_y = 10000, max_y = 10000):
    '''
    '''
    new_dataframe = pd.DataFrame()
    for column in dataframe.columns:
        column_name_x = column + "_x"
        column_name_y = column + "_y"
        new_dataframe[column_name_x] = dataframe[column]
        new_dataframe[column_name_y] = dataframe[column]

    return new_dataframe
    

def append_columns_to_compensated_dataframe(fcs_dataframe, new_columns_dataframe):
    '''
    '''
    return 0


def return_spreadsheet_as_dataframe(spreadsheet_file_path):
    '''
    '''
    return 0
    

def add_labels_as_grid_to_FCS(fcs_file_path, spreadsheet_file_path, new_fcs_file_path):
    '''
    The spreadsheet data should contain column labels in the first row and integer data for the labels.
    '''
    fcs_data = return_FCS_as_compensated_dataframe(fcs_file_path)
    spreadsheet_data = return_spreadsheet_as_dataframe(spreadsheet_file_path)

    #If number of rows match, proceed
    if fcs_data.shape[0] == spreadsheet_data.shape[0]:
        nodes_columns = return_xy_nodes_for_visualization(spreadsheet_data)
        appended_fcs_dataframe = append_columns_to_compensated_dataframe(fcs_data, nodes_columns)
        write_dataframe_as_FCS_file(appended_fcs_dataframe, new_fcs_file_path)
    else:
        print("Error: The number of events in ", fcs_file_path, "and", spreadsheet_file_path, "do not match.\n")
        return -1
    