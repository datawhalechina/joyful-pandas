****************************
第一章 预备知识
****************************

一、Python基础
===================

1. 列表推导式与条件赋值
--------------------------

在生成一个数字序列的时候，在 ``Python`` 中可以如下写出：

.. ipython:: python

    L = []
    def my_func(x):
        return 2*x

    for i in range(5):
        L.append(my_func(i))
    L

事实上可以利用列表推导式进行写法上的简化： ``[* for i in *]`` 。其中，第一个 ``*`` 为映射函数，其输入为后面 ``i`` 指代的内容，第二个 ``*`` 表示迭代的对象。

.. ipython:: python

    [my_func(i) for i in range(5)]

列表表达式还支持多层嵌套，如下面的例子中第一个 ``for`` 为外层循环，第二个为内层循环：

.. ipython:: python

    [m+'_'+n for m in ['a', 'b'] for n in ['c', 'd']]

除了列表推导式，另一个实用的语法糖是带有 ``if`` 选择的条件赋值，其形式为 ``value = a if condition else b`` ：

.. ipython:: python

    value = 'cat' if 2>1 else 'dog'
    value

等价于如下的写法：

.. code-block:: python

    a, b = 'cat', 'dog'
    condition = 2 > 1 # 此时为True
    if condition:
        value = a
    else:
        value = b

下面举一个例子，截断列表中超过5的元素，即超过5的用5代替，小于5的保留原来的值：

.. ipython:: python

    L = [1, 2, 3, 4, 5, 6, 7]
    [i if i <= 5 else 5 for i in L]

2. 匿名函数与map方法
------------------------

有一些函数的定义具有清晰简单的映射关系，例如上面的 ``my_func`` 函数，这时候可以用匿名函数的方法简洁地表示：

.. ipython:: python

    my_func = lambda x: 2*x
    my_func(3)
    multi_para_func = lambda a, b: a + b
    multi_para_func(1, 2) 

但上面的用法其实违背了“匿名”的含义，事实上它往往在无需多处调用的场合进行使用，例如上面列表推导式中的例子，用户不关心函数的名字，只关心这种映射的关系：

.. ipython:: python

    [(lambda x: 2*x)(i) for i in range(5)]

对于上述的这种列表推导式的匿名函数映射， ``Python`` 中提供了 ``map`` 函数来完成，它返回的是一个 ``map`` 对象，需要通过 ``list`` 转为列表：

.. ipython:: python

    list(map(lambda x: 2*x, range(5)))

对于多个输入值的函数映射，可以通过追加迭代对象实现：

.. ipython:: python

    list(map(lambda x, y: str(x)+'_'+y, range(5), list('abcde')))

3. zip对象与enumerate方法
-----------------------------------

zip函数能够把多个可迭代对象打包成一个元组构成的可迭代对象，它返回了一个 ``zip`` 对象，通过 ``tuple, list`` 可以得到相应的打包结果：

.. ipython:: python

    L1, L2, L3 = list('abc'), list('def'), list('hij')
    list(zip(L1, L2, L3))
    tuple(zip(L1, L2, L3))

往往会在循环迭代的时候使用到 ``zip`` 函数：

.. ipython:: python

    for i, j, k in zip(L1, L2, L3):
        print(i, j, k)

``enumerate`` 是一种特殊的打包，它可以在迭代时绑定迭代元素的遍历序号：

.. ipython:: python

    L = list('abcd')
    for index, value in enumerate(L):
        print(index, value)

用 ``zip`` 对象也能够简单地实现这个功能：

.. ipython:: python

    for index, value in zip(range(len(L)), L):
        print(index, value)

当需要对两个列表建立字典映射时，可以利用 ``zip`` 对象：

.. ipython:: python

    dict(zip(L1, L2))

既然有了压缩函数，那么 ``Python`` 也提供了 ``*`` 操作符和 ``zip`` 联合使用来进行解压操作：

.. ipython:: python

    zipped = list(zip(L1, L2, L3))
    zipped
    list(zip(*zipped)) # 三个元组分别对应原来的列表

二、Numpy基础
===================

1. np数组的构造
----------------------

