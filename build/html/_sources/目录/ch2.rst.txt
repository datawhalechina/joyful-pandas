****************************
第二章 pandas基础
****************************

.. ipython:: python
    
    import numpy as np
    import pandas as pd

在开始学习前，请保证 ``pandas`` 的版本号不低于如下所示的版本，否则请务必升级！请确认已经安装了 ``xlrd, xlwt, openpyxl`` 这三个包，其中xlrd版本不得高于 ``2.0.0`` 。

.. ipython:: python

    pd.__version__

一、文件的读取和写入
========================

1. 文件读取
-----------------

``pandas`` 可以读取的文件格式有很多，这里主要介绍读取 ``csv, excel, txt`` 文件。

.. ipython:: python

    df_csv = pd.read_csv('data/my_csv.csv')
    df_csv
    df_txt = pd.read_table('data/my_table.txt')
    df_txt
    df_excel = pd.read_excel('data/my_excel.xlsx')
    df_excel

这里有一些常用的公共参数， ``header=None`` 表示第一行不作为列名， ``index_col`` 表示把某一列或几列作为索引，索引的内容将会在第三章进行详述， ``usecols`` 表示读取列的集合，默认读取所有的列， ``parse_dates`` 表示需要转化为时间的列，关于时间序列的有关内容将在第十章讲解， ``nrows`` 表示读取的数据行数。上面这些参数在上述的三个函数里都可以使用。

.. ipython:: python

    pd.read_table('data/my_table.txt', header=None)
    pd.read_csv('data/my_csv.csv', index_col=['col1', 'col2'])
    pd.read_table('data/my_table.txt', usecols=['col1', 'col2'])
    pd.read_csv('data/my_csv.csv', parse_dates=['col5'])
    pd.read_excel('data/my_excel.xlsx', nrows=2)

在读取 ``txt`` 文件时，经常遇到分隔符非空格的情况， ``read_table`` 有一个分割参数 ``sep`` ，它使得用户可以自定义分割符号，进行 ``txt`` 数据的读取。例如，下面的读取的表以 ``||||`` 为分割：

.. ipython:: python

    pd.read_table('data/my_table_special_sep.txt')

上面的结果显然不是理想的，这时可以使用 ``sep`` ，同时需要指定引擎为 ``python`` ：

.. ipython:: python

    pd.read_table('data/my_table_special_sep.txt',
                  sep=' \|\|\|\| ', engine='python')

.. admonition:: ``sep`` 是正则参数
   :class: caution

    在使用 ``read_table`` 的时候需要注意，参数 ``sep`` 中使用的是正则表达式，因此需要对 ``|`` 进行转义变成 ``\|`` ，否则无法读取到正确的结果。有关正则表达式的基本内容可以参考第八章或者其他相关资料。

2. 数据写入
-----------------

一般在数据写入中，最常用的操作是把 ``index`` 设置为 ``False`` ，特别当索引没有特殊意义的时候，这样的行为能把索引在保存的时候去除。

.. ipython:: python

    df_csv.to_csv('data/my_csv_saved.csv', index=False)
    df_excel.to_excel('data/my_excel_saved.xlsx', index=False)

``pandas`` 中没有定义 ``to_table`` 函数，但是 ``to_csv`` 可以保存为 ``txt`` 文件，并且允许自定义分隔符，常用制表符 ``\t`` 分割：

.. ipython:: python

    df_txt.to_csv('data/my_txt_saved.txt', sep='\t', index=False)

如果想要把表格快速转换为 ``markdown`` 和 ``latex`` 语言，可以使用 ``to_markdown`` 和 ``to_latex`` 函数，此处需要安装 ``tabulate`` 包。

.. ipython:: python

    print(df_csv.to_markdown())
    print(df_csv.to_latex())

二、基本数据结构
========================

``pandas`` 中具有两种基本的数据存储结构，存储一维 ``values`` 的 ``Series`` 和存储二维 ``values`` 的 ``DataFrame`` ，在这两种结构上定义了很多的属性和方法。

