from hl7_to_dict import hl7_str_to_dict
#from confluent_kafka import Producer
import time
import json

#Set up my producer 
#p = Producer({'streams.producer.default.stream': '/hl7stream'})

str_msg=''
with open("input.txt") as f:
    for line in f:
        if line!='\n': 
            # Need to replace first line with a better one so parsers work
	    if line.find('MSH')>-1:
	        line="MSH|^~\&|LCS|LCA|LIS|TEST9999|2018||ORU^R01|HP146238639119566933|P|"+ '\n'
            # Now - Strip out the copy/pasted literal \r
            if line.find('\n')>-1:
                line=line[:-3] + '\n'
            str_msg=str_msg+line
        else:
            print(str_msg[:-1])
            # Put our json encoding and/or producer code here
            #p.produce('topic1', str_msg)
            # Or - just do a json.dumps(your_json) instead of str_msg
            #p.flush()
            d = hl7_str_to_dict(str_msg[:-1])
            print json.dumps(d)
            str_msg=''
            time.sleep(10)

