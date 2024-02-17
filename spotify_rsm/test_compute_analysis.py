import pytest
import compute_analysis as mycode
import os
import yaml
import pandas as pd 


config_files = ['userconfig.yml']
config = {}
for this_config_file in config_files:
    with open(this_config_file, 'r') as yamlfile:
        this_config = yaml.safe_load(yamlfile)
        config.update(this_config)


# Sonia's unit test for scatter plot
def test_correlation_analysis():
    input = pd.read_csv(config['dataset'])
    mycode.correlation_analysis(input)
    # exp_output = os.path.isfile('playlist_data_correlation_heatmap.png')

    assert os.path.isfile('playlist_data_correlation_heatmap.png'), "Correlation heatmap not created."