1. Series
--------------

``Series`` 一般由四个部分组成，分别是序列的值 ``data`` 、索引 ``index`` 、存储类型 ``dtype`` 、序列的名字 ``name`` 。其中，索引也可以指定它的名字，默认为空。

.. ipython:: python

    s = pd.Series(data = [100, 'a', {'dic1':5}],
                  index = pd.Index(['id1', 20, 'third'], name='my_idx'),
                  dtype = 'object',
                  name = 'my_name')
    s

.. admonition:: ``object`` 类型
   :class: note

    ``object`` 代表了一种混合类型，正如上面的例子中存储了整数、字符串以及 ``Python`` 的字典数据结构。此外，目前 ``pandas`` 把纯字符串序列也默认认为是一种 ``object`` 类型的序列，但它也可以用 ``string`` 类型存储，文本序列的内容会在第八章中讨论。

对于这些属性，可以通过 ``.`` 的方式来获取：

.. ipython:: python

    s.values
    s.index
    s.dtype
    s.name

利用 ``.shape`` 可以获取序列的长度：

.. ipython:: python

    s.shape

索引是 ``pandas`` 中最重要的概念之一，它将在第三章中被详细地讨论。如果想要取出单个索引对应的值，可以通过 ``[index_item]`` 可以取出。

.. ipython:: python

    s['third']

2. DataFrame
------------------

``DataFrame`` 在 ``Series`` 的基础上增加了列索引，一个数据框可以由二维的 ``data`` 与行列索引来构造：

.. ipython:: python

    data = [[1, 'a', 1.2], [2, 'b', 2.2], [3, 'c', 3.2]]
    df = pd.DataFrame(data = data,
                      index = ['row_%d'%i for i in range(3)],
                      columns=['col_0', 'col_1', 'col_2'])
    df

但一般而言，更多的时候会采用从列索引名到数据的映射来构造数据框，同时再加上行索引：

.. ipython:: python

    df = pd.DataFrame(data = {'col_0': [1,2,3], 'col_1':list('abc'),
                              'col_2': [1.2, 2.2, 3.2]},
                      index = ['row_%d'%i for i in range(3)])
    df

由于这种映射关系，在 ``DataFrame`` 中可以用 ``[col_name]`` 与 ``[col_list]`` 来取出相应的列与由多个列组成的表，结果分别为 ``Series`` 和 ``DataFrame`` ：

.. ipython:: python

    df['col_0']
    df[['col_0', 'col_1']]

与 ``Series`` 类似，在数据框中同样可以取出相应的属性：

.. ipython:: python

    df.values
    df.index
    df.columns
    df.dtypes # 返回的是值为相应列数据类型的Series
    df.shape

通过 ``.T`` 可以把 ``DataFrame`` 进行转置：

.. ipython:: python

    df.T

三、常用基本函数
========================

为了进行举例说明，在接下来的部分和其余章节都将会使用一份 ``learn_pandas.csv`` 的虚拟数据集，它记录了四所学校学生的体测个人信息。

.. ipython:: python

    df = pd.read_csv('data/learn_pandas.csv')
    df.columns

上述列名依次代表学校、年级、姓名、性别、身高、体重、是否为转系生、体测场次、测试时间、1000米成绩，本章只需使用其中的前七列。

.. ipython:: python

    df = df[df.columns[:7]]

1. 汇总函数
---------------

``head, tail`` 函数分别表示返回表或者序列的前 ``n`` 行和后 ``n`` 行，其中 ``n`` 默认为5：

.. ipython:: python

    df.head(2)
    df.tail(3)

``info, describe`` 分别返回表的 :red:`信息概况` 和表中 :red:`数值列对应的主要统计量` ：

.. ipython:: python

    df.info()
    df.describe()

.. admonition:: 更全面的数据汇总
   :class: note

    ``info, describe`` 只能实现较少信息的展示，如果想要对一份数据集进行全面且有效的观察，特别是在列较多的情况下，推荐使用 `pandas-profiling <https://pandas-profiling.github.io/pandas-profiling/docs/master/index.html>`__ 包，它将在第十一章被再次提到。

