# -*- coding: utf-8 -*-
"""
Created on Sat Dec 1 20:22:54 2018

@author: Aisha Aijaz Ahmad
"""
#import relevant libraries
#for implementing json file
import json
#for dataframe handling
import pandas as pd

#relevant dictionaries are given below for this coursework

#country code to continent name mapping dictionary
continents = {
  'AF' : 'Africa',
  'AS' : 'Asia',
  'EU' : 'Europe',
  'NA' : 'North America',
  'SA' : 'South America',
  'OC' : 'Oceania',
  'AN' : 'Antarctica'
}

#country code to continent code mapping dictionary
country_to_cont = {
  'AF' : 'AS',
  'AX' : 'EU',
  'AL' : 'EU',
  'DZ' : 'AF',
  'AS' : 'OC',
  'AD' : 'EU',
  'AO' : 'AF',
  'AI' : 'NA',
  'AQ' : 'AN',
  'AG' : 'NA',
  'AR' : 'SA',
  'AM' : 'AS',
  'AW' : 'NA',
  'AU' : 'OC',
  'AT' : 'EU',
  'AZ' : 'AS',
  'BS' : 'NA',
  'BH' : 'AS',
  'BD' : 'AS',
  'BB' : 'NA',
  'BY' : 'EU',
  'BE' : 'EU',
  'BZ' : 'NA',
  'BJ' : 'AF',
  'BM' : 'NA',
  'BT' : 'AS',
  'BO' : 'SA',
  'BQ' : 'NA',
  'BA' : 'EU',
  'BW' : 'AF',
  'BV' : 'AN',
  'BR' : 'SA',
  'IO' : 'AS',
  'VG' : 'NA',
  'BN' : 'AS',
  'BG' : 'EU',
  'BF' : 'AF',
  'BI' : 'AF',
  'KH' : 'AS',
  'CM' : 'AF',
  'CA' : 'NA',
  'CV' : 'AF',
  'KY' : 'NA',
  'CF' : 'AF',
  'TD' : 'AF',
  'CL' : 'SA',
  'CN' : 'AS',
  'CX' : 'AS',
  'CC' : 'AS',
  'CO' : 'SA',
  'KM' : 'AF',
  'CD' : 'AF',
  'CG' : 'AF',
  'CK' : 'OC',
  'CR' : 'NA',
  'CI' : 'AF',
  'HR' : 'EU',
  'CU' : 'NA',
  'CW' : 'NA',
  'CY' : 'AS',
  'CZ' : 'EU',
  'DK' : 'EU',
  'DJ' : 'AF',
  'DM' : 'NA',
  'DO' : 'NA',
  'EC' : 'SA',
  'EG' : 'AF',
  'SV' : 'NA',
  'GQ' : 'AF',
  'ER' : 'AF',
  'EE' : 'EU',
  'ET' : 'AF',
  'FO' : 'EU',
  'FK' : 'SA',
  'FJ' : 'OC',
  'FI' : 'EU',
  'FR' : 'EU',
  'GF' : 'SA',
  'PF' : 'OC',
  'TF' : 'AN',
  'GA' : 'AF',
  'GM' : 'AF',
  'GE' : 'AS',
  'DE' : 'EU',
  'GH' : 'AF',
  'GI' : 'EU',
  'GR' : 'EU',
  'GL' : 'NA',
  'GD' : 'NA',
  'GP' : 'NA',
  'GU' : 'OC',
  'GT' : 'NA',
  'GG' : 'EU',
  'GN' : 'AF',
  'GW' : 'AF',
  'GY' : 'SA',
  'HT' : 'NA',
  'HM' : 'AN',
  'VA' : 'EU',
  'HN' : 'NA',
  'HK' : 'AS',
  'HU' : 'EU',
  'IS' : 'EU',
  'IN' : 'AS',
  'ID' : 'AS',
  'IR' : 'AS',
  'IQ' : 'AS',
  'IE' : 'EU',
  'IM' : 'EU',
  'IL' : 'AS',
  'IT' : 'EU',
  'JM' : 'NA',
  'JP' : 'AS',
  'JE' : 'EU',
  'JO' : 'AS',
  'KZ' : 'AS',
  'KE' : 'AF',
  'KI' : 'OC',
  'KP' : 'AS',
  'KR' : 'AS',
  'KW' : 'AS',
  'KG' : 'AS',
  'LA' : 'AS',
  'LV' : 'EU',
  'LB' : 'AS',
  'LS' : 'AF',
  'LR' : 'AF',
  'LY' : 'AF',
  'LI' : 'EU',
  'LT' : 'EU',
  'LU' : 'EU',
  'MO' : 'AS',
  'MK' : 'EU',
  'MG' : 'AF',
  'MW' : 'AF',
  'MY' : 'AS',
  'MV' : 'AS',
  'ML' : 'AF',
  'MT' : 'EU',
  'MH' : 'OC',
  'MQ' : 'NA',
  'MR' : 'AF',
  'MU' : 'AF',
  'YT' : 'AF',
  'MX' : 'NA',
  'FM' : 'OC',
  'MD' : 'EU',
  'MC' : 'EU',
  'MN' : 'AS',
  'ME' : 'EU',
  'MS' : 'NA',
  'MA' : 'AF',
  'MZ' : 'AF',
  'MM' : 'AS',
  'NA' : 'AF',
  'NR' : 'OC',
  'NP' : 'AS',
  'NL' : 'EU',
  'NC' : 'OC',
  'NZ' : 'OC',
  'NI' : 'NA',
  'NE' : 'AF',
  'NG' : 'AF',
  'NU' : 'OC',
  'NF' : 'OC',
  'MP' : 'OC',
  'NO' : 'EU',
  'OM' : 'AS',
  'PK' : 'AS',
  'PW' : 'OC',
  'PS' : 'AS',
  'PA' : 'NA',
  'PG' : 'OC',
  'PY' : 'SA',
  'PE' : 'SA',
  'PH' : 'AS',
  'PN' : 'OC',
  'PL' : 'EU',
  'PT' : 'EU',
  'PR' : 'NA',
  'QA' : 'AS',
  'RE' : 'AF',
  'RO' : 'EU',
  'RU' : 'EU',
  'RW' : 'AF',
  'BL' : 'NA',
  'SH' : 'AF',
  'KN' : 'NA',
  'LC' : 'NA',
  'MF' : 'NA',
  'PM' : 'NA',
  'VC' : 'NA',
  'WS' : 'OC',
  'SM' : 'EU',
  'ST' : 'AF',
  'SA' : 'AS',
  'SN' : 'AF',
  'RS' : 'EU',
  'SC' : 'AF',
  'SL' : 'AF',
  'SG' : 'AS',
  'SX' : 'NA',
  'SK' : 'EU',
  'SI' : 'EU',
  'SB' : 'OC',
  'SO' : 'AF',
  'ZA' : 'AF',
  'GS' : 'AN',
  'SS' : 'AF',
  'ES' : 'EU',
  'LK' : 'AS',
  'SD' : 'AF',
  'SR' : 'SA',
  'SJ' : 'EU',
  'SZ' : 'AF',
  'SE' : 'EU',
  'CH' : 'EU',
  'SY' : 'AS',
  'TW' : 'AS',
  'TJ' : 'AS',
  'TZ' : 'AF',
  'TH' : 'AS',
  'TL' : 'AS',
  'TG' : 'AF',
  'TK' : 'OC',
  'TO' : 'OC',
  'TT' : 'NA',
  'TN' : 'AF',
  'TR' : 'AS',
  'TM' : 'AS',
  'TC' : 'NA',
  'TV' : 'OC',
  'UG' : 'AF',
  'UA' : 'EU',
  'AE' : 'AS',
  'GB' : 'EU',
  'US' : 'NA',
  'UM' : 'OC',
  'VI' : 'NA',
  'UY' : 'SA',
  'UZ' : 'AS',
  'VU' : 'OC',
  'VE' : 'SA',
  'VN' : 'AS',
  'WF' : 'OC',
  'EH' : 'AF',
  'YE' : 'AS',
  'ZM' : 'AF',
  'ZW' : 'AF'
}

