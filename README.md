Steps to get this to run:

1.  Clone the repo to the edge node.
2.  Run setup-environment.sh as user mapr ```bash setup-environment.sh```
3.  Run the "HL7toMapRStreams.py" (In Chris C repo) script to pick up a record, serialize to json, and write to the stream - maybe run this in a separate shell or ```python HL7toMapRStreams.py &```
4.  Run the "stream-to-db.py" script - this will wait for new records, and write the user info to mapr-DB
5.  Either in sqlline, or other tools, can use drill to query ```select * from dfs.`/user-table;```