2. 特征统计函数
-------------------

在 ``Series`` 和 ``DataFrame`` 上定义了许多统计函数，最常见的是 ``sum, mean, median, var, std, max, min`` 。例如，选出身高和体重列进行演示：

.. ipython:: python

    df_demo = df[['Height', 'Weight']]
    df_demo.mean()
    df_demo.max()

此外，需要介绍的是 ``quantile, count, idxmax`` 这三个函数，它们分别返回的是分位数、非缺失值个数、最大值对应的索引：

.. ipython:: python

    df_demo.quantile(0.75)
    df_demo.count()
    df_demo.idxmax() # idxmin是对应的函数

上面这些所有的函数，由于操作后返回的是标量，所以又称为聚合函数，它们有一个公共参数 ``axis`` ，默认为0代表逐列聚合，如果设置为1则表示逐行聚合：

.. ipython:: python

    df_demo.mean(axis=1).head() # 在这个数据集上体重和身高的均值并没有意义

3. 唯一值函数
------------------------

对序列使用 ``unique`` 和 ``nunique`` 可以分别得到其唯一值组成的列表和唯一值的个数：

.. ipython:: python

    df['School'].unique()
    df['School'].nunique()

``value_counts`` 可以得到唯一值和其对应出现的频数：

.. ipython:: python

    df['School'].value_counts()

如果想要观察多个列组合的唯一值，可以使用 ``drop_duplicates`` 。其中的关键参数是 ``keep`` ，默认值 ``first`` 表示每个组合保留第一次出现的所在行， ``last`` 表示保留最后一次出现的所在行， ``False`` 表示把所有重复组合所在的行剔除。

.. ipython:: python

    df_demo = df[['Gender','Transfer','Name']]
    df_demo.drop_duplicates(['Gender', 'Transfer'])
    df_demo.drop_duplicates(['Gender', 'Transfer'], keep='last')
    df_demo.drop_duplicates(['Name', 'Gender'],
                         keep=False).head() # 保留只出现过一次的性别和姓名组合
    df['School'].drop_duplicates() # 在Series上也可以使用

此外， ``duplicated`` 和 ``drop_duplicates`` 的功能类似，但前者返回了是否为唯一值的布尔列表，其 ``keep`` 参数与后者一致。其返回的序列，把重复元素设为 ``True`` ，否则为 ``False`` 。 ``drop_duplicates`` 等价于把 ``duplicated`` 为 ``True`` 的对应行剔除。

.. ipython:: python

    df_demo.duplicated(['Gender', 'Transfer']).head()
    df['School'].duplicated().head() # 在Series上也可以使用

4. 替换函数
----------------------

一般而言，替换操作是针对某一个列进行的，因此下面的例子都以 ``Series`` 举例。 ``pandas`` 中的替换函数可以归纳为三类：映射替换、逻辑替换、数值替换。其中映射替换包含 ``replace`` 方法、第八章中的 ``str.replace`` 方法以及第九章中的 ``cat.codes`` 方法，此处介绍 ``replace`` 的用法。

在 ``replace`` 中，可以通过字典构造，或者传入两个列表来进行替换：

.. ipython:: python

    df['Gender'].replace({'Female':0, 'Male':1}).head()
    df['Gender'].replace(['Female', 'Male'], [0, 1]).head()

另外， ``replace`` 还有一种特殊的方向替换，指定 ``method`` 参数为 ``ffill`` 则为用前面一个最近的未被替换的值进行替换， ``bfill`` 则使用后面最近的未被替换的值进行替换。从下面的例子可以看到，它们的结果是不同的：

.. ipython:: python

    s = pd.Series(['a', 1, 'b', 2, 1, 1, 'a'])
    s.replace([1, 2], method='ffill')
    s.replace([1, 2], method='bfill')

