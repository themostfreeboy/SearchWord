@echo off
color 1b
title 有道词典批量查询单词(ToDCY)
@echo To DCY
@echo Made By JXL
@echo 正在查询中......
@search.exe > out.txt
@echo 查询完成，查询结果存储于当前目录的"out.txt"文件中
@pause