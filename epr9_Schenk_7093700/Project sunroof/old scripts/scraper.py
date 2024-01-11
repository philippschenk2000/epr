# math & other stuff
import datetime as datetime
import re
import warnings

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# formalization & visualization
import seaborn as sns
from sklearn import linear_model
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.ensemble import GradientBoostingRegressor, AdaBoostRegressor, BaggingRegressor, RandomForestRegressor
from sklearn.ensemble import RandomForestClassifier
from sklearn.inspection import permutation_importance
# machine learning
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import Perceptron
from sklearn.linear_model import SGDClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVC, LinearSVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor


# Web scraping using Scrapy


def main():

    warnings.filterwarnings("ignore")
    pd.set_option('expand_frame_repr', False)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    urls = []
    filled_data = pd.DataFrame()
    profiles_with_offerings = pd.DataFrame()
    agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0',
        'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
        'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
        'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
        'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
        'AppleWebKit/537.36 (KHTML, like Gecko)',
        'Chrome/63.0.3239.132 Safari/537.36',
        'Mozilla/5.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7',
        'Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:16.0) Gecko/16.0 Firefox/16.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10']


    # FIRST PHASE - OLD USER DATA
    # get all the data for profiles.csv in November --> lock it in January and unlock it in November
    #''' <-- # !!!
    start_page = 1
    end_page = 5
    '''for i in range(0, 1):
        # Creating search urls
        for i in range(start_page, end_page):
            urls.append("http://api.scraperapi.com?api_key=cf1dfe285ad7b62e5387b4ad6e3fe1b5&url=https://www.ebay-kleinanzeigen.de/s-hessen/seite:{}/apple/k0l4279".format(i))
        profileurls = []
        # Finding the offer urls
        for i in urls:

             # lock this for the testing phase:
            user_agent = choice(agents)
            headers = {'User-Agent': user_agent}
            html = requests.get(url=i, headers=headers).content
            sel = Selector(text=html)
            getofferurls = getofferurl(sel)

            print('Die Anzeigen und deren dazugehörigen User werden sich von folgender Seite angeschaut...')
            print(i)
            # Finding for each offer-url the user-url
            for i in getofferurls:

                html = requests.get(url=i, headers=headers).content
                sel = Selector(text=html)
                profiles = sel.css('html body#vap div.site-base div.site-base--content div#site-content.l-page-wrapper.l-container-row section#viewad-main.l-container-row section#viewad-cntnt.l-row.a-double-margin.l-container-row aside#viewad-sidebar.a-span-8.l-col div#viewad-profile-box.l-container-row.contentbox--vip.no-shadow.j-sidebar-content div#viewad-contact div.l-container-row ul.iconlist li span.iconlist-text span.text-body-regular-strong.text-force-linebreak a::attr(href)').extract()
                if len(profiles) > 0:
                    y = ('http://api.scraperapi.com?api_key=cf1dfe285ad7b62e5387b4ad6e3fe1b5&url=https://www.ebay-kleinanzeigen.de' + profiles[0])
                    #y = 'http://api.scraperapi.com?api_key=cf1dfe285ad7b62e5387b4ad6e3fe1b5&url=https://www.ebay-kleinanzeigen.de/s-bestandsliste.html?userId=124149050'
                    profileurls.append(y)
                    # Scraping for each user-url with an offer from the search all profile data
                    for f in range(0, 1):
                        i = y
                        name1 = []; paymentdetails1 = []; usertype1 = []; offeringsonline1 = []; offeringssum1 = []; profilerating1 = []; profilefriendliness1 = []
                        profilereliability1 = []; profilereplyrate1 = []; profilereplyspeed1 = []; profilefollowers1 = []; offernames1 = []; location1 = []
                        description1 = []; prices1 = []; offerdates1 = []; shipping1 = []; start1 = []
                        user_agent = choice(agents)
                        headers = {'User-Agent': user_agent}
                        html = requests.get(url=i, headers=headers).content
                        sel = Selector(text=html)
                        # now we want to get all data scraped for this one user / data filtering
                        profildata = getprofiles(sel, i, name1, paymentdetails1, usertype1, offeringsonline1, offeringssum1, profilerating1, profilefriendliness1, profilereliability1, profilereplyrate1, profilereplyspeed1, profilefollowers1, offernames1, location1, description1, prices1, offerdates1, shipping1, start1)
                        df = profildata
                        # write it in csv / data filtering
                        df2 = pd.read_csv('csv_data/profiles.csv')
                        df2 = df2.append(df, ignore_index=True)
                        df2.to_csv('csv_data/profiles.csv', index=False) 

                        for i in range(0, 1):
                            df_profiles = pd.read_csv('csv_data/profiles.csv')
                            with open('1:df_profiles.textmate', 'w') as file:
                                file.write(str(df_profiles) + '\n')
                            # string to ints or floats / preprocessing
                            edited_profiles = editprofiledata(df_profiles)
                            with open('1:new_df_profiles.textmate', 'w') as file:
                                file.write(str(edited_profiles) + '\n')
                            # fill the missing data / prepocessing
                            filled_data = filledprofiledata(edited_profiles)
                            filled_data = filled_data.drop_duplicates(keep='first')
                            with open('1:filled_df_profiles.textmate', 'w') as file:
                                file.write(str(filled_data) + '\n')
                            profiles_with_offerings = filled_data.loc[filled_data['offeringsonline'] > 0]
                            with open('1:profiles_with_offerings.textmate', 'w') as file:
                                file.write(str(filled_data) + '\n')
                            profiles_with_offerings.to_csv('csv_data/profiles_old.csv', index=False)

                sleeptime = float(randint(0, 0))
                sleep(sleeptime)
    # '''


    # SECOND PHASE - STILL EXISTING USER DATA
    # get all the data for profiles_checked.csv in January --> lock it in November and unlock it in January
    ''' <-- # !!!
    df_new = pd.read_csv('csv_data/profiles_old.csv')
    df_old = pd.read_csv('csv_data/profiles_checked.csv')
    for i in range(0, 1):
        getofferurls = df_new['user-ID'][len(df_old):]
        profileurls = []
        for i in getofferurls:
            #i = 34965325
            y = ('http://api.scraperapi.com?api_key=cf1dfe285ad7b62e5387b4ad6e3fe1b5&url=https://www.ebay-kleinanzeigen.de/s-bestandsliste.html?userId={}'.format(i))
            profileurls.append(y)

            # Scraping for each user-url with an offer from the search all profile data
            for f in range(0, 1):
                i = y
                name1 = []; paymentdetails1 = []; usertype1 = []; offeringsonline1 = []; offeringssum1 = []; profilerating1 = []; profilefriendliness1 = []
                profilereliability1 = []; profilereplyrate1 = []; profilereplyspeed1 = []; profilefollowers1 = []; offernames1 = []; location1 = []
                description1 = []; prices1 = []; offerdates1 = []; shipping1 = []; start1 = []
                user_agent = choice(agents)
                headers = {'User-Agent': user_agent}
                html = requests.get(url=i, headers=headers).content
                sel = Selector(text=html)
                # now we want to get all data scraped for this one user / data filtering
                profildata = getprofiles(sel, i, name1, paymentdetails1, usertype1, offeringsonline1, offeringssum1, profilerating1, profilefriendliness1, profilereliability1, profilereplyrate1, profilereplyspeed1, profilefollowers1, offernames1, location1, description1, prices1, offerdates1, shipping1, start1)
                df = profildata
                # write it in csv / data filtering
                df2 = pd.read_csv('csv_data/profiles_checked.csv')
                df2 = df2.append(df, ignore_index=True)
                df2.to_csv('csv_data/profiles_checked.csv', index=False) # --> unlock this for the testing phase


            sleeptime = float(randint(6, 10))
            sleep(sleeptime)
    #'''


    # THIRD & FOURTH PHASE - ANALYSIS - COMPARING & PREDICTING
    # data analysis of the old user vs. the still existing user
    #'''
    for i in range(0, 1):
        df_profiles = pd.read_csv('csv_data/profiles.csv')
        with open('3:df_profiles_checked.textmate', 'w') as file:
            file.write(str(df_profiles) + '\n')
        # string to ints or floats / preprocessing
        edited_profiles = editprofiledata(df_profiles)
        with open('3:new df_profiles_checked.textmate', 'w') as file:
            file.write(str(edited_profiles) + '\n')
        # fill the missing data / prepocessing
        filled_data = filled_data.drop_duplicates(keep='first')
        filled_data = filledprofiledata(edited_profiles)
        with open('3:filled df_profiles_checked.textmate', 'w') as file:
            file.write(str(filled_data) + '\n')


        profiles_old = pd.read_csv('csv_data/profiles_old.csv')
        profiles_new = filled_data
        filled_data = combine_both(profiles_new, profiles_old)
        with open('3:profiles_with_offerings_checked.textmate', 'w') as file:
            file.write(str(filled_data) + '\n')


        # data analysis / analysis
        Trainingsvolumen = 150
        Testvolumen = 70
        del filled_data['offernames'], filled_data['description'], filled_data['prices'], filled_data['offerdates'], filled_data['name']
        filled_data = data_cleaning(filled_data)
        correl0 = analysis_correl(filled_data)


        '''
        for x in range(0, 1):
            X_testt = analysis_test(filled_data, Trainingsvolumen, Testvolumen)
            df_statistics0 = df_stats0(X_testt)
            with open('4:Infos Testset.textmate', 'w') as file:
                file.write(str(df_statistics0) + '\n')
            dataset = analysis_train(filled_data, Trainingsvolumen)
            df_statistics = df_stats(dataset)

            i = int(len(dataset))
            data = dataset
            results = predictions(data, i, X_testt, df_statistics, df_statistics0)
            with open('4:results.textmate', 'w') as file:
                file.write(str(results) + '\n')
            corr = correlation2(results)
    # '''




