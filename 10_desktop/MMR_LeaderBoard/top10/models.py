# hihi 덕배입니다.
from http.client import HTTPException

from django.db import models
from django.http import HttpResponse


class Player(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    mmr = models.IntegerField()


def get_player_rank(rquest: HttpResponse):
    if not player_id:
        raise HTTPException(status_code=400, detail="아이디 없음. 아이디 적어주세요.")