# A Question in Zhihu
[![author][badge-author]][my-zhihu] [![py-version][badge-py-version]][pypi] [![license][badge-license]][license]

##起因
某变态进入我航主南女卫生间偷拍被抓，我院希望息事宁人，引起广大学生不满，知乎上
同学们群情激奋。我对大家的言论很感兴趣，所以决定爬去该问题的发言做做调研
[问题链接](https://www.zhihu.com/question/46977820)

##目标
1. 统计该问题下所有发言的词频
2. 统计所有相关用户回答数量
3. 统计最活跃的10位用户发言的词频
4. 画个词云
5. 为每个用户的发言建立词向量
6. 对上述用户进行聚类
7. 分析各簇特点

##需要
- jieba
- zhihu_oauth
- scikit-learn
- matplotlib
- wordcloud
**可用pip自行安装**
- msyh.ttf，微软雅黑字体

##步骤
- [x] 获得该问题下的所有答案，记录答案ID，答案（0表示该记录为问题或答案），作者ID，内容
- [x] 获得每个答案下的所有评论，记录评论ID, 答案（所属答案的ID）,作者ID，内容
- [x] 将上述数据写入分隔符为‘|’的CSV文件。
- [x] 为所有用户建立属性为用户ID,用户名, 行业，学校，专业，公司，职位，地点的csv文件
- [x] 为整个数据集建立词频向量，内存中的格式为（用户, 词频向量）
- [x] 以一个用户的发言词频向量表征该用户，尝试集中聚类，看看类别中的用户在学校专业上有什么共同点。

##保证
- 纯属个人娱乐
- 绝不公开个人信息
- 一切可视化做脱敏处理

##用法
1. 爬取某问题下的相关用户信息
```
python user.py username password question_num
```
username: 你的知乎用户名，如+86130xxxxxxxx
password：你的知乎密码
question_num: 知乎问题号，该问题网页结尾处的那一串数字

2. 爬去某问题下的回答和评论并完成分词去停用词的操作
```
python says.py username password question_num
```

3. 统计top n词汇的词频
```
python freq.py n
```
n: 前n个出现频率高的词

4. 其他并未指定参数，lsa,聚类的参数需要自己设置