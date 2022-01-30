#!/usr/bin/env python
# coding: utf-8

# In[4]:


import json
from pandas.io.json import json_normalize
import argparse
import pandas as pd


def flatten_json(y):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x
    flatten(y)
    return out


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Converting json files into csv for Tableau processing')
    parser.add_argument(
        "-j", "--json", dest="json_file", help="PATH/TO/json file to convert", metavar="FILE", required=True)

    args = parser.parse_args()

    with open(args.json_file, "r", encoding='UTF-8') as inputFile:  # open json file
        json_data = json.loads(inputFile.read())  # load json content
        final_data = pd.DataFrame([flatten_json(elt) for elt in json_data['objects']])

    with open(args.json_file.replace(".json", ".csv"), "w", encoding='UTF-8') as outputFile:  # open csv file

        # saving DataFrame to csv
        final_data.to_csv(outputFile, index=False)


# In[ ]:




