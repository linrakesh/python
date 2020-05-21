import csv
records =[ 
    ["ID", "name", "Price", "Qty"],
          ["102","LG Monitor","6500","20"],
          ["103","KeyBoard","1350","156"],
          ["105","Hp Mouse","650","120"],
          ["106","Speaker","1670","136"]
]

f = open("stock.csv","w")
csvwriter = csv.writer(f,lineterminator="\n")
# csvwriter.writerow(header)
csvwriter.writerows(records)
f.close()
print("Check your file now....")
