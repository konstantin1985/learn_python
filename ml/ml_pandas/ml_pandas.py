# http://pythonforengineers.com/introduction-to-pandas/









# We'll read the file again, this time passing in a new
# variable sep = '\t', which tells Pandas the separator
# is tabs, not commas.
data = pd.read_csv("wages_hours.csv", sep = "\t")

# For this project, we will only look at age vs rate
# (salary). The first thing we need to do is extract
# those two fields from the dataframe.
data2 = data[["AGE", "RATE"]]

# We'll go for ascending (which is the default behaviour
# of the sort() function).
data_sorted = data2.sort(["AGE"])
data_sorted.head()

