#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
__author__ = 'Гаврилов Василий 91840'

from openpyxl import load_workbook
import pymysql

print("Откреывается dataset")
wb = load_workbook('./datas/dataset.xlsx',read_only=True)
sheet_array = wb.sheetnames
#print(sheet_array[0])
#sheet = wb[sheet_array[0]]
ws = wb.active
# print(ws[0][1].value)

rows = ws.max_row
cols = ws.max_column

print("Строк: ", rows)
print("Столбцов: ", cols)

print("start ii")
i=0
#tnvdId = dict({})
t = {}
g = {}
for row in ws:
    i+=1
    if i==1:
        continue
    idDTnvd = row[1].value
    idDTehr = row[2].value
    idDGroup = row[3].value

    try:
        codes = idDTnvd.split(';')
    except Exception:
        codes = idDTnvd
    if(isinstance(codes, int)==True):
        codes = str(codes).strip()
        try:
            if len(t[codes])>0:
                t[codes][idDTehr] += 1
        except KeyError:
            try:
                if len(t[codes])>0:
                    t[codes][idDTehr] = 1
            except KeyError:
                t[codes] = {}
                t[codes][idDTehr] = 1
    if(isinstance(codes, list)==True):
        for x in codes:
            if codes.count(x) > 1:
                codes.remove(x)
        for code in codes:
            code = str(code).strip()
            try:
                if len(t[code])>0:
                    t[code][idDTehr] += 1
            except KeyError:
                try:
                    if len(t[code])>0:
                        t[code][idDTehr] = 1
                except KeyError:
                    t[code] = {}
                    t[code][idDTehr] = 1



    try:
        groups = idDGroup.split(';')
    except Exception:
        groups = idDGroup
    if(isinstance(groups, int)==True):
        groups = str(groups).strip()
        try:
            if len(g[groups])>0:
                g[groups][idDTehr] += 1
        except KeyError:
            try:
                if len(g[groups])>0:
                    g[groups][idDTehr] = 1
            except KeyError:
                g[groups] = {}
                g[groups][idDTehr] = 1
    if(isinstance(groups, list)==True):
        for x in groups:
            if groups.count(x) > 1:
                groups.remove(x)
        for group in groups:
            group = str(group).strip()
            try:
                if len(g[group])>0:
                    g[group][idDTehr] += 1
            except KeyError:
                try:
                    if len(g[group])>0:
                        g[group][idDTehr] = 1
                except KeyError:
                    g[group] = {}
                    g[group][idDTehr] = 1


    if i%3000==1:
        print(i)
    # productNumber = ws[row][0].value
    # codestnvd = ws[row][1].value
    # technicalRegulations = ws[row][2].value
    # productGroup = ws[row][3].value
    # generalProductName = ws[row][4].value
    # il = ws[row][5].value
    # applicant = ws[row][6].value
    # applicantAddress = ws[row][7].value
    # manufacturer = ws[row][8].value
    # country = ws[row][9].value
    # manufacturerAddress = ws[row][10].value
print("end")
print("Кодов ТНВД",len(t))
print("9503004900: ",t["9503004900"])
'ТР ЕАЭС 043/2017 О требованиях к средствам обеспечения пожарной безопасности и пожаротушения'
print(g["Игрушки прочие"])