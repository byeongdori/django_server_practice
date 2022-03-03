# DB 설정 파일을 별도로 보관하여 보관

DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test_db',    # 데이터베이스명
        'USER': 'root',
        'PASSWORD': 'RLAQUDWN141!',    # 데이터베이스 비밀번호
        'HOST': 'localhost',
        'PORT': '3306',
    }
}