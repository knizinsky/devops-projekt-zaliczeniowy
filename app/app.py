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
    },
    {
        'name': 'Katarzyna Wiśniewska',
        'profession': 'Data Scientist',
        'skills': [
            'Python, R, SQL',
            'Uczenie maszynowe (scikit-learn, TensorFlow)',
            'Analiza danych (Pandas, NumPy)',
            'Przetwarzanie dużych zbiorów danych'
        ],
        'experience': [
            {'position': 'Data Scientist', 'company': 'DataTech', 'years': '2021-2025'},
            {'position': 'Data Analyst', 'company': 'DataLab', 'years': '2018-2021'}
        ],
        'location': 'Wrocław, Polska',
        'contact': {
            'email': 'katarzyna.wisniewska@example.com',
            'phone': '+48 321 654 987'
        },
    },
    {
        'name': 'Michał Zieliński',
        'profession': 'Backend Developer',
        'skills': [
            'Java, Spring, Hibernate',
            'Bazy danych (MySQL, PostgreSQL)',
            'API RESTful',
            'Wzorce projektowe (Design Patterns)'
        ],
        'experience': [
            {'position': 'Backend Developer', 'company': 'SoftWare Solutions', 'years': '2020-2025'},
            {'position': 'Junior Backend Developer', 'company': 'TechInno', 'years': '2017-2020'}
        ],
        'location': 'Poznań, Polska',
        'contact': {
            'email': 'michal.zielinski@example.com',
            'phone': '+48 654 321 987'
        },
    },
    {
        'name': 'Anna Nowakowska',
        'profession': 'UI/UX Designer',
        'skills': [
            'Adobe XD, Figma, Sketch',
            'Projektowanie UI, prototypowanie',
            'Zrozumienie potrzeb użytkowników',
            'Przeprowadzanie testów użyteczności'
        ],
        'experience': [
            {'position': 'UI/UX Designer', 'company': 'CreativeStudio', 'years': '2019-2025'},
            {'position': 'Junior Designer', 'company': 'DesignCraft', 'years': '2017-2019'}
        ],
        'location': 'Gdańsk, Polska',
        'contact': {
            'email': 'anna.nowakowska@example.com',
            'phone': '+48 876 543 210'
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
