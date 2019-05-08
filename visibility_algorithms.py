# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# AUTHOR: Delia Fano Yela
# DATE:  December 2018
# CONTACT: d.fanoyela@qmul.ac.uk
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Different implementations for computing the natural visibility graph (NVG) [1]
# and the horizontal visibility graph (HVG) [2].
# Here we only implement the undirected graphs versions.
# For the original implementation in Fortran 90/94 of both directed and undirected
# versions, please refer to [3].

# Here we can find two different implementations to compute the NVG and HVG
# of a given series of numbers:
#   1. The original implementation proposed in [3]
#   2. A divide and conquer (D&C) approach presented in [4]

# REFERENCES
# [1]: "From time series to complex networks: the visibility graph"
# Lucas Lacasa, Bartolo Luque, Fernando Ballesteros, Jordi Luque, Juan C. Nuno
# PNAS, vol. 105, no. 13 (2008) 4972-4975

# [2]: "Horizontal visibility graphs: exact results for random time series"
#Bartolo Luque, Lucas Lacasa, Jordi Luque, Fernando J. Ballesteros
#Physical Review E 80, 046103 (2009)

# [3]: http://www.maths.qmul.ac.uk/~lacasa/Software.html

# [4]: "Fast transformation from time series to visibility graphs"
# Xin Lan, Hongming Mo, Shiyu Chen, Qi Liu, and Yong decending
# Chaos 25, 083105 (2015); doi: 10.1063/1.4927835


# ------------------------------------------------------------------------------
# NATURAL VISIBILITY GRAPH ( NVG )
# ------------------------------------------------------------------------------
# a. BASIC IMPLEMENTATION
# --------------------------
def nvg(series, timeLine):
    # series is the data vector to be transformed
    # Get length of input series
    L = len(series)
    # timeLine is the vector containing the time stamps
    #if timeLine == None: timeLine = range(L)

    # initialise output
    all_visible = []


    for i in xrange(L-1):
        node_visible = []
        ya = float(series[i])
        ta = timeLine[i]

        for j in xrange(i+1,L):
            yb = float(series[j])
            tb = timeLine[j]

            yc = series[i+1:j]
            tc = timeLine[i+1:j]

            if all( yc[k] < (ya + (yb - ya)*(tc[k] - ta)/(tb-ta)) for k in xrange(len(yc)) ):
                node_visible.append(tb)

        if len(node_visible)>0 : all_visible.append([ta, node_visible])

    return all_visible

# b. DIVIDE & CONQUER
# --------------------------
def nvg_dc(series, timeLine, left, right, all_visible = None):

    #if timeLine == None : timeLine = range(len(series))
    if all_visible == None : all_visible = []

    node_visible = []

    if left < right : # there must be at least two nodes in the time series
        k = series[left:right].index(max(series[left:right])) + left

        # check if k can see each node of series[left...right]
        for i in xrange(left,right):
            if i != k :
                a = min(i,k)
                b = max(i,k)

                ya = float(series[a])
                ta = timeLine[a]
                yb = float(series[b])
                tb = timeLine[b]
                yc = series[a+1:b]
                tc = timeLine[a+1:b]

                if all( yc[j] < (ya + (yb - ya)*(tc[j] - ta)/(tb-ta)) for j in xrange(len(yc)) ):
                    node_visible.append(timeLine[i])

        if len(node_visible) > 0 : all_visible.append([timeLine[k], node_visible])

        nvg_dc(series,timeLine,left, k, all_visible = all_visible)
        nvg_dc(series,timeLine, k+1, right, all_visible = all_visible)

    return all_visible


# ------------------------------------------------------------------------------
# HORIZONTAL VISIBILITY GRAPH ( HVG )
# ------------------------------------------------------------------------------

# a. ORIGINAL IMPLEMENTATION
# --------------------------
def hvg(series, timeLine):
    # series is the data vector to be transformed
    #if timeLine == None: timeLine = range(len(series))
    # Get length of input series
    L = len(series)
    # initialise output
    all_visible = []

    for i in xrange(L-1):
        node_visible = []
        ya = series[i]
        ta = timeLine[i]
        for j in xrange(i+1,L):

            yb = series[j]
            tb = timeLine[j]

            yc = series[i+1:j]
            tc = timeLine[i+1:j]

            if all( yc[k] < min(ya,yb) for k in xrange(len(yc)) ):
                node_visible.append(tb)
            elif all( yc[k] >= max(ya,yb) for k in xrange(len(yc)) ):
                break

        if len(node_visible)>0 : all_visible.append([ta, node_visible])

    return all_visible


# b. DIVIDE & CONQUER HVG
# --------------------------
def hvg_dc(series,timeLine, left, right, all_visible = None):

    if all_visible == None : all_visible = []

    node_visible = []

    if left < right : # there must be at least two nodes in the time series
        k = series[left:right].index(max(series[left:right])) + left
        # check if k can see each node of series[left...right]

        for i in xrange(left,right):
            if i != k :
                a = min(i,k)
                b = max(i,k)

                ya = series[a]
                ta = timeLine[a]
                yb = series[b]
                tb = timeLine[b]
                yc = series[a+1:b]
                tc = timeLine[a+1:b]

                if all( yc[k] < min(ya,yb) for k in xrange(len(yc)) ):
                    node_visible.append(timeLine[i])
                elif all( yc[k] >= max(ya,yb) for k in xrange(len(yc)) ):
                    break

        if len(node_visible) > 0 : all_visible.append([timeLine[k], node_visible])

        hvg_dc(series,timeLine, left, k, all_visible = all_visible)
        hvg_dc(series,timeLine, k+1, right, all_visible = all_visible)

    return all_visible