def getofferurl(sel):

    links = []
    link = sel.css('a.ellipsis::attr(href)').extract()
    for x in link:
        x = 'http://api.scraperapi.com?api_key=cf1dfe285ad7b62e5387b4ad6e3fe1b5&url=https://www.ebay-kleinanzeigen.de' + x
        links.append(x)

    return links


def getprofiles(sel, i, name1, paymentdetails1, usertype1, offeringsonline1, offeringssum1, profilerating1, profilefriendliness1, profilereliability1, profilereplyrate1, profilereplyspeed1, profilefollowers1, offernames1, location1,  description1, prices1, offerdates1, shipping1, start1):

    userid = []
    for j in range(0, 1):
        if len(sel.css('html body#pstrads div.site-base div.site-base--content div#site-content.l-page-wrapper.l-container-row div.l-splitpage-flex div.l-splitpage-navigation section.l-container-row.contentbox.surface.userprofile.j-followeduser header.a-single-margin.l-container-row span.userprofile-details::text').extract()) < 1:
            print('Ebay-kleinanzeigen blockt noch diese Anfrage oder user wurde gelöscht')
            print(i)
            name = ''
            break
        else:
            paymentdetails = sel.css('.user-profile-secure-payment::text').extract() # Sicher bezahlen eingerichtet
            paymentdetails = sel.css('html body#pstrads div.site-base div.site-base--content div#site-content.l-page-wrapper.l-container-row div.l-splitpage-flex div.l-splitpage-navigation section.l-container-row.contentbox.surface.userprofile.j-followeduser header.a-single-margin.l-container-row span.user-profile-secure-payment::text').extract() # Sicher bezahlen eingerichtet
            if len(paymentdetails) > 0:
                paymentdetails = 'Sicherbezahleneingerichtet'
                name = sel.css('html body#pstrads div.site-base div.site-base--content div#site-content.l-page-wrapper.l-container-row div.l-splitpage-flex div.l-splitpage-navigation section.l-container-row.contentbox.surface.userprofile.j-followeduser header.a-single-margin.l-container-row h2.userprofile--name::text').extract()  # 'Rainer'
                if len(name) > 0:
                    name = name[0]
                else:
                    name = ''
                usertype = sel.css('span.userprofile-details:nth-child(7)::text').extract()  # Privater Nutzer
                start = sel.css('span.userprofile-details:nth-child(9)::text').extract()  # Aktiv seit 1.9.2009
                offeringscount = sel.css('span.userprofile-details:nth-child(11)::text').extract()  # 5 Anzeigen online / 522 gesamt
            else:
                name = sel.css('html body#pstrads div.site-base div.site-base--content div#site-content.l-page-wrapper.l-container-row div.l-splitpage-flex div.l-splitpage-navigation section.l-container-row.contentbox.surface.userprofile.j-followeduser header.a-single-margin.l-container-row h2.userprofile--name::text').extract()  # 'Rainer'
                if len(name) > 0:
                    name = name[0]
                else:
                    name = ''
                paymentdetails = 'keinSicherbezahlen'
                usertype = sel.css('span.userprofile-details:nth-child(3)::text').extract()  # Privater Nutzer
                start = sel.css('span.userprofile-details:nth-child(5)::text').extract()  # Aktiv seit 1.9.2009
                offeringscount = sel.css('span.userprofile-details:nth-child(7)::text').extract()  # 5 Anzeigen online / 522 gesamt

            profilerating = sel.css('html body#pstrads div.site-base div.site-base--content div#site-content.l-page-wrapper.l-container-row div.l-splitpage-flex div.l-splitpage-navigation section.l-container-row.contentbox.surface.userprofile.j-followeduser div.followuseritem-main ul.badges-iconlist li.userbadges-public-profile.userbadges-profile-rating div.iconlist-text::text').extract() # TOP Zufriedenheit
            if len(profilerating) > 0:
                profilerating = profilerating[0]
            profilefriendliness = sel.css('html body#pstrads div.site-base div.site-base--content div#site-content.l-page-wrapper.l-container-row div.l-splitpage-flex div.l-splitpage-navigation section.l-container-row.contentbox.surface.userprofile.j-followeduser div.followuseritem-main ul.badges-iconlist li.userbadges-public-profile.userbadges-profile-friendliness div.iconlist-text::text').extract() # Besonders freundlich
            if len(profilefriendliness) > 0:
                profilefriendliness = profilefriendliness[0]
            profilereliability = sel.css('html body#pstrads div.site-base div.site-base--content div#site-content.l-page-wrapper.l-container-row div.l-splitpage-flex div.l-splitpage-navigation section.l-container-row.contentbox.surface.userprofile.j-followeduser div.followuseritem-main ul.badges-iconlist li.userbadges-public-profile.userbadges-profile-reliability div.iconlist-text::text').extract() # Besonders zuverlässig
            if len(profilereliability) > 0:
                profilereliability = profilereliability[0]
            profilereplyrate = sel.css('html body#pstrads div.site-base div.site-base--content div#site-content.l-page-wrapper.l-container-row div.l-splitpage-flex div.l-splitpage-navigation section.l-container-row.contentbox.surface.userprofile.j-followeduser div.followuseritem-main ul.badges-iconlist li.userbadges-public-profile.userbadges-profile-replyRate div.iconlist-text::text').extract() # xxx% Antwortrate
            if len(profilereplyrate) > 0:
                profilereplyrate = profilereplyrate[0]
            profilereplyspeed = sel.css('html body#pstrads div.site-base div.site-base--content div#site-content.l-page-wrapper.l-container-row div.l-splitpage-flex div.l-splitpage-navigation section.l-container-row.contentbox.surface.userprofile.j-followeduser div.followuseritem-main ul.badges-iconlist li.userbadges-public-profile.userbadges-profile-replySpeed div.iconlist-text::text').extract() # 1h Antwortzeit
            if len(profilereplyspeed) > 0:
                profilereplyspeed = profilereplyspeed[0]
            profilefollowers = sel.css('html body#pstrads div.site-base div.site-base--content div#site-content.l-page-wrapper.l-container-row div.l-splitpage-flex div.l-splitpage-navigation section.l-container-row.contentbox.surface.userprofile.j-followeduser div.followuseritem-main ul.badges-iconlist li.userbadges-public-profile.userbadges-profile-followers div.iconlist-text::text').extract() # 27 Follower
            if len(profilefollowers) > 0:
                profilefollowers = profilefollowers[0]
            offernames = sel.css('a.ellipsis::text').extract()  # ['Elektro-Heckenschere Top Craft 661', 'Spinning Bike Aerobike 800', 'Asics Onitsuka Tiger Sneaker - 43,5', 'LED Nachtlicht', 'Snatch Schulrucksack']
            location = sel.css('div.aditem-main--top--left::text').extract() # ['13158 Rosenthal', '16515 Oranienburg', '13158 ...']
            description = sel.css('p.aditem-main--middle--description::text').extract() # ['Verkaufe eine gebrauchte Elekto-Heckenschere von der Firma Top Craft. Sie ist ca. 60cm lang und hat...', 'xxxx', ]
            prices = sel.css('p.aditem-main--middle--price-shipping--price::text').extract() # ['12 € VB', 'xy €', ]
            offerdates = sel.css('div.aditem-main--top--right::text').extract() # ['17.10.2022', 'xx.xx.xxxx', ]
            shipping = sel.css('p.aditem-main--middle--price-shipping--shipping::text').extract() # ['', 'Versand möglich', ]

        print(i.replace('http://api.scraperapi.com?api_key=cf1dfe285ad7b62e5387b4ad6e3fe1b5&url=', ''))
        userid.append(i.replace('http://api.scraperapi.com?api_key=cf1dfe285ad7b62e5387b4ad6e3fe1b5&url=https://www.ebay-kleinanzeigen.de/s-bestandsliste.html?userId=', ''))

        usertype3 = []
        for sub in usertype:
            usertype3.append(sub.replace("\n", ""))
        usertype0 = []
        for sub in usertype3:
            usertype0.append(sub.replace(" ", ""))

        start3 = []
        for sub in start:
            start3.append(sub.replace("\n", ""))
        start2 = []
        for sub in start3:
            start2.append(sub.replace(" ", ""))
        start0 = []
        for sub in start2:
            start0.append(sub.replace("Aktivseit", ""))
        start0 = start0[0]

        for i in range(0,1):
            if len(start0) == 0:
                break
            else:
                usertype0 = usertype0[0]

            offeringscount3 = []
            for sub in offeringscount:
                offeringscount3.append(sub.replace("\n", ""))
            offeringscount0 = []
            for sub in offeringscount3:
                offeringscount0.append(sub.replace(" ", ""))
            offeringscount0 = offeringscount0[0]
            x = re.split('[/]', offeringscount0)
            offeringsonline = x[0]
            offeringsonline = offeringsonline.replace('Anzeigenonline', '')
            if len(x) > 1:
                offeringssum = x[1]
                offeringssum = offeringssum.replace('gesamt', '')
            else:
                offeringssum = 0

            if len(profilefriendliness) > 0:
                profilefriendliness = profilefriendliness.replace(' ', '')
            if len(profilereliability) > 0:
                profilereliability = profilereliability.replace(' ', '')

            location3 = []
            for sub in location:
                location3.append(sub.replace("\n", ""))
            location2 = []
            for sub in location3:
                if sub != '':
                    location2.append(sub.replace(" ", ""))
            location0 = []
            for sub in location2:
                if sub != '':
                    location0.append(sub)

            description0 = []
            for sub in description:
                description0.append(sub.replace("\n", " "))

            prices3 = []
            for sub in prices:
                prices3.append(sub.replace("\n", ""))
            prices2 = []
            for sub in prices3:
                if sub != '':
                    prices2.append(sub.replace(" ", ""))
            prices0 = []
            for sub in prices2:
                if sub != '':
                    prices0.append(sub)

            offerdates3 = []
            for sub in offerdates:
                offerdates3.append(sub.replace("\n", ""))
            offerdates2 = []
            for sub in offerdates3:
                if sub != '':
                    offerdates2.append(sub.replace(" ", ""))
            offerdates0 = []
            for sub in offerdates2:
                if sub != '':
                    offerdates0.append(sub)

            shipping3 = []
            for sub in shipping:
                shipping3.append(sub.replace("\n", ""))
            shipping0 = []
            for sub in shipping3:
                if len(shipping3) < 1:
                    shipping0 = 'NurAbholung'
                else:
                    shipping0.append(sub.replace(" ", ""))

            name1.append(name)
            paymentdetails1.append(paymentdetails)
            usertype1.append(usertype0)
            start1.append(start0)
            offeringsonline1.append(offeringsonline)
            offeringssum1.append(offeringssum)
            profilerating1.append(profilerating)
            profilefriendliness1.append(profilefriendliness)
            profilereliability1.append(profilereliability)
            profilereplyrate1.append(profilereplyrate)
            profilereplyspeed1.append(profilereplyspeed)
            profilefollowers1.append(profilefollowers)
            offernames1.append(offernames)
            location1.append(location0)
            description1.append(description0)
            prices1.append(prices0)
            offerdates1.append(offerdates0)
            shipping1.append(shipping0)

    df = pd.DataFrame((zip(userid, name1, paymentdetails1, usertype1, start1, offeringsonline1, offeringssum1, profilerating1, profilefriendliness1, profilereliability1, profilereplyrate1, profilereplyspeed1, profilefollowers1, offernames1, location1, description1, prices1, offerdates1, shipping1)), columns=['user-ID', 'name', 'paymentdetails', 'usertype', 'start', 'offeringsonline', 'offeringssum', 'profilerating', 'profilefriendliness', 'profilereliability', 'profilereplyrate', 'profilereplyspeed', 'profilefollowers', 'offernames', 'location', 'description', 'prices', 'offerdates', 'shipping'])
    df['year'] = pd.DatetimeIndex(df['start']).year
    df['weekday'] = pd.DatetimeIndex(df['start']).weekday
    df['month'] = pd.DatetimeIndex(df['start']).day
    df['dayofmonth'] = pd.DatetimeIndex(df['start']).month
    df['scraptime'] = datetime.datetime.now()

    return df


