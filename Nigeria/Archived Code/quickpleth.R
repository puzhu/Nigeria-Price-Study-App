setwd("~/Documents/Price Project/Code/Web App Code/maps/Nigeria GADM Shapefiles")
library('maptools'); library("ggplot2"); library('dplyr')
nigeria1 <- readShapeSpatial("NGA_adm1.shp")
gpclibPermit()
nigeria1 <- fortify(nigeria1, region = "NAME_1")
load("~/Documents/Price Project/Code/Data Cleaning Code/Nigeria Data/Final Datasets/nigeriaData.Rda")

stateData <- tbl_df(data) %>%
        filter(item == "Rice Local") %>%
        group_by(state) %>%
        summarise(price = mean(meanPrice))
colnames(stateData) <- c("id", "price")
        
ggplot(stateData) + geom_map(aes(map_id = id, fill = price), map = nigeria1) + expand_limits(x = nigeria1$long, y = nigeria1$lat)
