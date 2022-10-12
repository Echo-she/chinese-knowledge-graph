# 政务公文的知识图谱构建研究

此项目为本人大创项目，已发表论文《基于 BiLSTM-CRF 的政务公文实体识别》，现公开代码给有需要的兄弟借鉴参考，有其他需要的可以加QQ：775075365

## 数据来源

​	该实验为政务公文命名实体识别，可以归纳为以下流程：①使用python中的scrapy框架收集政府信息公开文件，并使用pandas对数据进行前期清洗；②人工标明实体信息，按照合适百分比分割训练集，测试集，验证集；③构建神经网络模型并进行训练，测试，通过调整不同参数，结果达到最优效果；④分析结果，得到最优的实体识别模型。

​	本文数据为采集广西壮族自治区政府信息公开文件，5130条数据，共28.9M。对数据进行人工标注实体信息，采用BIO标注法，标注文件中的地点，组织，产品，时间，共4个实体类别。

​	前期人员要对训练集和测试集通过pandas清洗掉无用的数据，去重等，以免对数据标注和最终结果产生不必要的出入。

​	其次，本实验将在字符级别对文本进行编码，标记每个字符，并将每个字符的编号用作训练标签。非实体由O代表。将数据按照8:1:1分成训练集，测试集，验证集。

​	项目分为两部分，第一是命名实体识别，第二部分是关系抽取，并使用neo4j可视化。

## 命名实体识别

### 模型结构

![picture1](https://gitee.com/unlucky-she/chinese-knowledge-graph/raw/master/image/picture1.png)

### 模型参数

​	实验环境为Intel(R) Core(TM) i7-9750H，NVIDIA GeForce GTX 1650的GPU，内存为16G，硬盘容量TB。使用Python 3.7、Tensorflow 2.2.0、Keras 2.3.1的编译平台。

​	模型参数为Barth Size：64；Learning Rate：0.001；Embedding Size：200；Optimizer：Adam；Word Length：60；Epochs：30。

### 实验结果

![picture2](https://gitee.com/unlucky-she/chinese-knowledge-graph/raw/master/image/picture2.png)

![picture3](https://gitee.com/unlucky-she/chinese-knowledge-graph/raw/master/image/picture3.png)

![picture4](https://gitee.com/unlucky-she/chinese-knowledge-graph/raw/master/image/picture4.png)

![picture5](https://gitee.com/unlucky-she/chinese-knowledge-graph/raw/master/image/picture5.png)

## 知识图谱

### 关系抽取

![picture6](https://gitee.com/unlucky-she/chinese-knowledge-graph/raw/master/image/picture6.png)

### 构建知识图谱

![](https://gitee.com/unlucky-she/chinese-knowledge-graph/raw/master/image/picture7.png)

![picture8](https://gitee.com/unlucky-she/chinese-knowledge-graph/raw/master/image/picture8.png)

![picture9](https://gitee.com/unlucky-she/chinese-knowledge-graph/raw/master/image/picture9.png)