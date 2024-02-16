from  load_data import load_data
# from compute_analysis import compute_analysis
# from notify_done import notify_done
# from plot_data import plot_data

import pandas as pd
import logging
import yaml

config_paths = ['job_config.yml']

config = {}
for path in config_paths:
    with open(path, 'r') as f:
        this_config = yaml.safe_load(f)
        config.update(this_config)

logging.basicConfig (level = logging.INFO, filename='logging.log')

df = load_data(config['client_id'], config['client_secret'],config['playlist_url'])
print(df.head())



