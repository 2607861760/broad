import time
# start =time.clock()
import inputData
import filterData
import IVCompiler
import GVCompiler
import rules
import GV_Ac_Inc_Pvt
import qc
import compoundAvg
import data
import current
import curdens
import deac
import deacfitting
from functools import reduce
'''
inputData   导入csv文件
filterData  生成filterData表
IVCompiler  生成IVCompiler表
GVCompiler  生成GVCompiler表
rules       生成Activation/Inactivation
GV_Ac_Inc_Pvt   生成每个细胞均值曲线（大于10000的数据）
qc          生成qc表 得到qc score
compoundAvg         生成12化合物均值
data        fitting数据
current     current数据
curdens     CurDens_Pvt数据
deac        deac_tau数据
deacfitting  deac fitting数据
'''

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import math


class main():
    acylists = []
    inylists = []
    acmaxlist = []
    sslmaxlist = []
    aclabels = []
    inaclabels = []
    ivnames = []
    gvnames = []
    allInGV = []
    allAcIV = []
    allInIV = []
    allAcGV = []
    avglists = []
    semlists = []
    acsemlist = []
    insemlist = []
    IVlist = []
    PMlist = []
    perlists = []
    accurrentlist = []
    incurrentlist = []
    QCScorelist = []
    acnlists = []
    innlists = []
    inacindexlists = []
    acindexlists = []
    pmlist = []
    bfitlist = []
    taulist = []
    compoundtaulist = []
    acdiflists = []
    indiflists = []
    acfitlist = []
    infitlist = []
    deacfitlist = []
    deacavglists = []
    deacsemlists = []
    deacallavglist = []
    deacallsemlist = []
    acdomslist = []
    aconelist = []
    actenlist = []
    indomslist = []
    inonelist = []
    intenlist = []
    aconediflist = []
    actendiflist = []
    inonediflist = []
    intendiflist = []
    deacdiflist = []
    compoundlist = []
    alldeaclist = []
    allgvlist = []
    allcurlist=[]
    legend=[]
    colors = ['magenta', 'forestgreen', 'orange', 'royalblue']
    # compoundlist = ["DMSO", "BRD_5891", "BRD-K63095902-001-10-7", "BRD-K80149326-001-09-1",
    #                 "BRD-K29448633-001-08-1", "BRD-K64616955-001-09-7", "BRD-K00880242-001-08-1",
    #                 "BRD-K15634739-001-09-3",
    #                 "BRD-K54854617-001-09-6", "BRD-K81024213-001-07-5", "BRD-K92978277-001-08-0",
    #                 "BRD-K72469263-001-11-4"]

    def differ(a, b):
        difvalue = a-b
        return difvalue

    def confidence(list):
        newlist=[]
        for item in list:
            if item !='NAN':
                newlist.append(item)
        avg = np.average(newlist)
        std = np.std(newlist)
        interval = stats.t.interval(0.95, len(newlist) - 1, avg, std)
        return interval

    def Sample_Mean(list):
        std = np.std(list)
        sem = std/math.sqrt(len(list))
        return sem

    def tran(list):
        return [[r[col] for r in list] for col in range(len(list[0]))]

    def merge(list):
        nowlist=[[[now+32*n for now in items] for items in item] for n,item in enumerate(list)]
        newlist=[reduce(lambda x,y:x+y, item) for item in main.tran(nowlist)]
        return newlist

    def datarun(filelist, trim, cutoff, QCparameter, weightlist, comqc, curqc, deacqc):
        main.acylists = []
        main.inylists = []
        main.acmaxlist = []
        main.sslmaxlist = []
        main.aclabels = []
        main.inaclabels = []
        main.ivnames = []
        main.gvnames = []
        main.allInGV = []
        main.allAcIV = []
        main.allInIV = []
        main.allAcGV = []
        main.avglists = []
        main.semlists = []
        main.acsemlist = []
        main.insemlist = []
        main.IVlist = []
        main.PMlist = []
        main.perlists = []
        main.accurrentlist = []
        main.incurrentlist = []
        main.QCScorelist = []
        main.acnlists = []
        main.innlists = []
        main.inacindexlists = []
        main.acindexlists = []
        main.pmlist = []
        main.bfitlist = []
        main.taulist = []
        main.compoundtaulist = []
        main.acdiflists = []
        main.indiflists = []
        main.acfitlist = []
        main.infitlist = []
        main.deacfitlist = []
        main.deacavglists = []
        main.deacsemlists = []
        main.deacallavglist = []
        main.deacallsemlist = []
        main.acdomslist = []
        main.aconelist = []
        main.actenlist = []
        main.indomslist = []
        main.inonelist = []
        main.intenlist = []
        main.aconediflist = []
        main.actendiflist = []
        main.inonediflist = []
        main.intendiflist = []
        main.deacdiflist = []
        main.compoundlist = []
        main.alldeaclist = []
        main.allgvlist = []
        main.allcurlist=[]
        '''
            导入数据
        '''
        for listitem in filelist[0]:
            main.IVlist.append(inputData.readCSV(listitem))

        for listitem in filelist[1]:
            main.PMlist.append(inputData.readCSV(listitem))

        '''
            获取化合物名称
        '''
        main.compoundlist = main.tran(main.IVlist[-1])[2][3::32]
        for n in range(1, len(main.compoundlist)):
            if main.compoundlist[n-1] == main.compoundlist[n]:
                main.compoundlist[n-1] = str(main.compoundlist[n-1])+"_01"
                main.compoundlist[n] = str(main.compoundlist[n])+"_02"

        '''
            生成filterData数据
        '''
        filterDatas = []
        n = 0
        for csvitem in main.IVlist:
            filterDatas.append(filterData.filterData(
                csvitem, cutoff, trim))
            n += 1
        '''
            得到4组IV Complier
        '''
        allaccomplierIV = []
        allincomplierIV = []
        for filterDatasitem in filterDatas:
            accomplierIVs = []
            incomplierIVs = []
            for item in filterDatasitem:
                accomplierIV, incomplierIV = IVCompiler.read_excel(
                    main.IVlist[0], item, 0)
                accomplierIVs.append(accomplierIV)
                incomplierIVs.append(incomplierIV)
            allaccomplierIV.append(accomplierIVs)
            allincomplierIV.append(incomplierIVs)

        mvlist = np.linspace(-120, 20, 15)

        '''
            得到4组GV Complier和激活、失活IV/GV
        '''
        allincomplierGV = []
        allaccomplierGV = []

        for index in range(len(allaccomplierIV)):
            accomplierGV, incomplierGV = GVCompiler.read_excel(
                allaccomplierIV[index], mvlist, allincomplierIV[index])
            AcIV, InIV, AcGV, InGV = rules.rules(
                allaccomplierIV[index], allincomplierIV[index], accomplierGV, incomplierGV)
            allincomplierGV.append(incomplierGV)
            allaccomplierGV.append(accomplierGV)
            main.allAcGV.append(AcGV)
            main.allInIV.append(InIV)
            main.allAcIV.append(AcIV)
            main.allInGV.append(InGV)

        for n in range(len(main.IVlist)):
            acname = "Activation IV"+str(n+1)
            inname = "Inactivation IV"+str(n+1)
            ivname = "IV"+str(n+1)
            gvname = "GV"+str(n+1)
            main.aclabels.append(acname)
            main.inaclabels.append(inname)
            main.ivnames.append(ivname)
            main.gvnames.append(gvname)

        '''
        #     QC score
        # '''
        countlist = []
        totallist = []
        successlist = []
        Manuallist = []

        for i in range(len(main.IVlist)):
            count, total, success, Manual, QCScore = qc.qc(
                main.IVlist[i], filterDatas[i], allaccomplierIV[i], main.allAcIV[i], QCparameter, weightlist)
            countlist.append(count)
            totallist.append(total)
            successlist.append(success)
            Manuallist.append(Manual)
            main.QCScorelist.append(QCScore)

        '''
            12化合物均值（QC>=8 置信区间95%）
        '''

        main.acylists, main.inylists,acindexs,inacindexs,acstds,instds,acsems,insems,acnums,innums = compoundAvg.compound(
            main.allAcGV, main.allInGV, main.QCScorelist, comqc)
        main.acnlists, main.innlists = compoundAvg.allNlist(
            main.allAcGV, main.allInGV)
        '''组织GV导出数据'''
        acgvlist=np.asarray(main.acylists)
        ingvlist=np.asarray(main.inylists)
        acindexlist=np.asarray(acindexs)
        inacindexlist=np.asarray(inacindexs)
        acstdlist=np.asarray(acstds)
        instdlist=np.asarray(instds)
        acsemlist=np.asarray(acsems)
        insemlist=np.asarray(insems)
        gvlist=np.concatenate((acgvlist,ingvlist),axis = 2)
        indexlist=np.concatenate((acindexlist,inacindexlist),axis=2)
        stdlist=np.concatenate((acstdlist,instdlist),axis=2)
        semlist=np.concatenate((acsemlist,insemlist),axis=2)

        for n,item in enumerate(gvlist):
            npitem=[]
            for i,items in enumerate(item):
                npitem.append(list(items))
                npitem.append(list(indexlist[n][i]))
                npitem.append(list(stdlist[n][i]))
                npitem.append(list(semlist[n][i]))
            main.allgvlist.append(npitem)

        '''
            fitting每个细胞获取c值和差值
        '''

        for acitem in main.allAcGV:
            main.acfitlist.append(data.curve_fit(acitem))
            print(1111)
        for initem in main.allInGV:
            main.infitlist.append(data.curve_fit(initem))

        for n in range(len(main.acfitlist[0])):
            if main.acfitlist[1][n][2]=='NAN' or main.acfitlist[0][n][2]=='NAN' or main.acfitlist[2][n][2]=='NAN' or main.acfitlist[3][n][2]=='NAN':
                acdiflist = ['NAN', 'NAN', 'NAN']
            else:
                acdiflist = [main.differ(main.acfitlist[1][n][2], main.acfitlist[0][n][2]),
                             main.differ(main.acfitlist[2][n][2], main.acfitlist[1][n][2]),
                                          main.differ(main.acfitlist[3][n][2], main.acfitlist[1][n][2])]
            if main.infitlist[1][n][2]=='NAN' or main.infitlist[0][n][2]=='NAN' or main.infitlist[2][n][2]=='NAN' or main.infitlist[3][n][2]=='NAN':
                indiflist = ['NAN', 'NAN', 'NAN']
            else:
                indiflist = [main.differ(main.infitlist[1][n][2], main.infitlist[0][n][2]),
                             main.differ(main.infitlist[2][n][2], main.infitlist[1][n][2]),
                                          main.differ(main.infitlist[3][n][2], main.infitlist[1][n][2])]
            main.acdiflists.append(acdiflist)
            main.indiflists.append(indiflist)

        '''
            QC>=8数据平均值fitting
        '''
        acavgfitlist = []
        inavgfitlist = []
        for n in range(len(main.allAcGV)):
            acavgfit = data.avg_curve_fit(
                main.allAcGV[n], main.QCScorelist[n], comqc)
            inavgfit = data.avg_curve_fit(
                main.allAcGV[n], main.QCScorelist[n], comqc)
            acavgfitlist.append(acavgfit)
            inavgfitlist.append(inavgfit)

        '''
            生成deac数据
        '''
        intervallist = []
        k = 0
        for item in main.PMlist:
            perlist, pmlist = deac.pm(item)
            avglist = []
            semlist = []
            newperlist = main.tran(perlist)
            intervals = []
            for peritem in newperlist:
                h = 0
                for eachitem in peritem:
                    if eachitem == 100.0:
                        h += 1
                if h == len(peritem):
                    interval = (-100.0, 100.0)
                else:
                    interval = main.confidence(peritem)
                newlist = []
                m = 0
                for items in peritem:
                    if items >= interval[0] and items <= interval[1] and main.QCScorelist[k][m] >= deacqc:
                        newlist.append(items)
                    m += 1
                avglist.append(np.average(newlist))
                std = np.std(newlist)
                sem = std / math.sqrt(len(newlist))
                semlist.append(sem)
                intervals.append(interval)
            k += 1
            main.deacavglists.append(avglist)
            main.deacsemlists.append(semlist)
            main.perlists.append(perlist)
            main.pmlist.append(pmlist)
            intervallist.append(intervals)

        f = 0
        deacallstdlist=[]
        deacallindexlist=[]
        for item in main.perlists:
            nowlist = [item[i:i + 32] for i in range(0, len(item), 32)]
            denowavglist = []
            denowsemlist = []
            denowstdlist = []
            denowindexlist = []
            for nowitem in nowlist:
                nowavglist = []
                nowsemlist = []
                nowstdlist=[]
                nowindexlist=[]
                h = 0
                for eachitem in main.tran(nowitem):
                    newitem = []
                    for eachs in eachitem:
                        if eachs >= intervallist[f][h][0] and eachs <= intervallist[f][h][1]:
                            newitem.append(eachs)
                    h += 1
                    nowavglist.append(np.average(newitem))
                    std = np.std(newitem)
                    sem = std / math.sqrt(len(newitem))
                    nowsemlist.append(sem)
                    nowstdlist.append(std)
                    nowindexlist.append(len(newitem))
                denowavglist.append(nowavglist)
                denowsemlist.append(nowsemlist)
                denowstdlist.append(nowstdlist)
                denowindexlist.append(nowindexlist)
            f += 1
            main.deacallavglist.append(denowavglist)
            main.deacallsemlist.append(denowsemlist)
            deacallstdlist.append(denowstdlist)
            deacallindexlist.append(denowindexlist)
        '''组织deac导出数据'''
        deallavglist=main.tran(main.deacallavglist)
        deallsemlist=main.tran(main.deacallsemlist)
        deallstdlist=main.tran(deacallstdlist)
        deallindexlist=main.tran(deacallindexlist)

        for n, item in enumerate(deallavglist):
            npitem = []
            for i, items in enumerate(item):
                npitem.append(list(items))
                npitem.append(list(deallindexlist[n][i]))
                npitem.append(list(deallstdlist[n][i]))
                npitem.append(list(deallsemlist[n][i]))
            main.alldeaclist.append(npitem)

        '''
           deac fitting
        '''

        for item in main.pmlist:
            bfit, deacfit = deacfitting.deac_fit(item)
            main.deacfitlist.append(deacfit)
            main.bfitlist.append(bfit)
        for item in main.bfitlist:
            newlist = []
            for items in item:
                if items =='NAN':
                    newlist.append('NAN')
                else:
                    newlist.append(1 / items)
            main.taulist.append(newlist)

        aclist=main.merge(acnums)
        inlist=main.merge(innums)

        '''
            生成current数据
        '''

        for n in range(len(main.IVlist)):
            accurrent, incurrent = current.current(
                main.IVlist[n], filterDatas[n])
            main.accurrentlist.append(accurrent)
            main.incurrentlist.append(incurrent)
        main.acmaxlist, main.sslmaxlist, main.acsemlist, main.insemlist, main.acindexlists, main.inacindexlists,acnowlists,inacnowlists,acobjlist,inobjlist = curdens.CurDens_Pvt(
            main.accurrentlist, main.incurrentlist, main.QCScorelist, curqc,aclist,inlist)

        '''组织current输出数据'''
        accurlist=[]
        sslcurlist=[]
        for item in acobjlist:
            objlist = []
            objlist.append(item['avglist'])
            objlist.append(item['nlist'])
            objlist.append(item['stdlist'])
            objlist.append(item['semlist'])
            accurlist.append(objlist)
        for item in inobjlist:
            objlists=[]
            objlists.append(item['avglist'])
            objlists.append(item['nlist'])
            objlists.append(item['stdlist'])
            objlists.append(item['semlist'])
            sslcurlist.append(objlists)
        newaccurlist=np.asarray(accurlist)
        newsslcurlist=np.asarray(sslcurlist)
        main.allcurlist=[[list(items) for items in list(item)] for item in list(np.concatenate((newaccurlist,newsslcurlist),axis=2))]
        # for item in acnowlists:
        #     for items in item:
        #         for now in main.tran(items):
        #             n=len(now)
        #             avg=np.average(now)
        #             std=np.std(now)
        #             sem=std/math.sqrt(n)
        #         pass


        main.acdomslist, main.aconelist, main.actenlist = DMSO(
            main.acdiflists, main.acindexlists, comqc,aclist)
        main.indomslist, main.inonelist, main.intenlist = DMSO(
            main.indiflists, main.inacindexlists, comqc,inlist)

        main.aconediflist, main.actendiflist = gvdif(
            main.actenlist, main.aconelist,aclist)
        main.inonediflist, main.intendiflist = gvdif(
            main.intenlist, main.inonelist,inlist)

        deactaulist = deacavg(main.taulist, main.QCScorelist, deacqc)

        for n in range(len(deactaulist)):
            diflist = []
            for j in range(len(deactaulist[0])):
                dif = deactaulist[n][j]-deactaulist[n][0]
                diflist.append(dif)
            main.deacdiflist.append(diflist)

    def compic(acylists, inylists, compoundlist):  # 12化合物均值曲线
        x = np.linspace(-120, 20, 15)
        fig = plt.figure(figsize=(16, 16), dpi=80)
        st = fig.suptitle("Mean curve of 12 compounds", fontsize="x-large")
        legendline = []
        labels = ["GV(1)", "GV(2)", "GV(3)", "GV(4)"]
        colors = ["g", "b", "r", "olive"]

        ax1 = fig.add_subplot(4, 3, 1)
        for n in range(len(acylists[0])):
            line, = ax1.plot(x, acylists[0][n], color=colors[n])
            ax1.plot(x, inylists[0][n], color=colors[n])
            legendline.append(line, )
        ax1.set_title(compoundlist[0])

        ax2 = fig.add_subplot(432)
        for n in range(len(acylists[0])):
            ax2.plot(x, acylists[1][n], color=colors[n])
            ax2.plot(x, inylists[1][n], color=colors[n])
        ax2.set_title(compoundlist[1])

        ax3 = fig.add_subplot(433)
        for n in range(len(acylists[0])):
            ax3.plot(x, acylists[2][n], color=colors[n])
            ax3.plot(x, inylists[2][n], color=colors[n])
        ax3.set_title(compoundlist[2])

        ax4 = fig.add_subplot(434)
        for n in range(len(acylists[0])):
            ax4.plot(x, acylists[3][n], color=colors[n])
            ax4.plot(x, inylists[3][n], color=colors[n])
        ax4.set_title(compoundlist[3])

        ax5 = fig.add_subplot(435)
        for n in range(len(acylists[0])):
            ax5.plot(x, acylists[4][n], color=colors[n])
            ax5.plot(x, inylists[4][n], color=colors[n])
        ax5.set_title(compoundlist[4])

        ax6 = fig.add_subplot(436)
        for n in range(len(acylists[0])):
            ax6.plot(x, acylists[5][n], color=colors[n])
            ax6.plot(x, inylists[5][n], color=colors[n])
        ax6.set_title(compoundlist[5])

        ax7 = fig.add_subplot(437)
        for n in range(len(acylists[0])):
            ax7.plot(x, acylists[6][n], color=colors[n])
            ax7.plot(x, inylists[6][n], color=colors[n])
        ax7.set_title(compoundlist[6])

        ax8 = fig.add_subplot(438)
        for n in range(len(acylists[0])):
            ax8.plot(x, acylists[7][n], color=colors[n])
            ax8.plot(x, inylists[7][n], color=colors[n])
        ax8.set_title(compoundlist[7])

        ax9 = fig.add_subplot(439)
        for n in range(len(acylists[0])):
            ax9.plot(x, acylists[8][n], color=colors[n])
            ax9.plot(x, inylists[8][n], color=colors[n])
        ax9.set_title(compoundlist[8])

        ax10 = fig.add_subplot(4, 3, 10)
        for n in range(len(acylists[0])):
            ax10.plot(x, acylists[9][n], color=colors[n])
            ax10.plot(x, inylists[9][n], color=colors[n])
        ax10.set_title(compoundlist[9])

        ax11 = fig.add_subplot(4, 3, 11)
        for n in range(len(acylists[0])):
            ax11.plot(x, acylists[10][n], color=colors[n])
            ax11.plot(x, inylists[10][n], color=colors[n])
        ax11.set_title(compoundlist[10])

        ax12 = fig.add_subplot(4, 3, 12)
        for n in range(len(acylists[0])):
            ax12.plot(x, acylists[11][n], color=colors[n])
            ax12.plot(x, inylists[11][n], color=colors[n])
        ax12.set_title(compoundlist[11])

        fig.tight_layout()
        st.set_y(0.95)
        fig.subplots_adjust(top=0.92, bottom=0.08)

        plt.subplot(4, 3, 1).legend(legendline, labels, bbox_to_anchor=(
            2.2, 1.02, 1.05, 0.102), loc=4, borderaxespad=0)
        plt.show()

    def curdes_plot(acmaxlists, sslmaxlists, compoundlist):
        x = [1, 2, 3, 4]
        xlabel = ["IV1", "IV2", "IV3", "IV4"]
        fig = plt.figure(figsize=(16, 16), dpi=80)
        st = fig.suptitle("Peak Current Density", fontsize="x-large")
        legendline = []
        labels = ["Max Current Density (Ac)", "Max Current Density (SSI)"]
        ax1 = fig.add_subplot(431)
        line1, = ax1.plot(x, acmaxlists[0], color="b")
        line2, = ax1.plot(x, sslmaxlists[0], color="darkorange")
        ax1.set_title(compoundlist[0])
        legendline.append(line1,)
        legendline.append(line2,)
        ax1.set_xticks(x)
        ax1.set_xticklabels(["IV1", "IV2", "IV3", "IV4"])

        ax2 = fig.add_subplot(432)
        ax2.plot(x, acmaxlists[1], color="b")
        ax2.plot(x, sslmaxlists[1], color="darkorange")
        ax2.set_title(compoundlist[1])
        ax2.set_xticks(x)
        ax2.set_xticklabels(xlabel)

        ax3 = fig.add_subplot(433)
        ax3.plot(x, acmaxlists[2], color="b")
        ax3.plot(x, sslmaxlists[2], color="darkorange")
        ax3.set_title(compoundlist[2])
        ax3.set_xticks(x)
        ax3.set_xticklabels(xlabel)

        ax4 = fig.add_subplot(434)
        ax4.plot(x, acmaxlists[3], color="b")
        ax4.plot(x, sslmaxlists[3], color="darkorange")
        ax4.set_title(compoundlist[3])
        ax4.set_xticks(x)
        ax4.set_xticklabels(xlabel)

        ax5 = fig.add_subplot(435)
        ax5.plot(x, acmaxlists[4], color="b")
        ax5.plot(x, sslmaxlists[4], color="darkorange")
        ax5.set_title(compoundlist[4])
        ax5.set_xticks(x)
        ax5.set_xticklabels(xlabel)

        ax6 = fig.add_subplot(436)
        ax6.plot(x, acmaxlists[5], color="b")
        ax6.plot(x, sslmaxlists[5], color="darkorange")
        ax6.set_title(compoundlist[5])
        ax6.set_xticks(x)
        ax6.set_xticklabels(xlabel)

        ax7 = fig.add_subplot(437)
        ax7.plot(x, acmaxlists[6], color="b")
        ax7.plot(x, sslmaxlists[6], color="darkorange")
        ax7.set_title(compoundlist[6])
        ax7.set_xticks(x)
        ax7.set_xticklabels(xlabel)

        ax8 = fig.add_subplot(438)
        ax8.plot(x, acmaxlists[7], color="b")
        ax8.plot(x, sslmaxlists[7], color="darkorange")
        ax8.set_title(compoundlist[7])
        ax8.set_xticks(x)
        ax8.set_xticklabels(xlabel)

        ax9 = fig.add_subplot(439)
        ax9.plot(x, acmaxlists[8], color="b")
        ax9.plot(x, sslmaxlists[8], color="darkorange")
        ax9.set_title(compoundlist[8])
        ax9.set_xticks(x)
        ax9.set_xticklabels(xlabel)

        ax10 = fig.add_subplot(4, 3, 10)
        ax10.plot(x, acmaxlists[9], color="b")
        ax10.plot(x, sslmaxlists[9], color="darkorange")
        ax10.set_title(compoundlist[9])
        ax10.set_xticks(x)
        ax10.set_xticklabels(xlabel)

        ax11 = fig.add_subplot(4, 3, 11)
        ax11.plot(x, acmaxlists[10], color="b")
        ax11.plot(x, sslmaxlists[10], color="darkorange")
        ax11.set_title(compoundlist[10])
        ax11.set_xticks(x)
        ax11.set_xticklabels(xlabel)

        ax12 = fig.add_subplot(4, 3, 12)
        ax12.plot(x, acmaxlists[11], color="b")
        ax12.plot(x, sslmaxlists[11], color="darkorange")
        ax12.set_title(compoundlist[11])
        ax12.set_xticks(x)
        ax12.set_xticklabels(xlabel)

        fig.tight_layout()
        st.set_y(0.95)
        fig.subplots_adjust(top=0.92, bottom=0.08)
        plt.ylabel("Current Density (pA/pF)")

        plt.subplot(4, 3, 1).legend(legendline, labels, bbox_to_anchor=(
            2.2, 1.15, 1.05, 0.102), loc=4, borderaxespad=0)
        plt.show()


