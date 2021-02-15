from flask import Flask, url_for, render_template, url_for, request, redirect, session
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

app = Flask(__name__, static_folder='static')
Bootstrap(app)
app.debug = True
app.config.update(DEBUG=True)


@app.route('/')
def index():
    return render_template('main.html')


@app.route('/member')
def member():
    master = {'total': 5,
              'image': ['최승욱.jpg',
                        '조승우.jpg',
                        '김민석.jpg',
                        '염리민.jpg',
                        '변성훈.jpg'],
              'name': ['최승욱',
                       '조승우',
                       '김민석',
                       '염리민',
                       '변성훈'],
              'position': ['Researcher Leader',
                           'Researcher',
                           'Researcher',
                           'Researcher',
                           'Researcher'],
              'contact': ['ssnhe1234@naver.com',
                          'presco317@naver.com',
                          'tkdzma8080@naver.com',
                          'yanlimin@naver.com',
                          'Sunghoon@soongsil.ac.kr']}

    alumni_phD = {'total': 5,
                  'image': ['이경주.jpg',
                            '김설호.jpg',
                            '박영재.jpg',
                            '장효종.jpg',
                            '이나영.jpg'],
                  'name': ['이경주',
                           '김설호',
                           '박영재',
                           '장효종',
                           '이나영'],
                  'position': ['LG디스플레이',
                               '오스템임플란트',
                               '아이에프소프트',
                               'Drexel University, USA',
                               'Editorial Board Member - International Journal of Image Processing, USA']}

    alumni_MS = {'total': 19,
                 'image': ['이사무엘.jpg',
                           '윤성조.jpg',
                           '김대윤.jpg',
                           '강은정.jpg',
                           '김진서.jpg',
                           '김경섭.jpg',
                           '윤병훈.jpg',
                           '샐리.jpg',
                           '안권재.jpg',
                           '황대동.jpg',
                           '김상희.jpg',
                           '권주형.jpg',
                           '온진욱.jpg',
                           '정석현.jpg',
                           '김만기.jpg',
                           '최지수.jpg',
                           '송누리.jpg',
                           '최재갑.jpg',
                           '문지환.jpg'],
                 'name': ['이사무엘',
                          '윤성조',
                          '김대윤',
                          '강은정',
                          '김진서',
                          '김경섭',
                          '윤병훈',
                          '샐리',
                          '안권재',
                          '황대동',
                          '김상희',
                          '권주형',
                          '온진욱',
                          '정석현',
                          '김만기',
                          '최지수',
                          '송누리',
                          '최재갑',
                          '문지환'],
                 'position': ['고백기술',
                              '텔레컨스',
                              '케이엘넷',
                              '메타넷엠씨씨',
                              '아이브스',
                              'LG디스플레이',
                              'Immigration to Mexico',
                              'Vietnam',
                              '인지소프트',
                              '보성정보통신',
                              '삼성전기',
                              '한미반도체',
                              '(주)다사테크',
                              '삼성전자 VD사업부',
                              '(주)블라우비트',
                              '에스큐엔지니어링',
                              '현대오토에버',
                              '(주)이지다이아텍',
                              '']}

    return render_template('member.html', master_list=master, alumni_phD_list=alumni_phD, alumni_ms_list=alumni_MS, )


@app.route('/dataset')
def dataset():
    return render_template('dataset.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0')
