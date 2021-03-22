from flask import Flask

app = Flask(__name__)


@app.route('/')
def start():
    return f'''
<!doctype html>
<html lang="en">
<head>
<p>
Животные – наши соседи по планете. 
На животный мир невозможно смотреть только с биологической точки зрения, 
потому что при взгляде на него человечество испытывает целый спектр эмоций:
животные удивляют, вызывают страх и уважение, учат заботе, заставляются умиляться. 
Мы за ними наблюдаем и расплываемся в улыбке от их повадок, мы боремся за их выживание,
мы призываем наших детей интересоваться ими,потому что существование планеты без них было бы скучным и однообразным.
</p>

<!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" \
    integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" crossorigin="anonymous">

    <title></title>
  </head>
  <body>


    <!-- здесь будет код слайдера  -->
<div id="sliderBigImages" class="carousel slide" data-ride="carousel">
<div class="carousel-inner">
        <div class="carousel-item active">
            <img src="https://img2.goodfon.ru/original/1280x800/7/ad/gepard-koshka-hischnik-nebo.jpg" class="d-block w-100" alt="Природа">
        </div>
        <div class="carousel-item">
            <img src="http://wallpapers-image.ru/2560x1600/animal/wallpapers/wallpapers-animal-1.jpg" class="d-block w-100" alt="Природа">
        </div>
        <div class="carousel-item">
            <img src="https://i.artfile.ru/1600x1200_360183_[www.ArtFile.ru].jpg" class="d-block w-100" alt="Природа">
        </div>
    </div>
    <a class="carousel-control-prev" href="#sliderBigImages" role="button" data-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="sr-only">Previous</span>
    </a>
    <a class="carousel-control-next" href="#sliderBigImages" role="button" data-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="sr-only">Next</span>
    </a>
</div>

<body>
    <h2>
        Смотрите интресное:
    </h2>
    <p>
        <a href="/irbis">Снежный барс</a>
    </p>
    <p>
        <a href="/volk">Полярный волк</a>
    </p>
    <p>
        <a href="/sova">Полярная сова</a>
    </p>
    </body>

<!-- подключение JavaScript -->
<!-- Сначала jQuery, затем Bootstrap JS, а Popper.js подключать необязательно -->
<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js"
integrity="sha384-B0UglyR+jN6CkvvICOB2joaf5I4l3gm9GU6Hc1og6Ls7i6U/mkkaduKaBhlAXv9k" crossorigin="anonymous"></script>
  </body>
</html>
'''


@app.route('/irbis')
def irbis():
    return f'''
<!doctype html>
<html lang="en">
<head>
    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" \
    integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" crossorigin="anonymous">

    <title>Снежный барс</title>
</head>
<body>
<h2>Ирбисы</h2>
<p>
    Снежный барс (ирбис, ак барс) - крупное хищное млекопитающее из семейства
    кошачьих. Обитает в горных массивах Афганистана, Бирмы, Бутана, Индии,
    Казахстана, Кыргызстана, Китая, Монголии, Непала, Пакистана, России,
    Таджикистана и Узбекистана. Ирбис отличается тонким, длинным, гибким телом,
    относительно короткими лапами, небольшой головой и очень длинным хвостом.
    Достигая вместе с хвостом длины 200-230 см, весит до 55 кг. Окраска меха
    светлая дымчато-серая с кольцеобразными и сплошными тёмными пятнами.</p>
<p>
    Охотится снежный барс в основном на горных козлов и баранов, также в его
    рационе встречаются кабаны, фазаны и даже суслики. В силу труднодоступности
    местообитания вида, ирбисы до сих пор остаются малоизученными. Однако по
    приблизительным оценкам их количество варьируется примерно около 10 тысяч
    особей. По состоянию на 2013 год охота на ирбисов запрещена.</p>



<!-- здесь будет код слайдера  -->
<div id="sliderBigImages" class="carousel slide" data-ride="carousel">
<div class="carousel-inner">
        <div class="carousel-item active">
            <img src="https://i.artfile.ru/1920x1200_1111781_[www.ArtFile.ru].jpg" class="d-block w-100" alt="Природа">
        </div>
        <div class="carousel-item">
            <img src="https://img2.goodfon.ru/original/2048x1365/8/3a/snezhnyy-bars-irbis-vzglyad-6256.jpg" class="d-block w-100" alt="Природа">
        </div>
        <div class="carousel-item">
            <img src="https://s1.1zoom.ru/big0/556/310863-Lastochka.jpg" class="d-block w-100" alt="Природа">
        </div>
    </div>
    <a class="carousel-control-prev" href="#sliderBigImages" role="button" data-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="sr-only">Previous</span>
    </a>
    <a class="carousel-control-next" href="#sliderBigImages" role="button" data-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="sr-only">Next</span>
    </a>
</div>

<body>
    <h2>
        Смотрите также:
    </h2>
    <p>
        <a href="/irbis">Снежный барс</a>
    </p>
    <p>
        <a href="/volk">Полярный волк</a>
    </p>
    <p>
        <a href="/sova">Полярная сова</a>
    </p>
    </body>

<!-- подключение JavaScript -->
<!-- Сначала jQuery, затем Bootstrap JS, а Popper.js подключать необязательно -->
<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js"
integrity="sha384-B0UglyR+jN6CkvvICOB2joaf5I4l3gm9GU6Hc1og6Ls7i6U/mkkaduKaBhlAXv9k" crossorigin="anonymous"></script>
  </body>
</html>
'''


