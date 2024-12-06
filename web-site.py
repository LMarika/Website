import os
from flask import Flask, render_template, url_for
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)  #создание объекта Flask

menu = ["Установка", "Первое приложение", "Обратная связь"]  #Меню сайта


@app.route('/')
def index():
    """Маршрут главной страницы."""
    print(url_for('index'))  #Генерация URL-адреса по функции index
    return render_template('index.html', menu=menu)


@app.route('/about')
def about():
    """Маршрут дополнительной страницы."""
    print(url_for('about'))  #Генерация URL-адреса по функции about
    return render_template('about.html', title='О странице сайта', menu=menu)


@app.route('/profile/<path:username>')  #Создание динамического URL-адреса
def profile(username):
    return f"Пользователь: {username}"




if __name__ == '__main__':  #Запуск веб-сайта
    is_context = bool(int(os.getenv('CONTEXT')))
    if is_context:
        with app.test_request_context():  #Тестовый контекст запроса
            print(url_for('index'))
            print(url_for('about'))
            print(url_for('profile', username="LMarika"))
    else:
        app.run(debug=True)
