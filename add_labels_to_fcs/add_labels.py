#This file should contain most of the library functions.

from pathlib import Path
import random
import csv
import numpy as np
import os
import sys

import pandas as pd
import numpy as np
import flowkit as fk


def return_FCS_as_compensated_dataframe(fcs_file_path):
    '''
    Read the FCS file, and if there is a SPILL matrix in the metadata, apply the matrix as the compensation matrix.
    Return events as a pandas dataframe.
    '''

    sample = fk.Sample(fcs_file_path, cache_original_events=True)
    metadata = sample.get_metadata()

    #If SPILL is present in metadata:
    if 'spill' in metadata:
        sample.apply_compensation(metadata['spill'])
        events_df = sample.as_dataframe(source='comp')
    else:
        events_df = sample.as_dataframe(source='raw')

    return events_df


def write_dataframe_as_FCS_file(dataframe, new_fcs_file_path):
    '''
    TIMESTEP is arbitrarily set to 5 to enable visualization in FACSDiva.
    '''
    #Create a new FCS object from the data frame.
    sample_from_df = fk.Sample(dataframe, sample_id='new FCS file')
    sample_from_df.metadata.update({"$TIMESTEP": "5"})
    metadata = sample_from_df.get_metadata()
    
    #Export as a new FCS file.
    sample_from_df.export(new_fcs_file_path, source='raw', include_metadata = True)
    #print("Saved", new_file_path)


def return_spreadsheet_as_dataframe(spreadsheet_file_path):
    '''
    Open Excel file and return pandas dataframe.
    '''
    new_dataframe = pd.read_excel(Path(spreadsheet_file_path))

    return new_dataframe
    

def return_xy_nodes_for_visualization(dataframe, nodes_per_row=10, min_x = 10000, max_x = 200000):
    '''
    Take columns of labels and turn them into grids that can be gated.
    '''
    new_dataframe = pd.DataFrame()
    for column in dataframe.columns:
        column_name_x = column + "_x"
        column_name_y = column + "_y"
        new_dataframe[(column_name_x + "-A", column_name_x)] = dataframe[column]
        new_dataframe[(column_name_y + "-A", column_name_y)] = dataframe[column]

        clusters = list(dataframe[column])

        internode_distance = int((max_x - min_x)/nodes_per_row)
        jitter_range = int(0.3 * internode_distance)
        #print(internode_distance, jitter_range)
        
        #Add the labels.
        new_dataframe[(column_name_x + "-A", column_name_x)] = np.asarray(clusters) % nodes_per_row
        new_dataframe[(column_name_y + "-A", column_name_y)] = np.asarray(clusters) // nodes_per_row
    
        new_dataframe[(column_name_x + "-A", column_name_x)] += 1
        new_dataframe[(column_name_x + "-A", column_name_x)] *= internode_distance
        
        new_dataframe[(column_name_y + "-A", column_name_y)] += 1
        new_dataframe[(column_name_y + "-A", column_name_y)] *= internode_distance
        
        #Add some jitter for plotting purposes.
        jitter = list(random.choices(range(0, jitter_range), k=new_dataframe.shape[0]))
        new_dataframe[(column_name_x + "-A", column_name_x)] += jitter
        jitter = list(random.choices(range(0, jitter_range), k=new_dataframe.shape[0]))
        new_dataframe[(column_name_y + "-A", column_name_y)] += jitter
    
    return new_dataframe


def return_labels_with_fixed_column_names(dataframe):
    '''
    Take columns of labels and changes the column names to (pnn, pns) format.
    '''
    new_dataframe = pd.DataFrame()
    for column in dataframe.columns:
        new_dataframe[(column + "-A", column)] = dataframe[column]
    return new_dataframe


def append_columns_to_compensated_dataframe(fcs_dataframe, new_columns_dataframe):
    '''
    Simple concatenation of dataframes
    '''
    if fcs_dataframe.shape[0] == new_columns_dataframe.shape[0]:
        new_dataframe = pd.concat([fcs_dataframe, new_columns_dataframe], axis=1)
    else:
        print("The number of rows in the FCS file and the labels column(s) do not match.\n")
        return -1
    return new_dataframe


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


def add_labels_to_FCS(fcs_file_path, spreadsheet_file_path, new_fcs_file_path):
    '''
    The spreadsheet data should contain column labels in the first row and integer data for the labels.
    '''
    fcs_data = return_FCS_as_compensated_dataframe(fcs_file_path)
    spreadsheet_data = return_spreadsheet_as_dataframe(spreadsheet_file_path)

    #If number of rows match, proceed
    if fcs_data.shape[0] == spreadsheet_data.shape[0]:
        nodes_columns = return_labels_with_fixed_column_names(spreadsheet_data)
        appended_fcs_dataframe = append_columns_to_compensated_dataframe(fcs_data, nodes_columns)
        write_dataframe_as_FCS_file(appended_fcs_dataframe, new_fcs_file_path)
    else:
        print("Error: The number of events in ", fcs_file_path, "and", spreadsheet_file_path, "do not match.\n")
        return -1


def add_labels_as_grid_to_FCS_CLI():
    '''
    Command line input entry point.
    '''
    args = sys.argv[1:]
    #print('count of args :: {}'.format(len(args)))
    #for arg in args:
    #    print('passed argument :: {}'.format(arg))

    if len(args) < 3:
        print("Error: Not enough arguments passed.  Required arguments are fcs_file_path, spreadsheet_file_path, and new_fcs_file_path.\n")
        return -1
    add_labels_as_grid_to_FCS(args[0], args[1], args[2])


def add_labels_to_FCS_CLI():
    '''
    Command line input entry point.
    '''
    args = sys.argv[1:]
    #print('count of args :: {}'.format(len(args)))
    #for arg in args:
    #    print('passed argument :: {}'.format(arg))

    if len(args) < 3:
        print("Error: Not enough arguments passed.  Required arguments are fcs_file_path, spreadsheet_file_path, and new_fcs_file_path.\n")
        return -1
    add_labels_to_FCS(args[0], args[1], args[2])

