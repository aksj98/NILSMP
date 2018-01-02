import csv
#import 
count=0
a=[]
b=[]
c=[]
d=[]
e=[]
f=[]
g=[]
h=[]
with open('securities.csv', newline='') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		date=str(row['Date first added'])
		ts= str(row['Ticker symbol'])
		sec=str(row['Security'])
		sec2=str(row['SEC filings'])
		gisc=str(row['GICS Sector'])
		gisc2=str(row['GICS Sub Industry'])
		add=str(row['Address of Headquarters'])
		cik=str(row['CIK'])
		if date=="":
			date="2001-01-01"
		a.append(ts)
		b.append(sec)
		c.append(sec2)
		d.append(gisc)
		e.append(gisc2)
		f.append(add)
		g.append(date)
		h.append(cik)
		count=count+1


with open('securities.csv','w',newline='') as csvfile:
	fieldnames=['Ticker symbol','Security','SEC filings','GICS Sector','GICS Sub Industry','Address of Headquarters','Date first added','CIK']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()
	for items in range(count):
		writer.writerow({'Ticker symbol':a[items],'Security':b[items],'SEC filings':c[items],'GICS Sector':d[items],'GICS Sub Industry':e[items],'Address of Headquarters':f[items],'Date first added':g[items],'CIK':h[items]})
		
	

