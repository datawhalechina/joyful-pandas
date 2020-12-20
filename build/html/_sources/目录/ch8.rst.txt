****************************
第八章 文本数据
****************************

.. ipython:: python
    
    import numpy as np
    import pandas as pd

一、str对象
==============

1. str对象的设计意图
---------------------------

``str`` 对象是定义在 ``Index`` 或 ``Series`` 上的属性，专门用于逐元素处理文本内容，其内部定义了大量方法，因此对一个序列进行文本处理，首先需要获取其 ``str`` 对象。在Python标准库中也有 ``str`` 模块，为了使用上的便利，有许多函数的用法 ``pandas`` 照搬了它的设计，例如字母转为大写的操作：

.. ipython:: python
    
    var = 'abcd'
    str.upper(var) # Python内置str模块
    s = pd.Series(['abcd', 'efg', 'hi'])
    s.str
    s.str.upper() # pandas中str对象上的upper方法

根据文档 ``API`` 材料，在 ``pandas`` 的50个 ``str`` 对象方法中，有31个是和标准库中的 ``str`` 模块方法同名且功能一致，这为批量处理序列提供了有力的工具。

2. []索引器
------------------------

对于 ``str`` 对象而言，可理解为其对字符串进行了序列化的操作，例如在一般的字符串中，通过 ``[]`` 可以取出某个位置的元素：

.. ipython:: python
    
    var[0]

同时也能通过切片得到子串：

.. ipython:: python
    
    var[-1: 0: -2]

通过对 ``str`` 对象使用 ``[]`` 索引器，可以完成完全一致的功能，并且如果超出范围则返回缺失值：

.. ipython:: python
    
    s.str[0]
    s.str[-1: 0: -2]
    s.str[2]

3. string类型
-------------------------------

在上一章提到，从 ``pandas`` 的 ``1.0.0`` 版本开始，引入了 ``string`` 类型，其引入的动机在于：原来所有的字符串类型都会以 ``object`` 类型的 ``Series`` 进行存储，但 ``object`` 类型只应当存储混合类型，例如同时存储浮点、字符串、字典、列表、自定义类型等，因此字符串有必要同数值型或 ``category`` 一样，具有自己的数据存放类型，从而引入了 ``string`` 类型。

总体上说，绝大多数对于 ``object`` 和 ``string`` 类型的序列使用 ``str`` 对象方法产生的结果是一致，但是在下面提到的两点上有较大差异：

首先，应当尽量保证每一个序列中的值都是字符串的情况下才使用 ``str`` 属性，但这并不是必须的，其必要条件是序列中至少有一个可迭代（Iterable）对象，包括但不限于字符串、字典、列表。对于一个可迭代对象， ``string`` 类型的 ``str`` 对象和 ``object`` 类型的 ``str`` 对象返回结果可能是不同的。

.. ipython:: python
    
    s = pd.Series([{1: 'temp_1', 2: 'temp_2'}, ['a', 'b'], 0.5, 'my_string'])
    s.str[1]
    s.astype('string').str[1]

除了最后一个字符串元素，前三个元素返回的值都不同，其原因在于当序列类型为 ``object`` 时，是对于每一个元素进行 ``[]`` 索引，因此对于字典而言，返回temp_1字符串，对于列表则返回第二个值，而第三个为不可迭代对象，返回缺失值，第四个是对字符串进行 ``[]`` 索引。而 ``string`` 类型的 ``str`` 对象先把整个元素转为字面意义的字符串，例如对于列表而言，第一个元素即 "{"，而对于最后一个字符串元素而言，恰好转化前后的表示方法一致，因此结果和 ``object`` 类型一致。

