from django.db import models

# Model = DB의 테이블
# Field = DB의 컬럼

# 북마크를 만들 때 북마크 이름(varchar), URL 주소(varchar)가 필요

class Bookmark(models.Model):
    name = models.CharField('이름', max_length=100)
    # URLField는 (var)Charfield와 같은 형태를 갖고 있음
    url = models.URLField('URL')
    # 아래 2개는 Django에서 자동으로 들어가기 때문에 화면단에 따로 표시하지 않음.
    # DateTimeField = Django에서 생성시 자동으로 시간을 생성
    created_at = models.DateTimeField('생성 일시', auto_now_add=True)
    # Update시 자동으로 시간을 생성
    updated_at = models.DateTimeField('수정 일시', auto_now=True)


    def __str__(self):
        return self.name

    # 추가적으로 admin등 사용할 때 필요한 부부이 있어서 작성 / 위쪽 Bookmark 클래스만 정의해도 무관함.
    class Meta:
        verbose_name = '북마크'
        verbose_name_plural = '북마크 목록'

# makemigrations => migration.py라는 파일을 생성한다.
# 실제 DB에는 영향이 없으나, 실제 DB에 넣기 위한 정의를 하는 파일을 생성하는 것이다.

# migrate => migrations 폴더 안에 있는 migration 파일들을 실제 DB에 적용을 하는 명령어이다.

# migration => git의 commit과 같음 => github에 바로 적용되는 것이 아님 = DB에 바로 적용 X, [적용할] 파일 생성
# migrate => git의 push와 같음 => github에 바로 적용됨 = DB에 바로 적용됨, migrations 파일(들) 기록을 가지고 적용한다.