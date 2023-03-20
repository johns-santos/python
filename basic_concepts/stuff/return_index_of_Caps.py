def capital_indexes(str):
    list = []
    for count, value in enumerate(str):
        if value.isupper():
            list.append(count)
    print(list)
            
  
    
capital_indexes("TictActoE")