def editprofiledata(df_profiles):

    # makes it more computional
    df_profiles['name'] = df_profiles['name'].replace('[]', None).astype(str)
    name = []
    for x in df_profiles['name']:
        if x == 'nan':
            x = 0
        else:
            x = 1
        name.append(x)
    df_profiles['name'] = name

    df_profiles['paymentdetails'] = df_profiles['paymentdetails'].replace('Sicherbezahleneingerichtet', 1)
    df_profiles['paymentdetails'] = df_profiles['paymentdetails'].replace('keinSicherbezahlen', 0)
    df_profiles['usertype'] = df_profiles['usertype'].replace('GewerblicherNutzer', 1)
    df_profiles['usertype'] = df_profiles['usertype'].replace('PrivaterNutzer', 0)
    df_profiles['offeringsonline'] = df_profiles['offeringsonline'].astype(int)
    df_profiles['offeringssum'] = df_profiles['offeringssum'].astype(int)
    del df_profiles['start']


    # recognizing grammar mistakes in description
    df_grammar = pd.read_csv('csv_data/de_DE 2.csv', encoding='latin-1')
    df_grammar['Äbte'] = df_grammar['Äbte'].str.lower()
    data_list = []
    df_writing = []
    X = df_profiles['description']
    for text in X:
        text = re.sub(r'[!@#$(),"%^*?:.;~`0-9 ]', ' ', text)  # removing the symbols and numbers
        text = re.sub(r'[[]]', ' ', text)
        text = text.lower()
        data_list.append(text)  # appending to data_list

    cleaned_description = pd.DataFrame()
    c_length = []
    list = []
    list2 = []
    for d in df_grammar['Äbte']:
        list.append(d)

    for text in data_list:
        text = text.split(' ')
        list2.append(text)
        a = 0
        b = 0
        for x in text:
            if x not in list:
                if x != '':
                    a = a+1
            if x != '':
                b = b+1
        c_length.append(b)
        df_writing.append(a)

    # saving grammatical mistakes in cleaned_description
    cleaned_description['user-ID'] = df_profiles['user-ID']
    cleaned_description['mistakes_descr'] = df_writing
    cleaned_description['length_descr'] = c_length
    cleaned_description['perception_descr'] = cleaned_description['mistakes_descr']/cleaned_description['length_descr']
    df_profiles['perception_descr'] = cleaned_description['perception_descr']
    cleaned_description['perception_descr'] = cleaned_description['perception_descr'].fillna(0)
    cleaned_description['c_description'] = list2
    with open('cleaned_description.textmate', 'w') as file:
        file.write(str(cleaned_description) + '\n')


    # build profilerating binary
    profilerating = []
    for i in range(0, len(df_profiles['profilerating'])):
        if df_profiles['profilerating'][i] != '[]':
            profilerating.append(df_profiles['profilerating'][i])
        else:
            profilerating.append(None)
    df_profiles['profilerating'] = profilerating
    df_profiles['profilerating'] = df_profiles['profilerating'].replace('TOP', 3)
    df_profiles['profilerating'] = df_profiles['profilerating'].replace('OK', 2)
    df_profiles['profilerating'] = df_profiles['profilerating'].replace('NA JA', 1)
    df_profiles['profilerating'] = df_profiles['profilerating'].astype(float)


    # build profilefriendliness binary
    profilefriendliness = []
    for i in range(0, len(df_profiles['profilefriendliness'])):
        if df_profiles['profilefriendliness'][i] != '[]':
            profilefriendliness.append(df_profiles['profilefriendliness'][i])
        else:
            profilefriendliness.append(None)
    df_profiles['profilefriendliness'] = profilefriendliness
    df_profiles['profilefriendliness'] = df_profiles['profilefriendliness'].replace('Besondersfreundlich', 3)
    df_profiles['profilefriendliness'] = df_profiles['profilefriendliness'].replace('Sehrfreundlich', 2)
    df_profiles['profilefriendliness'] = df_profiles['profilefriendliness'].replace('Freundlich', 1)
    df_profiles['profilefriendliness'] = df_profiles['profilefriendliness'].astype(float)


    # build profilereliability binary
    profilereliability = []
    for i in range(0, len(df_profiles['profilereliability'])):
        if df_profiles['profilereliability'][i] != '[]':
            profilereliability.append(df_profiles['profilereliability'][i])
        else:
            profilereliability.append(None)
    df_profiles['profilereliability'] = profilereliability
    df_profiles['profilereliability'] = df_profiles['profilereliability'].replace('Besonderszuverlässig', 3)
    df_profiles['profilereliability'] = df_profiles['profilereliability'].replace('Sehrzuverlässig', 2)
    df_profiles['profilereliability'] = df_profiles['profilereliability'].replace('Zuverlässig', 1)
    df_profiles['profilereliability'] = df_profiles['profilereliability'].astype(float)


    # build profilereplyrate binary
    profilereplyrate = []
    for i in df_profiles['profilereplyrate']:
        if len(i) > 2:
            i = i.replace('%', '')
            profilereplyrate.append(i)
        else:
            profilereplyrate.append(None)
    df_profiles['profilereplyrate'] = profilereplyrate
    df_profiles['profilereplyrate'] = df_profiles['profilereplyrate'].astype(float)


    # build profilereplyspeed binary
    profilereplyspeed = []
    for i in range(0, len(df_profiles['profilereplyspeed'])):
        if df_profiles['profilereplyspeed'][i] != '[]':
            df_profiles['profilereplyspeed'][i] = df_profiles['profilereplyspeed'][i].replace('h', '')
            df_profiles['profilereplyspeed'][i] = df_profiles['profilereplyspeed'][i].replace('10min', '0.16')
            profilereplyspeed.append(df_profiles['profilereplyspeed'][i])
        else:
            profilereplyspeed.append(None)
    df_profiles['profilereplyspeed'] = profilereplyspeed
    df_profiles['profilereplyspeed'] = df_profiles['profilereplyspeed'].astype(float)
    df_profiles['profilereplyspeed'].fillna(df_profiles['profilereplyspeed'].mean())


    # build profilefollowers binary
    profilefollowers = []
    for i in range(0, len(df_profiles['profilefollowers'])):
        if df_profiles['profilefollowers'][i] != '[]':
            profilefollowers.append(df_profiles['profilefollowers'][i])
        else:
            profilefollowers.append(None)
    df_profiles['profilefollowers'] = profilefollowers
    df_profiles['profilefollowers'] = df_profiles['profilefollowers'].astype(float)


    # build shipping binary
    shipping = []
    for i in df_profiles['shipping']:
        if len(i) == 18:
            shipping.append(1)
        else:
            shipping.append(0)
    df_profiles['shipping'] = shipping


    # location
    X = df_profiles['location']
    location = []
    for y in range(0, len(X)):
        if len(X[y]) > 4:
            location.append(X[y][2:7])
        else:
            location.append(None)
    df_profiles['location'] = location
    df_profiles['location'] = df_profiles['location'].astype(float)
    df_profiles.rename(columns={'paymentdetails': 'Sicher_bezahlen', 'usertype': 'Gewerblicher_user', 'year': 'startyear', 'weekday': 'startweekday', 'month': 'startdayofmonth', 'dayofmonth': 'startmonth', 'scraptime': 'scrape_time', 'perception_descr': 'mistake_rate'}, inplace=True)

    return df_profiles


