
combinefinal$x<-ifelse(combinefinal$LazyClass_x==0, "fail", "pass")





combinefinal$x<-ifelse(combinefinal$MIM_diff<0, "descresed", ifelse(combinefinal$FeatureEnvy_diff>0, "inceased", "inchanged" ))
combinefinal$y<-ifelse(combinefinal$Pull.Up.Attribute==0, "nonrefac", "refac")

sold<-table(combinefinal$x,combinefinal$y)
chisq.test(sold, simulate.p.value = TRUE)
cramersV(sold, simulate.p.value = TRUE)