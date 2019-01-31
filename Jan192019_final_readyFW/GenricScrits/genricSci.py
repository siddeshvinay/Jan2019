from PROSpecific import test1
import xlrd
import xlutils
import xlwt
from GenricScrits import ParanObject as PO
from GenricScrits import MapObject as MO
def readXLdataupdate(self,FileName, SheetName):
    try:
        openXL=xlrd.open_workbook(FileName)
        XLsheet=openXL.sheet_by_name(SheetName)
        Mapob=MO.MapObject()
        par = PO.Param_Object()
        TestCaseMap = {}
        KeyWordMap = {}
        Classname=[]
        KeywordName=[]
        Parmlist=[]
        TCmap={}
        Keymap={}
        prama=None


        numrow=XLsheet.nrows
        i=0

        while i< numrow:
            rowval=XLsheet.cell_value(i,0)
            if rowval.find("[COMMENT]")==-1 and rowval.find("END")==-1:
                if rowval.find("TestCase")>-1:
                    Runstatus=XLsheet.cell_value(i,1)
                    if int(Runstatus)==1:
                        TCID=XLsheet.cell_value(i,3)
                        # print(TCID)
                        TCDES=XLsheet.cell_value(i,4)
                        TestCaseMap[TCID] = prama


                        pralist = []

                        for j in range(i+1, numrow):
                            cellval=XLsheet.cell_value(j,0)
                            # print(cellval)
                            if cellval.find("[COMMENT]") == -1 and cellval.find("END") == -1 and cellval.find("TestCase")==-1:
                                cellcount=XLsheet.ncols

                                for x in range(cellcount):
                                    # Parmlist = []
                                    # par=PO.Param_Object()

                                    keycell=XLsheet.cell_value(j,x)
                                    if x==0:
                                        KeywordName=XLsheet.cell_value(j,0)
                                        # par.setKeywordName(KeywordName)
                                        Mapob.setKeywordName(KeywordName)
                                    elif x==2:
                                        Classname=XLsheet.cell_value(j,2)
                                        # par.setClassName(Classname)
                                        Mapob.setClassName(Classname)
                                    elif x >=3:
                                        prama=XLsheet.cell_value(j, x)
                                        if prama.find("##")==-1:
                                            Parmlist.append(XLsheet.cell_value(j, x))
                                            # print(Parmlist)
                                        else:
                                            break
                                    # par.setRowNumber(j+1)
                                    # par.setparmlist(Parmlist)
                                    # Mapob.setRowNumber(j+1)
                                    # Mapob.setparmlist(Parmlist)
                                    # pralist.append(Mapob.getparmlist())
                                    # print(pralist)


                            elif cellval.find("TestCase") > -1:
                                break
                            elif cellval.find("END") > -1:
                                count=1
                                break
                        # TCID=XLsheet.cell_value(i,3)
                        # TCDES=XLsheet.cell_value(i,28)
                        # TestCaseMap[TCID]=TCDES

                        # KeyWordMap[TCID]=pralist

                    else:
                        for j in range(i+2, numrow):
                            cellval = XLsheet.cell_value(j, 0)
                            if cellval.find("TestCase")>-1:
                                break
                            elif cellval.find("END") >-1:
                                count=1
                                break
                    # i = j
            elif cellval.find("END")>-1:
                break
            i=i+1
            Mapob.setTcMap(TestCaseMap)
            # Mapob.setKeyMap(KeyWordMap)
            # print(Mapob.getparmlist())


        return Mapob

    except Exception as e:
        print(e)


def getkeywordandtestvalues():
    FileName = "C:/Users/Dell/PycharmProjects/MYFW/Controller_XLsheets/Testdata.xlsx"
    SheetName = "Data"
    mapobje = readXLdataupdate("Test", FileName, SheetName)
    TCMAP = {}
    KEYWORDMAP = {}
    r = 0
    cTT = 5
    cGTNID = 6
    rowNum = 3
    iTCid = 3
    objList = []
    TCMAP.update(mapobje.getTcMap())
    KEYWORDMAP.update(mapobje.getKeyMap())
    # print(TCMAP.keys())
    # print(KEYWORDMAP)

    for setkey in TCMAP.keys():
        # print(setkey)
        TestKeyset = setkey

        # FileName = "C:/Users/Dell/PycharmProjects/MYFW/Controller_XLsheets/GTN_5728.xlsx"
        # SheetName = "Data"
        openXL = xlrd.open_workbook(FileName)
        XLsheet = openXL.sheet_by_name(SheetName)
        ncol = XLsheet.ncols
        # print(ncol)

        keyword=None
        ClassName=None
        rownum=None
        for row in range(XLsheet.nrows):
            for col in range(XLsheet.ncols):
                if XLsheet.cell_value(row, col) == TestKeyset:
                    rownum = row
                    Keyword = XLsheet.cell_value(rownum, 0)
                    if Keyword!="TestCase":
                        ClassName = XLsheet.cell_value(rownum, 2)
                        # print(rownum, " + ", Keyword, " + ", ClassName)
                        TestData = XLsheet.row_values(rownum, 3, ncol)
                        TestValues = []
                        for x in range(len(TestData)):
                            if TestData[x] == "##":
                                break
                            else:
                                TestValues.append(TestData[x])
                        test1.Testcasae1(ClassName, TestValues)
                        # test1.Testcasae1(ClassName)


                        # return keyword, ClassName, TestValues


#getkeywordandtestvalues()
    #test=KEYWORDMAP.get(TestKeyset)
    #print(len(test))
    # print(mapobje.getKeywordname())