def filledprofiledata(edited_profiles):

    edited_profiles['profilerating'] = edited_profiles['profilerating'].fillna(0)
    edited_profiles['profilefriendliness'] = edited_profiles['profilefriendliness'].fillna(0)
    edited_profiles['profilereliability'] = edited_profiles['profilereliability'].fillna(0)
    edited_profiles['profilereplyrate'] = edited_profiles['profilereplyrate'].fillna(0)
    edited_profiles['profilereplyspeed'] = edited_profiles['profilereplyspeed'].fillna(24)
    edited_profiles['profilefollowers'] = edited_profiles['profilefollowers'].fillna(0)
    del edited_profiles['scrape_time']

    return edited_profiles


def combine_both(profiles_new, profiles_old):

    old_user = list(profiles_old['user-ID'])
    new_user = list(profiles_new['user-ID'])

    missing = []
    for i in old_user:
        if i in new_user:
            missing.append(0)
        else:
            missing.append(1)
    profiles_old['scam_account'] = missing
    profiles_old['scam_account'][10] = 1

    return profiles_old




def data_cleaning(filled_data):

    latlong = pd.read_csv('csv_data/plz_geocoord.csv', delimiter=';')
    latlong.rename(columns={'PLZ': 'location'}, inplace=True)

    latlong['lng'] = float(latlong['lng'].replace(',', '.'))
    merged_data = pd.merge(filled_data, latlong, on='location', how='left')
    with open('3:correl_data', 'w') as file:
        file.write(str(merged_data) + '\n')

    return merged_data


