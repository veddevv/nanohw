# LES DETTE FØRST / READ THIS FIRST
Noen versjoner (kansje alle) av NanoHW kan være ødelagte, og jeg vet ikke hvordan man kan fikse de foreløpig. Takk for at du forstår.
/ Some versions (maybe all) of NanoHW may be broken and I don't know how to fix them yet. Thank you for your understanding.

DETTE REPOET ER NÅ ARKIVERT. / THIS REPO IS NOW ARCHIVED.


# NanoHW

**NanoHW** (/ˈnænoʊ eɪtʃ dʌbəl.juː/) er en allsidig og interaktiv skrivebordsapplikasjon laget for Windows ved hjelp av Python og Tkinter.

## Funksjoner

### Systeminfo
- **Operativsysteminformasjon**: Viser detaljer om OS-versjon og type.
- **CPU-info**: Viser CPU-modell, kjerner og bruksstatistikk.
- **Minneinfo**: Gir informasjon om total og tilgjengelig systemminne.

### NanoPaint
- **Fri Tegning**: Lar brukere tegne fritt på et lerret ved å bruke valgt penselfarge og størrelse.
- **Fargevelger**: Gir en fargevelger for å velge tegnefarger.
- **Penselstørrelsejustering**: Brukere kan justere penselstørrelsen med en glidebryter.
- **Tøm Lerret**: Lar brukere tømme lerretet med et knappetrykk for å starte en ny tegning.

**Merk:** En separat, fullt pakket versjon av **NanoPaint** med utvidede funksjoner vil være tilgjengelig snart. Følg med for oppdateringer!

## Krav
- **Python**: Versjon 3.x
- **Tkinter**: Inkludert i standard Python-installasjoner.
- **PyInstaller**: For å lage en selvstendig eksekverbar fil.

## Installering

1. **Klon Repository**:
   ```
   git clone https://github.com/veddevv/nanohw.git
   cd nanohw
   ```

2. **Installer Avhengigheter**:
   Sørg for at du har Python og pip installert. Deretter, installer nødvendige pakker:
   ```
   pip install -r requirements.txt
   ```

3. **Kjør Applikasjonen**:
   Du kan kjøre Python-skriptet direkte:
   ```
   python nanohw.py
   ```

   Eller, hvis du foretrekker en selvstendig eksekverbar fil, kan du bruke den medfølgende `.exe`-filen i `dist`-mappen.

## Bruk

- Åpne applikasjonen for å se systeminformasjon under fanen "System Info".
- Bytt til fanen "NanoPaint" for å begynne å tegne, velge farger og justere penselstørrelser.

## Lisens

Dette prosjektet er lisensiert under GNU General Public License v3.0. Se LICENSE-filen for flere detaljer.

## Bidra

Du er velkommen til å forgrene repositoryet, åpne problemer og sende pull-forespørsel. Bidrag er velkomne!
