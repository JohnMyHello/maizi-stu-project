#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2015/11/3
@author: yopoing
Common模块View业务处理。
"""
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger
from django.shortcuts import render
from models import *

# 首页
def index(request):
    #课程信息
    course = Course.objects.order_by('index')[:4]
    #课程点击排序
    course_click_count = Course.objects.order_by('-click_count')
    #课程学生排序
    course_student_count = Course.objects.order_by('-student_count')
    #首页轮播广告
    ad = Ad.objects.all()
    #分页器
    Course_list = getPage(request, Course.objects.all())
    return render(request, "common/index.html", locals())


#分页代码
def getPage(request, Course_list):
        paginator = Paginator(Course_list,3)  #创建分页类，每页放置2条数据
        try:
            page = int(request.GET.get('page',1))
            Course_list = paginator.page(page)
        except(EmptyPage, InvalidPage, PageNotAnInteger):
            Course_list = paginator.page(1)
        return Course_list