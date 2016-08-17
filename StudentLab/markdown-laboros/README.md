#Laboratorijas darbu Markdown noformēšanas paraugs

Šajā repo atrodami faili, kurus izmantoju, lai noformētu laboratorijas darbu iekš Markdown.

--------------------------------------

##Markdown plusi:

+ Nav nepieciešams pārzināt n-tās LaTex komandas
+ Acij patīkamāks
+ Tiek izmantots http://physics.stackexchange.com/ tādēļ var *Ctr-c + Ctr-v* 
+ Viegli eksportējams html formātā

##Izmantošana:
Tā kā šie faili atrodās uz GitHub, tad visus šeit atrodamos failus var iegūt divejādi:
+ kreisajā augšējā stūrī nolādēt ZIP failu
+ No komandrindiņas:

	**git clone https://github.com/akels/markdown-laboros.git**

Kas izveidos mapi ar nosaukumu latex-laboros tajā vietā, no kuras tiek izsaukta komanda, ko var mainīt ar **cd** un redzēt ar **ls**.

+ Lai nokompilētu dokumentu:
	
	**make**

+ Ja vēlamies failu ar citu nosaukumu, tad rediģējam Makefile pirmo rindiņu vai arī **make** izpildām ar argumentu:
	
	**make Labors.pdf**
 
##Nokonfigurēšana uz Ubuntu

Izmantotās pakas:
+ **pandoc**
+ **texlive-latex-recommended**
+ **texlive-xetex**
+ **make**

Tātad, lai nokonfigurētu uz Ubuntu pietiek terminālī ar komandu:

*sudo apt-get install* **pandoc texlive-latex-recommended texlive-xetex make**
