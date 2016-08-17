Python pielietojumi fizikā
===========================
Šajā repo ir atrodami ipython-notebook faili, kuri pārsvarā iegūti izsijājot, Github hostēto. No manis šeit ir atrodami piemēri, kā es izmantoju python, lai apstrādātu laboratorijas datus, un viens kopsavilkums, kam vajadzētu kalpot kā formulu lapai.
______________________________

##Laboratorijas apstrādei

Esmu iekļāvis:
+ datu ielasīšanu no teksta faila
+ to attēlošana grafikā
+ jaunas kolonnas aprēķināšana
+ brīvi izvēlētas funkcijas piekārtošana datiem:
	- parametru noteikšana funkcijai, lai X^2 vērtība būtu minimāla
	- kovariācijas matricas noteikšana
	- funkcijas līknes attēlošana uz datiem


##Izmantošana
Visi faili atrodās uz GitHub, bet ne visi atrodās iekš manā repo, jo citādi nevarētu nodrošināt vienmēr jaunāko materiālu. Tādēļ, lai iegūtu šī repo saturu jāizpilda komandrindiņā sekojoša komanda:

+ **git clone --recursive https://github.com/akels/python-visur.git**

Kur *--recursive* norāda, ka tiks lejuplādētas arī mapes, kuras norāda uz citiem repo.

Lai atvērtu, kādu no *.ipynb* failiem izpildām komandu:

+ **ipython-notebook '/vieta/kur/atrodās/fails.ipynb'**

##Nokonfigurēšana uz Ubuntu

Izmantotās pakas:

+ numpy
+ scipy
+ matplotlib
+ pandas
+ sympy
+ ipython-notebook
+ ipython-qtconsole

Tā kā pakas - *numpy*, *scipy*, *matplotlib* - ir savstarpēji atkarīgas, tad pietiek ar komandu:

*sudo apt-get install* **python-scipy python-pandas python-sympy ipython-notebook ipython-qtconsole**
______________________________

##Papildus literatūra:

+ http://www.loria.fr/~rougier/teaching/matplotlib/
+ http://pandas.pydata.org/pandas-docs/stable/basics.html