最一般的方法是通过 ``array`` 来构造：

.. ipython:: python

    import numpy as np
    np.array([1,2,3])

下面讨论一些特殊数组的生成方式：

【a】等差序列： ``np.linspace, np.arange``

.. ipython:: python

    np.linspace(1,5,11) # 起始、终止（包含）、样本个数
    np.arange(1,5,2) # 起始、终止（不包含）、步长

【b】特殊矩阵： ``zeros, eye, full``

.. ipython:: python

    np.zeros((2,3)) # 传入元组表示各维度大小
    np.eye(3) # 3*3的单位矩阵
    np.eye(3, k=1) # 偏移主对角线1个单位的伪单位矩阵
    np.full((2,3), 10) # 元组传入大小，10表示填充数值
    np.full((2,3), [1,2,3]) # 每行填入相同的列表

【c】随机矩阵： ``np.random``

最常用的随机生成函数为 ``rand, randn, randint, choice`` ，它们分别表示0-1均匀分布的随机数组、标准正态的随机数组、随机整数组和随机列表抽样：

.. ipython:: python

    np.random.rand(3) # 生成服从0-1均匀分布的三个随机数
    np.random.rand(3, 3) # 注意这里传入的不是元组，每个维度大小分开输入

对于服从区间 :math:`a` 到 :math:`b` 上的均匀分布可以如下生成：

.. ipython:: python

    a, b = 5, 15
    (b - a) * np.random.rand(3) + a

一般的，可以选择已有的库函数：

.. ipython:: python

    np.random.uniform(5, 15, 3)

``randn`` 生成了 :math:`N\rm{(\mathbf{0}, \mathbf{I})}` 的标准正态分布：

.. ipython:: python

    np.random.randn(3)
    np.random.randn(2, 2)

对于服从方差为 :math:`\sigma^2` 均值为 :math:`\mu` 的一元正态分布可以如下生成：

.. ipython:: python

    sigma, mu = 2.5, 3
    mu + np.random.randn(3) * sigma

同样的，也可选择从已有函数生成：

.. ipython:: python

    np.random.normal(3, 2.5, 3)

``randint`` 可以指定生成随机整数的最小值最大值（不包含）和维度大小：

.. ipython:: python

    low, high, size = 5, 15, (2,2) # 生成5到14的随机整数
    np.random.randint(low, high, size)

``choice`` 可以从给定的列表中，以一定概率和方式抽取结果，当不指定概率时为均匀采样，默认抽取方式为有放回抽样：

.. ipython:: python

    my_list = ['a', 'b', 'c', 'd']
    np.random.choice(my_list, 2, replace=False, p=[0.1, 0.7, 0.1 ,0.1])
    np.random.choice(my_list, (3,3))

当返回的元素个数与原列表相同时，不放回抽样等价于使用 ``permutation`` 函数，即打散原列表：

.. ipython:: python

    np.random.permutation(my_list)

最后，需要提到的是随机种子，它能够固定随机数的输出结果：

.. ipython:: python

    np.random.seed(0)
    np.random.rand()
    np.random.seed(0)
    np.random.rand()

2. np数组的变形与合并
-------------------------

【a】转置： ``T``

.. ipython:: python

    np.zeros((2,3)).T

【b】合并操作： ``r_, c_``

对于二维数组而言， ``r_`` 和 ``c_`` 分别表示上下合并和左右合并：

.. ipython:: python

    np.r_[np.zeros((2,3)),np.zeros((2,3))]
    np.c_[np.zeros((2,3)),np.zeros((2,3))]

一维数组和二维数组进行合并时，应当把其视作列向量，在长度匹配的情况下只能够使用左右合并的 ``c_`` 操作：

.. ipython:: python

    try:
        np.r_[np.array([0,0]),np.zeros((2,1))]
    except Exception as e:
        Err_Msg = e
    Err_Msg
    np.r_[np.array([0,0]),np.zeros(2)]
    np.c_[np.array([0,0]),np.zeros((2,3))]

【c】维度变换： ``reshape``

