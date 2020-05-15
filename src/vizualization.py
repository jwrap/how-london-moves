import matplotlib.pyplot as plt
import geopandas as gpd

def scatterplot(df, figsize=(16,12), resolution='ward', logx=False, logy=False, savefig=False, sharex=False):
    """Plot population vs amenities by category
    
    Args:
        df (DataFrame) : Amenities merged with population data
        figsize (tuple) : Figure size
        resolution (str) : Resolution
        logx (bool) : Set x scale to log 
        logy (bool) : Set y scale to log
        
    Returns:
        None
    
    """
    nrows = 3
    ncols = 4
    fig, ax = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize, sharex=sharex)
    k = 0
    index = df.index.tolist()

    for i in range(nrows):
        for j in range(ncols):
            x = df.loc["total_population"].div(1000)
            y = df.iloc[k]
            ax[i, j].scatter(x, y)
            ax[i, j].set_title(df.index[k])
            ax[i, j].set_xlabel('total_population')
            ax[i, j].set_title(f'{df.index[k].capitalize().replace("_", " ")}')
            ax[i, j].set_ylabel(f'Number of amenities in a {resolution}')
            ax[i, j].set_xlabel(f'Population per {resolution} (x1000)')
            if logx:
                ax[i, j].set_xscale('log')
            if logy:
                ax[i, j].set_yscale('log')
            k += 1
            if k == 10:
                break

    fig.delaxes(ax[2, 2])
    fig.delaxes(ax[2, 3])
    fig.tight_layout();
    if savefig:
        plt.savefig(f'../figures/scatter-{resolution}.png', dpi=300)
    
def choropleth(gdf, figsize=(20,20), cmap='viridis', resolution='ward',savefig=False):
    """Plot amenities types on map
    
    Args:
        gdf (GeoDataFrame) : Amenities data
        figsize (tuple) : Figure size
        cmap (str) : Color map
        
    Returns:
        None
    
    """
    nrows = 4
    ncols = 3
    fig, ax = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize, sharex=True)
    k = 0
    columns = ['nightlife',
               'mobility',
               'eatery',
               'community',
               'public_services',
               'culture_entertainment',
               'education',
               'wellbeing',
               'economic_activity',
               'family']
    for i in range(nrows):
        for j in range(ncols):
            gdf[gdf[columns[k]] > 0].to_crs(epsg=3857).plot(column=columns[k], ax=ax[i, j], legend=True, scheme='fisher_jenks', cmap=cmap)
            gdf[gdf[columns[k]] == 0].to_crs(epsg=3857).plot(color='gray', alpha=.5, ax=ax[i,j], linewidth=0.1, edgecolor='black')
            ax[i, j].set_title(f'{columns[k].capitalize().replace("_", " ")}')
            ax[i, j].axis('off')
            k += 1
            if k == 10:
                break

    fig.delaxes(ax[3, 1])
    fig.delaxes(ax[3, 2])
    fig.tight_layout();
    if savefig:
        plt.savefig(f'../figures/choropleth-{resolution}.png', dpi=300)