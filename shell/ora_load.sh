#!/bin/ksh

###########################################################################################

#脚本名称: load.sh

#脚本功能: 导入数据文件到指定数据库的指定数据表中

#涉及文件:

#脚本调用: sh load.sh -u user -p passwd -i sid -a '|' -f file.unl -t tablename

#脚本参数:    

#输出文件: 

#返回值 : 

#使用实例:    

# sh load.sh -u fhts -p fhts -i odsbptdb -a '|' -f tmp.unl -t tmp -m truncate

# yyyy-mm-dd (日期格式，如果不填默认yyyymmdd)

#编写人 : sqniu

#编写日期: 2009/10/16

###########################################################################################

usage(){
                echo
                echo " $0(数据装载)"
                echo " ===================="
                echo " Usage:"
                echo " sh $0 -u -p -i -t -f -a -e -d "
                echo " 参数:"
                echo " -u oracle数据库用户"
                echo " -p oracle数据库密码"
                echo " -i oracle tra_id"
                echo " -t 要装载的数据库表"
                echo " -f 需要装载数据文件(包括绝对路径)"
                echo " [-a] 记录分隔符,默认为'|'"
         echo " [-ae] 包含字段数据特殊符"
         echo " [-d] 载入时间类型"
                echo " [-l] 装载数据行数 默认全部装入"
         echo " [-e] 载如文件的结束符"
                echo " [-nls] 装载数据字符集 UTF8 或者ZHS16GBK"
         echo " [-s] 跳过文件行数"
         echo " [-m] 数据装载方式TRUNCATE APPEND INSERT,默认TRUNCATE"
         echo " [-txt] 文件预处理S清除文件空格A文件尾加分隔符U文件转换UNIX格式"
                echo " [-c] 参数文件 字段名@字段后置处理"
         echo " [-cm] 参数文件内容默认追加，A 末尾追加，R 全量替换 ，H 依据文件头信息"
                echo
                exit -1
}
# 函数

writeLog()
{
    echo -e $1
    echo -e $1 >>$LOG
}
mk_control_file()
{
_USER_PSWD=$1
_Separator=$2
_File=$3
_TableName=$4
_Meathod=$5

DescTempFile=${Base_File}.desc.$$
DescTempFile2=${Base_File}.2.desc.$$
SqlLog=${Base_File}.log.$$
sqlplus -S ${_USER_PSWD} <<TMP >>/dev/null
set echo off;
set feedback off;
set tab off;
set heading off;
set pagesize 0;
set linesize 1000;
set numwidth 12;
set termout off;
set trimout on;
set trimspool on;

spool ${DescTempFile};
desc ${_TableName}
spool off;
TMP
if [ $? != 0 ]
then
    writeLog "\n====================\n数据库连接错误！\n===================="
    exit -1
fi
Line_File="AAAAA"
if [ -f ${DescTempFile} ]
then
    cat ${DescTempFile}|sed '1,2d'|sed 's/[ ][ ]*/ /g'|sed '$d'|sed 's/^ //g'|awk '{if ($2=="DATE" || $4=="DATE") {print $1 " DATE \"'${DateType}'\""} else {print $1}}'|sed 's/$/,/g'|sed '$s/,$//'|sed '/^$/d'|sed 's/NOT NULL //g'|sed 's/ VARCHAR2/ CHAR/g'|sed 's/ VARCHAR/ CHAR/g'>>${DescTempFile2}
Line_File=`head -1 ${DescTempFile}`
else
        rm -f ${DescTempFile}
        rm -f ${DescTempFile2}
    writeLog "\n====================\n数据库连接错误！\n===================="
    exit -1
fi

if [ ${Line_File:0:5} = "ERROR" ]
then
rm -f ${DescTempFile}
rm -f ${DescTempFile2}
writeLog "\n====================\n表不存在！\n===================="
exit -1
fi

echo "LOAD DATA ${Nls_String} INFILE '${_File}' ${Line_closed} BADFILE 'bad_${_TableName}.bad' ${_Meathod} INTO TABLE ${_TableName} FIELDS TERMINATEd BY \"${_Separator}\" " > ${Base_File}.ctl
echo ${End_Sqlite} >>${Base_File}.ctl
echo "TRAILING NULLCOLS ">>${Base_File}.ctl
echo "(">>${Base_File}.ctl
cat ${DescTempFile2} >>${Base_File}.ctl
rm -f ${_TableName}
rm -f ${DescTempFile}
rm -f ${DescTempFile2}

}

mk_exec_shell()
{
_USER_PSWD=$1
_Separator=$2
_File=$3
_TableName=$4
_SkipRow=$5
    echo "sqlldr ${_USER_PSWD} control=${Base_File}.ctl skip=${_SkipRow} ${Load_rows} rows=${CtlRow} errors=10000 bindsize=${BindSize} readsize=${ReadSize} log=log_${Base_File}.log bad=bad_${Base_File}.bad" > load_${Base_File}.sh
}