.. admonition:: 正则替换请使用 ``str.replace``
   :class: caution

    虽然对于 ``replace`` 而言可以使用正则替换，但是当前版本下对于 ``string`` 类型的正则替换还存在 `bug <https://github.com/pandas-dev/pandas/pull/36038>`__ ，因此如有此需求，请选择 ``str.replace`` 进行替换操作，具体的方式将在第八章中讲解。

逻辑替换包括了 ``where`` 和 ``mask`` ，这两个函数是完全对称的： ``where`` 函数在传入条件为 ``False`` 的对应行进行替换，而 ``mask`` 在传入条件为 ``True`` 的对应行进行替换，当不指定替换值时，替换为缺失值。

.. ipython:: python

    s = pd.Series([-1, 1.2345, 100, -50])
    s.where(s<0)
    s.where(s<0, 100)
    s.mask(s<0)
    s.mask(s<0, -50)

需要注意的是，传入的条件只需是与被调用的 ``Series`` 索引一致的布尔序列即可：

.. ipython:: python

    s_condition= pd.Series([True,False,False,True],index=s.index)
    s.mask(s_condition, -50)

数值替换包含了 ``round, abs, clip`` 方法，它们分别表示按照给定精度四舍五入、取绝对值和截断：

.. ipython:: python

    s = pd.Series([-1, 1.2345, 100, -50])
    s.round(2)
    s.abs()
    s.clip(0, 2) # 前两个数分别表示上下截断边界

.. admonition:: 练一练
   :class: hint

    在 ``clip`` 中，超过边界的只能截断为边界值，如果要把超出边界的替换为自定义的值，应当如何做？

5. 排序函数
----------------

排序共有两种方式，其一为值排序，其二为索引排序，对应的函数是 ``sort_values`` 和 ``sort_index`` 。

为了演示排序函数，下面先利用 ``set_index`` 方法把年级和姓名两列作为索引，多级索引的内容和索引设置的方法将在第三章进行详细讲解。

.. ipython:: python

    df_demo = df[['Grade', 'Name', 'Height',
                  'Weight']].set_index(['Grade','Name'])

对身高进行排序，默认参数 ``ascending=True`` 为升序：

.. ipython:: python

    df_demo.sort_values('Height').head()
    df_demo.sort_values('Height', ascending=False).head()

在排序中，经常遇到多列排序的问题，比如在体重相同的情况下，对身高进行排序，并且保持身高降序排列，体重升序排列：

.. ipython:: python

    df_demo.sort_values(['Weight','Height'],ascending=[True,False]).head()

索引排序的用法和值排序完全一致，只不过元素的值在索引中，此时需要指定索引层的名字或者层号，用参数 ``level`` 表示。另外，需要注意的是字符串的排列顺序由字母顺序决定。

.. ipython:: python

    df_demo.sort_index(level=['Grade','Name'],ascending=[True,False]).head()

6. apply方法
------------------

``apply`` 方法常用于 ``DataFrame`` 的行迭代或者列迭代，它的 ``axis`` 含义与第2小节中的统计聚合函数一致， ``apply`` 的参数往往是一个以序列为输入的函数。例如对于 ``.mean()`` ，使用 ``apply`` 可以如下地写出： 

.. ipython:: python

    df_demo = df[['Height', 'Weight']]
    def my_mean(x):
        res = x.mean()
        return res

    df_demo.apply(my_mean)

同样的，可以利用 ``lambda`` 表达式使得书写简洁，这里的 ``x`` 就指代被调用的 ``df_demo`` 表中逐个输入的序列：

.. ipython:: python

    df_demo.apply(lambda x:x.mean())

若指定 ``axis=1`` ，那么每次传入函数的就是行元素组成的 ``Series`` ，其结果与之前的逐行均值结果一致。

.. ipython:: python

    df_demo.apply(lambda x:x.mean(), axis=1).head()

