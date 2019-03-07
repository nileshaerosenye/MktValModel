#! /bin/sh


count=0
while read line
do
	# Else for all tickers we write them to a file
	#echo -n "Processing $count\r"
	count=$(expr $count + 1)

	ticker=$(echo $line | awk -F "," '{print $1}')
	echo "$count | $ticker"

	# CURL from Stockpup and store the csv into rawCSV directory
	$( curl get www.stockpup.com/data/${ticker}_quarterly_financial_data.csv > ../rawCSV/${ticker}.csv 2>/dev/null  )

	sleep 1

done < ../data/Sym_500000000.csv
