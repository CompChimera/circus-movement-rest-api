"""
blocklist.py

This file just contains the blocklist of the JWT toekns. It will be imported by app and the logout resource so that tokens can be added to the blocjklist when the user logs out.

TODO: Should be in a db. Something like redis maybe.  
"""

BLOCKLIST = set()