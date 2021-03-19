from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'GET':
        return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                <link rel="stylesheet"
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                crossorigin="anonymous">
                                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                                <title>Отбор астронавтов</title>
                              </head>
                              <body>
                                <h1 class="h1-black">Заявка на Яндекс Лицей</h1>
                                <div>
                                    <form class="login_form" method="post">
                                        <input type="text" class="form-control" id="surname" placeholder="Введите фамилию" name="surname">
                                        <input type="text" class="form-control" id="name" placeholder="Введите имя" name="name">
                                        <p> </p>
                                        <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                        <p> </p>
                                        <div class="form-group">
                                            <label for="classSelect">Какое у вас образование?</label>
                                            <select class="form-control" id="classSelect" name="education">
                                              <option>дошкольное образование</option>
                                              <option>начальное (общее образование)</option>
                                              <option>основное (общее образование)</option>
                                              <option>среднее (общее образование)</option>
                                              <option>среднее профессиональное образование</option>
                                              <option>бакалавриат (высшее образование)</option>
                                              <option>специалитет, магистратура (высшее образование)</option>
                                              <option>подготовка кадров высшей квалификации (высшее образование)</option>
                                            </select>
                                        </div>
                                        <p> </p>
                                        <div class="form-group">
                                            <label>Кем Вы хотите стать?</label>
                                            <div class="form-check">
                                                <input type="checkbox" class="form-check-input" id="1" name="profession" value="инженер-исследователь">
                                                <label class="form-check-label" for="1">Инженер-исследователь</label>
                                            </div>
                                            <div class="form-check">
                                                <input type="checkbox" class="form-check-input" id="2" name="profession" value="пилот">
                                                <label class="form-check-label" for="2">Пилот</label>
                                            </div>
                                            <div class="form-check">
                                                <input type="checkbox" class="form-check-input" id="3" name="profession" value="строитель">
                                                <label class="form-check-label" for="3">Строитель</label>
                                            </div>
                                            <div class="form-check">
                                                <input type="checkbox" class="form-check-input" id="4" name="profession" value="экзобиолог">
                                                <label class="form-check-label" for="4">Экзобиолог</label>
                                            </div>
                                            <div class="form-check">
                                                <input type="checkbox" class="form-check-input" id="5" name="profession" value="врач">
                                                <label class="form-check-label" for="5">Врач<label>
                                            </div>
                                            <div class="form-check">
                                                <input type="checkbox" class="form-check-input" id="6" name="profession" value="инженер по терраформированию">
                                                <label class="form-check-label" for="6">Инженер по терраформированию</label>
                                            </div>
                                            <div class="form-check">
                                                <input type="checkbox" class="form-check-input" id="7" name="profession" value="климатолог">
                                                <label class="form-check-label" for="7">Климатолог</label>
                                            </div>
                                            <div class="form-check">
                                                <input type="checkbox" class="form-check-input" id="8 name="profession" value="специалист по радиационной защите">
                                                <label class="form-check-label" for="8">Специалист по радиационной защите</label>
                                            </div>
                                            <div class="form-check">
                                                <input type="checkbox" class="form-check-input" id="9" name="profession" value="астрогеолог">
                                                <label class="form-check-label" for="9">Астрогеолог</label>
                                            </div>
                                            <div class="form-check">
                                                <input type="checkbox" class="form-check-input" id="10" name="profession" value="гляциолог">
                                                <label class="form-check-label" for="10">Гляциолог</label>
                                            </div>
                                            <div class="form-check">
                                                <input type="checkbox" class="form-check-input" id="11" name="profession" value="инженер жизнеобеспечения">
                                                <label class="form-check-label" for="11">Инженер жизнеобеспечения</label>
                                            </div>
                                            <div class="form-check">
                                                <input type="checkbox" class="form-check-input" id="12" name="profession" value="метеоролог">
                                                <label class="form-check-label" for="12">Метеоролог</label>
                                            </div>
                                            <div class="form-check">
                                                <input type="checkbox" class="form-check-input" id="13" name="profession" value="оператор марсохода">
                                                <label class="form-check-label" for="13">Оператор марсохода</label>
                                            </div>
                                            <div class="form-check">
                                                <input type="checkbox" class="form-check-input" id="14" name="profession" value="киберинженер">
                                                <label class="form-check-label" for="14">Киберинженер</label>
                                            </div>
                                            <div class="form-check">
                                                <input type="checkbox" class="form-check-input" id="15" name="profession" value="штурман">
                                                <label class="form-check-label" for="15">Штурман</label>
                                            </div>
                                            <div class="form-check">
                                                <input type="checkbox" class="form-check-input" id="16" name="profession" value="програмист">
                                                <label class="form-check-label" for="16">програмист</label>
                                            </div>
                                        </div>
                                        <p> </p>
                                        <div class="form-group">
                                            <label for="form-check">Укажите пол</label>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                              <label class="form-check-label" for="male">
                                                Мужской
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                              <label class="form-check-label" for="female">
                                                Женский
                                              </label>
                                            </div>
                                        </div>
                                        <p> </p>                                        
                                        <div class="form-group">
                                            <label for="about">Почему Вы хотите принять участие в Яндекс Лицеи?</label>
                                            <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                        </div>
                                        <p> </p>                                        
                                        <div class="form-group">
                                            <label for="photo">Приложите фотографию</label>
                                            </br><input type="file" class="form-control-file" id="photo" name="file">
                                        </div>   
                                        <p> </p>                                        
                                        <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                            <label class="form-check-label" for="acceptRules">Готов стать програмистом? </label>
                                        </div>
                                        <p> </p>                                        
                                        <button type="submit" class="btn btn-primary">Записаться</button>
                                    </form>
                                </div>
                              </body>
                            </html>'''
    elif request.method == 'POST':
        print('email:', request.form['email'])
        print('surname:', request.form['surname'])
        print('name:', request.form['name'])
        print('education:', request.form['education'])
        print('profession:', ', '.join(request.form.getlist('profession')))
        print('file:', request.form['file'])
        print('about:', request.form['about'])
        print('sex:', request.form['sex'])
        print('accept:', request.form['accept'])
        return "Вы подали заявку на Яндекс Лицей ожидайте"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