def analysis_correl(filled_data):

    corr = filled_data.corr(method='pearson')
    plt.figure(figsize=(20, 6))
    sns.heatmap(corr, annot=True, cmap='Blues')
    plt.title('Correlation matrix')
    plt.show()

    return corr


def analysis_test(filled_data, Trainingsvolumen, Testvolumen):

    X_testt = (filled_data.head(Trainingsvolumen+Testvolumen)).tail(Testvolumen)
    with open('4:Testset.textmate', 'w') as file:
        file.write(str(X_testt) + '\n')

    return X_testt


def df_stats0(X_testt):
    df_statistics = pd.DataFrame()
    df_statistics['mean'] = X_testt.mean()
    df_statistics['median'] = X_testt.median()
    df_statistics['max'] = X_testt.max()
    df_statistics['min'] = X_testt.min()
    df_statistics['count'] = X_testt.count()
    df_statistics['std'] = X_testt.std()

    return df_statistics


def analysis_train(filled_data, Trainingsvolumen):

    dataset = filled_data.head(Trainingsvolumen)
    with open('4:Trainingset.textmate', 'w') as file:
        file.write(str(dataset) + '\n')

    return dataset


def df_stats(dataset):
    df_statistics = pd.DataFrame()
    df_statistics['mean'] = dataset.mean()
    df_statistics['median'] = dataset.median()
    df_statistics['max'] = dataset.max()
    df_statistics['min'] = dataset.min()
    df_statistics['count'] = dataset.count()
    df_statistics['std'] = dataset.std()

    return df_statistics