这里再举一个例子： ``mad`` 函数返回的是一个序列中偏离该序列均值的绝对值大小的均值，例如序列1,3,7,10中，均值为5.25，每一个元素偏离的绝对值为4.25,2.25,1.75,4.75，这个偏离序列的均值为3.25。现在利用 ``apply`` 计算升高和体重的 ``mad`` 指标：

.. ipython:: python

    df_demo.apply(lambda x:(x-x.mean()).abs().mean())

这与使用内置的 ``mad`` 函数计算结果一致：

.. ipython:: python

    df_demo.mad()

.. admonition:: 谨慎使用 ``apply``
   :class: caution

    得益于传入自定义函数的处理， ``apply`` 的自由度很高，但这是以性能为代价的。一般而言，使用 ``pandas`` 的内置函数处理和 ``apply`` 来处理同一个任务，其速度会相差较多，因此只有在确实存在自定义需求的情境下才考虑使用 ``apply`` 。

四、窗口对象
==========================

``pandas`` 中有3类窗口，分别是滑动窗口 ``rolling`` 、扩张窗口 ``expanding`` 以及指数加权窗口 ``ewm`` 。需要说明的是，以日期偏置为窗口大小的滑动窗口将在第十章讨论，指数加权窗口见本章练习。

1. 滑窗对象
--------------

要使用滑窗函数，就必须先要对一个序列使用 ``.rolling`` 得到滑窗对象，其最重要的参数为窗口大小 ``window`` 。

.. ipython:: python
    
    s = pd.Series([1,2,3,4,5])
    roller = s.rolling(window = 3)
    roller

在得到了滑窗对象后，能够使用相应的聚合函数进行计算，需要注意的是窗口包含当前行所在的元素，例如在第四个位置进行均值运算时，应当计算(2+3+4)/3，而不是(1+2+3)/3：

.. ipython:: python

    roller.mean()
    roller.sum()

对于滑动相关系数或滑动协方差的计算，可以如下写出：

.. ipython:: python

    s2 = pd.Series([1,2,6,16,30])
    roller.cov(s2)
    roller.corr(s2)

此外，还支持使用 ``apply`` 传入自定义函数，其传入值是对应窗口的 ``Series`` ，例如上述的均值函数可以等效表示：

.. ipython:: python

    roller.apply(lambda x:x.mean())

``shift, diff, pct_change`` 是一组类滑窗函数，它们的公共参数为 ``periods=n`` ，默认为1，分别表示取向前第 ``n`` 个元素的值、与向前第 ``n`` 个元素做差（与 ``Numpy`` 中不同，后者表示 ``n`` 阶差分）、与向前第 ``n`` 个元素相比计算增长率。这里的 ``n`` 可以为负，表示反方向的类似操作。

.. ipython:: python

    s = pd.Series([1,3,6,10,15])
    s.shift(2)
    s.diff(3)
    s.pct_change()
    s.shift(-1)
    s.diff(-2)

将其视作类滑窗函数的原因是，它们的功能可以用窗口大小为 ``n+1`` 的 ``rolling`` 方法等价代替：

.. ipython:: python

    s.rolling(3).apply(lambda x:list(x)[0]) # s.shift(2)
    s.rolling(4).apply(lambda x:list(x)[-1]-list(x)[0]) # s.diff(3)
    def my_pct(x):
        L = list(x)
        return L[-1]/L[0]-1

    s.rolling(2).apply(my_pct) # s.pct_change()

.. admonition:: 练一练
   :class: hint

    ``rolling`` 对象的默认窗口方向都是向前的，某些情况下用户需要向后的窗口，例如对1,2,3设定向后窗口为2的 ``sum`` 操作，结果为3,5,NaN，此时应该如何实现向后的滑窗操作？

2. 扩张窗口
-------------

扩张窗口又称累计窗口，可以理解为一个动态长度的窗口，其窗口的大小就是从序列开始处到具体操作的对应位置，其使用的聚合函数会作用于这些逐步扩张的窗口上。具体地说，设序列为a1, a2, a3, a4，则其每个位置对应的窗口即[a1]、[a1, a2]、[a1, a2, a3]、[a1, a2, a3, a4]。

