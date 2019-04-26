# encoding: utf8

import clusters


row_names, col_names, data = clusters.readfile('blogdata.txt')
best_matches = clusters.kcluster(data, k=5)
print best_matches

for row in best_matches:
    for row_id in row:
        print row_names[row_id]
    print '\n\n'
