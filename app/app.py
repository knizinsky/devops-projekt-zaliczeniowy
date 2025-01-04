from flask import Flask, render_template

app = Flask(__name__)

about_info = {
    'name': 'Jan Kowalski',
    'profession': 'Developer DevOps',
    'skills': [
        'Automatyzacja procesów CI/CD',
        'Zarządzanie chmurą (AWS, GCP, Azure)',
        'Konteneryzacja i orkiestracja (Docker, Kubernetes)',
        'Bezpieczeństwo i monitorowanie'
    ],
    'contact': {
        'email': 'jan.kowalski@example.com',
        'phone': '+48 123 456 789'
    }
}

@app.route('/')
def home():
    home_data = {
        'welcome_message': 'Witaj na mojej stronie!',
        'description': 'Jestem profesjonalnym Developerem DevOps, specjalizującym się w automatyzacji procesów i zarządzaniu infrastrukturą.'
    }
    return render_template('index.html', home_data=home_data)

@app.route('/about')
def about():
    return render_template('about.html', about_info=about_info)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
