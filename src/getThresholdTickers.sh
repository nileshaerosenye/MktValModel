#! /bin/sh

allTickersList=$1
threshold=$2
fOut="../data/Sym_${threshold}.csv"
echo "Sym,MktCap" > $fOut

if [ $# -ne 2 ]; then
	echo "Usage : $0 [Symbols list with MktCap] [threshold MktCap]"
	exit 1
fi

count=0
while read line
do
	mktCap=$(echo $line | awk -F "," '{print $2}')
	if [ $mktCap -lt $threshold ]; then
		echo ""
		echo "$count records written to $fOut"
		break
	fi

	# Else for all tickers we write them to a file
	echo $line >> $fOut
	echo -n "Processed: $count\r"

	count=$(expr $count + 1)
	
done < $allTickersList