除了对于某些对象的 ``str`` 序列化方法不同之外，两者另外的一个差别在于， ``string`` 类型是 ``Nullable`` 类型，但 ``object`` 不是。这意味着 ``string`` 类型的序列，如果调用的 ``str`` 方法返回值为整数 ``Series`` 和布尔 ``Series`` 时，其分别对应的 ``dtype`` 是 ``Int`` 和 ``boolean`` 的 ``Nullable`` 类型，而 ``object`` 类型则会分别返回 ``int/float`` 和 ``bool/object`` ，取决于缺失值的存在与否。同时，字符串的比较操作，也具有相似的特性， ``string`` 返回 ``Nullable`` 类型，但 ``object`` 不会。

.. ipython:: python
    
    s = pd.Series(['a'])
    s.str.len()
    s.astype('string').str.len()
    s == 'a'
    s.astype('string') == 'a'
    s = pd.Series(['a', np.nan]) # 带有缺失值
    s.str.len()
    s.astype('string').str.len()
    s == 'a'
    s.astype('string') == 'a'


最后需要注意的是，对于全体元素为数值类型的序列，即使其类型为 ``object`` 或者 ``category`` 也不允许直接使用 ``str`` 属性。如果需要把数字当成 ``string`` 类型处理，可以使用 ``astype`` 强制转换为 ``string`` 类型的 ``Series`` ：

.. ipython:: python
    
    s = pd.Series([12, 345, 6789])
    s.astype('string').str[1]

二、正则表达式基础
=====================

这一节的两个表格来自于 `learn-regex-zh <https://github.com/cdoco/learn-regex-zh>`__ 这个关于正则表达式项目，其使用 ``MIT`` 开源许可协议。这里只是介绍正则表达式的基本用法，需要系统学习的读者可参考 `正则表达式必知必会 <https://book.douban.com/subject/26285406/>`__ 一书。

1. 一般字符的匹配
---------------------

正则表达式是一种按照某种正则模式，从左到右匹配字符串中内容的一种工具。对于一般的字符而言，它可以找到其所在的位置，这里为了演示便利，使用了 ``python`` 中 ``re`` 模块的 ``findall`` 函数来匹配所有出现过但不重叠的模式，第一个参数是正则表达式，第二个参数是待匹配的字符串。例如，在下面的字符串中找出 ``apple`` ：

.. ipython:: python

    import re
    re.findall('Apple', 'Apple! This Is an Apple!')

2. 元字符基础
----------------

======   =====================================================
元字符      描述
======   =====================================================
.           匹配除换行符以外的任意字符
[ ]           字符类，匹配方括号中包含的任意字符。
[^ ]           否定字符类，匹配方括号中不包含的任意字符
\*           匹配前面的子表达式零次或多次
\+           匹配前面的子表达式一次或多次
?           匹配前面的子表达式零次或一次
{n,m}           花括号，匹配前面字符至少 n 次，但是不超过 m 次
(xyz)           字符组，按照确切的顺序匹配字符xyz。
\|           分支结构，匹配符号之前的字符或后面的字符
\\           转义符，它可以还原元字符原来的含义
^           匹配行的开始
$           匹配行的结束
======   =====================================================

.. ipython:: python

    re.findall('.', 'abc')
    re.findall('[ac]', 'abc')
    re.findall('[^ac]', 'abc')
    re.findall('[ab]{2}', 'aaaabbbb') # {n}指匹配n次
    re.findall('aaa|bbb', 'aaaabbbb')
    re.findall('a\\?|a\*', 'aa?a*a')
    re.findall('a?.', 'abaacadaae')

3. 简写字符集
---------------

此外，正则表达式中还有一类简写字符集，其等价于一组字符的集合：

======   ================================================
简写      描述
======   ================================================
\\w        匹配所有字母、数字、下划线: [a-zA-Z0-9\_]
\\W        匹配非字母和数字的字符: [^\\w]
\\d        匹配数字: [0-9]
\\D        匹配非数字: [^\\d]
\\s        匹配空格符: [\\t\\n\\f\\r\\p{Z}]
\\S        匹配非空格符: [^\\s]
\\B        匹配一组非空字符开头或结尾的位置，不代表具体字符
======   ================================================

