# Wahlkampagnen-Website: Yvone Janssen (Aufsichtsrat apoBank)

Dieses Repository enthält den vollständigen lokalen Entwurf für die Kampagnen-Website von **Yvone Janssen** zur Kandidatur für den Aufsichtsrat der **Deutschen Apotheker- und Ärztebank eG (apoBank)**.

---

## 🚀 1. Lokale Vorschau starten

Die Website nutzt das virtuelle Python-Environment (`.venv`) und startet einen lokalen Live-Reload-Server:

### Option A: Per Doppelklick (Windows)
* Einfach auf **`start.bat`** doppelklicken. Der Browser öffnet sich automatisch unter `http://127.0.0.1:8000`.

### Option B: Über das Terminal / PowerShell
```powershell
# Abhängigkeiten im venv installieren (falls neu aufgesetzt):
.\.venv\Scripts\pip.exe install -r requirements.txt

# Server starten:
.\.venv\Scripts\python.exe dev.py
```

*Sobald du Dateien im Editor speicherst, aktualisiert sich die Website im Browser automatisch ohne manuelles Neuladen.*

---

## 🎨 2. Design & Farben der apoBank

Das Design folgt der Farbwelt der apoBank:
* **apo-Blau (Primärfarbe):** `#012169` (seriöses, tiefes Bankenblau)
* **apo-Teal (Akzentfarbe):** `#00a2b8` (Gesundheits-/Zukunfts-Akzent)
* **apo-Gold (Warmakzent):** `#fed161`
* **apo-Lebenslinie:** Farbverlauf aus Gold, Oliv (`#b6be8a`) und Teal in der Top-Bar und im Footer.

---

## 📝 3. Inhalte anpassen

* **Echtes Porträtfoto einbinden:**
  Lege das Foto einfach in den Ordner `assets/images/` (z. B. als `yvone-janssen.jpg`) und passe in [index.html](file:///e:/repos/website_build/index.html) in Zeile ~120 das `src`-Attribut an:
  ```html
  <img src="assets/images/yvone-janssen.jpg" alt="Porträt Yvone Janssen" class="w-full h-full object-cover">
  ```
* **Texte & Vita anpassen:**
  Alle Texte befinden sich in [index.html](file:///e:/repos/website_build/index.html) in sauber kommentierten Abschnitten (`#motivation`, `#schwerpunkte`, `#werdegang`, `#wahl`, `#kontakt`).
* **Impressum & Datenschutz:**
  Ergänze in [impressum.html](file:///e:/repos/website_build/impressum.html) und [datenschutz.html](file:///e:/repos/website_build/datenschutz.html) die reale Anschrift und Kontaktdaten.

---

## 🌐 4. Vom lokalen Entwurf ins Internet (Die 3-Monate-Lösung)

### Schritt 1: Domain anmieten (ca. 5–10 € / Jahr)
* Gehe zu einem vertrauenswürdigen Registrar wie **IONOS**, **Strato**, **INWX** oder **Cloudflare**.
* Sichere die Wunschdomain, z. B. `yvone-janssen.de` oder `yvone-janssen-apobank.de`.
* Domains werden standardmäßig für 1 Jahr registriert. Kündige sie einfach nach den 3 Monaten zum Ablauf des Jahres.

### Schritt 2: Kostenloses Hosting (z. B. Netlify oder Vercel)
* Da dies eine statische Website ist (kein PHP, keine Datenbank), ist das Hosting auf **Netlify** oder **Vercel** **dauerhaft kostenlos**, extrem schnell und bietet ein automatisches **kostenloses SSL-Zertifikat** (HTTPS / Schlosssymbol).
* Du kannst den gesamten Ordner `website_build` einfach per **Drag & Drop** in das Netlify-Dashboard ziehen (unter `app.netlify.com/drop`). Die Seite ist sofort online!

### Schritt 3: Domain mit dem Hosting verbinden (2 Minuten)
* Im Netlify- oder Vercel-Dashboard klickst du auf **"Domain hinzufügen"** und gibst deinen Domainnamen ein.
* Der Hoster zeigt dir zwei einfache DNS-Einträge (einen `A-Record` und einen `CNAME`).
* Diese beiden Werte trägst du in der Verwaltung deines Domainanbieters ein. Fertig! Innerhalb von ca. 15 bis 60 Minuten ist die Website weltweit verschlüsselt erreichbar.
