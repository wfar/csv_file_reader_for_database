# Python 3.7 2019
# opens, reads in a csv and creates insert statment in SQL


import csv


month_d = {"1": "JAN", "2": "FEB", "3": "MAR", "4": "APR", "5": "MAY", "6": "JUN",
         "7": "JUL", "8": "AUG", "9": "SEP", "10": "OCT", "11": "NOV", "12": "DEC" }



with open("Loan.csv", "r", newline = "") as my_file:
    file_read = csv.reader(my_file)

    count = 0
    for row in file_read:

        if count > 0:
        
            date_list = row[1].split("/")
            month = month_d.get( date_list[0] )
            date = "{}-{}-{}".format( date_list[1], month, date_list[2] )
                    
           
            print("Insert into Loan values (" + row[0] + ", " + "'" + date + "'" + ", " + "'" +
                  row[2] + "'" + ", " + row[3] + ", " + row[4] + ", " +
                  row[5] + ", " + "'" + row[6] + "'" + ", " + row[7] + ", " + row[8] + ");" )
            
        count += 1

    print( str(count - 1) + " rows have been printed!")
