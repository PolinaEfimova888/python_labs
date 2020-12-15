import re
for item in range(1,7) :
  f = open('figure'+str(item)+'.txt')
  object_size = f.readline()
  f.readline
  all_units = []
  max_size = 0
  all_units_in_line = []
  while(f.readline()):
            all_units.append(f.readline())
  for units in all_units:
    temp=0
    temp =[ temp+1for unit in units if unit=='1']
    all_units_in_line.append(len(temp) if len(temp)>0 else 0)

  print(float(object_size)/float(max(all_units_in_line))) if max(all_units_in_line)>0 else print('does not exist') 
