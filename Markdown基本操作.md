# Markdown 基本操作

---

- **优雅地沉浸式记录，专注内容而不是纠结排版**
- **「心中无尘，码字入神」**
- 中文教程：[Markdown 语法教程](https://markdown.com.cn/)
- 在线体验：[Markdown在线编辑器](https://markdown.com.cn/editor/)

---

## 1. 标题语法

# 标题1
## 标题2
### 标题3
#### 标题4
##### 标题5

标题1
===

标题2
---

## 2. 段落语法

- 使用 **空白行** 区分段落：

I really like using Markdown.

I think I'll use it to format all of my documents from now on.

## 3. 换行语法

- **末尾加两个以上空格**  
First line with two spaces after.  
And the next line.

- **末尾加 HTML 换行标签** <br>
First line with the HTML tag after.<br>
And the next line.

- **首句末尾加反斜杠** \
First line with a backslash after.\
And the next line.

- **首句末尾不加内容**  
First line with nothing after.
And the next line.

## 4. 强调语法
- 粗体  
前后各 2 个`*`符号---
I just love **bold text**.
- 斜体  
前后各 1 个`*`符号---
Italicized text is the *cat's meow*.
- 粗体+斜体  
前后各 3 个`*`符号---
This text is ***really important***.
- 删除线  
前后分别添加`~~`符号--- 
~~The world is flat.~~

## 5. 引用语法
- 单段落引用：段落前添加`>`符号
> Dorothy followed her through many of the beautiful rooms in her castle.

- 多个段落的块引用：段落之间的空白行添加`>`符号
> Dorothy followed her through many of the beautiful rooms in her castle.
>
> The Witch bade her clean the pots and kettles and sweep the floor and keep the fire fed with wood.

- 嵌套块引用：在要嵌套的段落前**重复**添加`>`符号
> Dorothy followed her through many of the beautiful rooms in her castle.
>
>> The Witch bade her clean the pots and kettles and sweep the floor and keep the fire fed with wood.

- 带有其它元素的块引用
> #### The quarterly results look great!
>
> - Revenue was off the chart.
> - Profits were higher than ever.
>
>  *Everything* is going according to **plan**.

## 6. 列表语法
- 有序列表
    1. First item
    2. Second item
    3. Third item
        1. Indented item
        2. Indented item
    8. Fourth item


- 无序列表
    - First item
    - Second item
    - Third item
        - Indented item
        - Indented item
    - Fourth item

## 7.  代码语法
- 代码前后添加反引号``(`)``  
    At the command prompt, type `nano`.
- 多层嵌套  
    ``Use `code` in your Markdown file.``
- 代码块:3个反引号``(`)`` 或 整体缩进  
    ``` python
    import numpy as np
    ts = pd.Series(np.random.randn(1000), index = pd.date_range("1/1/2000", periods=1000))
    ts = ts.cumsum()
    ts.plot(figsize = (16,10),fontsize = 14,colormap = 'rainbow')
    ```

    import numpy as np
    ts = pd.Series(np.random.randn(1000), index = pd.date_range("1/1/2000", periods=1000))
    ts = ts.cumsum()
    ts.plot(figsize = (16,10),fontsize = 14,colormap = 'rainbow')

## 8. 分隔线语法
- 在一行内只使用`***`或`---`或`___`
- 为保证兼容性，分隔线前后应添加空白行

***

---------

_______

## 9. 链接语法
- 用法：`[超链接显示名](超链接地址 "超链接title")`
- 示例：这些是链接 [Markdown语法](https://markdown.com.cn "最好的markdown教程")
    [百度](https://www.baidu.com/)
    [必应](https://cn.bing.com/)
    [B站](https://www.bilibili.com/)
    [谷歌学术](https://scholar.google.com/)
- 强调：This is the ***[Markdown Guide](https://www.markdownguide.org)***.
- 网址：<https://markdown.com.cn>
    - 不同的 Markdown 应用程序处理URL中间的空格方式不一样。为了兼容性，请尽量使用`%20`代替空格。
    - 使用 [link](https://www.example.com/my%20great%20page) 代替 [link](https://www.example.com/my great page)
- 邮箱：<fake@example.com>
- 引用类型链接：[Zircon: The Metamorphic Mineral][1]

[1]:https://pubs.geoscienceworld.org/msa/rimg/article/83/1/261/520746/Zircon-The-Metamorphic-Mineral

## 10. 图片语法
- 直接复制粘贴：![image.png](attachment:image.png "Magic Gardens")
- 插入图片链接：![示例图片](https://markdown.com.cn/assets/img/philly-magic-garden.9c0b4415.jpg "Magic Gardens")

- 插入文献图片：![文献图片](https://gsw.silverchair-cdn.com/gsw/Content_public/Journal/rimg/83/1/10.2138_rmg.2017.83.9/2/rmg.2017.83.9_fig01.png?Expires=1632449302&Signature=qrloU07nJZJu8yFCVfmUxRHAQkuq7ptsUK1fH2RxVKnAex2esugGXAmn5cXTfmnvGeWj7l2AoZZDgY2gUFLtWpHvZbN0eiCfCXOGrRmtn0AkXkSpzPkDwCgYq5K6iigdkMTX99xOGwqsXoVhhcDK4cqsPKOHSLCZxWsdQZbxU6PoYcUgmR0O3wgCvNlUbXV6PlP2YelcYle~d6wF-WfcXQ2d6Dj~MoY7RX0YL53kezVCf1b1nJu25sbYkbl3xFhFaKiaLrfsIoYu0jclUf5cgWnG16n1GGXdWB2mvIciYvJIXA4LOyrJzdKP7tqA7g3ZLMBFDAkkLx-H8af-BAHpuQ__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA "Typical internal zoning and textures of zircons from different metamorphic grades.")

- 为图片增加链接：[![文献图片](https://gsw.silverchair-cdn.com/gsw/Content_public/Journal/rimg/83/1/10.2138_rmg.2017.83.9/2/rmg.2017.83.9_fig01.png?Expires=1632449302&Signature=qrloU07nJZJu8yFCVfmUxRHAQkuq7ptsUK1fH2RxVKnAex2esugGXAmn5cXTfmnvGeWj7l2AoZZDgY2gUFLtWpHvZbN0eiCfCXOGrRmtn0AkXkSpzPkDwCgYq5K6iigdkMTX99xOGwqsXoVhhcDK4cqsPKOHSLCZxWsdQZbxU6PoYcUgmR0O3wgCvNlUbXV6PlP2YelcYle~d6wF-WfcXQ2d6Dj~MoY7RX0YL53kezVCf1b1nJu25sbYkbl3xFhFaKiaLrfsIoYu0jclUf5cgWnG16n1GGXdWB2mvIciYvJIXA4LOyrJzdKP7tqA7g3ZLMBFDAkkLx-H8af-BAHpuQ__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA "Typical internal zoning and textures of zircons from different metamorphic grades.")](https://pubs.geoscienceworld.org/msa/rimg/article/83/1/261/520746/Zircon-The-Metamorphic-Mineral)

## 11. 转义字符语法
- 在斜杠前添加反斜杠字符`\`以保留原字符
* Without the backslash, this would be a bullet in an unordered list.  
\* Without the backslash, this would be a bullet in an unordered list.

- 可转义的字符类型

|Character|Name|
    |:---|:---|
    |\	|backslash|
    |\`	|backtick|
    |\*	|asterisk|
    |_	|underscore|
|{ }	|curly braces|
|\[ \]	|brackets|
|( )	|parentheses|
    |#	|pound sign|
    |\+	|plus sign|
    |\-	|minus sign|
    |\.	|dot|
    |!	|exclamation mark|
    |\|	|pipe|
    
- Tip: 
    - 使用连字符和管道创建表可能很麻烦。为了加快该过程，请尝试使用 [Markdown Tables Generator](https://www.tablesgenerator.com/markdown_tables)。
    - 使用图形界面构建表，然后将生成的Markdown格式的文本复制到文件中。

## 12. 内嵌HTML标签
- 行级内联标签，即同一行内 Markdown 语法可与 HTML 标签联用：  
    This **word** is bold. This <em>word</em> is italic.
- 区块标签：  
    This is a regular paragraph.
    
    <table>
        <tr>
            <td>Foo</td>
        </tr>
    </table>

    This is another regular paragraph.

## 13. LaTex公式
- 参考资料：
    [LaTeX 公式篇](https://zhuanlan.zhihu.com/p/110756681)
    [LaTeX公式手册(全网最全)](https://www.cnblogs.com/1024th/p/11623258.html)
- 行内公式：$ f(x) = a+b $
- 行间公式：$$ f(x) = a+b $$
- 手动编号：$$ f(x) = a - b \tag{1.1} $$
- 根号、分式：`\sqrt`表示平方根，`\sqrt[n]`表示n次方根，`\frac`表示分式
    $$\sqrt{x} + \sqrt{x^{2}+\sqrt{y}} = \sqrt[3]{k_{i}} - \frac{x}{m}$$
- 上下标：`_`表示下标、`^`表示上标，但上下标内容不止一个字符时，需用**大括号**括起来。单引号`'`表示求导
    $$ a_{ij}^{2} + b^3_{2}=x^{t} + y' + x''_{12} $$
- 希腊字母：$$ \alpha^{2} + \beta = \Theta  $$ 
    <div align=center><img src="https://pic1.zhimg.com/80/v2-da3e717cf670582fbfbdddee33073524_720w.jpg"><\div>
- 矩阵：`&`用于分隔列，`\`用于分隔行，`\ldots`点位于基线上，`\cdots`点设置为居中，`\vdots`使其垂直，`\ddots`对角线排列  
    $$A=
\begin{pmatrix}
a & b & \cdots & c  \\
d & e & \cdots & f  \\
\vdots & \vdots & \ddots & \vdots  \\
g & h & \cdots & j
\end{pmatrix}
\tag{5.1}
$$
- 向量：`\vec`表示向量，`\overrightarrow`表示箭头向右的向量，`\overleftarrow`表示箭头向左的向量
    $$\vec{a} + \overrightarrow{AB} + \overleftarrow{DE}$$
- 积分、极限：`\int`表示积分，`\lim`表示极限， `\sum`表示求和，`\prod`表示乘积，`^`、`_`表示上、下限
    $$  \lim_{x \to \infty} x^2_{22} - \int_{1}^{5}x\mathrm{d}x + \sum_{n=1}^{20} n^{2} = \prod_{j=1}^{3} y_{j}  + \lim_{x \to -2} \frac{x-2}{x} $$
- 多行公式：
    $$D(x) = \begin{cases}
    \lim\limits_{x \to 0} \frac{a^x}{b+c}, & x<3 \\
    \pi, & x=3 \\
    \int_a^{3b}x_{ij}+e^2 \mathrm{d}x,& x>3 \\
    \end{cases}$$
- 拆分单个公式：
    $$\begin{split}
    \cos 2x &= \cos^2x - \sin^2x \\
    &=2\cos^2x-1
    \end{split}$$

- 锆石Zr同位素瑞利分馏模拟
    <font size=6 face='Times New Roman'>
    $$ \delta^{94}Zr_{zircon} = (\delta^{94}Zr_{melt,0} + 1000)\alpha F^{(\alpha-1)} - 1000 \tag{1}$$
    $$ \delta^{94}Zr_{melt} = (\delta^{94}Zr_{melt,0} + 1000) F^{(\alpha-1)} - 1000 \tag{2}$$
