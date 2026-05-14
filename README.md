[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/wxDq4rbD)
# Zadaća 2 - REST API aplikacija

## O projektu

Ova aplikacija omogućava praćenje laboratorijske opreme u telekomunikacijskoj laboratoriji. 
Sistem pruža evidenciju instrumenata (naziv, inventurni broj, proizvođač, cijena i sl.) 
te vrsta mjerenja koja se izvode u laboratoriji.

## Tim

- **Student A**: Maida Kamenčić - resurs: `instruments`
- **Student B**: Amer Imamovic - resurs: `measurements`

## Instalacija i pokretanje

### Preduvjeti

- Python 3.11.9
- pip

### Koraci

1. Klonirajte repozitorij:
```bash
git clone <url-repozitorija>
cd <naziv-repozitorija>
```

2. Kreirajte virtuelno okruženje:
```bash
python -m venv venv
```

3. Aktivirajte virtuelno okruženje:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`

4. Instalirajte zavisnosti:
```bash
pip install -r requirements.txt
```

5. Pokrenite aplikaciju:
```bash
uvicorn main:app --reload
```

6. Otvorite browser na adresi: `http://localhost:8000/docs`

## API Endpointi

### Resurs A: `/resursi_a`

| Metoda | Ruta | Opis |
|--------|------|------|
| GET | `/instruments` | Lista svih resursa (filter po dostupnosti uređaja) |
| GET | `/instruments/{id}` | Dohvatanje resursa po ID-u |
| POST | `/instruments` | Kreiranje novog resursa |
| PUT | `/instruments/{id}` | Potpuna zamjena resursa |
| PATCH | `/instruments/{id}` | Djelimično ažuriranje resursa |
| DELETE | `/instruments/{id}` | Brisanje resursa |

**Primjer zahtjeva:**
```bash
# Kreiranje novog resursa
curl -X POST "http://localhost:8000/instruments" \
  -H "Content-Type: application/json" \
  -d '{"name": "Osciloskop",
      "inventory_number": "OS-123", 
       "manufacturer": "Rigol Tehnologies",
       "price": 1500.00,
       "is_available": true
       "location": "Stelekt Lab"}'
```

### Resurs B: `/resursi_b`

GET	/measurements	Lista svih mjerenja iz baze podataka
GET	/measurements/{id}	Dohvatanje jednog specifičnog mjerenja po ID-u
POST	/measurements	Kreiranje novog zapisa o mjerenju
PUT	/measurements/{id}	Potpuna zamjena podataka postojećeg mjerenja
PATCH	/measurements/{id}	Djelimična izmjena (npr. samo vrijednosti) mjerenja
DELETE	/measurements/{id}	Trajno brisanje mjerenja iz baze

**Primjer zahtjeva:**
```bash
# Kreiranje novog mjerenja
curl -X POST "http://localhost:8000/measurements" \
  -H "Content-Type: application/json" \
  -d '{
        "measurement_type": "Temperatura",
        "value": 24.5,
        "unit": "°C",
        "is_automated": true,
        "notes": "Mjerenje izvršeno u glavnom laboratoriju"
      }'
```

## Korištenje AI alata

### Alat: [GitHub Copilot / ChatGPT / ...]
**Model:** Copilot model

**Primjer 1:**
- **Prompt:** Kako da napišem query upit za varijablu dostupnosti uređaja?
- **Kako je pomoglo:** AI je predložio kako da koristim `Query` iz FastAPI-ja za filtriranje rezultata na osnovu dostupnosti uređaja.
- **Prilagodbe:** Prilagodila sam kod polju `is_available` u Instrument modelu.

**Primjer 2:**
- **Prompt:** Kako da popravim upozorenje "from_orm is deprecated" koje mi se stalno pojavljuje u VS Code-u?
- **Kako je pomoglo:** AI je objasnio da se u novoj verziji biblioteke koristi model_validate umjesto starije metode
- **Prilagodbe:** Primijenio sam ove izmjene u svim funkcijama

**Primjer 3:**
- **Prompt:** Zašto mi funkcija vraća null za ID tek kreiranog mjerenja iako je ono spašeno u bazu?
- **Kako je pomoglo:** AI mi je objasnio koncept sinhronizacije između Pythona i SQL-a i važnost funkcije session.refresh
- **Prilagodbe:** Dodala sam session.refresh(db_measurement) nakon svakog commit() poziva.
## Napomene

[Dodatne napomene specifične za vašu implementaciju]



##Provjera 
U zadatku 1 dodano je tip mjerenja ne smije biti prazan string i da provjerim da ne bi stavljao isti tip mjerenja, u zadatku 2 sam dodao da mogu izbrojati ukupan broj mjerenja koji se nalazi trenutno u bazi 

GET/measurments/count- vraca nam ukupan broj mjrenja i vrati nam odgovor 200, a POST/measurments ima sada provjeru da ne bi bio dupli tip mjerenja odgovor je 201, promjenom modela u zadatku 1 smo omogucili da tip mjerenja ne smije biti prazan string. U slucaju kada u post napisemo isto ime imati cemo error kod 409, a ako probamo poslati prazan string kao tip mjerenja imati cemo 422