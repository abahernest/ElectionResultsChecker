The Software is an Election Result Checker.
It shows the election results per polling unit and wards in each LGA.

It uses a database which contains dummy results for the 2011 electiions from different polling units, wards, and LGA.
The hierachy of Organization is as follows, from top to bottom
States > LGAs > Wards > Polling Units

The central idea behind the software is that, given all the individual results announced in polling units (announced_pu_results) under any LGA, we should be able to get
anestimated result for that LGA, which can then be cross-checked with the result announced at the local government level (announced_lga_results)

UNDERSTANDING THE DATABASE:
Below are the Tables in the database and what they represent

'POLLING_UNIT' : contains a list of polling units (each polling unit has a ward ID, LGA ID, and state ID)
'WARD': contains a list of wards
'LGA': contains a list of LGA
'ANNOUNCED_PU_RESULTS': contains dummy results of various polling units, with results from each polling unit stored on about 9 rows with the score
from each party being the individual rows. i.e for polling_unit_uniqueid =8, we have results as follows: PDP:802, DPP:719, ACN:416,PPA:939,CDC:394,JP:

NB: 'polling_unit'.uniqueid == 'announced_pu_results'.uniqueid
    polling_unitid != polling_unit_uniqueid
    
'ANNOUNCED_LGA_RESULTS': contains dummy results of various local governments as announced at the local government coalition center


The Software contains 4 web pages

1. Landing/ Welcome Page
2. PU Results: Displays the result for any individual polling unit based on the input provided
3. LGA Results: Displays the summed total results of all the polling units under any particular local government. NOTE: performed sum of each result from separate polling units and not results from the 'announced_lga' table
4. New PU: For entering results for all parties of a new polling unit