``reshape`` 能够帮助用户把原数组按照新的维度重新排列。在使用时有两种模式，分别为 ``C`` 模式和 ``F`` 模式，分别以逐行和逐列的顺序进行填充读取。

.. ipython:: python

    target = np.arange(8).reshape(2,4)
    target
    target.reshape((4,2), order='C') # 按照行读取和填充
    target.reshape((4,2), order='F') # 按照列读取和填充

特别地，由于被调用数组的大小是确定的， `reshape` 允许有一个维度存在空缺，此时只需填充-1即可：

.. ipython:: python

    target.reshape((4,-1))

下面将 ``n*1`` 大小的数组转为1维数组的操作是经常使用的：

.. ipython:: python

    target = np.ones((3,1))
    target
    target.reshape(-1)

3. np数组的切片与索引
---------------------------

数组的切片模式支持使用 ``slice`` 类型的 ``start:end:step`` 切片，还可以直接传入列表指定某个维度的索引进行切片：

.. ipython:: python

    target = np.arange(9).reshape(3,3)
    target
    target[:-1, [0,2]]

此外，还可以利用 ``np.ix_`` 在对应的维度上使用布尔索引，但此时不能使用 ``slice`` 切片：

.. ipython:: python
    
    target[np.ix_([True, False, True], [True, False, True])]
    target[np.ix_([1,2], [True, False, True])]

当数组维度为1维时，可以直接进行布尔索引，而无需 ``np.ix_`` ：

.. ipython:: python
    
    new = target.reshape(-1)
    new[new%2==0]

4. 常用函数
---------------

为了简单起见，这里假设下述函数输入的数组都是一维的。

【a】 ``where``

``where`` 是一种条件函数，可以指定满足条件与不满足条件位置对应的填充值：

.. ipython:: python

    a = np.array([-1,1,-1,0])
    np.where(a>0, a, 5) # 对应位置为True时填充a对应元素，否则填充5

【b】 ``nonzero, argmax, argmin``

这三个函数返回的都是索引， ``nonzero`` 返回非零数的索引， ``argmax, argmin`` 分别返回最大和最小数的索引：

.. ipython:: python

    a = np.array([-2,-5,0,1,3,-1])
    np.nonzero(a)
    a.argmax()
    a.argmin()

【c】 ``any, all``

``any`` 指当序列至少 :red:`存在一个`  ``True`` 或非零元素时返回 ``True`` ，否则返回 ``False``

``all`` 指当序列元素 :red:`全为`  ``True`` 或非零元素时返回 ``True`` ，否则返回 ``False``

.. ipython:: python

    a = np.array([0,1])
    a.any()
    a.all()

【d】 ``cumprod, cumsum, diff``

``cumprod, cumsum`` 分别表示累乘和累加函数，返回同长度的数组， ``diff`` 表示和前一个元素做差，由于第一个元素为缺失值，因此在默认参数情况下，返回长度是原数组减1

.. ipython:: python

    a = np.array([1,2,3])
    a.cumprod()
    a.cumsum()
    np.diff(a)

【e】 统计函数

常用的统计函数包括 ``max, min, mean, median, std, var, sum, quantile`` ，其中分位数计算是全局方法，因此不能通过 ``array.quantile`` 的方法调用：

.. ipython:: python

    target = np.arange(5)
    target
    target.max()
    np.quantile(target, 0.5) # 0.5分位数

但是对于含有缺失值的数组，它们返回的结果也是缺失值，如果需要略过缺失值，必须使用 ``nan*`` 类型的函数，上述的几个统计函数都有对应的 ``nan*`` 函数。

.. ipython:: python

    target = np.array([1, 2, np.nan])
    target
    target.max()
    np.nanmax(target)
    np.nanquantile(target, 0.5)

对于协方差和相关系数分别可以利用 ``cov, corrcoef`` 如下计算：

.. ipython:: python

    target1 = np.array([1,3,5,9])
    target2 = np.array([1,5,3,-9])
    np.cov(target1, target2)
    np.corrcoef(target1, target2)

最后，需要说明二维 ``Numpy`` 数组中统计函数的 ``axis`` 参数，它能够进行某一个维度下的统计特征计算，当 ``axis=0`` 时结果为列的统计指标，当 ``axis=1`` 时结果为行的统计指标：