def DMSO(diflist, indexlists, comqc,index):
    scorelist = main.QCScorelist
    nowdiflist = main.tran(diflist)
    domslist = avglist(nowdiflist[0], scorelist, indexlists, 0, comqc,index)
    tenlist = avglist(nowdiflist[2], scorelist, indexlists, 2, comqc,index)
    onelist = avglist(nowdiflist[1], scorelist, indexlists, 1, comqc,index)
    return domslist, onelist, tenlist


def avglist(list, score, nlist, index, comqc,aaa):  # list,scroelist
    print(nlist)
    nowavglist = []
    interval = main.confidence(list)
    for n in range(1, 13):
        now = {}
        newlists = []
        nlists = 0
        for h in range(32):
            # t = 32 * (n - 1) + h
            # if score[0][t] >= 8 and score[1][t] >= 8 and score[2][t] >= 8 and score[3][t] >= 8:
            #     newlists.append(list[t])
            #     nlists += 1
            # if index <= 1:
                # if list[t]>=interval[0] and list[t]<=interval[1] and score[index + 1][t] >= 8 and score[index][
                #     t] >= 8:

            # else:
            #     if list[t]>=interval[0] and list[t]<=interval[1] and score[index + 1][t] >= 8 and score[index-1][
            #         t] >= 8:
            #         newlists.append(list[t])
            #         nlists += 1
            t = 32 * (n - 1) + h
            if index <= 1:
                if t in aaa[index + 1] and t in aaa[index] and t in nlist[index + 1] and t in nlist[index] and score[index + 1][t] >= comqc and score[index][
                        t] >= comqc and list[t]!='NAN':
                    newlists.append(list[t])
                    nlists += 1
            else:
                if t in aaa[index + 1] and t in aaa[index-1] and t in nlist[index + 1] and t in nlist[index - 1] and score[index + 1][t] >= comqc and \
                        score[index - 1][
                            t] >= comqc and list[t]!='NAN':
                    newlists.append(list[t])
                    nlists += 1
        now['avg'] = np.average(newlists)
        now['n'] = nlists
        now['std'] = np.std(newlists)
        now['sem'] = np.std(newlists) / nlists
        nowavglist.append(now)
    return nowavglist


def gvdif(list1, list2,indexs):
    tendiflist = []
    onediflist = []
    for n in range(len(list1)):
        dif = list1[n]['avg']-list1[0]['avg']
        tendiflist.append(dif)
        indif = list2[n]['avg'] - list2[0]['avg']
        onediflist.append(indif)
    return onediflist, tendiflist


def deacavg(list, qcscore, deacqc):
    deacavglist = []
    n = 0
    for item in list:
        interval = main.confidence(item)
        nowlist = [item[i:i + 32] for i in range(0, len(item), 32)]
        deacavg = []
        j = 0
        for nowitem in nowlist:
            newlist = []
            m = 0
            for items in nowitem:
                if items!='NAN':
                    if items >= interval[0] and items <= interval[1] and qcscore[n][j*32+m] >= deacqc:
                        newlist.append(items)
                m += 1
            deacavg.append(np.average(newlist))
            j += 1
        deacavglist.append(deacavg)
        n += 1
    return deacavglist


# end = time.clock()
# print('Running time: %s Seconds'%(end-start))