@app.route('/volk')
def volk():
    return f'''
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">


    <title>Полярный волк</title>
</head>
<h1>Полярный волк</h1>
<p>
Полярные волки имеют светлый с серебристым отливом окрас шерсти, небольшие уши  и густой мех. 
К зиме могут сменить цвет шубы на практически белый. Мех густой, двухслойный. Один слой состоит из жестких осевых волос,
хорошо отталкивающих грязь и воду, а второй --  из теплого пуха, хорошо сохраняющего тепло. 
Из всех подвидов серого волка -  полярный считается одним из самых крупных.  Длина тела полярного волка без хвоста:
130—150 см. Высота в холке: 80—93 см. В Сибири и на Аляске крупные матёрые волки могут весить более 77 кг. Самки обычно 
более мелкие по сравнению с самцами. В 1987 году на Чукотке был убит волк весом 84 килограмма.

Внешним видом волк напоминает большую собаку с острыми ушами. Ноги по отношению к телу длинные,
сильные, лапы крупные, голова с широким лбом, морда у волка тоже достаточно широкая, вытянутая,
с боков опушена «бакенбардами». Хвост всегда опущен и выражает волчье настроение, спокоен ли он или испуган,
по движению и положению хвоста  можно судить о положении волка в стае.

</p>



<!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" \
    integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" crossorigin="anonymous">

    <title></title>
  </head>
  <body>


    <!-- здесь будет код слайдера  -->
<div id="sliderBigImages" class="carousel slide" data-ride="carousel">
<div class="carousel-inner">
        <div class="carousel-item active">
            <img src="https://top10a.ru/wp-content/uploads/2020/01/6-105.jpg" class="d-block w-100" alt="Природа">
        </div>
        <div class="carousel-item">
            <img src="https://avatars.mds.yandex.net/get-zen_doc/1894366/pub_5e41b283b83d707e09fb2914_5e41b5614794a43797944822/scale_1200" class="d-block w-100" alt="Природа">
        </div>
        <div class="carousel-item">
            <img src="https://proza.ru/pics/2017/11/25/1289.jpg" class="d-block w-100" alt="Природа">
        </div>
    </div>
    <a class="carousel-control-prev" href="#sliderBigImages" role="button" data-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="sr-only">Previous</span>
    </a>
    <a class="carousel-control-next" href="#sliderBigImages" role="button" data-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="sr-only">Next</span>
    </a>
</div>

<body>
    <h2>
        Смотрите интресное:
    </h2>
    <p>
        <a href="/irbis">Снежный барс</a>
    </p>
    <p>
        <a href="/volk">Полярный волк</a>
    </p>
    <p>
        <a href="/sova">Полярная сова</a>
    </p>
    </body>

<!-- подключение JavaScript -->
<!-- Сначала jQuery, затем Bootstrap JS, а Popper.js подключать необязательно -->
<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js"
integrity="sha384-B0UglyR+jN6CkvvICOB2joaf5I4l3gm9GU6Hc1og6Ls7i6U/mkkaduKaBhlAXv9k" crossorigin="anonymous"></script>
  </body>
</html>
'''


@app.route('/sova')
def sova():
    return f'''
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">


    <title>Полярная сова</title>
</head>
<h1>Полярная сова</h1>
<p>
Белая сова - самая крупная птица из отряда совообразных в тундре. Голова круглая, радужина глаз ярко-жёлтая.

Самки крупнее самцов. Длина тела самца может достигать 55-65 см, масса – 2-2,5 кг, самки - 70 см и 3 кг. 
Размах крыльев составляет в среднем 142-166 см.

Окраска покровительственная: для взрослых птиц характерно белое оперение с тёмными поперечными пестринами. 
Белое оперение полярной совы маскирует её на фоне снега. У самок и молодых птиц пестрин больше, чем у самцов.

Птенцы коричневого цвета. Клюв чёрный, почти до конца покрыт перьями-щетинками. Оперение ног похоже на шерсть,
образует «космы».
</p>

<!-- Bootstrap CSS -->
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css"
      integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" crossorigin="anonymous">

<title></title>
</head>
<body>


<!-- здесь будет код слайдера  -->
<div id="sliderBigImages" class="carousel slide" data-ride="carousel">
    <div class="carousel-inner">
        <div class="carousel-item active">
            <img src="https://animalreader.ru/wp-content/uploads/2014/10/c2e234d8916ab3fa3301eed185d35d65-e1413379584714.jpg" class="d-block w-100" alt="Природа">
        </div>
        <div class="carousel-item">
            <img src="https://animal-book.ru/wp-content/uploads/2016/02/polyarnaya-sova.jpg" \
            class="d-block w-100" alt="Природа">
        </div>
        <div class="carousel-item">
            <img src="https://s3.nat-geo.ru/images/2019/5/16/0a7914764e1541dc9dbacb4413f2291a.max-1200x800.jpg" class="d-block w-100" \
            alt="Природа">
        </div>
    </div>
    <a class="carousel-control-prev" href="#sliderBigImages" role="button" data-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="sr-only">Previous</span>
    </a>
    <a class="carousel-control-next" href="#sliderBigImages" role="button" data-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="sr-only">Next</span>
    </a>
</div>

<body>
<h2>
    Смотрите интресное:
</h2>
<p>
        <a href="/irbis">Снежный барс</a>
    </p>
    <p>
        <a href="/volk">Полярный волк</a>
    </p>
    <p>
        <a href="/sova">Полярная сова</a>
</p>
</body>

<!-- подключение JavaScript -->
<!-- Сначала jQuery, затем Bootstrap JS, а Popper.js подключать необязательно -->
<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
        integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo"
        crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js"
        integrity="sha384-B0UglyR+jN6CkvvICOB2joaf5I4l3gm9GU6Hc1og6Ls7i6U/mkkaduKaBhlAXv9k"
        crossorigin="anonymous"></script>
</body>
</html>
'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
