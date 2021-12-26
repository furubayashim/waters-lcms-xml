#!/usr/bin/env python

import xml.etree.ElementTree as ET
import pandas as pd
import sys

if len(sys.argv) >1:
    xmlfilename = sys.argv[1]
else:
    print("need file name as argument")
    sys.exit()

root = ET.parse(xmlfilename).getroot()

samplelist = []
sampledatalist = []

for sample in root.iter('SAMPLE'):
    samplelist.append(sample.get('name'))
    compoundlist = []
    arealist = []
    for compound in sample.iter('COMPOUND'):
        compoundlist.append(compound.get('name'))
        arealist.append(float(compound[0].get('area')))
    sampledatalist.append(arealist)

df = pd.DataFrame(sampledatalist,columns=compoundlist,index=samplelist)

df.to_excel('{}-output.xlsx'.format(xmlfilename[:-4]))
