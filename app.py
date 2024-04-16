from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add_reminder():
    reminder = request.form['reminder']
    with open("lembretes.txt", "a") as arquivo:
        arquivo.write(reminder + "\n")
    return 'Lembrete adicionado com sucesso! <a href="/">Voltar</a>'

@app.route('/list')
def list_reminders():
    reminders = []
    if os.path.exists("lembretes.txt"):
        with open("lembretes.txt", "r") as arquivo:
            reminders = arquivo.readlines()
    return render_template('list.html', reminders=reminders)

if __name__ == '__main__':
    app.run(debug=True)
