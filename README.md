# How London Moves
An exploratory analysis of urban amenities and travel behavior in Greater London.

## Introduction
The objective of this exercise was to understand if and how urban amenities affect travel behavior. It is understood that urban amenities (such as restaurants, parks, and community centers) play a role in defining the attractiveness of an area. Using points-of-interest data from OpenStreetMaps as well as open data from the [London Data Store](https://data.london.gov.uk) and [Transport for London](https://api-portal.tfl.gov.uk/docs), we were able to generate an overview of urban amenity distribution in relation to travel volumes around Greater London.

## Repo How-to
This repo is structured as follows:
```
├── data
│   ├── external                                  <- External data sets
│   ├── raw                                       <- Unprocessed data sets used for the analysis
│   ├── processed                                 <- Final data sets used for the analysis
│
├── figures                                       <- Figures generated
│
├── notebooks                
│   ├── 1-data-gathering-preprocessing.ipynb      <- Notebook for data pre-processing
│   ├── 2- exploratory-data-analysis.ipynb        <- Notebook for exploratory data analysis 
│
├── src                                           <- Standalone scripts used for data visualization
```

## Main findings

From the data we found that:

1. Areas in Central London contain a higher concentration of amenities (of all kinds) and attract a larger volume of travelers.
2. Incidences of eatery, nightlife and economic activity amenities are highly correlated.
3. Central London areas that attract a markedly larger volume of travelers than other peripheral areas contain more amenities on average, and substantially more eatery, nightlife and culture & entertainment amenities.

More here:
[Link to Medium post](https://medium.com)

## Contributors

If you are interested in the project, please, either fork it and submit a pull request, or contact us via Twitter or email.

_Jin Rui Yap_ [@jinruii](https://twitter.com/jinruii), _Mikhail Sirenko_ [@mikhailsirenko](https://twitter.com/mikhailsirenko)