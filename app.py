# Use the MySportsFeeds API to retrieve MLB info
# 1/27/2018 v3

# IMPORT
import requests
import json
# also import
from lineup import Lineup

'''
# FOR TESTS
# Red Sox ids
# ids = ['10300','11064','10303', '11339','10301','12551','10297','10296','11065']
# Yankee ids
#
'''

def main():
    ids = ['10300','11064','10303', '11339','10301','12551','10297','10296','11065']
    soxs = Lineup()
    print (soxs.create_lineup_dictionary(ids))

if __name__ == "__main__":
    main()