#starting new class for task 2
class TaskTwo:
    #task 2a
    """
    Definition Description:
        This method takes two inputs. It prints the histogram for the frequency of users' 
        countries who visited or viewed that particular document.
        
    Parameters: choice, docid
        choice tells the function if the call was made from task 2b or from somewhere else.
        docid is the particular document id required.
    """
    def view_country(self, choice, docid):
        Data_List = []
        with open('C:/Users/Aisha Aijaz Ahmad/Desktop/dataset.json', 'r') as json_file:
            for line in json_file:
                Data_List.append(json.loads(line))
        x=pd.DataFrame.from_records(Data_List)
        byCountry = x.loc[x.subject_doc_id == docid]     
        x_rank = byCountry.groupby('visitor_country').size()
        if choice == 0:
            x_rank.plot.bar(title = "Visitor Country Counts",rot = 0)
        return byCountry
        
    #task 2b
    """
    Definition Description:
        This method takes one input. It prints the histogram for the frequency of users' 
        continents who visited or viewed that particular document. 
        To do this, it calls the 2a function and gets the list by country, then converts
        the names of the countries to continent using mapping dictionaries, groups them by
        continent, and plots the required histogram.
        
    Parameters: docid
        docid is the particular document id required.
    """
    def country_to_continent(self, docid):
        z = self.view_country(1, docid)
        z['Continent_Name']=z['visitor_country'].apply(self.get_countryname)
        y_rank = z.groupby('Continent_Name').size()
        y_rank.plot.bar(title = "Continents Count", rot = 0)
        return
    
    """
    Definition Description:
        This function maps the country code to the continent code and then maps that continent code
        to the country code.
    Parameters: country_code
        It is an alias for the required dictionary.
        
    """
    #for task 2a
    def get_countryname(self, country_code):
        return continents[country_to_cont[country_code]]

#end of class
