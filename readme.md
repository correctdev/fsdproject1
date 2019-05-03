News reporting is a text report that was written to answer the following question.

Prerequisites:
Have the news database installed

 to install the news database download newsdata.sql then run the following command in your terminal. 
    psql -d news -f newsdata.sql
    
Now that you have data it time to create the psql views need to run the program. Run the following command in your terminal.
psql -d news -f newsdata.sql

Running the program:

Once the view are created place newsreportingtool.py in your python environment then run python newsreportingtool in the terminal.

To see an example of the output open output.txt.


