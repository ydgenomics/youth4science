数据分析步骤
1. 样本类型(1/2/多个)
2. 数据类型(计数/计量/等级)
3. 数据正态性与方差齐性
4. 均值差异/中位数差异

检验方法
- t检验
- Wilcoxon sum rank test (Mann-Whitney *U* test)

两组数据检验
| 场景         | 假设      | R 函数                            |
| ---------- | ------- | ------------------------------- |
| 配对、正态      | 配对 t    | `t.test(x, y, paired=TRUE)`     |
| 独立、正态、方差齐  | 独立 t    | `t.test(x, y, var.equal=TRUE)`  |
| 独立、正态、方差不齐 | Welch t | `t.test(x, y, var.equal=FALSE)` |
| 独立、非正态     | 非参数     | `wilcox.test(x, y)`             |

---

[3分钟搞懂独立样本t检验与配对样本t检验的区别](https://mp.weixin.qq.com/s/i0qbchfdtEPsVsBAVK6gEQ)

独立样本t检验： 比较的是两组完全独立、互不相关的个体。
F检验检查两组数据的方差比是否为1
配对样本t检验： 比较的是同一组个体在两种不同条件或时间点下的表现。

[临床研究干货 | 小样本、方差不齐？校正t检验 VS 秩和检验这样选！](https://mp.weixin.qq.com/s/qT_IJGX-jDKwBgYOuNGw3Q)

<details>
  <summary> <strong> 正态性检验(Normality test)及其R代码 </strong> </summary>

下面给出**最常用的 4 种正态性检验**及对应 R 代码，按“**先看图→再检验→最后决策**”的顺序排列，复制即可跑。

---

### 1. 图示法（快速目测）
**Q-Q图看数据点是否大致分布在一条对角线上，直方图看形状是否接近钟形曲线**

```r
x <- rnorm(50, mean=10, sd=2)   # 你的数据替换这里

# 1.1 直方图+密度曲线
pdf("hist_lines.pdf")
hist(x, probability=TRUE, col="skyblue", main="Histogram")
lines(density(x), col="red", lwd=2)
dev.off()

# 1.2 Q-Q 图
pdf("qq.pdf")
qqnorm(x); qqline(x, col="red")
dev.off()
```

---

### 2. Shapiro-Wilk 检验（最常用，3≤n≤5000）
```r
shapiro.test(x)
# p > 0.05  ⇒  不拒绝“数据来自正态分布”
```

---

### 3. Kolmogorov-Smirnov 检验（需指定参数，易过拟合）
```r
# 必须先给出μ、σ；否则 p 值偏保守
ks.test(x, "pnorm", mean=mean(x), sd=sd(x))
# 结果仅作参考，不推荐小样本
```

---

### 4. Anderson-Darling 检验（功效高，需 n ≥ 8）
```r
library(nortest)
ad.test(x)
```

---

### 5. Jarque-Bera 检验（基于偏度、峰度，大样本）
```r
library(tseries)
jarque.bera.test(x)   # 需要 n ≥ 30 才稳定
```

---

### 6. 一次性批量检验（多变量/多组）
```r
# 假设 data.frame 里有多列数值
df <- data.frame(a = rnorm(50),
                 b = runif(50))   # b 明显非正态

lapply(df, function(col){
  if(is.numeric(col)) shapiro.test(col)
})
```

---

### 7. 正态性决策流程（实用版）
1. 先画 **Q-Q 图** → 目测是否近似直线。  
2. 若需正式报告：**Shapiro-Wilk** 足够（除非 n>5000）。  
3. 若分组检验，每组单独做 Shapiro；组多时可用 **Bonferroni** 校正 α 水平。  
4. 若检验显示非正态：  
   - 小样本 → 考虑 **数据变换**（log、Box-Cox）。  
   - 大样本 → 中心极限定理保障，可直接用 **稳健方法** 或 **非参数检验**。

---

### 速查表
| 方法 | R 函数 | 样本量 | 备注 |
|---|---|---|---|
| Shapiro-Wilk | `shapiro.test(x)` | 3–5000 | 首选 |
| Anderson-Darling | `nortest::ad.test(x)` | ≥8 | 功效高 |
| Jarque-Bera | `tseries::jarque.bera.test(x)` | ≥30 | 基于矩 |
| Kolmogorov-Smirnov | `ks.test(x,"pnorm",...)` | 任意 | 需先指定参数，保守 |

把 `x` 换成你的向量/每列数据即可直接出结果。


**Ref**
- [0代码1分钟搞定SCI的正态性检验和QQ图（统计教程）](https://mp.weixin.qq.com/s/cR0Y1UZCr4eaQzWtd_2YLA)
</details>

<details>
  <summary> <strong>方差齐性检验及其R代码 </strong> </summary>

方差齐性检验（Homogeneity of Variance Test）用于检验不同组数据的方差是否相等，是许多统计方法（如ANOVA、t检验）的前提假设之一。以下是几种常用的方差齐性检验方法及其R代码实现：
- Bartlett test
- Levene test
- Fligner-Killeen test
- F test

不同方差齐性检验的考虑点：1.是否依赖数据正态性；2.是否有组数限制；

#### 1. **Bartlett检验**
- **适用场景**：数据服从正态分布。
- **原假设**：各组方差相等。
- **R代码**：
  ```r
  # 示例数据
  set.seed(123)
  group1 <- rnorm(30, mean = 10, sd = 2)
  group2 <- rnorm(30, mean = 12, sd = 3)
  group3 <- rnorm(30, mean = 11, sd = 2.5)
  data <- data.frame(
    value = c(group1, group2, group3),
    group = factor(rep(c("A", "B", "C"), each = 30))
  )

  # Bartlett检验
  bartlett.test(value ~ group, data = data)
  ```
- **结果解读**：若p值 > 0.05，不拒绝原假设，认为方差齐性成立。

#### 2. **Levene检验**
- **适用场景**：对正态性假设不敏感，更稳健（推荐）。
- **原假设**：各组方差相等。
- **R代码**：
  ```r
  # 加载car包
  library(car)

  # Levene检验（默认用中位数）
  leveneTest(value ~ group, data = data)

  # 可选：用均值（类似Bartlett）
  leveneTest(value ~ group, data = data, center = mean)
  ```
- **结果解读**：p值 > 0.05表示方差齐性。

#### 3. **Fligner-Killeen检验**
- **适用场景**：非正态数据，稳健非参数方法。
- **原假设**：各组方差相等。
- **R代码**：
  ```r
  fligner.test(value ~ group, data = data)
  ```

#### 4. **可视化辅助：箱线图与残差图**
```r
# 箱线图
boxplot(value ~ group, data = data, col = "lightblue")

# 残差图（ANOVA后）
model <- aov(value ~ group, data = data)
plot(model, 1)  # 残差vs拟合图
```

#### **选择建议**
- **正态数据**：Bartlett检验（敏感但功效高）。
- **非正态或未知**：Levene检验（默认推荐）。
- **严重偏离正态**：Fligner-Killeen检验。

#### **注意事项**
1. 若方差齐性不满足，可考虑：
   - 数据转换（如对数、平方根）。
   - 使用非参数方法（如Kruskal-Wallis检验）。
   - 校正ANOVA（如Welch’s ANOVA）。
   ```r
   # Welch's ANOVA（方差不齐时）
   oneway.test(value ~ group, data = data, var.equal = FALSE)
   ```

2. 样本量差异较大时，Levene检验更稳健。

通过以上方法，可系统检验方差齐性并选择合适的后续分析策略。

方差齐性 F 检验（F-test for equality of variances）  
—— 仅比较 **两组** 方差是否相等，是最经典、最敏感的方差齐性检验。

1. 原假设与备择假设  
H₀: σ₁² = σ₂²  
H₁: σ₁² ≠ σ₂² （双侧，也可单侧）

2. 检验统计量  
F = s₁² / s₂²  （把较大样本方差放在分子，使 F ≥ 1）  
自由度：df₁ = n₁ – 1，df₂ = n₂ – 1

3. 假设条件  
- 两组数据独立  
- 每组内部近似正态（对正态性最敏感）

4. R 实现  
基础包自带 `var.test()`，一行搞定：

```r
# 示例：两组独立正态数据
set.seed(123)
x <- rnorm(30, mean = 10, sd = 2)   # sd=2
y <- rnorm(25, mean = 12, sd = 3)   # sd=3

# 方差齐性 F 检验
vt <- var.test(x, y)
vt
```

输出解读  
- `F = 2.25` 是较大方差 / 较小方差  
- `p-value = 0.08` > 0.05 ⇒ 不拒绝 H₀，可认为两组方差齐性

5. 单侧检验（例如只想知道 x 的方差是否更大）  
```r
var.test(x, y, alternative = "greater")
```

6. 与 `bartlett.test()` 的区别  
- `var.test` 只能做 **两组**；`bartlett.test` 可做多组，但要求正态。  
- 对正态性敏感程度：F 检验 > Bartlett > Levene。

7. 可视化辅助  
```r
# 箱线图
boxplot(x, y, col = c("skyblue", "salmon"))

# 正态 Q-Q 图
qqnorm(x); qqline(x)
qqnorm(y); qqline(y)
```

8. 方差不齐时的后续方案  
- Welch 两样本 t 检验（默认方差不相等）：  
  ```r
  t.test(x, y, var.equal = FALSE)
  ```  
- 数据变换（对数、Box-Cox）  
- 非参数 Mann-Whitney U 检验

一句话总结：  
**只有两组**且**近似正态** → 用 `var.test()` 做 F 检验；  
**多组或正态存疑** → 改用 Levene/Bartlett/Fligner。

</details>