.. ipython:: python

    target = np.arange(1,10).reshape(3,-1)
    target
    target.sum(0)
    target.sum(1)

5. 广播机制
---------------------

广播机制用于处理两个不同维度数组之间的操作，这里只讨论不超过两维的数组广播机制。

【a】标量和数组的操作

当一个标量和数组进行运算时，标量会自动把大小扩充为数组大小，之后进行逐元素操作：

.. ipython:: python

    res = 3 * np.ones((2,2)) + 1
    res
    res = 1 / res
    res

【b】二维数组之间的操作

当两个数组维度完全一致时，使用对应元素的操作，否则会报错，除非其中的某个数组的维度是 :math:`m\times 1` 或者 :math:`1\times n` ，那么会扩充其具有 :math:`1` 的维度为另一个数组对应维度的大小。例如， :math:`1\times 2` 数组和 :math:`3\times 2` 数组做逐元素运算时会把第一个数组扩充为 :math:`3\times 2` ，扩充时的对应数值进行赋值。但是，需要注意的是，如果第一个数组的维度是 :math:`1\times 3` ，那么由于在第二维上的大小不匹配且不为 :math:`1` ，此时报错。

.. ipython:: python

    res = np.ones((3,2))
    res
    res * np.array([[2,3]]) # 第二个数组扩充第一维度为3
    res * np.array([[2],[3],[4]]) # 第二个数组扩充第二维度为2
    res * np.array([[2]]) # 等价于两次扩充，第二个数组两个维度分别扩充为3和2

【c】一维数组与二维数组的操作

当一维数组 :math:`A_k` 与二维数组 :math:`B_{m,n}` 操作时，等价于把一维数组视作 :math:`A_{1,k}` 的二维数组，使用的广播法则与【b】中一致，当 :math:`k!=n` 且 :math:`k, n` 都不是 :math:`1` 时报错。

.. ipython:: python

    np.ones(3) + np.ones((2,3))
    np.ones(3) + np.ones((2,1))
    np.ones(1) + np.ones((2,3))

6. 向量与矩阵的计算
--------------------------

【a】向量内积： ``dot``

.. math::

    \rm \mathbf{a}\cdot\mathbf{b} = \sum_ia_ib_i

.. ipython:: python

    a = np.array([1,2,3])
    b = np.array([1,3,5])
    a.dot(b)

【b】向量范数和矩阵范数： ``np.linalg.norm``

在矩阵范数的计算中，最重要的是 ``ord`` 参数，可选值如下：

=====  ============================  ==========================
ord    norm for matrices             norm for vectors
=====  ============================  ==========================
None   Frobenius norm                2-norm
'fro'  Frobenius norm                --
'nuc'  nuclear norm                  --
inf    max(sum(abs(x), axis=1))      max(abs(x))
-inf   min(sum(abs(x), axis=1))      min(abs(x))
0      --                            sum(x != 0)
1      max(sum(abs(x), axis=0))      as below
-1     min(sum(abs(x), axis=0))      as below
2      2-norm (largest sing. value)  as below
-2     smallest singular value       as below
other  --                            sum(abs(x)**ord)**(1./ord)
=====  ============================  ==========================

.. ipython:: python

    matrix_target =  np.arange(4).reshape(-1,2)
    matrix_target 
    np.linalg.norm(matrix_target, 'fro')
    np.linalg.norm(matrix_target, np.inf)
    np.linalg.norm(matrix_target, 2)

.. ipython:: python

    vector_target =  np.arange(4)
    vector_target
    np.linalg.norm(vector_target, np.inf)
    np.linalg.norm(vector_target, 2)
    np.linalg.norm(vector_target, 3)

【c】矩阵乘法： ``@``

.. math::

    \rm [\mathbf{A}_{m\times p}\mathbf{B}_{p\times n}]_{ij} = \sum_{k=1}^p\mathbf{A}_{ik}\mathbf{B}_{kj}

.. ipython:: python

    a = np.arange(4).reshape(-1,2)
    a
    b = np.arange(-4,0).reshape(-1,2)
    b
    a@b

