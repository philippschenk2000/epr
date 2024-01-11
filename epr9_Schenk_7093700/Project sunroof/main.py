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
    laender = ['AT', 'SI','BE', 'BG', 'CH', 'CY', 'CZ', 'DE', 'DK', 'EE','EL', 'ES', 'FI', 'FR', 'HU', 'IE', 'IT', 'LU', 'LV', 'LT', 'NL', 'NO', 'PL', 'PT', 'RO', 'SE', 'SI', 'SK', 'UK']



    LAND = 'DE'
    PLZ = 60528
    LAND_PLZ = str(LAND) + str(PLZ)

    #'''
    europe = pd.read_csv('csv_data/ALL_EU_states.csv')
    #europe['PV_FLAECHE'] = europe['PV_FLAECHE'].replace['"','']
    german_data3 = german_dataset3(europe, LAND_PLZ)
    correl = correl1(europe)
    #'''


    '''
    german_data = german_dataset(laender, LAND)
    german_data2 = german_dataset2(german_data, PLZ, LAND_PLZ)
    correl = correl2(german_data2)
    #'''


def correl1(europe):

    corr = europe.corr(method='pearson')
    plt.figure(figsize=(20, 6))
    sns.heatmap(corr, annot=True, cmap='Blues')
    plt.title('Correlation matrix')
    plt.show()

    pal=sns.color_palette('viridis', n_colors=10, as_cmap=True)
    sns.scatterplot(x='LNG', y='LAT', s=4.5, data=europe, palette=pal, hue='SUN1', cmap='Blues', vmin=2000, vmax=5500)
    plt.show()

    sns.set()
    cols = ['LAT', 'LNG', 'SUN1']
    sns.pairplot(europe[cols], size=3)
    plt.show()




