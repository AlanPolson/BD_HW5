# BD_HW5
My HW5 on DUMBO
and on cluster

note:
to debug on bash, run the following command:

cat citibike.csv | ./mapper.py | sort -k 1,1 | ./reducer.py >output
