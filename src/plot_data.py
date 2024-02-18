import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import ListedColormap
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True}) # avoiding the tick label cutoffs.


df = pd.read_csv('../data.csv')

# # Sonia's correlation plot
# Bring back the config file columns from usrconfig
def correlation_plot (df):
    '''Analyze previously-loaded data.

    This function calculates the correlation between all numerical 
    columns listed in columns_for_corr in userconfig.yml and generates a correlation plot

    Parameters
    ----------
    DataFrame object from load_data module, containing the track information for all the tracks in the playlist

    Returns
    -------
    analysis_output : correlation heatmap

    ''' 
   
    playlist_data_explore_corr = df[['popularity', 'danceability']]
    assert set(['popularity', 'danceability']).issubset(set(df.columns.tolist())), "Error selecting columns for correlation analysis. Make sure your columns exist in the dataset."
    sns.heatmap(playlist_data_explore_corr.corr(), annot=False)
    plt.autoscale()
    plt.savefig('playlist_data_correlation_heatmap.pdf')
    plt.title('Playlist Data Correlation')

# Melissa's plot:
def single_v_album_stripplot(df):
    '''Analyze previously-loaded data.

    This function uses a strip plot to analyze the contrast between single tracks, 
    albums and compilations.


    Parameters
    ----------
    DataFrame object from load_data module, containing the track information for all the tracks in the playlist
    mydf: pd.DataFrame,
    xvar: str, 
    yvar:str, 
    hue: str
        
    Returns
    -------
    pdf : Stripplot.pdf
   
    '''
    plt.figure()
    sns.stripplot(data=df, x='speechiness', y='album_album_type', hue='danceability')
    plt.xlabel('Speechiness')
    plt.savefig('single_v_album_analysis.pdf')


def artists_bar_plot(df):
    '''
    
    '''
    artists = df.artists.value_counts(ascending=True)[-11:].to_frame()
    fig, ax = plt.subplots()
    ax.barh(artists.index, artists['count'], color = 'g', edgecolor = 'b')
    ax.set_title('Top 10 Represented Artists in the Playlist')
    ax.set_xlabel('Number of tracks by the artist in the playlist')
    plt.savefig('artists_bar_plot.pdf')


# Ramin's 3d plot
def polularity_3d_plot(df):
    """
    
    """
    x = df['speechiness']/df['speechiness'].max()
    y = df['danceability']/df['danceability'].max()
    z = df['popularity']/df['popularity'].max()

    # axes instance
    fig = plt.figure(figsize=(6,6))
    ax = Axes3D(fig, auto_add_to_figure=False)
    fig.add_axes(ax)

    # get colormap from seaborn
    cmap = ListedColormap(sns.color_palette("rocket", 256).as_hex())

    # plot
    sc = ax.scatter(x, y, z, s=40, c=x, marker='o', cmap=cmap, alpha=1)
    ax.set_xlabel('Speechiness')
    ax.set_ylabel('Danceability')
    ax.set_zlabel('Popularity')

    # legend
    plt.legend(*sc.legend_elements(), bbox_to_anchor=(1.05, 1), loc=2)

    # save
    plt.savefig("Populalrity_3D.pdf", bbox_inches='tight')


def plot_data():
    correlation_plot(df)
    single_v_album_stripplot(df)
    artists_bar_plot(df)
    polularity_3d_plot(df)

plot_data()