.. ipython:: python

    s = pd.Series([1, 3, 6, 10])
    s.expanding().mean()

.. admonition:: 练一练
   :class: hint

    ``cummax, cumsum, cumprod`` 函数是典型的类扩张窗口函数，请使用 ``expanding`` 对象依次实现它们。

五、练习
======================

Ex1：口袋妖怪数据集
--------------------------

现有一份口袋妖怪的数据集，下面进行一些背景说明：

* ``#`` 代表全国图鉴编号，不同行存在相同数字则表示为该妖怪的不同状态
* 妖怪具有单属性和双属性两种，对于单属性的妖怪， ``Type 2`` 为缺失值
* ``Total, HP, Attack, Defense, Sp. Atk, Sp. Def, Speed`` 分别代表种族值、体力、物攻、防御、特攻、特防、速度，其中种族值为后6项之和

.. ipython:: python

    df = pd.read_csv('data/pokemon.csv')
    df.head(3)

1. 对 ``HP, Attack, Defense, Sp. Atk, Sp. Def, Speed`` 进行加总，验证是否为 ``Total`` 值。
2. 对于 ``#`` 重复的妖怪只保留第一条记录，解决以下问题：

(a) 求第一属性的种类数量和前三多数量对应的种类
(b) 求第一属性和第二属性的组合种类
(c) 求尚未出现过的属性组合

3. 按照下述要求，构造 ``Series`` ：

(a) 取出物攻，超过120的替换为 ``high`` ，不足50的替换为 ``low`` ，否则设为 ``mid``
(b) 取出第一属性，分别用 ``replace`` 和 ``apply`` 替换所有字母为大写
(c) 求每个妖怪六项能力的离差，即所有能力中偏离中位数最大的值，添加到 ``df`` 并从大到小排序

Ex2：指数加权窗口
--------------------------

1. 作为扩张窗口的 ``ewm`` 窗口

在扩张窗口中，用户可以使用各类函数进行历史的累计指标统计，但这些内置的统计函数往往把窗口中的所有元素赋予了同样的权重。事实上，可以给出不同的权重来赋给窗口中的元素，指数加权窗口就是这样一种特殊的扩张窗口。

其中，最重要的参数是 ``alpha`` ，它决定了默认情况下的窗口权重为 :math:`w_i = (1 - \alpha)^i, i\in \{0, 1, ..., t\}` ，其中 :math:`i=t` 表示当前元素， :math:`i=0` 表示序列的第一个元素。

从权重公式可以看出，离开当前值越远则权重越小，若记原序列为 ``x`` ，更新后的当前元素为 :math:`y_t` ，此时通过加权公式归一化后可知：

.. math::

    y_t &=\frac{\sum_{i=0}^{t} w_i x_{t-i}}{\sum_{i=0}^{t} w_i} \\
    &=\frac{x_t + (1 - \alpha)x_{t-1} + (1 - \alpha)^2 x_{t-2} + ...
    + (1 - \alpha)^{t} x_{0}}{1 + (1 - \alpha) + (1 - \alpha)^2 + ...
    + (1 - \alpha)^{t}}\\

对于 ``Series`` 而言，可以用 ``ewm`` 对象如下计算指数平滑后的序列：

.. ipython:: python

    np.random.seed(0)
    s = pd.Series(np.random.randint(-1,2,30).cumsum())
    s.head()
    s.ewm(alpha=0.2).mean().head()

请用 ``expanding`` 窗口实现。

2. 作为滑动窗口的 ``ewm`` 窗口

从第1问中可以看到， ``ewm`` 作为一种扩张窗口的特例，只能从序列的第一个元素开始加权。现在希望给定一个限制窗口 ``n`` ，只对包含自身的最近的 ``n`` 个元素作为窗口进行滑动加权平滑。请根据滑窗函数，给出新的 :math:`w_i` 与 :math:`y_t` 的更新公式，并通过 ``rolling`` 窗口实现这一功能。