def german_dataset(laender, LAND):

    df = pd.DataFrame()
    LAND1 = LAND
    nuts0 = []
    nuts1 = []
    nuts2 = []
    nuts3 = []
    plz = []
    plz1 = []
    for LAND in laender:
        if LAND1 not in laender:
            print('Das Land "{}" ist noch nicht in unserer Datenbank'.format(LAND))
            break
        df1 = pd.read_csv('csv_data/NUTS/pc2020_{}_NUTS-2021_v1.0.csv'.format(LAND), delimiter=';')
        for x in df1['NUTS3']:
            nuts3.append(x[1:6])
            nuts2.append(x[1:5])
            nuts1.append(x[1:4])
            nuts0.append(x[1:3])
        for x in df1['CODE']:
            if LAND == 'UK':
                x = x.split(' ')
                x = x[0]
                plz.append(x[1:])
            elif LAND == 'NL':
                plz.append(x[1:5])
            elif LAND == 'PT':
                plz.append(x[1:5])
            else:
                plz.append(x[1:-1])
        df = df.append(df1)
        plz1.append(plz)
    df['NUTS3'] = nuts3
    df['NUTS2'] = nuts2
    df['NUTS2'] = df['NUTS2'].replace('LU00', 'LU')
    df['NUTS2'] = df['NUTS2'].replace('EE00', 'EE')
    df['NUTS2'] = df['NUTS2'].replace('LV00', 'LV')
    df['NUTS2'] = df['NUTS2'].replace('LT01', 'LT')
    df['NUTS2'] = df['NUTS2'].replace('LT02', 'LT')
    df['NUTS2'] = df['NUTS2'].replace('SI03', 'SI')
    df['NUTS2'] = df['NUTS2'].replace('SI04', 'SI')
    df['NUTS1'] = nuts1
    df['LAND'] = nuts0
    df['PLZ'] = plz
    df['LAND_PLZ'] = df['LAND']+df['PLZ']
    del df['CODE']

    latlong1 = pd.DataFrame()
    for LAND in laender:
        if LAND == 'EL':
            latlong = pd.read_table('csv_data/GEOCOORD/{}.txt'.format(LAND), delimiter=',')
            latlong['LAND'] = 'EL'
            latlong['BUNDESLAND'] = 'EL'
            latlong['PLZ'] = latlong['PLZ'].astype(str)
        else:
            latlong = pd.read_table('csv_data/GEOCOORD/{}.txt'.format(LAND), header=None)
            latlong.rename(columns={0: 'LAND', 1: 'PLZ', 2: 'STADT', 3: 'BUNDESLAND', 8: 'VORWAHL', 9: 'LAT', 10: 'LNG'}, inplace=True)
            del latlong[4], latlong[5], latlong[6], latlong[7], latlong[11], latlong['VORWAHL']
        latlong['PLZ'] = latlong['PLZ'].astype(str)
        latlong['PLZ'] = latlong['PLZ'].drop_duplicates(keep='first')
        latlong['PLZ'] = latlong['PLZ'].astype(str)
        latlong = latlong.loc[latlong['PLZ'] != 'nan']

        if LAND == 'UK':
            latlong['LAND'] = latlong['LAND'].replace(['GB'], 'UK')

        xxx = []
        for i in latlong['PLZ']:
            i = i.replace(' CEDEX', '')
            if LAND == 'UK':
                i = i
            else:
                if len(i) == 4:
                    i = '0'+i
                elif len(i) == 3:
                    i = '00'+i
                elif len(i) == 2:
                    i = '000'+i
                elif len(i) == 1:
                    i = '0000'+i
                else:
                    i = i
                if LAND == 'BE' or LAND == 'AT' or LAND == 'BG' or LAND == 'CH' or LAND == 'CY' or LAND == 'DK' or LAND == 'HU' or LAND == 'LI' or LAND == 'MK' or LAND == 'NO' or LAND == 'SI' or LAND == 'DK' or LAND == 'NL':
                    i = i[1:]
                elif LAND == 'MT' or LAND == 'IE' or LAND == 'IS' or LAND == 'LU':
                    i = i[2:]
                elif LAND == 'RO':
                    if len(i) == 5:
                        i = '0'+i
                elif LAND == 'FR':
                    i = i.split(' ')
                    i = i[0]
                elif LAND == 'PT':
                    i = i[:4]

            xxx.append(i)
        latlong['PLZ'] = xxx

        latlong['LAND_PLZ'] = latlong['LAND'] + latlong['PLZ'].astype(str)
        latlong1 = latlong1.append(latlong, ignore_index=True)
    df = df.drop_duplicates(keep='first')


    del df['LAND'], df['PLZ']
    df1 = pd.merge(latlong1, df, on='LAND_PLZ', how='left')

    country_codes = pd.read_csv('csv_data/energy_data/country_codes.csv')
    del country_codes['alpha-3'], country_codes['iso_3166-2'], country_codes['region'], country_codes['sub-region'], country_codes['intermediate-region'], country_codes['region-code'], country_codes['sub-region-code'], country_codes['intermediate-region-code']
    df = pd.merge(df1, country_codes, on='LAND', how='left')

    net_installed_capacity_of_electric_power_plants_public_solar = pd.read_csv('csv_data/energy_data/UNdata_Export_20221113_215209962.txt', delimiter=';')
    del net_installed_capacity_of_electric_power_plants_public_solar['Commodity - Transaction'], net_installed_capacity_of_electric_power_plants_public_solar['Year'], net_installed_capacity_of_electric_power_plants_public_solar['Quantity Footnotes'], net_installed_capacity_of_electric_power_plants_public_solar['Unit']
    df = pd.merge(df, net_installed_capacity_of_electric_power_plants_public_solar, on='NAME', how='left')

    total_solar = pd.read_csv('csv_data/energy_data/UNdata_Export_20221113_215348121.txt', delimiter=';')
    del total_solar['Commodity - Transaction'], total_solar['Year'], total_solar['Quantity Footnotes'], total_solar['Unit']
    df = pd.merge(df, total_solar, on='NAME', how='left')

    installed = pd.read_csv('csv_data/energy_data/UNdata_Export_20221113_220643718.txt', delimiter=';')
    del installed['Year']
    df = pd.merge(df, installed, on='NAME', how='left')

    cities = pd.read_csv('csv_data/energy_data/city_level_NUTS2.csv')
    del cities['TIME'], cities['GEO_LABEL'], cities['UNIT'], cities['LANDCOVER'], cities['Flag and Footnotes']
    df = pd.merge(df, cities, on='NUTS2', how='left')
    df['STADT_LEVEL'] = df['STADT_LEVEL'].astype(float)

    emissions = pd.read_csv('csv_data/energy_data/emissions.csv')
    emissions = emissions.loc[emissions['TIME_PERIOD'] == 2020]
    del emissions['DATAFLOW'], emissions['LAST UPDATE'], emissions['freq'], emissions['unit'], emissions['OBS_FLAG'], emissions['TIME_PERIOD']
    df = pd.merge(df, emissions, on='LAND', how='left')

    prices = pd.read_csv('csv_data/energy_data/energy_prices1.csv')
    prices = prices.loc[prices['TIME_PERIOD'] == 2021]
    del prices['DATAFLOW'], prices['LAST UPDATE'], prices['freq'], prices['product'], prices['currency'], prices['indic_en'], prices['unit'], prices['TIME_PERIOD'], prices['OBS_FLAG']
    df = pd.merge(df, prices, on='LAND', how='left')

    flaeche = pd.read_csv('csv_data/energy_data/nrg_inf_stcs_1_Data.csv')
    flaeche = flaeche.loc[flaeche['TIME'] == 2020]
    del flaeche['TIME'], flaeche['PLANT_TEC'], flaeche['UNIT'], flaeche['Flag and Footnotes']
    df = pd.merge(df, flaeche, on='NAME', how='left')

    dichte = pd.read_csv('csv_data/energy_data/population_density.csv')
    dichte = dichte.loc[dichte['TIME_PERIOD'] == 2018]
    del dichte['DATAFLOW'], dichte['LAST UPDATE'], dichte['freq'], dichte['unit'], dichte['TIME_PERIOD'], dichte['OBS_FLAG']
    df = pd.merge(df, dichte, on='NUTS2', how='left')
    df['POP_DICHTE'] = df['POP_DICHTE'].astype(float)

    solar_prod = pd.read_csv('csv_data/energy_data/solar_energy_prod.csv')
    solar_prod = solar_prod.loc[solar_prod['TIME'] == 2020]
    del solar_prod['TIME'], solar_prod['SIEC'], solar_prod['UNIT'], solar_prod['Flag and Footnotes'], solar_prod['NRG_BAL']
    df = pd.merge(df, solar_prod, on='NAME', how='left')

    df = df.drop_duplicates(keep='first')
    df['LAND_PLZ'] = df['LAND_PLZ'].astype(str)
    df['LAND_PLZ'] = df['LAND_PLZ'].drop_duplicates(keep='first')
    df['LAND_PLZ'] = df['LAND_PLZ'].astype(str)
    df = df.loc[df['LAND_PLZ'] != 'nan']
    df = df.reset_index()
    del df['index']

    with open('df.textmate', 'w') as file:
        file.write(str(df) + '\n')

    return df


