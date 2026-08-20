import pandas as pd
import matplotlib
import matplotlib.pyplot as plt


col_names = ["DEST", "1960", "1965","1970","1975","1980","1985","1990"] #,"1991",
#     "1992","1993","1994","1995","1996","1997","1998","1999","2000",
#     "2001","2002","2003","2004","2005","2006","2007","2008","2009",
#     "2010","2011"
# ]

df = pd.read_csv(
    '../DATA/energy_use_quad.csv',
    names=col_names,
    index_col=0,
    usecols=[0, 1, 2, 3, 4, 5, 6, 7],
)
print(df)
print('-' * 60)

df2 = df.transpose()
print(df2)
print('-' * 60)

print(df2.index)
print(df2.columns)

for header in 'Transportation', 'Industrial', 'Residential and commercial':
    plt.plot(df2[header], label=header)
plt.legend()
plt.show()
