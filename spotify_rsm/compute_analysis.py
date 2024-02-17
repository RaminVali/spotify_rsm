import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import argparse
import yaml
import seaborn as sns

config_files = ['userconfig.yml']
config = {}
for this_config_file in config_files:
    with open(this_config_file, 'r') as yamlfile:
        this_config = yaml.safe_load(yamlfile)
        config.update(this_config)

def compute_analysis():
    '''Analyze previously-loaded data.

    This function runs an analytical measure of your choice (mean, median, linear regression, etc...)
    and returns the data in a format of your choice.

    Parameters
    ----------
    None

    Returns
    -------
    analysis_output : Any

    '''
    
    # Sonia's Analysis Function

    def correlation_analysis ():
        # insert docstring here 

        try:
            playlist_data = pd.read_csv(config['dataset'])
        except FileNotFoundError as e:
            e.add_note("There was an issue loading your dataset. Please check job and user configuration files.")
            raise e 
        playlist_data_explore_corr = playlist_data[config['columns_for_corr']]
        assert set(config['columns_for_corr']).issubset(set(playlist_data.columns.tolist())), "Error selecting columns for correlation analysis. Make sure your columns exist in the dataset."

        ax = sns.heatmap(playlist_data_explore_corr.corr(), annot=config['annotate_heatmap'])
        plt.savefig('playlist_data_correlation_heatmap.png')