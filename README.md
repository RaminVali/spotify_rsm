# spotify_rsm
Simple team repository for DSI BRS Assignment

## Table of contents
* [General info] (#general-info)
* [Technologies] (#technologies)
* [Setup] (#setup)

## General info
This project is simple analysis that generates different kind of plots based on a Spotify Playlist

## Technologies
Project is created with:
* Python 3.11.5
* Bash Command

## Setup
To run this project, install it locally using: 
!pip install git+https://github.com/RaminVali/spotify_rsm
from setup.py import Analysis

analysis_obj = Analysis.Analysis('config.yml')
analysis_obj.load_data()

analysis_output = analysis_obj.compute_analysis()
print(analysis_output)

analysis_figure = analysis_obj.plot_data()
