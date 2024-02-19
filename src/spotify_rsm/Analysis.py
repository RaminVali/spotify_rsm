from src.spotify_rsm.load_data import load_data
from src.spotify_rsm.compute_analysis import compute_analysis
from src.spotify_rsm.plot_data import plot_data

# import load_data
# import compute_analysis
# import plot_data

from typing import Optional
import matplotlib.pyplot as plt
import yaml
import requests
import pandas as pd
import logging
import matplotlib.pyplot as plt
import os



logging.basicConfig (level = logging.INFO, filename='logs/logging.log')


class Analysis:
    def __init__(self, analysis_config: str) -> None:
        CONFIG_PATHS = ['configs/system_config.yml', 'configs/user_config.yml']

        # add the analysis config to the list of paths to load
        paths = CONFIG_PATHS + [analysis_config]

        # initialize empty dictionary to hold the configuration
        config = {}

        # load each config file and update the config dictionary
        for path in paths:
            with open(path, 'r') as f:
                this_config = yaml.safe_load(f)
            config.update(this_config)
        self.config = config

    def load_data(self) -> pd.DataFrame:
        #data = requests.get('/url/to/data').json()
        self.data = load_data(self.config)
        return self.data
        

    def compute_analysis(self) -> pd.DataFrame:
        output = compute_analysis(self.data)
        return output


    def plot_data(self, save_path: Optional[str]=None) -> plt.Figure:
        if save_path:
            os.mkdir(save_path)
        plot_data(self.data, save_path, self.config)
        plt.show()
        plt.show()
        plt.show()
        plt.show()


    def notify_done(self, message='Your Spotify data analysis is now complete.') -> None:
        ''' Notify the user that analysis is complete.

        Send a notification to the user through the ntfy.sh webpush service.

        Important Note
        ---------------
        You must subscribe to the specified topic name in ntfy.sh! 
        See topicname in userconfig.yml for this module's topic name.

        Parameters
        ----------
        message : str
        Text of the notification to send

        Returns
        -------
        None

        '''
        
        requests.post(f"https://ntfy.sh/{self.config['topicname']}", 
            data=message.encode(encoding='utf-8'))
        

### Running in concole:
# analysis_object = Analysis('../configs/analysis_config.yml')
# analysis_object.load_data()
# analysis_output = analysis_object.compute_analysis()
# print(analysis_output)
# analysis_object.notify_done()
# analysis_object.plot_data() # sample path: '../img2/'


