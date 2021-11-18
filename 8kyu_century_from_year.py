def century(year):return(int(str(year).zfill(4)[:2]),int(str(year).zfill(4)[:2])+1)[year%100>0]
