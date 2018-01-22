from django.db import models


# Create your models here.
class AreaInfo(models.Model):
    '''地区类'''
    atitle = models.CharField("当前区域", max_length=20)
    # 地区名称
    aParent = models.ForeignKey('self', null=True, blank=True)

    def __str__(self):
        return self.atitle

    class Meta:
        db_table = "booktest_areainfo"

    def title(self):
        return self.atitle

    title.admin_order_field = 'atitle'
    title.short_description = '区域名称'

    def parent(self):
        if self.aParent is None:
            return ""
        else:
            return self.aParent.atitle

    parent.short_description = '父级区域名称'


# 给pictest定义一个模型管理器类
class PictestAdmin(models.Manager):
    def add_pic_sql(self, pic_path):
        # self对应的名字在哪,这个model就是哪个的类名
        pic_test = self.model
        # 创建下面的pictest类对象
        pic_obj = pic_test()
        pic_obj.up_pics = pic_path
        pic_obj.save()
        return pic_obj


class Pictest(models.Model):
    up_pics = models.ImageField(upload_to="area/")
    object = PictestAdmin()