def german_dataset2(german_data, PLZ, LAND_PLZ):

    df1 = pd.read_csv('csv_data/EMHIRES_PVGIS_TSh_CF_n2.csv')
    df1 = df1.reset_index()
    df1.rename(columns={'FR42': 'FRF1','FR61': 'FRI1','FR72': 'FRK1','FR25': 'FRD1','FR26': 'FRC1','FR52': 'FRH0','FR24': 'FRB0','FR21': 'FRF2','FR83': 'FRM0','FR43': 'FRC2','FR23': 'FRD2','FR10': 'FR10','FR81': 'FRJ1','FR63': 'FRI2','FR41': 'FRF3','FR62': 'FRJ2','FR30': 'FRE1','FR51': 'FRG0','FR22': 'FRE2','FR53': 'FRI3','FR82': 'FRL0','FR71': 'FRK2'}, inplace=True)
    df1.rename(columns={'IE02': 'IE05','IE01': 'IE04'}, inplace=True)
    df1.rename(columns={'NO01': 'NO01', 'NO0A': 'NO03', 'NO08': 'NO04', 'NO06': 'NO02', 'NO05': 'NO09'}, inplace=True)
    df1.rename(columns={'SE11 ': 'SE11'}, inplace=True)
    df1.rename(columns={'UKI3UKI4 ': 'UKI3', 'UKI5UKI6 ': 'UKI5'}, inplace=True)

    df2 = pd.read_csv('csv_data/EMHIRESPV_TSh_CF_Country_19862015.csv')
    df2 = df2[len(df2)-len(df1):]
    df2 = df2.reset_index()
    df2['CY'] = df2['CY'].astype(float)*1.25
    df1['SE33'] = df1['SE33'].astype(float)
    df1['LT'] = df2['LT'].astype(float)*1.25
    df1['LU'] = df2['LU'].astype(float)*1.25
    df1['LV'] = df2['LV'].astype(float)*1.25
    df1['EE'] = df2['EE'].astype(float)*1.25
    df1['SI'] = df2['SI'].astype(float)*1.25

    df1['SE11'] = df1['SE11'].astype(float)
    del df1['time_step']
    df1 = df1.loc[df1['year'] > 2012]

    sun1 = []
    for i in range(0, len(german_data['NUTS2'])):
        y = german_data['NUTS2'][i]
        if y in df1.columns:
            xx = sum(df1[str(y)])
            if xx > 0:
                sun1.append(xx)
            else:
                sun1.append(2000)
        else:
            sun1.append(None)

    german_data['SUN1'] = sun1

    german_data = german_data.sort_values(['LAT', 'LNG'], ascending=[True, True])
    german_data.fillna(method='ffill', inplace=True)
    german_data.fillna(method='bfill', inplace=True)
    german_data = german_data.sort_values(['LAND', 'PLZ'], ascending=[True, False])

    your_location = german_data.loc[german_data['LAND_PLZ'] == LAND_PLZ]
    print(your_location)
    nuts2 = your_location['NUTS2'].tolist()
    if len(nuts2) > 0:
        nuts2 = nuts2[0]
    else:
        print('Die PLZ ist ungültig')
    print('Das Solar-Potential wrd für die PV-Anlage berechnet....')
    with open('df1.textmate', 'w') as file:
        file.write(str(german_data) + '\n')
    german_data.to_csv('csv_data/ALL_EU_states2.csv', index=False)


    return german_data


def german_dataset3(german_data, LAND_PLZ):

    german_data1 = german_data.loc[german_data['LAND_PLZ'] == LAND_PLZ]
    print(german_data1)

    return german_data


def correl2(german_data2):

    corr = german_data2.corr(method='pearson')
    plt.figure(figsize=(20, 6))
    sns.heatmap(corr, annot=True, cmap='Blues')
    plt.title('Correlation matrix')
    plt.show()

    pal=sns.color_palette('viridis', n_colors=10, as_cmap=True)
    sns.scatterplot(x='LNG', y='LAT', s=3, data=german_data2, palette=pal, hue='SUN1', cmap='Blues', vmin=2000, vmax=5500)
    plt.show()

    sns.set()
    cols = ['LAT', 'LNG', 'SUN1']
    sns.pairplot(german_data2[cols], size=3)
    plt.show()


main()
