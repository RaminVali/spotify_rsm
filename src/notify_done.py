import requests 
import yaml

config_files = ['../src/userconfig.yml']
config = {}
for this_config_file in config_files:
    with open(this_config_file, 'r') as yamlfile:
        this_config = yaml.safe_load(yamlfile)
        config.update(this_config)

def notify_done():

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
    message = 'Your Spotify data analysis is now complete.'
    
    requests.post(f"https://ntfy.sh/{config['topicname']}", 
        data=message.encode(encoding='utf-8'))