三、练习
===================

Ex1：利用列表推导式写矩阵乘法
------------------------------------

一般的矩阵乘法根据公式，可以由三重循环写出：

.. ipython:: python

    M1 = np.random.rand(2,3)
    M2 = np.random.rand(3,4)
    res = np.empty((M1.shape[0],M2.shape[1]))
    for i in range(M1.shape[0]):
        for j in range(M2.shape[1]):
            item = 0
            for k in range(M1.shape[1]):
                item += M1[i][k] * M2[k][j]
            res[i][j] = item
    (np.abs((M1@M2 - res) < 1e-15)).all() # 排除数值误差

请将其改写为列表推导式的形式。

Ex2：更新矩阵
------------------

设矩阵 :math:`A_{m\times n}` ，现在对 :math:`A` 中的每一个元素进行更新生成矩阵 :math:`B` ，更新方法是 :math:`\displaystyle B_{ij}=A_{ij}\sum_{k=1}^n\frac{1}{A_{ik}}` ，例如下面的矩阵为 :math:`A` ，则 :math:`B_{2,2}=5\times(\frac{1}{4}+\frac{1}{5}+\frac{1}{6})=\frac{37}{12}` ，请利用 ``Numpy`` 高效实现。 

.. math::

    A=\left[ \begin{matrix} 1 & 2 &3\\4&5&6\\7&8&9 \end{matrix} \right]

Ex3：卡方统计量
--------------------------

设矩阵 :math:`A_{m\times n}` ，记 :math:`B_{ij} = \frac{(\sum_{i=1}^mA_{ij})\times (\sum_{j=1}^nA_{ij})}{\sum_{i=1}^m\sum_{j=1}^nA_{ij}}` ，定义卡方值如下：

.. math::

    \chi^2 = \sum_{i=1}^m\sum_{j=1}^n\frac{(A_{ij}-B_{ij})^2}{B_{ij}}

请利用 ``Numpy`` 对给定的矩阵 :math:`A` 计算 :math:`\chi^2` 。

.. ipython:: python

    np.random.seed(0)
    A = np.random.randint(10, 20, (8, 5))

Ex4：改进矩阵计算的性能
------------------------------

设 :math:`Z` 为 :math:`m\times n` 的矩阵， :math:`B` 和 :math:`U` 分别是 :math:`m\times p` 和 :math:`p\times n` 的矩阵， :math:`B_i` 为 :math:`B` 的第 :math:`i` 行， :math:`U_j` 为 :math:`U` 的第 :math:`j` 列，下面定义 :math:`\displaystyle R=\sum_{i=1}^m\sum_{j=1}^n\|B_i-U_j\|_2^2Z_{ij}` ，其中 :math:`\|\mathbf{a}\|_2^2` 表示向量 :math:`\mathbf{a}` 的分量平方和 :math:`\sum_i a_i^2` 。

现有某人根据如下给定的样例数据计算 :math:`R` 的值，请充分利用 ``Numpy`` 中的函数，基于此问题改进这段代码的性能。

.. ipython:: python
    
    np.random.seed(0)
    m, n, p = 100, 80, 50
    B = np.random.randint(0, 2, (m, p))
    U = np.random.randint(0, 2, (p, n))
    Z = np.random.randint(0, 2, (m, n))

.. ipython:: python

    def solution(B=B, U=U, Z=Z):
        L_res = []
        for i in range(m):
            for j in range(n):
                norm_value = ((B[i]-U[:,j])**2).sum()
                L_res.append(norm_value*Z[i][j])
        return sum(L_res)

    solution(B, U, Z)

Ex5：连续整数的最大长度
------------------------------

输入一个整数的 ``Numpy`` 数组，返回其中严格递增连续整数子数组的最大长度。例如，输入 [1,2,5,6,7]，[5,6,7]为具有最大长度的递增连续整数子数组，因此输出3；输入[3,2,1,2,3,4,6]，[1,2,3,4]为具有最大长度的递增连续整数子数组，因此输出4。请充分利用 ``Numpy`` 的内置函数完成。（提示：考虑使用 ``nonzero, diff`` 函数）