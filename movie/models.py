from django.db import models
from django.contrib.auth.models import User


# チェックした内容を入れる箱
class Check (models.Model):
    ch1 = models.BooleanField(default=False, verbose_name="1")
    ch2 = models.BooleanField(default=False, verbose_name="2")
    ch3 = models.BooleanField(default=False, verbose_name="3")
    ch4 = models.BooleanField(default=False, verbose_name="4")
    ch5 = models.BooleanField(default=False, verbose_name="5")
    ch6 = models.BooleanField(default=False, verbose_name="6")
    ch7 = models.BooleanField(default=False, verbose_name="7")
    ch8 = models.BooleanField(default=False, verbose_name="8")
    ch9 = models.BooleanField(default=False, verbose_name="9")
    ch10 = models.BooleanField(default=False, verbose_name="10")
    ch11 = models.BooleanField(default=False, verbose_name="11")
    ch12 = models.BooleanField(default=False, verbose_name="12")
    ch13 = models.BooleanField(default=False, verbose_name="13")
    ch14 = models.BooleanField(default=False, verbose_name="14")
    ch15 = models.BooleanField(default=False, verbose_name="15")
    ch16 = models.BooleanField(default=False, verbose_name="16")
    ch17 = models.BooleanField(default=False, verbose_name="17")
    ch18 = models.BooleanField(default=False, verbose_name="18")
    ch19 = models.BooleanField(default=False, verbose_name="19")
    ch20 = models.BooleanField(default=False, verbose_name="20")
    ch21 = models.BooleanField(default=False, verbose_name="21")
    ch22 = models.BooleanField(default=False, verbose_name="22")
    ch23 = models.BooleanField(default=False, verbose_name="23")
    ch24 = models.BooleanField(default=False, verbose_name="24")
    ch25 = models.BooleanField(default=False, verbose_name="25")
    ch26 = models.BooleanField(default=False, verbose_name="26")
    ch27 = models.BooleanField(default=False, verbose_name="27")
    ch28 = models.BooleanField(default=False, verbose_name="28")
    ch29 = models.BooleanField(default=False, verbose_name="29")
    ch30 = models.BooleanField(default=False, verbose_name="30")
    ch31 = models.BooleanField(default=False, verbose_name="31")
    ch32 = models.BooleanField(default=False, verbose_name="32")
    ch33 = models.BooleanField(default=False, verbose_name="33")
    ch34 = models.BooleanField(default=False, verbose_name="34")
    ch35 = models.BooleanField(default=False, verbose_name="35")
    ch36 = models.BooleanField(default=False, verbose_name="36")
    ch37 = models.BooleanField(default=False, verbose_name="37")
    ch38 = models.BooleanField(default=False, verbose_name="38")
    ch39 = models.BooleanField(default=False, verbose_name="39")
    ch40 = models.BooleanField(default=False, verbose_name="40")
    ch41 = models.BooleanField(default=False, verbose_name="41")
    ch42 = models.BooleanField(default=False, verbose_name="42")
    ch43 = models.BooleanField(default=False, verbose_name="43")
    ch44 = models.BooleanField(default=False, verbose_name="44")
    ch45 = models.BooleanField(default=False, verbose_name="45")
    ch46 = models.BooleanField(default=False, verbose_name="46")
    ch47 = models.BooleanField(default=False, verbose_name="47")
    ch48 = models.BooleanField(default=False, verbose_name="48")

    def __str__(self):
        return History.objects.get()

