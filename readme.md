<h2>News reporting is a text report that was written to answer the following question.</h2></br>
-Most popular three articles of all time : Title - Views</br>
-Most accessed articles of all time : Title - Views</br>
-Most popular authors : Author - Views</br>
-Failure % above 1 % by date: Date | Failure %</br>


Prerequisites:
Have the news database installed

Popluate the news database by downloading and unziping newsdata.zip then run the following command in your terminal. 
    psql -d news -f newsdata.sql
    
Now that you have data it time to create the psql views need to run the program. Run the following command in your terminal.

psql -d news -f newsdata.sql

Running the program:

Once the view are created place newsreportingtool.py in your python environment then run python newsreportingtool in the terminal.

To see an example of the output open output.txt.


