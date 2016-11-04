#! /usr/bin/env python
# -*- mode: python; coding: utf-8 -*-
# Copyright 2016 the HERA Collaboration
# Licensed under the 2-clause BSD license.

"""Onetime transfer of geo-locations of antennas into the M&C database.

"""
from __future__ import absolute_import, division, print_function

from hera_mc import geo_location, mc

data = {}
data['HH0'] = [80,0,'WGS84','34J',6601070.74,540901.60,1052.63]
data['HH1'] = [104,1,'WGS84','34J',6601070.74,540916.20,1052.62]
data['HH11'] = [64,11,'WGS84','34J',6601083.38,540894.30,1052.48]
data['HH12'] = [53,12,'WGS84','34J',6601083.38,540908.90,1052.41]
data['HH13'] = [31,13,'WGS84','34J',6601083.38,540923.50,1052.35]
data['HH14'] = [65,14,'WGS84','34J',6601083.38,540938.10,1052.49]
data['HH2'] = [96,2,'WGS84','34J',6601070.74,540930.80,1052.61]
data['HH23'] = [88,23,'WGS84','34J',6601096.03,540887.00,1052.34]
data['HH24'] = [9,24,'WGS84','34J',6601096.03,540901.60,1052.36]
data['HH25'] = [20,25,'WGS84','34J',6601096.03,540916.20,1052.35]
data['HH26'] = [89,26,'WGS84','34J',6601096.03,540930.80,1052.34]
data['HH27'] = [43,27,'WGS84','34J',6601096.03,540945.40,1052.44]
data['HH37'] = [105,37,'WGS84','34J',6601108.67,540894.30,1052.26]
data['HH38'] = [22,38,'WGS84','34J',6601108.67,540908.90,1052.25]
data['HH39'] = [81,39,'WGS84','34J',6601108.67,540923.50,1052.22]
data['HH40'] = [10,40,'WGS84','34J',6601108.67,540938.10,1052.24]
data['HH52'] = [72,52,'WGS84','34J',6601121.32,540901.60,1052.10]
data['HH53'] = [112,53,'WGS84','34J',6601121.32,540916.20,1052.07]
data['HH54'] = [97,54,'WGS84','34J',6601121.32,540930.80,1052.08]
data['PH00'] = [44,-1,'WGS84','34J',6601070.71,541018.40,1052.58]
data['PH01'] = [14,-1,'WGS84','34J',6601070.71,541033.00,1052.51]
data['PH02'] = [86,-1,'WGS84','34J',6601070.71,541047.60,1052.65]
data['PH11'] = [69,-1,'WGS84','34J',6601083.36,541011.10,1052.40]
data['PH12'] = [40,-1,'WGS84','34J',6601083.36,541025.70,1052.42]
data['PH13'] = [101,-1,'WGS84','34J',6601083.36,541040.30,1052.45]
data['PH14'] = [102,-1,'WGS84','34J',6601083.36,541054.90,1052.50]
data['PH23'] = [125,-1,'WGS84','34J',6601096.00,541003.80,1052.35]
data['PH24'] = [84,-1,'WGS84','34J',6601096.00,541018.40,1052.27]
data['PH25'] = [100,-1,'WGS84','34J',6601096.00,541033.00,1052.29]
data['PH26'] = [85,-1,'WGS84','34J',6601096.00,541047.60,1052.28]
data['PH27'] = [54,-1,'WGS84','34J',6601096.00,541062.20,1052.32]
data['PH37'] = [17,-1,'WGS84','34J',6601108.64,541011.10,1052.19]
data['PH38'] = [68,-1,'WGS84','34J',6601108.64,541025.70,1052.27]
data['PH39'] = [62,-1,'WGS84','34J',6601108.64,541040.30,1052.15]
data['PH40'] = [0,-1,'WGS84','34J',6601108.64,541054.90,1052.21]
data['PH52'] = [2,-1,'WGS84','34J',6601121.29,541018.40,1052.04]
data['PH53'] = [21,-1,'WGS84','34J',6601121.29,541033.00,1052.06]
data['PH54'] = [45,-1,'WGS84','34J',6601121.29,541047.60,1052.04]
data['PI1'] = [61,-1,'WGS84','34J',6601297.98,541025.46,1050.46]
data['PI10'] = [70,-1,'WGS84','34J',6601269.68,541051.49,1050.86]
data['PI11'] = [56,-1,'WGS84','34J',6601264.30,541062.70,1051.00]
data['PI12'] = [71,-1,'WGS84','34J',6601256.15,541066.53,1051.01]
data['PI13'] = [59,-1,'WGS84','34J',6601248.01,541075.19,1051.13]
data['PI14'] = [23,-1,'WGS84','34J',6601238.91,541070.59,1051.06]
data['PI15'] = [50,-1,'WGS84','34J',6601233.81,541080.71,1051.15]
data['PI16'] = [38,-1,'WGS84','34J',6601227.86,541065.71,1051.16]
data['PI17'] = [26,-1,'WGS84','34J',6601223.65,541064.08,1051.29]
data['PI18'] = [87,-1,'WGS84','34J',6601218.44,541047.60,1051.20]
data['PI19'] = [103,-1,'WGS84','34J',6601210.09,541048.01,1051.42]
data['PI2'] = [63,-1,'WGS84','34J',6601293.37,541014.05,1050.67]
data['PI20'] = [42,-1,'WGS84','34J',6601194.45,541024.57,1051.35]
data['PI21'] = [15,-1,'WGS84','34J',6601188.31,541014.75,1051.43]
data['PI22'] = [99,-1,'WGS84','34J',6601197.15,540989.20,1051.35]
data['PI23'] = [1,-1,'WGS84','34J',6601202.09,541004.20,1051.41]
data['PI24'] = [47,-1,'WGS84','34J',6601208.50,540991.94,1051.20]
data['PI25'] = [83,-1,'WGS84','34J',6601212.70,540998.57,1051.32]
data['PI26'] = [37,-1,'WGS84','34J',6601214.55,540982.91,1051.15]
data['PI27'] = [4,-1,'WGS84','34J',6601219.63,540981.56,1051.11]
data['PI28'] = [90,-1,'WGS84','34J',6601232.06,540978.85,1051.16]
data['PI29'] = [82,-1,'WGS84','34J',6601237.61,540979.69,1051.11]
data['PI3'] = [67,-1,'WGS84','34J',6601285.51,541012.14,1050.59]
data['PI30'] = [98,-1,'WGS84','34J',6601239.31,540974.05,1051.00]
data['PI31'] = [74,-1,'WGS84','34J',6601243.03,540986.50,1051.05]
data['PI32'] = [106,-1,'WGS84','34J',6601250.36,540982.98,1050.83]
data['PI33'] = [116,-1,'WGS84','34J',6601277.50,540926.63,1050.53]
data['PI34'] = [115,-1,'WGS84','34J',6601256.70,540880.69,1050.68]
data['PI35'] = [114,-1,'WGS84','34J',6601235.90,540877.88,1050.87]
data['PI36'] = [113,-1,'WGS84','34J',6601215.10,540875.07,1051.05]
data['PI37'] = [112,-1,'WGS84','34J',6601194.30,540872.25,1051.25]
data['PI38'] = [127,-1,'WGS84','34J',6601173.50,540869.44,1051.45]
data['PI39'] = [41,-1,'WGS84','34J',6601167.86,540930.80,1051.53]
data['PI4'] = [58,-1,'WGS84','34J',6601279.50,541018.80,1050.61]
data['PI40'] = [16,-1,'WGS84','34J',6601133.93,540981.90,1051.94]
data['PI41'] = [13,-1,'WGS84','34J',6601158.00,541041.84,1051.80]
data['PI42'] = [46,-1,'WGS84','34J',6601121.29,541091.40,1052.04]
data['PI43'] = [124,-1,'WGS84','34J',6601083.36,541142.50,1052.44]
data['PI44'] = [123,-1,'WGS84','34J',6601146.58,541149.80,1051.87]
data['PI45'] = [122,-1,'WGS84','34J',6601171.90,541103.18,1051.62]
data['PI46'] = [57,-1,'WGS84','34J',6601184.51,541098.70,1051.60]
data['PI47'] = [121,-1,'WGS84','34J',6601192.70,541100.71,1051.37]
data['PI48'] = [120,-1,'WGS84','34J',6601213.50,541100.07,1051.20]
data['PI49'] = [119,-1,'WGS84','34J',6601234.30,541098.19,1050.99]
data['PI5'] = [3,-1,'WGS84','34J',6601276.86,541029.51,1050.75]
data['PI50'] = [118,-1,'WGS84','34J',6601259.10,541095.68,1050.83]
data['PI6'] = [73,-1,'WGS84','34J',6601285.12,541035.74,1050.72]
data['PI7'] = [66,-1,'WGS84','34J',6601284.89,541043.32,1050.59]
data['PI8'] = [117,-1,'WGS84','34J',6601279.90,541042.88,1050.61]
data['PI9'] = [49,-1,'WGS84','34J',6601280.54,541056.50,1050.70]
data['PPA10'] = [28,-1,'WGS84','34J',6601156.75,541024.09,1051.65]
data['PPA12'] = [34,-1,'WGS84','34J',6601156.81,541054.13,1051.70]
data['PPA14'] = [51,-1,'WGS84','34J',6601156.86,541084.09,1051.74]
data['PPA6'] = [19,-1,'WGS84','34J',6601156.78,540964.09,1051.68]
data['PPA8'] = [29,-1,'WGS84','34J',6601156.82,540994.09,1051.66]
data['PPE10'] = [93,-1,'WGS84','34J',6601140.80,541024.11,1051.82]
data['PPE12'] = [94,-1,'WGS84','34J',6601140.82,541054.10,1051.87]
data['PPE14'] = [95,-1,'WGS84','34J',6601140.83,541084.15,1051.85]
data['PPE6'] = [91,-1,'WGS84','34J',6601140.81,540964.11,1051.86]
data['PPE8'] = [92,-1,'WGS84','34J',6601140.81,540994.13,1051.81]
data['SA11'] = [55,-1,'WGS84','34J',6601156.75,541039.09,1051.70]
data['SA13'] = [27,-1,'WGS84','34J',6601156.81,541069.13,1051.69]
data['SA5'] = [25,-1,'WGS84','34J',6601156.76,540949.12,1051.69]
data['SA7'] = [48,-1,'WGS84','34J',6601156.78,540979.09,1051.62]
data['SA9'] = [24,-1,'WGS84','34J',6601156.82,541009.09,1051.66]
data['SC10'] = [77,-1,'WGS84','34J',6601148.77,541024.11,1051.71]
data['SC11'] = [32,-1,'WGS84','34J',6601148.77,541039.11,1051.84]
data['SC12'] = [78,-1,'WGS84','34J',6601148.80,541054.08,1051.77]
data['SC13'] = [30,-1,'WGS84','34J',6601148.80,541069.08,1051.81]
data['SC14'] = [79,-1,'WGS84','34J',6601148.84,541084.11,1051.78]
data['SC5'] = [35,-1,'WGS84','34J',6601148.77,540949.14,1051.78]
data['SC6'] = [75,-1,'WGS84','34J',6601148.75,540964.11,1051.73]
data['SC7'] = [18,-1,'WGS84','34J',6601148.75,540979.11,1051.72]
data['SC8'] = [76,-1,'WGS84','34J',6601148.80,540994.13,1051.74]
data['SC9'] = [5,-1,'WGS84','34J',6601148.80,541009.13,1051.72]
data['SE11'] = [7,-1,'WGS84','34J',6601140.80,541039.11,1051.87]
data['SE13'] = [12,-1,'WGS84','34J',6601140.82,541069.10,1051.80]
data['SE5'] = [33,-1,'WGS84','34J',6601140.78,540949.13,1051.80]
data['SE7'] = [6,-1,'WGS84','34J',6601140.81,540979.11,1051.82]
data['SE9'] = [52,-1,'WGS84','34J',6601140.81,541009.13,1051.82]
data['SG10'] = [109,-1,'WGS84','34J',6601132.83,541024.09,1051.89]
data['SG11'] = [60,-1,'WGS84','34J',6601132.83,541039.09,1051.91]
data['SG12'] = [110,-1,'WGS84','34J',6601132.84,541054.10,1051.93]
data['SG13'] = [39,-1,'WGS84','34J',6601132.84,541069.10,1051.91]
data['SG14'] = [111,-1,'WGS84','34J',6601132.84,541084.13,1051.90]
data['SG5'] = [8,-1,'WGS84','34J',6601132.78,540949.12,1051.91]
data['SG6'] = [107,-1,'WGS84','34J',6601132.81,540964.13,1051.96]
data['SG7'] = [11,-1,'WGS84','34J',6601132.81,540979.13,1051.92]
data['SG8'] = [108,-1,'WGS84','34J',6601132.84,540994.12,1051.89]
data['SG9'] = [36,-1,'WGS84','34J',6601132.84,541009.12,1051.90]

sorted_keys = sorted(data.keys())

parser = mc.get_mc_argument_parser()
args = parser.parse_args()
db = mc.connect_to_mc_db(args)

for k in sorted_keys:
    d = geo_location.GeoLocation()
    d.station_name = k
    d.station_number = data[k][0]
    d.future_station_number = data[k][1]
    d.datum = data[k][2]
    d.tile = data[k][3]
    d.northing = data[k][4]
    d.easting = data[k][5]
    d.elevation = data[k][6]
    print(d)
    with db.sessionmaker() as session:
        session.add(d)

session.commit()
