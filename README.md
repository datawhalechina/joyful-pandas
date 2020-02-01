# Joyful-Pandas

#### 一、写作初衷

在使用Pandas之前，几乎所有的大型表格处理问题都是用xlrt和python循环实现，虽然这已经几乎能完成一切的需求，但其缺点也显而易见，其一就是速度问题，其二就是代码的复用性几乎为0。

曾经也尝试过去零星地学Pandas，但不得不说这个包实在太过庞大，每次使用总觉得盲人摸象，每个函数的参数也很多，学习的路线并不是十分平缓。如果你刚刚手上使用Pandas，那么在碎片的学习过程中，报错是常常发生的事，并且很难修（因为不理解内部的操作），即使修好了下次又不会，令人有些沮丧。

上个学期（2019秋季），我偶然找到了一本完全关于Pandas的书，Theodore Petrou所著的Pandas Cookbook，现在可在网上下到pdf，不过现在还没有中文版。寒假开始后，立即快速地过了一遍，发现之前很多搞不清的概念得到了较好的解答，逐步地再对着User Guide一字一句查看，最后总是建立了大的一些宏观概念。

最关键的一步，我想是通读了官方User Guide的绝大部分内容，这可能是非常重要的一个台阶，毕竟官方的教程总是会告诉你重点在哪里。因此，经过了一段时间的思考，结合了Wes Mckinney（Pandas之父）的[Python for Data Analysis](<http://93.174.95.29/_ads/A3AD6E6B2504B95EC39A6C57D465BA5D>)、先前提到的[Pandas Cookbook](<http://93.174.95.29/_ads/23950B4446ABB5DD27168D6B0FB2C8DB>)和官方的[User Guide](<https://pandas.pydata.org/pandas-docs/version/1.0.0/user_guide/index.html>)，由此想按照自己的思路编一套关于Pandas的教程，完整梳理Pandas的主线内容，杜绝浅尝辄止，保证涉及每个部分的核心概念和函数。最后，希望达到的境界自然是“所写所得即所想”，这大概需要更多的实践，也是努力实现的目标方向。

关于项目的名字，我想原先使用Pandas时非常的痛苦（Painful），那现在是时候转变为“Joyful-Pandas”了！

#### 二、编排思路

本项目共有九章，可以大致分为4个板块：

１、拿到数据必然先要读取它，分析完了数据必然是要保存它，读取了数据之后，我们面对了怎样的对象（Series? of Dataframe?）是第一重要的课题，因此了解序列和数据框的常规操作及其组件（component）便是必须涉及的内容。

２、对于一个DataFrame而言，如果一个操作使得它的元素信息减少了，那就对应了索引，即第二章的内容；如果这个操作使得数据的信息被充分地使用，那有两种可能，第一是数据被分组，从组内提取了关键的信息，第二就是数据呈现的结构或形态上的变化，使得我们更容易地能够地进一步处理数据，这两者分别对应了第三章与第四章的内容；最终如果一个操作使得原本不属于这个数据框的信息被加入了进来，那往往是涉及到了合并操作，对应了第五章的内容。从数据信息增减的角度，拆解成了3个板块，4个章节，几乎串联其了官方文档关于数据框操作的全部内容，我想这样的安排是合适的。

３、如果说前面我们关心了序列和数据框这两种容器的结构和操作，那么下面就要关心其中的元素，特别地，我们将在第六章涉及到分类变量、缺失型变量和文本型变量，第七章涉及到时间序列，第八章涉及到Pandas中的Plot模块（图可以看做元素的某种呈现）。

４、正如前面所说，Pandas的学习往往是任务驱动型，一个操作或者某个方法，不去使用自然会很快地忘记（除非你天赋异禀！），因此我在2-8章都会添加“问题和练习”的部分。其中，问题中出现的往往是对于教程中某个细节的深入，或者在这一个章节中重要的函数，希望你能够查阅相关资料阅读以解决问题；而练习部分包含了两个综合题，分别是两个不同的案例，相当于对前面所学知识的考察与综合运用，虽然并不是非常复杂，但是想要全部完成，的确是要动不少脑筋才行。最终，在第9章中会添加若干个我曾经遇到过但解决方案复杂，或者我想到的某一个一时半会儿还没有解决办法的问题，具有一定的挑战性，如果有较好的解决方案，欢迎交流分享，谢谢：）

5、基于完整性，我也为所有的章节练习编写了参考答案，当然它可能不是最好的（也许永远没有最好的），但是不失为一种提示与策略。

最后，祝你有所收获！

#### 三、内容导航

<table>
  <tr>
    <th>章节</th>
    <th>小节</th>
    <th>内容</th>
  </tr>
  <tr>
    <td>第1章：Pandas基础</td>
    <td>一、文件读取与写入</td>
    <td>1. 读取</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>2. 写入</td>
  </tr>
  <tr>
    <td></td>
    <td rowspan="2">二、基本数据结构</td>
    <td>1. Series</td>
  </tr>
  <tr>
    <td></td>
    <td>2. DataFrame</td>
  </tr>
  <tr>
    <td></td>
    <td rowspan="5">三、常用基本函数</td>
    <td>1. head和tail</td>
  </tr>
  <tr>
    <td></td>
    <td>2. unique/nunique/count/value_counts</td>
  </tr>
  <tr>
    <td></td>
    <td>3. describe函数</td>
  </tr>
  <tr>
    <td></td>
    <td>4. idxmax和nlargest</td>
  </tr>
  <tr>
    <td></td>
    <td>5. apply函数</td>
  </tr>
  <tr>
    <td></td>
    <td rowspan="2">四、排序</td>
    <td>1. 索引排序</td>
  </tr>
  <tr>
    <td></td>
    <td>2. 值排序</td>
  </tr>
  <tr>
    <td rowspan="21">第2章：索引</td>
    <td rowspan="4">一、单级索引</td>
    <td>1. loc方法、iloc方法、[]操作符</td>
  </tr>
  <tr>
    <td>2. 布尔索引</td>
  </tr>
  <tr>
    <td>3. 快速标量索引</td>
  </tr>
  <tr>
    <td>4. 区间索引</td>
  </tr>
  <tr>
    <td rowspan="5">二、多级索引</td>
    <td>1. 创建多级索引</td>
  </tr>
  <tr>
    <td>2. 索引名修改</td>
  </tr>
  <tr>
    <td>3. 多层索引切片</td>
  </tr>
  <tr>
    <td>4. 多层索引中的slice对象</td>
  </tr>
  <tr>
    <td>5. 索引层的交换</td>
  </tr>
  <tr>
    <td rowspan="6">三、索引设定</td>
    <td>1. index_col参数</td>
  </tr>
  <tr>
    <td>2. reindex方法</td>
  </tr>
  <tr>
    <td>3. reindex_like方法</td>
  </tr>
  <tr>
    <td>4. set_index方法</td>
  </tr>
  <tr>
    <td>5. reset_index方法</td>
  </tr>
  <tr>
    <td>6. rename方法</td>
  </tr>
  <tr>
    <td rowspan="3">四、常用索引型函数</td>
    <td>1. where函数</td>
  </tr>
  <tr>
    <td>2. mask函数</td>
  </tr>
  <tr>
    <td>3. query函数</td>
  </tr>
  <tr>
    <td rowspan="2">五、重复元素处理</td>
    <td>1. duplicated方法</td>
  </tr>
  <tr>
    <td>2. drop_duplicates方法</td>
  </tr>
  <tr>
    <td>六、抽样函数</td>
    <td></td>
  </tr>
  <tr>
    <td rowspan="9">第3章：分组</td>
    <td rowspan="2">一、SAC过程</td>
    <td>1. 内涵</td>
  </tr>
  <tr>
    <td>2. apply过程</td>
  </tr>
  <tr>
    <td rowspan="2">二、groupby函数</td>
    <td>1. 分组函数的基本内容</td>
  </tr>
  <tr>
    <td>2. groupby对象的特点</td>
  </tr>
  <tr>
    <td rowspan="3">三、聚合、过滤和变换</td>
    <td>1. 聚合（Aggregation）</td>
  </tr>
  <tr>
    <td>2. 过滤（Filteration）</td>
  </tr>
  <tr>
    <td>3. 变换（Transformation）</td>
  </tr>
  <tr>
    <td rowspan="2">四、apply函数</td>
    <td>1. apply函数的灵活性</td>
  </tr>
  <tr>
    <td>2. 用apply同时统计多个指标</td>
  </tr>
  <tr>
    <td rowspan="7">第4章：变形</td>
    <td rowspan="3">一、透视表</td>
    <td>1. pivot</td>
  </tr>
  <tr>
    <td>2. pivot_table</td>
  </tr>
  <tr>
    <td>3. crosstab（交叉表）</td>
  </tr>
  <tr>
    <td rowspan="2">二、其他变形方法</td>
    <td>1. melt</td>
  </tr>
  <tr>
    <td>2. 压缩与展开</td>
  </tr>
  <tr>
    <td rowspan="2">三、哑变量与因子化</td>
    <td>1. Dummy Variable（哑变量）</td>
  </tr>
  <tr>
    <td>2. factorize方法</td>
  </tr>
  <tr>
    <td rowspan="7">第5章：合并</td>
    <td rowspan="2">一、append与assign</td>
    <td>1. append方法</td>
  </tr>
  <tr>
    <td>2. assign方法</td>
  </tr>
  <tr>
    <td rowspan="2">二、combine与update</td>
    <td>1. comine方法</td>
  </tr>
  <tr>
    <td>2. update方法</td>
  </tr>
  <tr>
    <td>三、concat方法</td>
    <td></td>
  </tr>
  <tr>
    <td rowspan="2">四、merge与join</td>
    <td>1. merge函数</td>
  </tr>
  <tr>
    <td>2. join函数</td>
  </tr>
  <tr>
    <td>第6章：特殊类型数据</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>第7章：时间序列</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>第8章：可视化</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>第9章：有挑战性的例子</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td rowspan="8">参考答案</td>
    <td rowspan="2">第2章</td>
    <td>练习一</td>
  </tr>
  <tr>
    <td>练习二</td>
  </tr>
  <tr>
    <td rowspan="2">第3章</td>
    <td>练习一</td>
  </tr>
  <tr>
    <td>练习二</td>
  </tr>
  <tr>
    <td rowspan="2">第4章</td>
    <td>练习一</td>
  </tr>
  <tr>
    <td>练习二</td>
  </tr>
  <tr>
    <td rowspan="2">第5章</td>
    <td>练习一</td>
  </tr>
  <tr>
    <td>练习二</td>
  </tr>
</table>

#### 四、版本要求

１、Pandas于2020年1月29日发布了1.0.0的版本，本项目全部使用新版本

```
Python: 3.6+
Numpy: 1.17.4
Pandas: 1.0.0
Matplotlib: 3.1.2
```

#### 五、反馈

１、欢迎任何有益的建议或想法，可邮件(1801214626@qq.com)交流！

２、不免有错误，欢迎提Issues！

#### 六、参考资料

1、[Python for Data Analysis](<http://93.174.95.29/_ads/A3AD6E6B2504B95EC39A6C57D465BA5D>) Wes McKinney著

2、[Pandas Cookbook](<http://93.174.95.29/_ads/23950B4446ABB5DD27168D6B0FB2C8DB>) Theodore Petrou著

3、[User Guide for Pandas v-1.0.0](<https://pandas.pydata.org/pandas-docs/version/1.0.0/user_guide/index.html>) Pandas开发团队编写