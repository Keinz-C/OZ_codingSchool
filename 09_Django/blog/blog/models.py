from django.db import models


# 블로그 필요 요소 : 제목, 본문, 작성자, 작성일자, 수정일자, 카테고리 etc...

class Blog(models.Model):
    # 특정한 카테고리 내에서 선택할 수 있도록
    # ('DB에 들어갈 내용', '화면단에 보여질 내용')
    CATEGORY_CHOICES = (
        ('free', '자유'),
        ('travel', '여행'),
        ('cat', '고양이'),
        ('dog', '강아지'),
    )

    # CharField여도 choices가 있다면 select box를 django가 자동적으로 generate 해준다.
    category = models.CharField('카테고리', max_length=15, choices=CATEGORY_CHOICES)
    title = models.CharField('제목', max_length=100)
    content = models.TextField('본문')
    # 추후 작성자 추가
    create_at = models.DateTimeField('작성일자', auto_now_add=True)
    updated_at = models.DateTimeField('수정일자', auto_now=True)

    def __str__(self):
        return f'[{self.get_category_display()}] {self.title[:10]}'

    class Meta:
        verbose_name = '블로그'
        verbose_name_plural = '블로그 목록'