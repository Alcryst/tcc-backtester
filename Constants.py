"""
Texas Capital Collective In-House Backtester Constants
@date-created: 03/2024
@last-modified: 03/2024
"""

HOURS_IN_DAY = 24
MINUTES_IN_HOUR = 60

##################
#     PRICING    #
##################
OPEN = "open"
CLOSE = "close"
HIGH = "high"
LOW = "low"

##################
# TIME INTERVALS #
##################
# a map of interval string representations their floating point value in terms of days
#        i.e.: { rep: val } where n / val yields the number of intervals in n days
"""
@TODO: not sure about { 1wk, 1mo, 3mo } if we only count the days the market are open,
     someone should take a look and adjust the values
"""
INTERVALS = {'1m': 1 / (HOURS_IN_DAY * MINUTES_IN_HOUR),
             '2m': 2 / (HOURS_IN_DAY * MINUTES_IN_HOUR),
             '5m': 5 / (HOURS_IN_DAY * MINUTES_IN_HOUR),
             '15m': 15 / (HOURS_IN_DAY * MINUTES_IN_HOUR),
             '30m': 30 / (HOURS_IN_DAY * MINUTES_IN_HOUR),
             '60m': HOURS_IN_DAY,
             '90m': 90 / (HOURS_IN_DAY * MINUTES_IN_HOUR),
             '1h': HOURS_IN_DAY,
             '1d': 1,
             '5d': 5,
             '1wk': 7,
             '1mo': 30,
             '3mo': 90}

##################
#      ERRORS    #
##################
INVALID_TIME_INTERVAL = ValueError("Invalid Time Interval: Not enough time between start and end date")
INVALID_STEP_INTERVAL = ValueError("Invalid Step Interval")