def predictions(data, i, X_testt, df_statistics, df_statistics0):
    rlog = []; rsvc = []; rknn = []; rgaussian = []; rperception = []; rlinear_svc = []; rsgd = []; rdecision_tree = []; rrandom_forest = []; rxgb = []; rbag = []; rada = []
    rxgb2 = []; rdecision_tree2 = []; rrandom_forest2 = []; rada2 = []; rextra2 = []; rknn2 = []; rcat2 = []; rgradient2 = []; rbag2 = []

    df_train = data.head(i)
    Datum = pd.DataFrame()
    Y_train = df_train['scam_account'].astype(float)
    del df_train['scam_account']
    X_train = df_train.astype(float)
    df_test = X_testt

    '''abhängige Variable'''
    Y_test = df_test['scam_account']
    del df_test['scam_account']
    ''''''

    X_test = df_test
    print('Fortschritt: ' + str(round(0 * 100, 1)) + '%')

    # create a xgboost regression model
    xgb2 = XGBRegressor(n_estimators=1000, max_depth=7, eta=0.1, subsample=0.7, colsample_bytree=0.8)
    xgb2.fit(X_train.values, Y_train.values)
    decision_tree2 = DecisionTreeRegressor()
    decision_tree2.fit(X_train.values, Y_train.values)
    random_forest2 = RandomForestRegressor()
    random_forest2.fit(X_train, Y_train)
    ada2 = AdaBoostRegressor()
    ada2.fit(X_train, Y_train)
    extra2 = ExtraTreesRegressor()
    extra2.fit(X_train, Y_train)
    knn2 = KNeighborsRegressor()
    knn2.fit(X_train, Y_train)
    gradient2 = GradientBoostingRegressor()
    gradient2.fit(X_train, Y_train)
    bag2 = BaggingRegressor()
    bag2.fit(X_train, Y_train)

    lin_reg = linear_model.LinearRegression()
    lin_reg.fit(X_train, Y_train)
    logreg = LogisticRegression()
    logreg.fit(X_train.values, Y_train.values)
    svc = SVC()
    svc.fit(X_train.values, Y_train.values)
    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(X_train.values, Y_train.values)
    gaussian = GaussianNB()
    gaussian.fit(X_train.values, Y_train.values)
    perceptron = Perceptron()
    perceptron.fit(X_train.values, Y_train.values)
    linear_svc = LinearSVC()
    linear_svc.fit(X_train.values, Y_train.values)
    sgd = SGDClassifier()
    sgd.fit(X_train.values, Y_train.values)
    decision_tree = DecisionTreeClassifier()
    decision_tree.fit(X_train.values, Y_train.values)
    random_forest = RandomForestClassifier(n_estimators=100)
    random_forest.fit(X_train.values, Y_train.values)
    #xgb = XGBClassifier(n_estimators=1000, learning_rate=0.05)
    #xgb.fit(X_train.values, Y_train.values)
    #bag = BaggingClassifier()
    #bag.fit(X_train.values, Y_train.values)
    ada = AdaBoostClassifier()
    ada.fit(X_train.values, Y_train.values)


    df_statistics['mean'] = np.round(X_train.mean(),3)
    df_statistics = df_statistics.iloc[1:, :]
    df_statistics['lin_coef'] = np.around(lin_reg.coef_, 4)
    df_statistics['impact'] = np.around(df_statistics['lin_coef']*df_statistics['mean'], 4)


    df_statistics['lin_coef'] = np.around(lin_reg.coef_, 4)
    results = permutation_importance(knn, X_train, Y_train, scoring='neg_mean_squared_error')
    importance = results.importances_mean
    df_statistics['knn_coef'] = np.around(importance, 4)
    results = permutation_importance(gaussian, X_train, Y_train, scoring='neg_mean_squared_error')
    importance = results.importances_mean
    df_statistics['gaus_coef'] = np.around(importance, 4)
    #df_statistics['perce_coef'] = np.around(perceptron.coef_, 4)
    #df_statistics['lin_svc_coef'] = np.around(linear_svc.coef_, 4)
    #df_statistics['sgd_coef'] = np.around(sgd.coef_, 4)
    df_statistics['xgb_coeff'] = np.around(xgb2.feature_importances_, 4)
    df_statistics['svc_coeff'] = np.around(svc.coef0, 4)
    df_statistics['dec_coeff'] = np.around(decision_tree.feature_importances_, 4)
    df_statistics['ran_coeff'] = np.around(random_forest.feature_importances_, 4)
    results = permutation_importance(ada, X_train, Y_train, scoring='neg_mean_squared_error')
    importance = results.importances_mean
    df_statistics['ada_coef'] = np.around(importance, 4)


    with open('4:Infos Trainset.textmate', 'w') as file:
        file.write(str(df_statistics) + '\n')


    lin_reg = linear_model.LinearRegression()
    lin_reg.fit(X_test, Y_test)
    df_statistics0['mean'] = X_test.mean()
    df_statistics0 = df_statistics0.iloc[1:, :]
    df_statistics0['coeff'] = np.around(lin_reg.coef_, 4)
    df_statistics0['impact'] = np.around(df_statistics0['coeff'] * df_statistics0['mean'], 4)
    with open('4:Infos Testset.textmate', 'w') as file:
        file.write(str(df_statistics0) + '\n')

    a = []
    for l in range(0, len(X_test)):

        values = X_test.values[l]
        prediction_log = logreg.predict_proba([values])
        if prediction_log[0][1] > 0.5:
            rlog.append(1)
        else:
            rlog.append(0)
        prediction_svc = svc.predict([values])
        rsvc.append((prediction_svc[0]))
        prediction_knn = knn.predict([values])
        rknn.append((prediction_knn[0]))
        prediction_gaussian = gaussian.predict([values])
        rgaussian.append((prediction_gaussian[0]))
        prediction_perceptron = perceptron.predict([values])
        rperception.append((prediction_perceptron[0]))
        prediction_linear_svc = linear_svc.predict([values])
        rlinear_svc.append((prediction_linear_svc[0]))
        prediction_sgd = sgd.predict([values])
        rsgd.append((prediction_sgd[0]))
        prediction_decision_tree = decision_tree.predict([values])
        rdecision_tree.append((prediction_decision_tree[0]))
        prediction_random_forest = random_forest.predict([values])
        rrandom_forest.append((prediction_random_forest[0]))
        #prediction_xgb = xgb.predict([values])
        #rxgb.append((prediction_xgb[0]))
        #prediction_bag = bag.predict([values])
        #rbag.append((prediction_bag[0]))
        prediction_ada = ada.predict([values])
        rada.append((prediction_ada[0]))

        z = (l+1)/len(X_test)
        print('Fortschritt: ' + str(round(z*100, 1)) + '%')

        prediction_xgb2 = xgb2.predict([X_test.values[l]])
        rxgb2.append(round(prediction_xgb2[0], 3))
        prediction_decision_tree2 = decision_tree2.predict([X_test.values[l]])
        rdecision_tree2.append(round(prediction_decision_tree2[0], 3))
        prediction_random_forest2 = random_forest2.predict([X_test.values[l]])
        rrandom_forest2.append(round(prediction_random_forest2[0], 3))
        prediction_ada2 = ada2.predict([X_test.values[l]])
        rada2.append(round(prediction_ada2[0], 3))
        prediction_extra2 = extra2.predict([X_test.values[l]])
        rextra2.append(round(prediction_extra2[0], 3))
        prediction_knn2 = knn2.predict([X_test.values[l]])
        rknn2.append(round(prediction_knn2[0], 3))
        prediction_gradient2 = gradient2.predict([X_test.values[l]])
        rgradient2.append(round(prediction_gradient2[0], 3))
        prediction_bag2 = bag2.predict([X_test.values[l]])
        rbag2.append(round(prediction_bag2[0], 3))


    df_testresults = pd.DataFrame()
    df_testresults['Events'] = Y_test

    df_testresults['log'] = rlog
    df_testresults['svc'] = rsvc
    df_testresults['knn'] = rknn
    df_testresults['gaussian'] = rgaussian
    df_testresults['perception'] = rperception
    df_testresults['linear_svc'] = rlinear_svc
    df_testresults['sgd'] = rsgd
    df_testresults['decision_tree'] = rdecision_tree
    df_testresults['random_forest'] = rrandom_forest
    #df_testresults['xgb'] = rxgb
    #df_testresults['bag'] = rbag
    df_testresults['ada'] = rada

    df_testresults['xgb2'] = rxgb2
    df_testresults['rdecision_tree2'] = rdecision_tree2
    df_testresults['rrandom_forest2'] = rrandom_forest2
    df_testresults['rada2'] = rada2
    df_testresults['rextra2'] = rextra2
    df_testresults['rextra2'] = rextra2
    df_testresults['rknn2'] = rknn2
    df_testresults['rgradient2'] = rgradient2
    df_testresults['rbag2'] = rbag2

    return df_testresults


def correlation2(results):
    corr = results.corr(method='pearson')
    plt.figure(figsize=(20, 6))
    sns.heatmap(corr, annot=True, cmap='Blues')
    plt.title('Correlation matrix')
    plt.show()

    return corr


main()