[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/wxDq4rbD)
# Zadaća 2 - REST API aplikacija

## O projektu

Ova aplikacija omogućava praćenje laboratorijske opreme u telekomunikacijskoj laboratoriji. 
Sistem pruža evidenciju instrumenata (naziv, inventurni broj, proizvođač, cijena i sl.) 
te vrsta mjerenja koja se izvode u laboratoriji.

## Tim

- **Student A**: Maida Kamenčić - resurs: `instruments`
- **Student B**: [Ime Prezime] - resurs: `/resursi_b`

## Instalacija i pokretanje

### Preduvjeti

- Python 3.10 ili noviji
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

[Analogno kao za Resurs A]

## Korištenje AI alata

### Alat: [GitHub Copilot / ChatGPT / ...]
**Model:** Copilot model

**Primjer 1:**
- **Prompt:** Kako da napišem query upit za varijablu dostupnosti uređaja?
- **Kako je pomoglo:** AI je predložio kako da koristim `Query` iz FastAPI-ja za filtriranje rezultata na osnovu dostupnosti uređaja.
- **Prilagodbe:** Prilagodila sam kod polju `is_available` u Instrument modelu.

**Primjer 2:**
- **Prompt:** [Npr. "Implementiraj PATCH endpoint sa exclude_unset=True"]
- **Kako je pomoglo:** [Opis]
- **Prilagodbe:** [Opis]

## Napomene

[Dodatne napomene specifične za vašu implementaciju]