# 1)data0205 cd4是一组艾滋病人的CD4细胞水平，采用合适的统计方法（说明选用依据），检验艾滋病人的CD4细胞水平是否小于400。
# 1.计量资料；2.判断正态性和方差齐 -> 样本量为10 -> ；3.单样本t检验
library(haven)

d_cd4 <- read_sav("./DATA/data0205+cd4.sav"); head(cd4)

cd4 <- d_cd4$cd4

# description info
summary(cd4)
mean(cd4)
sd(cd4) # 标准差
# hist(cd4, col="black", main = "cd4 histogram", xlab = "cd4") # 频数直方图

# 正态性检验
shapiro.test(cd4) # p > 0.05, 服从正态分布

t.test(cd4, mu=400, alernative = "less") # p < 0.05, 拒绝原假设, cd4 < 400

wilcox.test(cd4, mu=400, alternative = "less") # p < 0.05, 拒绝原假设, cd4 < 400

# shapiro.test()做Shapiro-Wilk normality test的正态检验

# 2)data0206 protein是某种灵长类动物栖息地内几种植物的叶片蛋白质干重比例，采用合适的统计方法（说明选用依据），检验是否与15%差异。
# 该物种栖息地内所有种类植物叶片蛋白质干重比例的99%置信区间是多少

library(haven)
d_protein <- read_sav('./DATA/data0206+protein.sav'); head(d_protein)

dim(d_protein)

t.test(d_protein$protein, mu=15, conf.level = 0.99, alernative = "two.sided")

shapiro.test(d_protein$protein) # p = 3.456e-05 < 0.05, 不服从正态分布

wilcox.test(d_protein$protein, mu=15, conf.int = TRUE, conf.level= 0.99, alternative = "two.sided") # must be one of "two.sided" (default), "greater" or "less". 
# data:  d_protein$protein
# V = 566.5, p-value = 0.4961
# alternative hypothesis: true location is not equal to 15
# 99 percent confidence interval:
#  12.56998 17.44001
# sample estimates:
# (pseudo)median
#       14.31494