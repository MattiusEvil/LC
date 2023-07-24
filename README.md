# LC
Life-Checker that will help me to organize my time better

I start making this app after I understood, that my time are very unorganized. So in the end of this project I wish take easy run application that will help me control my time better than before.

Work book:
1. In start of the work I thought how to make logic that will do those work that I need. So the algorithm is not so smart cause it is just notificator that make activities with the databases. The logic can be described by the sending formated time from text form or button and this values will throw in the database by postgresql. There will be ablitity to see database as a table and delete rows from the table.
2. After making plan and some simple functions I had started work for interface. The most simple way to make gui in the python is the PySimpleGUI. After fast investigation of this modele I start make small window with the forms and buttons. This stage was the easy so I started work foor another moment.
3. After that I workerd with postresql and maked some functions that send data, get rows from the database. System work in the local machine on "timekeeper" database and "times" table. Rows when my waste time less that halfhour also lighting like green. And for last in the DB block needed to sat about format of time. In the database and in the python type of the value is the float value but I need make tha "00:00" format. I want to say about ":" indead ".". I maked it in the format function that check value and with sending and taking value make it for right format.
4. Also I maked button for view of the table and functions that delete rows and table. This was called some problems, for example is that I wnted make disable button untill the user clicked on the row and ablity of updating values of PySimpleGUI was the problem for me, but not now.
5. In the last hard work was the probles of autowork in the 18:00 for localtime. For resolved was used standart python libraries (datetime and time). Also I used the "shedule". By the suffering of date types anyway I finished installation of time setting and for end I must do the designt moment.
6. Design is not my powerfull side, but I tries make some primitive things that will may me to use this application without pain for my eyes. I put picture for welcome window and make the table window more pretty
7. Testing anyway is not for me today, so I solved that other problems I will take for later)


Problems:
-Optimizitaion
-Design
-New functions
/More settings
/Work with the time: timezone, more work with time data in the table
/Autonomity: json way and other details