.. ipython:: python

    re.findall('.s', 'Apple! This Is an Apple!')
    re.findall('\w{2}', '09 8? 7w c_ 9q p@')
    re.findall('\w\W\B', '09 8? 7w c_ 9q p@')
    re.findall('.\s.', 'Constant dropping wears the stone.')
    re.findall('上海市(.{2,3}区)(.{2,3}路)(\d+号)',
               '上海市黄浦区方浜中路249号 上海市宝山区密山路5号')

三、文本处理的五类操作
=======================

1. 拆分
-----------

``str.split`` 能够把字符串的列进行拆分，其中第一个参数为正则表达式，可选参数包括从左到右的最大拆分次数 ``n`` ，是否展开为多个列 ``expand`` 。

.. ipython:: python

    s = pd.Series(['上海市黄浦区方浜中路249号',
                '上海市宝山区密山路5号'])
    s.str.split('[市区路]')
    s.str.split('[市区路]', n=2, expand=True)

与其类似的函数是 ``str.rsplit`` ，其区别在于使用 ``n`` 参数的时候是从右到左限制最大拆分次数。但是当前版本下 ``rsplit`` 因为 ``bug`` 而无法使用正则表达式进行分割：

.. ipython:: python

    s.str.rsplit('[市区路]', n=2, expand=True)

2. 合并
-----------

关于合并一共有两个函数，分别是 ``str.join`` 和 ``str.cat`` 。 ``str.join`` 表示用某个连接符把 ``Series`` 中的字符串列表连接起来，如果列表中出现了字符串元素则返回缺失值：

.. ipython:: python

    s = pd.Series([['a','b'], [1, 'a'], [['a', 'b'], 'c']])
    s.str.join('-')

``str.cat`` 用于合并两个序列，主要参数为连接符 ``sep`` 、连接形式 ``join`` 以及缺失值替代符号 ``na_rep`` ，其中连接形式默认为以索引为键的左连接。

.. ipython:: python

    s1 = pd.Series(['a','b'])
    s2 = pd.Series(['cat','dog'])
    s1.str.cat(s2,sep='-')
    s2.index = [1, 2]
    s1.str.cat(s2, sep='-', na_rep='?', join='outer')

3. 匹配
-----------

``str.contains`` 返回了每个字符串是否包含正则模式的布尔序列：

.. ipython:: python

    s = pd.Series(['my cat', 'he is fat', 'railway station'])
    s.str.contains('\s\wat')

``str.startswith`` 和 ``str.endswith`` 返回了每个字符串以给定模式为开始和结束的布尔序列，它们都不支持正则表达式：

.. ipython:: python

    s.str.startswith('my')
    s.str.endswith('t')

如果需要用正则表达式来检测开始或结束字符串的模式，可以使用 ``str.match`` ，其返回了每个字符串起始处是否符合给定正则模式的布尔序列：

.. ipython:: python

    s.str.match('m|h')
    s.str[::-1].str.match('ta[f|g]|n') # 反转后匹配

当然，这些也能通过在 ``str.contains`` 的正则中使用 ``^`` 和 ``$`` 来实现：

.. ipython:: python

    s.str.contains('^[m|h]')
    s.str.contains('[f|g]at|n$')

除了上述返回值为布尔的匹配之外，还有一种返回索引的匹配函数，即 ``str.find`` 与 ``str.rfind`` ，其分别返回从左到右和从右到左第一次匹配的位置的索引，未找到则返回-1。需要注意的是这两个函数不支持正则匹配，只能用于字符子串的匹配：

.. ipython:: python

    s = pd.Series(['This is an apple. That is not an apple.'])
    s.str.find('apple')
    s.str.rfind('apple')

4. 替换
-----------

``str.replace`` 和 ``replace`` 并不是一个函数，在使用字符串替换时应当使用前者。

.. ipython:: python

    s = pd.Series(['a_1_b','c_?'])
    s.str.replace('\d|\?', 'new')

当需要对不同部分进行有差别的替换时，可以利用 ``子组`` 的方法，并且此时可以通过传入自定义的替换函数来分别进行处理，注意 ``group(k)`` 代表匹配到的第 ``k`` 个子组（圆括号之间的内容）：

