progdir = 'D:/Academic/Project/Graduation/'
datadir = 'D:/data/Graduation/'

# ===================
# namelist for model
# ===================

d01name = 'CN27GD_182X138'
d02name = 'CN9GD_98X74'
d03name = 'CN3GD_152X110'

# time range
def get_STR(year,month):
    if month == "Jul":
        STR = f'{year}-07-01T00'
    elif month == "Sep":
        STR = f'{year}-09-01T00'
    return STR

def get_END(year,month):
    if month == "Jul":
        END = f'{year}-07-31T23'
    elif month == "Sep":
        END = f'{year}-09-30T23'
    return END


# ===================
# namelist for fnl composite (abandoned)
# ===================

demodir = datadir + 'FNL/test/'
batchdir = datadir + 'FNL/test_batch_read/'

# ===================
# namelist for data preprocess
# ===================

grid_d01 = datadir + 'GRID/GRIDCRO2D_D01.nc'
grid_d02 = datadir + 'GRID/GRIDCRO2D_D02.nc'
grid_d03 = datadir + 'GRID/GRIDCRO2D_D03.nc'

CB_Sep = datadir + 'COMBINE/Sep/'
CB_Jul = datadir + 'COMBINE/Jul/'

# ===================
# namelist for processed data
# ===================

processed_dir = datadir + 'processed/'