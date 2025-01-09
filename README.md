# Flask Web Application with Docker and CI/CD

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Docker](https://img.shields.io/badge/Docker-Enabled-green)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-yellow)
![Security Scan](https://img.shields.io/badge/Security%20Scan-Trivy-red)

## 🛠️ Opis projektu

Celem tego projektu jest stworzenie prostej aplikacji webowej przy użyciu frameworka **Flask**. Aplikacja jest konteneryzowana za pomocą **Docker**, a cały proces budowania, testowania i wdrażania jest automatyzowany za pomocą **GitHub Actions**. Dodatkowo, użyto narzędzia **Trivy** do skanowania obrazu Docker pod kątem podatności bezpieczeństwa.

---

## 🖥️ Wymagania

- **Docker** - do uruchamiania aplikacji w kontenerze.
- **Git** - do zarządzania wersjami.
- **Python 3.13+** (jeśli nie używasz Docker).

---

## ⬇️ Instalacja

### 1. **Uruchamianie aplikacji za pomocą Docker**

Aby uruchomić aplikację w Dockerze, wykonaj poniższe kroki:

1. **Sklonuj repozytorium**:

   ```bash
   git clone https://github.com/twoje-repozytorium.git
   cd twoje-repozytorium
   ```

2. **Zbuduj obraz Docker**:

 ```bash
docker build -t flask-webapp .
```


3. **Uruchom aplikację**:

```bash
docker run -p 5000:5000 flask-webapp
```
Odwiedź aplikację w przeglądarce pod adresem http://127.0.0.1:5000.

### 2. **Uruchamianie aplikacji bez Docker**
Zainstaluj wymagane zależności:

```bash
python -m venv venv
source venv/bin/activate  # Na systemach Unix / Mac
venv\Scripts\activate     # Na systemach Windows
pip install -r requirements.txt
```

Uruchom aplikację:

```bash
python app.py
```

Odwiedź aplikację w przeglądarce pod adresem http://127.0.0.1:5000.

## ♾️ CI/CD z GitHub Actions
Projekt wykorzystuje GitHub Actions do zautomatyzowanego procesu Continuous Integration (CI) i Continuous Deployment (CD).

**Proces CI obejmuje:**
- Budowanie obrazu Docker.
- Testowanie aplikacji.
- Skanowanie obrazu Docker pod kątem podatności bezpieczeństwa za pomocą narzędzia Trivy.
- Wysyłanie obrazu do GitHub Container Registry (jeśli zmiany zostały zmergowane do gałęzi main).
- Workflow uruchamia się automatycznie przy każdym pushu lub pull request do gałęzi main.

**Narzędzia i technologie:**
- Python 3.13+
- Flask - Framework do budowy aplikacji webowych w Pythonie.
- Docker - Konteneryzacja aplikacji.
- GitHub Actions - Automatyzacja procesu CI/CD.
- Trivy - Skanowanie obrazów Docker pod kątem podatności bezpieczeństwa.
W przypadku wykrycia krytycznych lub wysokich podatności, rekomenduje się aktualizację obrazu bazowego lub usunięcie zagrożeń.

