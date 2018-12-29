# risk-meetup-13-python-selenium
Repozitorijum posvecen radionici o automatizaciji testova u pythonu i seleniumu

Automatizacija procesa i pravilno održavanje koda ključan su faktor svake 
uspešne aplikacije ili servisa. Kako aplikacije tokom izmena moraju održati određen 
kvalitet i nivo bezbednosti, automatizacijom zamornih testova postižemo da u svakom trenutku naša aplikacija bude sigurna i da istovremeno testiramo stotine funkcionalnosti na više platformi.
Uz pomoć Seleniuma i Webdriver-a možemo lako to izvesti.

Na ovom predavanju biće reči o automatizaciji, Selenium-u u programskom jeziku Python, dobrim i lošim praksama pisanja održivog koda i testova, osnovnim konceptima struktuiranja koda prilikom testiranja (Page Object Model), kao i nekim konceptima razvoja aplikacija. Za kraj, biće reči i o pojedinim CI alatima, Gherkin sintaksi, Mocha i Chai bibliotekama.

Kroz malu radionicu i demonstraciju koda, proći ćemo kroz ove osnove i napisati par automatizovanih testova komercijalnih sajtova.

Tokom predavanja biće korišćeni git i servis GitHub, programski jezik Python, Selenium i Webdriver. Kurs je namenjen svima koji imaju osnovno znanje programiranja, kao i poznavanje osnovnih koncepata objektno orijetisanog programiranja i sintakse programskog jezika Python.

Kako je ova grana programiranja u ekspanziji zbog rastućeg broja korisnika aplikacija i rapidnih 
promena softvera, ovaj kurs može biti koristan pogotovo kada se uzme u obzir da nijedan kurs 
na Matematičkom fakultetu ne pokriva ovu temu na odgovarajući način. 


Kompletno predavanje možete videti na sledećem linku

[![selenium](http://img.youtube.com/vi/bd8dU8UURxo/0.jpg)](http://www.youtube.com/watch?v=bd8dU8UURxo "selenium")


---

## Preduslovi za pokretanje

Za pokretanje programa i praćenje radionice neophodno je instalirati sledeće stvari

1. **Pip (python2.7)**

Python je najčešće dolazi uz operativni sistem, a pip će nam biti potreban za instaliranje biblioteka
za praćenje ove radionice. Sledeći linkovi mogu pomoći pri instalaciji.
```sh
https://www.python.org/download/releases/2.7/
https://pip.pypa.io/en/stable/installing/
```

2. **Java**

Ukoliko nemate javu instaliranu na svom sistemu, možete je instalirati putem ovih komandi na Ubunutu operativnom 
sistemu.
```sh
$ sudo apt-get update
$ sudo apt-get install default-jre
$ sudo apt-get install default-jdk
$ sudo add-apt-repository ppa:webupd8team/java
$ sudo apt-get install oracle-java8-installer
```
3. **Selenium**

Biblioteka koju ćemo koristiti za pisanje automatskih testova u pythonu.
```
pip install selenium
```

4. **Selenium standalone server i Chrome webdriver**

Na ovom sajtu je potrebno skinuti selenium standalone server (.jar ) kao i chrome webdriver i sačuvati ih u istom
direktorijumu. Obratiti pažnju da webdriver treba skinuti za operativni sistem koji koristite.
```sh
https://www.seleniumhq.org/download/
```

---

## Pokretanje programa

1. Ući u direktorijum gde je sačuvan selenium standalone server i webdriver i pokrenuti ga na portu 4444

```
$ java -jar selenium-server-standalone-3.141.59
```

2. Pokrenuti željeni test sa

```
$ python testname.py
```