# 映画の基礎情報を入れる箱
class Data(models.Model):
    no = models.IntegerField()
    title = models.CharField(max_length=100)
    memo = models.CharField(max_length=500)
    year = models.IntegerField()
    picture = models.ImageField(default=False, verbose_name="メイン画像")

    ch1 = models.BooleanField(default=False, verbose_name="１時間")
    ch2 = models.BooleanField(default=False, verbose_name="１時間半")
    ch3 = models.BooleanField(default=False, verbose_name="２時間")
    ch4 = models.BooleanField(default=False, verbose_name="２時間半")
    ch5 = models.BooleanField(default=False, verbose_name="３時間以上")
    ch6 = models.BooleanField(default=False, verbose_name="ニュートラル")
    ch7 = models.BooleanField(default=False, verbose_name="気分上々")
    ch8 = models.BooleanField(default=False, verbose_name="超元気")
    ch9 = models.BooleanField(default=False, verbose_name="明るくなりたい")
    ch10 = models.BooleanField(default=False, verbose_name="疲れた")
    ch11 = models.BooleanField(default=False, verbose_name="何も考えたくない")
    ch12 = models.BooleanField(default=False, verbose_name="ただ笑いたい")
    ch13 = models.BooleanField(default=False, verbose_name="アンニュイ")
    ch14 = models.BooleanField(default=False, verbose_name="そもそも映画みれるかな？")
    ch15 = models.BooleanField(default=False, verbose_name="ビジネス")
    ch16 = models.BooleanField(default=False, verbose_name="スポーツ")
    ch17 = models.BooleanField(default=False, verbose_name="ファッション")
    ch18 = models.BooleanField(default=False, verbose_name="音楽")
    ch19 = models.BooleanField(default=False, verbose_name="旅行")
    ch20 = models.BooleanField(default=False, verbose_name="ゲーム")
    ch21 = models.BooleanField(default=False, verbose_name="歴史")
    ch22 = models.BooleanField(default=False, verbose_name="海外")
    ch23 = models.BooleanField(default=False, verbose_name="サイエンス")
    ch24 = models.BooleanField(default=False, verbose_name="エンタメ")
    ch25 = models.BooleanField(default=False, verbose_name="不思議")
    ch26 = models.BooleanField(default=False, verbose_name="マニアックな情報")
    ch27 = models.BooleanField(default=False, verbose_name="前向きになりたい")
    ch28 = models.BooleanField(default=False, verbose_name="向上心")
    ch29 = models.BooleanField(default=False, verbose_name="自分探し")
    ch30 = models.BooleanField(default=False, verbose_name="自分が嫌い")
    ch31 = models.BooleanField(default=False, verbose_name="自分が大好き")
    ch32 = models.BooleanField(default=False, verbose_name="努力できない")
    ch33 = models.BooleanField(default=False, verbose_name="ドキドキ")
    ch34 = models.BooleanField(default=False, verbose_name="わくわく")
    ch35 = models.BooleanField(default=False, verbose_name="ハラハラ")
    ch36 = models.BooleanField(default=False, verbose_name="恋愛って。。")
    ch37 = models.BooleanField(default=False, verbose_name="知的好奇心")
    ch38 = models.BooleanField(default=False, verbose_name="視点")
    ch39 = models.BooleanField(default=False, verbose_name="アーティスティック")
    ch40 = models.BooleanField(default=False, verbose_name="超常現象")
    ch41 = models.BooleanField(default=False, verbose_name="希望")
    ch42 = models.BooleanField(default=False, verbose_name="夢探し")
    ch43 = models.BooleanField(default=False, verbose_name="美しさ")
    ch44 = models.BooleanField(default=False, verbose_name="古き良き時代")
    ch45 = models.BooleanField(default=False, verbose_name="怖いことなど何もない")
    ch46 = models.BooleanField(default=False, verbose_name="未来予想図")
    ch47 = models.BooleanField(default=False, verbose_name="Based on T")

    def __str__(self):
        return '< Data (タイトル) : ' + str(self.title) + ' >'


# 映画の画像を入れる箱
# class Picture(AbstractBaseUser, PermissionsMixin):
#     picture_image = models.ImageField(null=True, blank=True)
    # FileField(upload_to="media")

# 結果履歴を入れる箱
class History (models.Model):
    pub_date = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=300)

    def __str__(self):
        return str(self.pub_date)

    class Meta:
        ordering = ('-pub_date',)
