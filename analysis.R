# these packages have to be installed first
# install.packages(c('readxl','tidyverse','nlme','emmeans','performance'))

library(readxl)
library(tidyverse)
library(emmeans)
library(nlme)
library(performance)

df <- read_xlsx(path = 'Project Data.xlsx', sheet='Combined')

# convert to 'long' format
df_l <- df %>% pivot_longer( - c(Sex,Condition),  names_pattern = '(.*) ',  names_to = 'min', values_to = 'height' ) 

half_hours <- seq(0,180,by=30)

df_l <-  df_l %>% mutate( min = as.numeric(min),
                          min_f = cut(min, half_hours, labels= seq(.5,3,by=.5) ),
                          id = interaction(Sex,Condition) ) %>% 
                  mutate( min = as.numeric(as.character(min_f)) )

df_l_avg <- df_l %>% group_by(Sex,Condition,min,min_f,id) %>% summarize( height_avg = mean(height) )

# two-way interaction with Sex:Condition not needed 
with( df_l_avg, interaction.plot(Sex,Condition,height_avg) )

# 3-way interaction plots
with(  df_l %>% filter( Sex == 'Male' ) , interaction.plot( min_f, Condition, height ) )
with(  df_l %>% filter( Sex == 'Female' ) , interaction.plot( min_f, Condition, height ) )

# linear mixed effect
lme_fit <- lme( height_avg ~ (Sex+Condition+min)^3  - Sex:Condition , data = df_l_avg, random = ~ 1 | id )

# model diagnostic plots
check_model( lme_fit ) # decent fit

# anova table
anova(lme_fit)
  
# trend comparisons

# time main effect
test( emtrends( lme_fit, ~ min , var = 'min' )  ) # significant trend, overall

# Condition*min
emtrends( lme_fit, ~ Condition , var = 'min'  ) %>% cld

# looks like Serotonin ON has strongest trend

# Sex*min
emtrends( lme_fit, ~ Sex , var = 'min'  ) %>% cld

# looks like Female might have a slightly stronger trend

# Sex*Condition*min
emtrends( lme_fit, ~ Condition | Sex, var = 'min'  ) %>% cld

# Significant differences in Condition only for Female

emtrends( lme_fit, ~ Sex | Condition, var = 'min'  ) %>% cld
# Female/Male significant difference only at Serotonin ON

# all trend comparisons
emtrends( lme_fit, ~ Sex*Condition , var = 'min'  ) %>% cld
# Female & Serotonin ON the strongest trend; rest can't be told apart

df_l_avg$fitted <- fitted( lme_fit ) 

# plot
p <- ggplot(df_l_avg)+
  aes( x = min, y = height_avg, color = Condition )+
  geom_line( linetype=3, show.legend=F )+
  geom_line( aes(y=fitted), size=1 )+
  facet_wrap(~Sex)+
  xlab('Hours')+
  ylab('Average Quadrant')+
  theme_classic()+
  scale_x_continuous(breaks = seq(0.5,3,by=.5) )+
  scale_y_continuous(breaks = seq(1,3.5,by=.5) )+
  guides(color =  guide_legend('') )

ggsave('results/plots/trends_by_sex.png',plot = p, width=8,height=8,units='in' )

p <- ggplot(df_l_avg)+
  aes( x = min, y = height_avg, color = Sex )+
  geom_line( linetype=3, show.legend=F )+
  geom_line( aes(y=fitted), size=1 )+
  facet_wrap(~Condition)+
  xlab('Hours')+
  ylab('Average Quadrant')+
  theme_classic()+
  scale_x_continuous(breaks = seq(0.5,3,by=.5) )+
  scale_y_continuous(breaks = seq(1,3.5,by=.5) )+
  guides(color =  guide_legend('') )

ggsave('results/plots/trends_by_condition.png',plot = p, width=8,height=8,units='in' )
  
  











