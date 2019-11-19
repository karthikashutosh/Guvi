starting_point=int(input("enter the starting point:"))
ending_point=int(input("enter the ending point:"))
total_distance=ending_point-starting_point

if(total_distance>5):
 basic_fare =((total_distance-5)*8)+100
else:
 basic_fare=100
peak_time=int(input("enter 1 for peak time and 0 for normal time="))
if(peak_time==1):
 total_fare=basic_fare+(0.25*basic_fare)
 print(total_fare)
else:
 print(basic_fare)
 
