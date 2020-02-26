from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import AnalysisTask, CollectType
from .forms import UploadFileForm


# Create your views here.
def index(request):
    devices_list = [{'id': i, 'name': 'device_%s' % i} for i in range(5)]
    context = locals()
    return render(request, 'devices_collect/index.html', context)

'''
/devices_collect/detail/d_id
'''
def detail(request, d_id):
    devices_list = [{'id': i, 'name': 'device_%s' % i} for i in range(5)]
    device_name = 'device_%s' % d_id
    device = devices_list[d_id % 5]
    d_id = d_id + 1
    context = locals()
    return render(request, 'devices_collect/details.html', context)

def analysis_result(request):
    pass

# 任务启动页面
'''
上传excel，输入分析参数，等待结果
pic放在picitures/task/

task表：task_id, name, creator, time, 

显示上述信息+任务分析结果链接
'''
def analysis_task_page(request):
    pass


'''
新建任务---产生任务id--->任务表单填充---后台生成任务进程--->提示任务新建成功
'''

'''
新建任务
'''
def analysis_task_create(request):
    title = '收集任务页'
    collect_types = CollectType.objects.all()
    context = locals()
    return render(request, 'devices_collect/task_create.html', context)


'''
填充表单
1、上传excel文件
2、输入任务名和相关定制参数
3、提交按钮
'''
def analysis_task_info(request):
    task = AnalysisTask()
    task.creator = 'gary'
    task.save()
    context = locals()
    return render(request, 'devices_collect/analysis_task_info.html', context)


'''
返回任务生成信息
'''
def analysis_task_submit_res(requset):
    pass

'''
上传文件
'''
def do_upload_file(request):
    if request.method == 'POST':
        files = request.FILES.getlist('file', None)
        for file in files:
            from devices_collect.utils.ExcelHandler import handle_upload_file
            handle_upload_file(file, '0')
            # return HttpResponseRedirect('devices_collect/index.html')
    return HttpResponse('上传成功')

def upload_file(request):
    return render(request, 'devices_collect/upload_file.html', {})