from flask import Flask, render_template

app = Flask(__name__)

users = [
    {
        'name': 'Jan Kowalski',
        'profession': 'Developer DevOps',
        'skills': [
            'Automatyzacja procesów CI/CD',
            'Zarządzanie chmurą (AWS, GCP, Azure)',
            'Konteneryzacja i orkiestracja (Docker, Kubernetes)',
            'Bezpieczeństwo i monitorowanie'
        ],
        'experience': [
            {'position': 'DevOps Engineer', 'company': 'TechCorp', 'years': '2020-2025'},
            {'position': 'System Administrator', 'company': 'NetSolutions', 'years': '2016-2020'}
        ],
        'location': 'Warszawa, Polska',
        'contact': {
            'email': 'jan.kowalski@example.com',
            'phone': '+48 123 456 789'
        },
    },
    {
        'name': 'Adam Nowak',
        'profession': 'Frontend Developer',
        'skills': [
            'React.js, Vue.js',
            'HTML, CSS, JavaScript',
            'Testowanie UI (Cypress, Jest)',
            'Projektowanie interfejsów użytkownika'
        ],
        'experience': [
            {'position': 'Frontend Developer', 'company': 'WebCreations', 'years': '2019-2025'},
            {'position': 'Junior Developer', 'company': 'StartApp', 'years': '2017-2019'}
        ],
        'location': 'Kraków, Polska',
        'contact': {
            'email': 'adam.nowak@example.com',
            'phone': '+48 987 654 321'
        },
    }
]

@app.route('/')
def home():
    home_data = {
        'welcome_message': 'Witaj na stronie głównej!',
        'description': 'Kliknij w poniższy przycisk, aby zobaczyć listę użytkowników.'
    }
    return render_template('index.html', home_data=home_data)

@app.route('/users')
def user_list():
    return render_template('users.html', users=users)

@app.route('/user/<int:user_id>')
def user_detail(user_id):
    user = users[user_id]
    return render_template('user_detail.html', user=user)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
