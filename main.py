from fastapi import FastAPI
from uuid import UUID
from models import News

app = FastAPI()

db: list[News] = [
    News(id=3,
    title="Уважаемые преподаватели, студенты и партнеры Astana IT University!",
    content="Уважаемые преподаватели, студенты и партнеры Astana IT University!\
    Начиная с августа 2020 года, приступив к должности ректора Astana IT University для себя\
    я ставил три задачи: концентрация талантов (студентов и преподавателей), \
    консолидация ресурсов (инфраструктура, дом студентов, привлечение финансовых средств,\
    работа с партнерами и др.), эффективное управление (менеджмент, новые возможности для\
    студентов и преподавателей). При этом необходимо было развивать параллельно науку и \
    проекты третьей миссии вуза. Ряд инициатив мы запустили сразу, результаты которых видны \
    уже сегодня. Например, актуализация и запуск новых образовательных программ в бакалавриате, \
    магистратуре и докторантуре, а также внедрение AITU Excellence Test, AITU iCode, AITU Open,\
    AITU iQyn для отбора талантливых студентов, AITU Project Challenge для вовлечения студентов\
    в решение практических задач от заказчиков рынка. Отдельно стоит отметить открытие и запуск \
    AITU IT School для школьников старше 5 класса и Колледжа AITU IT College для школьников старше \
    9 класса кто хочет получить практические ИТ знания и дальше поступать к нам. Успешно работает наша\
    военная кафедра, где студенты получают самые передовые знания по военным наукам. Через Центр компетенции \
    и совершенствования получают образование внешние слушатели по сертифицированным программам наших партнеров\
    ИТ вендоров и в этом году впервые запущена программа МБА для сотрудников Национального банка РК. С 2022 \
    года начал работу Цифровой институт непрерывного образования со своими онлайн курсами для наших студентов."),
    
    News(id=1,
    title="Развитие цифровой культуры в высшем образовании: европейский опыт (DigCEE)",
    content="Целью модуля является рассмотрение и дальнейшее применение теоретических и практических основ развития цифровой культуры в условиях высшего образования\
    с точки зрения политики Европейского Союза.Модуль «Развитие цифровой культуры в условиях высшего образования: европейский опыт» включает в себя следующие основные мероприятия:\
    обучение (лекции и практические занятия), отчеты, круглые столы, семинары, мастер-классы, летняя школа, конференция.\
    В рамках учебного модуля обучение пройдут студенты бакалавриата образовательных программ AITU «Media Technologies», «Digital Journalism», «IT Management», «IT Entrepreneurship», \
    «Software Engineering», «Cyber Security». Модуль предоставит обучающимся возможность творчески использовать технологии и анализировать влияние технологических изменений на культурный фактор в \
    области общественных отношений. После завершения курса студенты будут иметь глубокие знания о политике ЕС в области цифровой трансформации образования, понимание о влиянии технологий на \
    социально-общественные отношения и способов использования современных информационных технологий для развития общества, а также способность аналитически применять полученные теоретические знания на практике. \
    Внедрение предлагаемого модуля будет способствовать развитию интереса к политике ЕС в области цифровизации образования, диверсификации исследований ЕС на местном и национальном уровнях. Все разработанные учебные\
    материалы после реализации проекта могут быть использованы в качестве основы для формирования европейской траектории в рамках образовательных программ вузов Казахстана."),
    
     News(id=2,
    title="Визит делегации Посольства Республики Корея в Astana IT University",
    content="5 октября 2022 года в Astana IT University состоялся визит делегации Посольства Республики Корея в Республике Казахстан, Первого Секретаря и руководителя политического отдела Мистера Янг Себёк и старшего эксперта политического отдела Есбола Сартаева.\
    В ходе встречи Проректором по академической и воспитательной работе Кумалаковым Б.А. была проведена презентация университета, его основных достижений и программ. Болатжан Арменович отметил о существовании в AITU субкультуры студентов, заинтересованных в изучении корейского языка и культуры. Таким образом, стороны обсудили возможность открытия центра корейского языка для студентов AITU.   \
    Господин Себёк, в свою очередь, подчеркнул важность развития IT- сектора, что было отражено в недавнем Послании Главы государства К.-Ж. Токаева. Также Г-н Себёк выразил глубокую благодарность за теплый прием и восхищение подробной презентацией об университете.\
    По итогам встречи был проведен ознакомительный тур по лабораториям, военной кафедре, научной библиотеке и коворкингу AITU.\
    Отметим, что на сегодняшний день Университетом заключены меморандумы о сотрудничестве с корейскими вузами, в частности с Youngsan University, Inha University и Kyungpook National University, в рамках которых предусмотрены программы академической мобильности студентов и преподавателей."),

    News(id=4,
    title="Образовательные гранты общественного фонда «Қазақстан халқына»",
    content="Целью программы является поддержка выпускников сельских школ и студентов из социально-уязвимых слоев населения, повышение доступности высшего образования для данной категории граждан страны. \
        Перечень образовательные программы высшего и/или послевузовского образования (ОВПО) университетов, участвующих в Благотворительной программе «Образовательные гранты ОФ «Қазақстан халқына» на 2022 — 2023 учебный год размещен на сайте ОФ «Қазақстан халқына»: https://qazaqstanhalqyna.kz/ru/programs/17-charity-ru/190 \
             По выбору специальностей у абитуриентов нет никаких ограничений."),

    

]

@app.get("/")
async def root():
    return {"hello": "world"}


@app.get("/api/v1/news")
async def fetch_news():
    return db

@app.post("/api/v1/news")
async def show_news(news: News):
    db.append(news)
    return {"id": news.id}