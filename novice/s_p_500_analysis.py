from __future__ import unicode_literals
from fuzzywuzzy import fuzz,process,string_processing,utils
import pdb
from datetime import datetime, timedelta

def find_mapped_forbes_2000():
    forbes_2000_file=open('/home/matt/Desktop/Industry_Ratings/data/Forbes_Global_2000_2013.csv','rb')
    mapped_entities_file=open('/home/matt/Desktop/Industry_Ratings/data/entities.csv','rb')
    matches_file=open('/home/matt/Desktop/Industry_Ratings/data/matches_name.csv','w')

    count = 0
    #lines = sum(1 for line in forbes_2000_file)
    #print "number of forbes lines: ", lines
    #forbes_2000_file.seek(0)
    for line in forbes_2000_file:
        #print "in outer loop"
        forbes_2000_company = line.decode('utf-8').split(",")
        mapped_entities_file.seek(0)
        matched_entity = "--,--"
        for item in mapped_entities_file:
            #print "in inner loop"
            mapped_entity = item.decode('utf-8').split(",")
            forbes_processed = utils.full_process(forbes_2000_company[0])
            entity_processed = utils.full_process(mapped_entity[1])
            if (fuzz.ratio(forbes_processed,entity_processed) > 85):
                #print forbes_processed, entity_processed
                matched_entity = mapped_entity[0] + "," + string_processing.StringProcessor.strip(mapped_entity[1])
                count +=1
                break
        match = forbes_2000_company[0] + "," + forbes_2000_company[2] + "," + matched_entity + "," + forbes_2000_company[8]
        print match.encode('utf-8')
        matches_file.write(match.encode('utf-8'))
    forbes_2000_file.close()
    mapped_entities_file.close()
    matches_file.close()
    print "total matches: ", count

def find_mapped_S_P_500():
    s_p_500_file=open('/home/matt/Desktop/Industry_Ratings/data/S_P_500_2013.csv','rb')
    mapped_entities_file=open('/home/matt/Desktop/Industry_Ratings/data/entities.csv','rb')
    matches_file=open('/home/matt/Desktop/Industry_Ratings/data/s_p_500_matches_name.csv','w')

    count = 0
    #lines = sum(1 for line in forbes_2000_file)
    #print "number of forbes lines: ", lines
    #forbes_2000_file.seek(0)
    for line in s_p_500_file:
        #print "in outer loop"
        print line
        mapped_entities_file.seek(0)
        matched_entity = "--,--,"
        for item in mapped_entities_file:
            #print "in inner loop"
            mapped_entity = item.decode('utf-8').split(",")
            s_p_500_processed = utils.full_process(line)
            entity_processed = utils.full_process(mapped_entity[1])
            if (fuzz.ratio(s_p_500_processed,entity_processed) > 85):
                #print forbes_processed, entity_processed
                matched_entity = mapped_entity[0] + "," + string_processing.StringProcessor.strip(mapped_entity[1]) + ","
                count +=1
                break
        match =   matched_entity + line
        #hereprint match.encode('utf-8')
        matches_file.write(match.encode('utf-8'))
    s_p_500_file.close()
    mapped_entities_file.close()
    matches_file.close()
    print "total matches: ", count

