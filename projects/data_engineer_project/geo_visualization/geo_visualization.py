import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.patches import Patch
from matplotlib.font_manager import FontProperties

from matplotlib import rc
%matplotlib inline
from matplotlib import font_manager

# 한글 폰트 위치
f_path = "C:/windows/Fonts/malgun.ttf"
font_manager.FontProperties(fname=f_path).get_name()


# Define color map
color_map = {
    'cluster00': '#ff1f1f',  # Light red
    'cluster01': '#2045fa',  # Light blue
    'cluster02': 'green',
    'cluster03': 'purple',
    'cluster04': 'orange',
}

# Define file paths
shp_file = 'sig.shp'

# Load the shapefile
gdf = gpd.read_file(shp_file, encoding='euc-kr')

# Convert 'SIG_CD' to string
gdf['SIG_CD'] = gdf['SIG_CD'].astype(str)

# Load each cluster file and add the color to the geodataframe
for i in range(5):
    cluster = pd.read_csv(f'cluster0{i}.csv', encoding='cp949')
    cluster['SIG_CD'] = cluster['SIG_CD'].astype(str)
    gdf.loc[gdf['SIG_CD'].isin(cluster['SIG_CD']), 'color'] = color_map[f'cluster0{i}']

# Assign gray color to the regions that do not belong to any cluster
gdf['color'].fillna('gray', inplace=True)

#plt.rcParams['font.family'] = 'Arial'
rc('font', family='Malgun Gothic')

fig, ax = plt.subplots(1, 1, figsize=(14, 14))  # Increase the figure size

# Plot the geodataframe with colors assigned to each cluster
gdf.plot(color=gdf['color'], ax=ax, edgecolor='white')  # Add white edge color

# Hide axes and borders
ax.axis('off')
for spine in ax.spines.values():
    spine.set_visible(False)

# Define font properties for the legend
font = FontProperties()
font.set_family('serif')
font.set_name('Arial')
font.set_size(14)
    
# Define legend elements
legend_elements = [Patch(facecolor=color_map[f'cluster0{i}'], edgecolor='white', label=f'Cluster0{i}') for i in range(5)]

# Add the legend to the plot
ax.legend(handles=legend_elements, loc='upper right', bbox_to_anchor=(1, 1), prop=font)

# Adjust the plot margins
plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
plt.title('군집 분포 지도')

# Save the figure
plt.savefig('result_of_clustering.png', bbox_inches='tight')

plt.show()
