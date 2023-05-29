# https://www.geeksforgeeks.org/performing-google-search-using-python-code/


try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

# to search
query = "LAKE UTOPIA PAPER LIMITED"
splitter = query.split(' ')
print(len(splitter))

pert_links = []
for each in search(query, tld="co.in", num=10, stop=10, pause=2):
    for each_word in splitter:
        ew_l = each_word.lower()
        if ew_l in each:
            if each not in pert_links:
                pert_links.append(each)
print('\n')
for each in pert_links:
    print(each)

#
def gt_links():
    pass

