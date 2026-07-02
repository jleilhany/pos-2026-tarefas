from flask import Flask, redirect, url_for, session, request, render_template
from authlib.integrations.flask_client import OAuth
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.debug = True
app.secret_key = 'development'
oauth = OAuth(app)


oauth.register(
    name='suap',
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    api_base_url='https://suap.ifrn.edu.br/api/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://suap.ifrn.edu.br/o/token/',
    authorize_url='https://suap.ifrn.edu.br/o/authorize/',
    fetch_token=lambda: session.get('suap_token')
)


@app.route('/')
def index():
    if 'suap_token' in session:
        meus_dados = oauth.suap.get('rh/meus-dados')
        return render_template('user.html', user_data=meus_dados.json())
    else:
        return render_template('index.html')


@app.route('/login')
def login():
    redirect_uri = url_for('auth', _external=True)
    print(redirect_uri)  
    return oauth.suap.authorize_redirect(redirect_uri)

@app.route('/logout')
def logout():
    session.pop('suap_token', None)
    return redirect(url_for('index'))

@app.route('/login/authorized')
def auth():
    token = oauth.suap.authorize_access_token()
    session['suap_token'] = token
    return redirect(url_for('index'))


@app.route('/boletim')
def boletim():
    if 'suap_token' not in session:
        return redirect(url_for('login'))
    
    ano = request.args.get('ano', '2024')
    periodo = request.args.get('periodo', '1')
    
    print(f"Buscando boletim: ano={ano}, período={periodo}")
    
    boletim_data = oauth.suap.get(f'ensino/meu-boletim/{ano}/{periodo}/?page=1')
    meus_dados = oauth.suap.get('rh/meus-dados')
    
    if boletim_data.status_code == 200:
        dados = boletim_data.json()
        disciplinas = dados.get('results', [])
        total = dados.get('count', 0)
    else:
        disciplinas = []
        total = 0
    
    return render_template(
        'boletim.html',
        user_data=meus_dados.json(),
        boletim=disciplinas,
        total_disciplinas=total,
        ano_selecionado=ano,
        periodo_selecionado=periodo
    )


@app.route('/profile')
def profile():
    if 'suap_token' not in session:
        return redirect(url_for('login'))
    meus_dados = oauth.suap.get('rh/meus-dados')
    return render_template('profile.html', user_data=meus_dados.json())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)