#Assignment4
#Q1 & Q2
##This is my assignment4 for big data.
##The code will generate two files with each line including a increasing number:
* ###1.txt
!["1"](/1.jpeg "result for 1000")
* ###2.txt
!["2"](/2.jpeg "result for 1000000")

//
time1: 18 seconds.
time2: 21 seconds.
no,reason:time2/time1=1.166667
mapreduce runs the tasks on a lot of machines simultaneously.

#Q3
time1: 0.0003376007080078125 seconds.
time2: 0.30457377433776855 seconds.
python program (without using mapreduce) that runs in a single computer is faster. Because the amount of data is too small. when data size is small, it spends more time transfering data to other machines. If the amount of data is larger than 10 billon, mapreduce will work more efficient.
