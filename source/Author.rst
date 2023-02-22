*********
Author
*********

耿远昊，华东师范大学统计学本科，威斯康星大学麦迪逊分校统计学硕士，Datawhale成员，《pandas数据处理与分析》作者。pandas contributor，积极参与pandas开源社区生态建设，包括漏洞修复、功能实现与性能优化等，对pandas在数据处理与分析中的应用有丰富经验。

Contributions to pandas project
======================================

Merged
-------------

* `#33783 <https://github.com/pandas-dev/pandas/pull/33783>`__ DOC: fix doc for ``crosstab`` with Categorical data input
* `#36516 <https://github.com/pandas-dev/pandas/pull/36516>`__ DOC: Correct inconsistent description on default ``DateOffset`` setting
* `#37607 <https://github.com/pandas-dev/pandas/pull/37607>`__ BUG: ``nunique`` not ignoring both ``None`` and ``np.nan``
* `#37830 <https://github.com/pandas-dev/pandas/pull/37830>`__ BUG: ``MultiIndex.drop`` does not raise if labels are partially found
* `#38029 <https://github.com/pandas-dev/pandas/pull/38029>`__ BUG: ``unstack`` with missing levels results in incorrect ``index`` names
* `#38089 <https://github.com/pandas-dev/pandas/pull/38089>`__ BUG: ``merge_ordered`` fails with list-like ``left_by`` or ``right_by``
* `#38170  <https://github.com/pandas-dev/pandas/pull/38170>`__ BUG: unexpected ``merge_ordered`` results caused by wrongly ``groupby``
* `#38173  <https://github.com/pandas-dev/pandas/pull/38173>`__ BUG: array-like ``quantile`` fails on column ``groupby``
* `#38257 <https://github.com/pandas-dev/pandas/pull/38257>`__ BUG: ``groupby.apply`` on the ``NaN`` group drops values with original ``axes`` return
* `#38408 <https://github.com/pandas-dev/pandas/pull/38408>`__ ENH: add end and end_day ``origin`` for ``resample``
* `#38492 <https://github.com/pandas-dev/pandas/pull/38492>`__ BUG: ``CategoricalIndex.reindex`` fails when ``Index`` passed with labels all in category
* `#44827 <https://github.com/pandas-dev/pandas/pull/44827>`__ PERF: faster ``Dataframe`` construction from ``recarray``
* `#46546 <https://github.com/pandas-dev/pandas/pull/46546>`__ BUG: ``pd.concat`` with identical key leads to multi-indexing error
* `#46654 <https://github.com/pandas-dev/pandas/pull/46654>`__ TST: add validation checks on levels keyword from ``pd.concat``
* `#46656 <https://github.com/pandas-dev/pandas/pull/46656>`__ BUG: ``df.nsmallest`` get wrong results when ``NaN`` in the sorting column
* `#47605 <https://github.com/pandas-dev/pandas/pull/47605>`__ BUG: ``df.groupby().resample()[[cols]]`` without key columns raise ``KeyError``
* `#47685 <https://github.com/pandas-dev/pandas/pull/47685>`__ TST: avoid sort when concat int-index ``Dataframes`` with ``sort=False``
* `#47708 <https://github.com/pandas-dev/pandas/pull/47708>`__ BUG: ``json_normalize`` raises boardcasting error with list-like ``metadata``
* `#47714 <https://github.com/pandas-dev/pandas/pull/47714>`__ BUG: ``df.fillna`` ignores axis when ``DataFrame`` is single block
* `#47717 <https://github.com/pandas-dev/pandas/pull/47717>`__ TST: add test for ``groupby`` with ``dropna=False`` on multi-index
* `#47731 <https://github.com/pandas-dev/pandas/pull/47731>`__ BUG: ``groupby.corrwith`` fails with ``axis=1`` and ``other=df``
* `#47757 <https://github.com/pandas-dev/pandas/pull/47757>`__ BUG: ``wide_to_long`` fails when ``stubnames`` miss and ``i`` contains ``string`` column
* `#47779 <https://github.com/pandas-dev/pandas/pull/47779>`__ PERF: efficient ``argmax/argmin`` for ``SparseArray``
* `#47810 <https://github.com/pandas-dev/pandas/pull/47810>`__ BUG: fix ``SparseArray.unique`` IndexError and ``_first_fill_value_loc`` algo

Mail
=================

1801214626@qq.com 

Github
================

https://github.com/GYHHAHA

WeChat
===============

.. image:: _static/wx.png
   :height: 200px
   :width: 200 px
   :scale: 100 %
   :align: left