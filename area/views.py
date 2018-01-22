from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from area.models import *
from django.conf import settings
# 这个是导入获取图片内容的包,里面有几个方法可以获取内容
from django.core.files.uploadedfile import InMemoryUploadedFile
from area.models import *
from django.core.paginator import Paginator


# Create your views here.
def show_area(request):
    return render(request, "area/show_area.html")


def get_prov(request):
    # 获取所有的省级信息
    areas = AreaInfo.objects.filter(aParent__isnull=True)
    # 拼接成json数据
    area_list = []
    for area in areas:
        area_list.append((area.id, area.atitle))
    return JsonResponse({"val": area_list})


def get_city(request, pid):
    area = AreaInfo.objects.get(id=pid)
    areas = area.areainfo_set.all()
    area_list = []
    for area in areas:
        area_list.append((area.id, area.atitle))
    return JsonResponse({"val": area_list})


def base(request):
    return render(request, "area/base.html")


def child(request):
    return render(request, "area/child.html")


def upload_pic(request):
    return render(request, "area/upload_pic.html")


def upload_addr(request):
    # 1 获取对应的图片对象
    pic = request.FILES["pic"]
    print(pic.name)
    # 2 生成上传路径
    pic_path = settings.MEDIA_ROOT + "/area/" + pic.name
    print(pic_path)
    # 3 把上传的文件写入到自己创建的文件内容中
    with open(pic_path, "wb") as f:
        # 这个方法表示文件内容大于64KB
        if pic.multiple_chunks():
            for pic_val in pic.chunks():
                f.write(pic_val)
        # 这里说明内容小于64KB,直接用一个read方法全部写入
        else:
            f.write(pic.read())
    # 写法一# 创建模型类对象,吧文件路径写入到数据库中
    # pic_sql = Pictest()
    # # 给数据库表中写入数据
    # pic_sql.up_pics = "area/" + pic.name
    # pic_sql.save()

    # 写法二,利用模型管理器类
    # pic_path =
    Pictest.object.add_pic_sql(pic_path)
    return HttpResponse("上传成功")


def provice_area(request, num):
    if num == "":
        num = 1
    # 查询出所有省级地区的信息
    areas = AreaInfo.objects.filter(aParent__isnull=True)
    # 对显示出来的信息进行分类
    # area1 = Paginator(areas,10) 后面跟上的参数是要分页的数据的对象和每页显示几条数据
    areas_pag = Paginator(areas, 10)
    # 打印分页之后的总页数
    print(areas_pag.num_pages)
    # 打印页码的列表
    print(areas_pag.page_range)
    # 提取出第num页的内容对象
    # areas_pag.page() 跳转到第几页,获取他的对象
    areas = areas_pag.page(num)
    print(type(num))
    # 打印当前页的页码
    print(areas.number)
    # 所有数据的总数目
    print(areas_pag.count)
    # areas的paginator属性就是上面的areas_pag对象
    # 返回当前页的查询集
    # areas.object_list
    print(areas.paginator)
    # 判断当前页是否有上一页,返回的是布尔值
    # areas.has_previous()
    # 判断当前页是否有下一页,返回的是布尔值
    # areas.has_next()
    # 返回的是当前页的上一页的页码
    # areas.previous_page_number()
    # 返回的是当前页的下一页的页码
    # areas.next_page_number()
    return render(request, "area/provice_area.html", {"areas": areas})
