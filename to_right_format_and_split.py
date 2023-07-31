import pandas as pd

import pandas as pd

source, dest = input().split()
df = pd.read_csv(source, header=None)
df.columns = ['path_file1', 'start1', 'end1', 'path_file2', 'start2', 'end2']
df['name_file1'] = df['path_file1'].apply(lambda x : x.split('/')[-1])
df['name_file2'] = df['path_file2'].apply(lambda x : x.split('/')[-1])
df['par_dir1'] = df['path_file1'].apply(lambda x : x.split('/')[-2])
df['par_dir2'] = df['path_file2'].apply(lambda x : x.split('/')[-2])
new_df = df[['par_dir1', 'name_file1', 'start1', 'end1', 'par_dir2', 'name_file2', 'start2', 'end2']]
new_df1 = new_df[new_df['start1'] % 2 == 1]
new_df2 = new_df[new_df['start1'] % 2 == 0]

new_df1.to_csv(dest + '1', sep=',', index=False, header=False)
new_df2.to_csv(dest + '2', sep=',', index=False, header=False)
