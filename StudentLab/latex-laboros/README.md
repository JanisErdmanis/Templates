#Laboratorijas darbu LaTex noformēšanas paraugs

Šajā repo atrodami galvenie faili, kurus izmantoju, lai noformētu laboratorijas darbu iekš LaTex.

--------------------------------------
##Atrodamo failu atšifrējums:

+ *sagatave.sty*

	Satur informāciju par pievienotajiem moduļiem un noformējumu

+ *Labors.tex*
 
	Fails, kurš tiek rediģēts veidojot laboru

+ */build*

	Mape, kurā ievietota *sagatave.sty*, *LU logo* un arī nepieciešamie faili, lai izveidotu paraugdokumentu

##Izmantošana:
Tā kā šie faili atrodās uz GitHub, tad visus šeit atrodamos failus var iegūt divejādi:
+ kreisajā augšējā stūrī nolādēt ZIP failu
+ No komandrindiņas:

	**git clone https://github.com/akels/latex-laboros.git**
	
Kas izveidos mapi ar nosaukumu latex-laboros tajā vietā, no kuras tiek izsaukta komanda, ko var mainīt ar **cd** un redzēt ar **ls**.

##Latex nokonfigurēšana uz Ubuntu

+ Nepieciešamās pakas, lai darbs nokompilētos:
	
	 **texlive-xetex**
	 
	 **texlive-latex-recommended**

+ Tādēļ, lai nokonfigurētu uz Ubuntu pietiek terminālī ar komandu:
	
	*sudo apt-get install* **texlive-xetex texlive-latex-recommended**

+ Tagad, lai nokompilētu dokumentu izpildām komandu:

	**xelatex "/mapes/atrašanās/vieta/Labors.tex"**

Lai padarītu rakstīšanu praktiskāku varam izmantot *texmaker*, kuram iestatijumos pie build komandas nomainām *latex* pret *xelatex* 
