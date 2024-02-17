import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('playlist_data.csv')

#Defining the function for a scatter plot
def plot_data( mydf: pd.DataFrame, xvar: str, yvar:str, fig_width: int, fig_length: int, title:str, xlabel: str, ylabel: str, legend: str):
    
    ''' Analyze and plot scatter data

    Generates a scatter plot and saves it as a pdf

    Parameters
    ----------
    mydf: pd.DataFrame, 
    xvar: str, 
    yvar:str, 
    fig_width: int, 
    fig_length: int, 
    title:str, 
    xlabel: str, 
    ylabel: str, 
    legend: str
        
    Returns
    -------
    pdf : matplotlib.Figure
    '''

    fig, ax = plt.subplots(figsize=(fig_width, fig_length))
    ax.scatter(mydf[xvar], mydf[yvar])
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(alpha=0.8)
    ax.legend(legend)

plt.savefig('Scatter_plot.pdf')

#Defining the function for a stripplot
def plot_data_stripplot( mydf: pd.DataFrame, xvar: str, yvar:str, hue: str): 
     ''' Analyze and plot stripplot data

    Generates a scatter plot and saves it as a pdf

    Parameters
    ----------
    mydf: pd.DataFrame,
    xvar: str, 
    yvar:str, 
    hue: str
        
    Returns
    -------
    pdf : Stripplot.pdf
    '''
    sns.stripplot(data=mydf, x=xvar, y=yvar, hue=hue)
    plt.xlabel(xvar)
    plt.ylabel(yvar)
   
plt.savefig('Stripplot.pdf')




