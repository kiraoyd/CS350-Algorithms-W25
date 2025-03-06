def ffloyds(table, total_nodes):
    road_block = 0
    #for every roadblock lifted...
    while road_block < total_nodes:
        r = 0
        #for each row...
        while r < total_nodes:
            c = 0
            #for each column...
            while c < total_nodes:
                #as long as we are not looking at a road_block row/column, or the self-edge diagonal
                if r != c and r != road_block and c != road_block:
                    #does lifting the road_block get us a better path?
                    if table[r][road_block] + table[road_block][c] < table[r][c]:
                        table[r][c] = table[r][road_block] + table[road_block][c]
                c += 1
            r+=1
        road_block += 1


