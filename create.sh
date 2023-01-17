
#!/bin/bash
echo '输入文件名称'
read fileName
echo '输入git文件路径'
read git_prefix
echo '输入开始时间(格式yyyy-mm-dd)'
read startTime
echo '输入结束时间(格式yyyy-mm-dd)'
read endTime
echo '输入屏蔽记录关键字(逗号分隔)'
read text
#获取当前目录路径
projectHome=`pwd`
echo $projectHome

cd $git_prefix

git_log(){
    git log --pretty=format:"%ai , %s" --since=$startTime --before=$endTime >> commit.csv
    mv commit.csv $projectHome
}

git_log
cd $projectHome
python ReadCsv.py --fileName $fileName --text $text
