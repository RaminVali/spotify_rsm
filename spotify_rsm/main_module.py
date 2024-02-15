from  load_data import load_data
from compute_analysis import compute_analysis
from notify_done import notify_done
from plot_data import plot_data

def main():
    """The main function that calls all the submodules and does the analysis, we will complete
    this once we get todays lesson."""

    ''' Load config into an Analysis object

    Load system-wide configuration from `configs/system_config.yml`, user configuration from
    `configs/user_config.yml`, and the specified analysis configuration file

    Parameters
    ----------
    analysis_config : str
        Path to the analysis/job-specific configuration file

    Returns
    -------
    analysis_obj : Analysis
        Analysis object containing consolidated parameters from the configuration files

    Notes
    -----
    The configuration files should include parameters for:
        * GitHub API token
        * ntfy.sh topic
        * Plot color
        * Plot title
        * Plot x and y axis titles
        * Figure size
        * Default save path

    '''

    load_data()
    compute_analysis()
    notify_done()
    plot_data()
    print('everything worked!')


main()