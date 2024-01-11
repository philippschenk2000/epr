# formalization & visualization
import warnings

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# Web scraping using Scrapy

# machine learning


def main():

    warnings.filterwarnings("ignore")
    pd.set_option('expand_frame_repr', False)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)

    data = pd.read_csv('csv_data/sunroof_solar.csv')
    print(data.head())

    correl = correl2(data)


    return data


def correl2(data):

        corr = data.corr(method='pearson')
        plt.figure(figsize=(20, 6))
        sns.heatmap(corr, annot=True, cmap='Blues')
        plt.title('Correlation matrix')
        plt.show()

        pal=sns.color_palette('viridis', n_colors=10, as_cmap=True)
        sns.scatterplot(x='lng_avg', y='lat_avg', s=3, data=data, palette=pal, hue='yearly_sunlight_kwh_w', cmap='Blues', vmin=2000, vmax=5500)
        plt.show()

        sns.set()
        cols = ['lng_avg', 'lat_avg', 'yearly_sunlight_kwh_f', 'yearly_sunlight_kwh_n', 'yearly_sunlight_kwh_s', 'yearly_sunlight_kwh_e']
        sns.pairplot(data[cols], size=3)
        plt.show()


main()