def analyze_all_s_p_500_events():
    s_p_500_file=open('/home/matt/Desktop/Industry_Ratings/data/s_p_500_all_events.csv','rw')
    analyzed_file=open('s_p_500_analysis.csv','w')
    botnet_count = []
    event_count = []
    jan_count = 0
    feb_count = 0
    mar_count = 0
    apr_count = 0
    may_count = 0
    jun_count = 0
    jul_count = 0
    aug_count = 0
    sep_count = 0
    oct_count = 0
    nov_count = 0
    dec_count = 0
    epoch_date = datetime.strptime('1970-01-01', '%Y-%m-%d')
    entity_ids = [30,34,36,38,39,40,42,48,64,71,72,86,88,90,97,113,124,130,138,144,157,168,185,186,191,194,202,207,227,228,229,231,232,233,235,236,238,239,241,242,244,245,251,252,253,255,256,261,264,266,269,277,278,280,282,292,293,294,295,296,297,303,316,317,319,320,321,323,324,325,326,337,346,347,348,361,362,372,373,375,378,383,384,385,385,386,387,388,389,390,391,392,393,394,396,397,400,401,403,404,405,407,408,413,414,415,422,433,434,435,436,437,440,441,442,444,451,459,460,464,480,518,528,533,534,535,537,538,541,542,543,544,547,548,549,560,561,565,568,570,577,578,587,588,592,593,594,595,598,599,602,604,605,607,608,609,612,613,614,617,619,620,621,622,624,626,627,631,633,638,639,644,645,649,650,654,657,658,660,661,662,665,666,668,671,672,673,677,683,687,688,691,694,695,696,698,699,700,701,704,707,712,713,717,721,726,727,730,731,732,733,734,735,737,738,739,742,743,744,745,746,747,749,750,751,752,753,754,755,756,757,760,763,764,768,769,770,771,773,775,777,779,780,783,784,787,788,789,791,793,795,799,800,801,802,803,804,806,807,809,811,813,815,816,818,819,821,822,823,824,825,830,834,835,836,837,838,839,840,844,845,850,851,852,853,854,856,858,859,861,862,863,865,869,872,874,876,879,880,881,882,885,887,889,891,892,893,894,897,898,904,905,911,913,914,921,923,929,931,935,936,942,943,945,949,950,951,952,955,956,957,958,962,965,974,984,986,987,988,990,995,998,1004,1005,1006,1032,1044,1056,1057,1061,1070,1073,1081,1085,1094,1100,1101,1102,1104,1107,1125,1128,1132,1133,1143,1146,1150,1153,1154,1161,1168,1169,1174,1185,1204,1226,1232,1241,1245,1248,1250,1266,1278,1283,1304,1310,1345,1375,1400,1422,1432,1444,1461,1466,1539,1561,1593,1594,1597,1604,1622,1643,1665,1686,1697,1703,1713,1763,1768,1800,1924,1946,68140,68160,68215,68263,68269,68286,68304,68307,68323,68332,68358,68384,77015,77067,77087,77276,77354,77439,77509,77642,77967,77969,78396,79009,79322,79450,79484,79627,79745,79879,79887,79896,79939,80153,80372,80419,80444,80557,81068,81307,81374,81528,82208]
    #feb_count, mar_count, apr_count, may_count, jun_count, jul_count, aug_count, sep_count, oct_count, nov_count, dec_count = 0
    for line in s_p_500_file:
        daily_events = line.split(',')
        #print daily_events[0]
        event_date = epoch_date + timedelta(int(daily_events[0]))
        #line_to_write = str(event_date)+','+line
        #analyzed_file.write(line_to_write)
        if str(daily_events[2])=='BOTNET':
            #print int(daily_events[1])
            if event_date.month == 1:
                jan_count += int(daily_events[3])
            if event_date.month == 2:
                feb_count += int(daily_events[3])
            if event_date.month == 3:
                mar_count += int(daily_events[3])
            if event_date.month == 4:
                apr_count += int(daily_events[3])
            if event_date.month == 5:
                may_count += int(daily_events[3])
            if event_date.month == 6:
                jun_count += int(daily_events[3])
            if event_date.month == 7:
                jul_count += int(daily_events[3])
            if event_date.month == 8:
                aug_count += int(daily_events[3])
            if event_date.month == 9:
                sep_count += int(daily_events[3])
            if event_date.month == 10:
                oct_count += int(daily_events[3])
            if event_date.month == 11:
                nov_count += int(daily_events[3])
            if event_date.month == 12:
                dec_count += int(daily_events[3])
    print jan_count,feb_count,mar_count,apr_count,may_count,jun_count,jul_count,aug_count,sep_count,oct_count,nov_count,dec_count
        
        
            
            
        
    
