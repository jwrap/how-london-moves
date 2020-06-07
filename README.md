[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jwrap/how-london-moves/master)

# How London Moves
Exploratory data analysis of urban amenities and travel behavior in Greater London

## Introduction
The objective of this exercise was to understand if and how urban amenities affect travel behavior. It is understood that urban amenities (such as restaurants, parks, and community centers) play a role in defining the attractiveness of an area. Using points-of-interest data from OpenStreetMaps as well as open data from the [London Data Store](https://data.london.gov.uk) and [Transport for London](https://api-portal.tfl.gov.uk/docs), we were able to generate an overview of urban amenity distribution in relation to travel volumes around Greater London.

Read more about the project in our [article](https://medium.com) on Medium.

## How to use this repo
You can easily reproduce the whole project by rerunning two Jupyter Notebooks sequentially on your machine. To use visualization scripts from the src folder do the following: 1). download setup.py file and put into the project directory 2). run `pip install editable .` command in Anaconda prompt in the project directory (the dot at the end is important). This command will turn the project folder in a Python package and make scripts from src folder easily accessible. Read more about this "trick" [here](https://godatadriven.com/blog/write-less-terrible-code-with-jupyter-notebook/).

Alternatively, launch the repo with MyBinder by clicking on the binder bage from the top of the page. 

This repo is structured as follows:
```
├── data
│   ├── external                                  <- External data sets
│   ├── processed                                 <- Final preprocessed data sets used for the analysis
│   ├── raw                                       <- Unprocessed data sets used for the analysis
│
├── figures                                       <- Generated figures
│
├── notebooks                
│   ├── 1-data-gathering-preprocessing.ipynb      <- Notebook with the code for data gathering and preprocessing
│   ├── 2-exploratory-data-analysis.ipynb         <- Notebook used for exploratory data analysis 
│
├── src                                           <- Standalone scripts used for data visualization
```

## Main findings

1. Areas in Central London contain a higher concentration of amenities (of all kinds) and attract a larger volume of travelers.
2. Incidences of eatery, nightlife and economic activity amenities are highly correlated.
3. Central London areas that attract a markedly larger volume of travelers than other peripheral areas contain more amenities on average, and substantially more eatery, nightlife and culture & entertainment amenities.

## Authors

_Jin Rui Yap_ [@jinruii](https://twitter.com/jinruii), _Mikhail Sirenko_ [@mikhailsirenko](https://twitter.com/mikhailsirenko), _Trivik Verma_ [@TrivikV](https://twitter.com/TrivikV).

## Refernces
1. London Datastore (2019). Statistical GIS Boundary Files for London. Retrieved from https://data.london.gov.uk/dataset/statistical-gis-boundary-files-london
2. Office for National Statistics (2019). Census Output Area population estimates – London, England (supporting information). Retrieved from https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationestimates/datasets/censusoutputareaestimatesinthelondonregionofengland
3. Geofabrik (2020). Download OpenStreetMap data for this region: England. Retrieved from http://download.geofabrik.de/europe/great-britain/england/greater-london.html.