if [ $# -lt 5 ]

then
    echo "参数有误,请检查......"
        usage
fi

while [ 1 ]
    do
        if [ "$1" = "-u" ]
        then
            shift 1
            user=$1
        fi

        if [ "$1" = "-p" ]
        then
            shift 1
            passwd=$1
        fi

        if [ "$1" = "-i" ]
        then
            shift 1
            server=$1
        fi

        if [ "$1" = "-t" ]
        then
            shift 1
            TableName=$1
        fi

        if [ "$1" = "-f" ]
        then
            shift 1
            File=$1
        fi

    if [ "$1" = "-a" ]
        then
            shift 1
            Separator=$1
        fi

    if [ "$1" = "-d" ]
        then
            shift 1
            DateType=$1
        fi

    if [ "$1" = "-s" ]
        then
            shift 1
            SkipLine=$1
        fi
      if [ "$1" = "-m" ]
        then
            shift 1
            Meathod=$1
        fi
        
        if [ "$1" = "-l" ]
        then
            shift 1
            Load_rows=$1
        fi
        if [ "$1" = "-ae" ]
        then
            shift 1
            End_Sqlite=$1
        fi
        if [ "$1" = "-e" ]
        then
            shift 1
            Line_closed=$1
        fi
        if [ "$1" = "-nls" ]
        then
            shift 1
            Nls_String=$1
        fi
      if [ "$1" = "-c" ]
        then
            shift 1
            Config=$1
        fi
        if [ "$1" = "-txt" ]
        then
            shift 1
            Prepare=$1
        fi
    if [ "$1" = "-cm" ]
        then
            shift 1
            ConfigP=$1
        fi
     shift 1
        if [ $# -eq 0 ]

        then
            break
        fi
    done

    if [ "$SkipLine" = "" ]
    then
        SkipLine=0
    fi
    if [ "$Separator" = "" ]
    then
        Separator="|"
    fi
    if [ "$DateType"x = ""x ]
    then
        DateType=yyyymmdd
    fi
    if [ "$Meathod" = "" ]
    then
        Meathod=TRUNCATE 
    fi
    if [ "$End_Sqlite" != "" ]
    then
        End_Sqlite="OPTIONALLY ENCLOSED BY "$End_Sqlite
    fi
    if [ "$Load_rows" != "" ]
    then
        Load_rows="load="$Load_rows
    fi
    if [ "$Nls_String" != "" ]
    then
        Nls_String="CHARACTERSET "$Nls_String
    fi
    if [ "$Line_closed" = "w" ]
    then
        Line_closed=\""str "X\'0D0A\'\"
    fi
USER_PSWD=$user/$passwd@$server

Base_File=`basename $File`

# 环境变量区
DATE=`date +%Y%m%d`
LOG=$HOME/log/$DATE/LoadTable/$File.$DATE 
LOG_DIR=`dirname $LOG`
CtlRow=100000
BindSize=16384000
ReadSize=16384000

if [ ! -d $LOG_DIR ]
then
    mkdir -p $LOG_DIR
    retcode=$?
    if [ "$retcode" != "0" ]
    then
        echo -e "\n==================\n 不能创建日志文件路径\n=================="
        exit -1
    fi
fi
if [ ! -f $LOG ]
then
    >$LOG
    retcode=$?
    if [ "$retcode" != "0" ]
    then
        echo -e "\n==================\n 不能创建日志文件 \n==================="
        exit -1
    fi
fi

   cp $File ${File}.temp
if [ "${Prepare:0:1}" = "U" ] || [ "${Prepare:1:1}" = "U" ] || [ "${Prepare:2:1}" = "U" ]
then
   dos2unix ${File}.temp
fi
 
if [ "${Prepare:0:1}" = "S" ] || [ "${Prepare:1:1}" = "S" ] || [ "${Prepare:2:1}" = "S" ]
then
      sed -i 's/ //g' ${File}.temp
fi
if [ "${Prepare:0:1}" = "A" ] || [ "${Prepare:1:1}" = "A" ] || [ "${Prepare:2:1}" = "A" ]
then
      sed -i 's/$/'${Separator}'/g' ${File}.temp
fi

mk_control_file $USER_PSWD $Separator ${File}.temp $TableName $Meathod
if [ "$ConfigP" = "" ]
then
        echo ")">>${Base_File}.ctl
fi

if [ "$ConfigP" = "A" ]
then
       while read LINE
       do
       if [ `echo ${LINE:0:1}` == '#' ]
       then
       continue
       fi
       Tab_Line1=`echo ${LINE}|awk -F '@' '{print $1}'|tr a-z A-Z`
       Tab_Line2=`echo ${LINE}|awk -F '@' '{print $2}'`
       sed -i 's/'${Tab_Line1}'/'${Tab_Line1}${Tab_Line2}'/g' ${Base_File}.ctl
       done<${Config}
fi

if [ "$ConfigP" = "R" ]
then
           sed -i '5,$d' ${Base_File}.ctl
       while read LINE
       do
       if [ `echo ${LINE:0:1}` == '#' ]
       then
       continue
       fi
       Tab_Line1=`echo ${LINE}|awk -F '@' '{print $1}'|tr a-z A-Z`
       Tab_Line2=`echo ${LINE}|awk -F '@' '{print $2}'`
       echo ${Tab_Line1}${Tab_Line2},>> ${Base_File}.ctl
       done<${Config}
       sed -i '$s/,$//' ${Base_File}.ctl
       sed -i '/^$/d' ${Base_File}.ctl
    echo ")" >>${Base_File}.ctl
fi


if [ "$ConfigP" = "H" ]
then
        SiikipLine=1
        sed -i '5,$d' ${Base_File}.ctl
        head -1 ${File}.temp >${Base_File}.hctl
        sed -i 's/'${Separator}'/,/g' ${Base_File}.hctl
        sed -i '$s/,$//' ${Base_File}.hctl
        sed -i '/^$/d' ${Base_File}.hctl
        cat ${Base_File}.hctl >>${Base_File}.ctl
        echo ")" >>${Base_File}.ctl
fi

mk_exec_shell $USER_PSWD $Separator ${File}.temp $TableName $SkipLine
echo -e "\n=================================\n日志:log_${Base_File}.log\n================================="