.. ipython:: python

    s = pd.Series(['上海市黄浦区方浜中路249号',
                   '上海市宝山区密山路5号',
                   '北京市昌平区北农路2号'])
    pat = '(\w+市)(\w+区)(\w+路)(\d+号)'
    city = {'上海市': 'Shanghai', '北京市': 'Beijing'}
    district = {'昌平区': 'CP District',
                '黄浦区': 'HP District',
                '宝山区': 'BS District'}
    road = {'方浜中路': 'Mid Fangbin Road',
            '密山路': 'Mishan Road',
            '北农路': 'Beinong Road'}
    def my_func(m):
        str_city = city[m.group(1)]
        str_district = district[m.group(2)]
        str_road = road[m.group(3)]
        str_no = 'No. ' + m.group(4)[:-1]
        return ' '.join([str_city,
                        str_district,
                        str_road,
                        str_no])

    s.str.replace(pat, my_func)

这里的数字标识并不直观，可以使用 ``命名子组`` 更加清晰地写出子组代表的含义：

.. ipython:: python

    pat = '(?P<市名>\w+市)(?P<区名>\w+区)(?P<路名>\w+路)(?P<编号>\d+号)'
    def my_func(m):
        str_city = city[m.group('市名')]
        str_district = district[m.group('区名')]
        str_road = road[m.group('路名')]
        str_no = 'No. ' + m.group('编号')[:-1]
        return ' '.join([str_city,
                        str_district,
                        str_road,
                        str_no])

    s.str.replace(pat, my_func)

这里虽然看起来有些繁杂，但是实际数据处理中对应的替换，一般都会通过代码来获取数据从而构造字典映射，在具体写法上会简洁的多。

5. 提取
-----------

提取既可以认为是一种返回具体元素（而不是布尔值或元素对应的索引位置）的匹配操作，也可以认为是一种特殊的拆分操作。前面提到的 ``str.split`` 例子中会把分隔符去除，这并不是用户想要的效果，这时候就可以用 ``str.extract`` 进行提取：

.. ipython:: python

    pat = '(\w+市)(\w+区)(\w+路)(\d+号)'
    s.str.extract(pat)

通过子组的命名，可以直接对新生成 ``DataFrame`` 的列命名：

.. ipython:: python

    pat = '(?P<市名>\w+市)(?P<区名>\w+区)(?P<路名>\w+路)(?P<编号>\d+号)'
    s.str.extract(pat)

``str.extractall`` 不同于 ``str.extract`` 只匹配一次，它会把所有符合条件的模式全部匹配出来，如果存在多个结果，则以多级索引的方式存储：

.. ipython:: python

    s = pd.Series(['A135T15,A26S5','B674S2,B25T6'], index = ['my_A','my_B'])
    pat = '[A|B](\d+)[T|S](\d+)'
    s.str.extractall(pat)
    pat_with_name = '[A|B](?P<name1>\d+)[T|S](?P<name2>\d+)'
    s.str.extractall(pat_with_name)

``str.findall`` 的功能类似于 ``str.extractall`` ，区别在于前者把结果存入列表中，而后者处理为多级索引，每个行只对应一组匹配，而不是把所有匹配组合构成列表。

.. ipython:: python

    s.str.findall(pat)

四、常用字符串函数
=======================

除了上述介绍的五类字符串操作有关的函数之外， ``str`` 对象上还定义了一些实用的其他方法，在此进行介绍：

1. 字母型函数
-----------------

``upper, lower, title, capitalize, swapcase`` 这五个函数主要用于字母的大小写转化，从下面的例子中就容易领会其功能：

.. ipython:: python

    s = pd.Series(['lower', 'CAPITALS', 'this is a sentence', 'SwApCaSe'])
    s.str.upper()
    s.str.lower()
    s.str.title()
    s.str.capitalize()
    s.str.swapcase()

2. 数值型函数
----------------

