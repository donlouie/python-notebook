def past(h, m, s):
    # Good Luck!
    return h*60*60*1000+m*60*1000+1000*s

# * Other Solution
# Solution 1


def past(h, m, s):
    return (3600*h + 60*m + s) * 1000
