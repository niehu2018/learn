

#install.packages("pdftools")

library(pdftools)

# 拆分PDF文件
# extract some pages
pdf_subset('https://cran.r-project.org/doc/manuals/r-release/R-intro.pdf',
           pages = 1:3, output = "subset.pdf")

# Should say 3
pdf_length("subset.pdf")



# 合并PDF文件
pdf("test.pdf")
plot(mtcars)
dev.off()

# Combine them with the other one
pdf_combine(c("test.pdf", "subset.pdf"), output = "joined.pdf")
# Should say 4
pdf_length("joined.pdf")




# 如果你要把多个图片写入到同一个pdf里面，每个图片是一个页面
pdf("myOut.pdf")
for (i in 1:10){
    plot(rnorm(10))
}
dev.off()