这里着重需要介绍的是 ``pd.to_numeric`` 方法，它虽然不是 ``str`` 对象上的方法，但是能够对字符格式的数值进行快速转换和筛选。其主要参数包括 ``errors`` 和 ``downcast`` 分别代表了非数值的处理模式和转换类型。其中，对于不能转换为数值的有三种 ``errors`` 选项， ``raise, coerce, ignore`` 分别表示直接报错、设为缺失以及保持原来的字符串。

.. ipython:: python

    s = pd.Series(['1', '2.2', '2e', '??', '-2.1', '0'])
    pd.to_numeric(s, errors='ignore')
    pd.to_numeric(s, errors='coerce')

在数据清洗时，可以利用 ``coerce`` 的设定，快速查看非数值型的行：

.. ipython:: python

    s[pd.to_numeric(s, errors='coerce').isna()]

3. 统计型函数
----------------

``count`` 和 ``len`` 的作用分别是返回出现正则模式的次数和字符串的长度：

.. ipython:: python

    s = pd.Series(['cat rat fat at', 'get feed sheet heat'])
    s.str.count('[r|f]at|ee')
    s.str.len()

4. 格式型函数
----------------

格式型函数主要分为两类，第一种是除空型，第二种时填充型。其中，第一类函数一共有三种，它们分别是 ``strip, rstrip, lstrip`` ，分别代表去除两侧空格、右侧空格和左侧空格。这些函数在数据清洗时是有用的，特别是列名含有非法空格的时候。

.. ipython:: python

    my_index = pd.Index([' col1', 'col2 ', ' col3 '])
    my_index.str.strip().str.len()
    my_index.str.rstrip().str.len()
    my_index.str.lstrip().str.len()

对于填充型函数而言， ``pad`` 是最灵活的，它可以选定字符串长度、填充的方向和填充内容：

.. ipython:: python

    s = pd.Series(['a','b','c'])
    s.str.pad(5,'left','*')
    s.str.pad(5,'right','*')
    s.str.pad(5,'both','*')

上述的三种情况可以分别用 ``rjust, ljust, center`` 来等效完成，需要注意 ``ljust`` 是指右侧填充而不是左侧填充：

.. ipython:: python

    s.str.rjust(5, '*')
    s.str.ljust(5, '*')
    s.str.center(5, '*')

在读取 ``excel`` 文件时，经常会出现数字前补0的需求，例如证券代码读入的时候会把"000007"作为数值7来处理， ``pandas`` 中除了可以使用上面的左侧填充函数进行操作之外，还可用 ``zfill`` 来实现。

.. ipython:: python

    s = pd.Series([7, 155, 303000]).astype('string')
    s.str.pad(6,'left','0')
    s.str.rjust(6,'0')
    s.str.zfill(6)

五、练习
===================

Ex1：房屋信息数据集
---------------------------

现有一份房屋信息数据集如下：

.. ipython:: python

    df = pd.read_excel('data/house_info.xls', usecols=[
                    'floor','year','area','price'])
    df.head(3)

1. 将 ``year`` 列改为整数年份存储。
2. 将 ``floor`` 列替换为 ``Level, Highest`` 两列，其中的元素分别为 ``string`` 类型的层类别（高层、中层、低层）与整数类型的最高层数。
3. 计算房屋每平米的均价 ``avg_price`` ，以 ``***元/平米`` 的格式存储到表中，其中 ``***`` 为整数。

Ex2：《权力的游戏》剧本数据集
-------------------------------------

现有一份权力的游戏剧本数据集如下：

.. ipython:: python

    df = pd.read_csv('data/script.csv')
    df.head(3)

1. 计算每一个 ``Episode`` 的台词条数。
2. 以空格为单词的分割符号，请求出单句台词平均单词量最多的前五个人。
3. 若某人的台词中含有问号，那么下一个说台词的人即为回答者。若上一人台词中含有 :math:`n` 个问号，则认为回答者回答了 :math:`n` 个问题，请求出回答最多问题的前五个人。