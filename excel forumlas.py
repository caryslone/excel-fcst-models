####
### Style color level formula for june without any of the if fcst strat or round functions.
=SUMIF(bup[[style code]:[style code]],bup[@[pattern after sku 24]:[pattern after sku 24]],bup[[2023 units]:[2023 units]])*
XLOOKUP(bup[@[superstyle]:[superstyle]],style[[style]:[style]],style[jun])*
XLOOKUP(bup[@[size]:[size]],size[[size]:[size]],size[[percent]:[percent]])*
(1+bup[@[growth override 23]:[growth override 23]])



#Meateater forecast unit code--------------------------------
###Probably need to look at using previous month inventory as max acheivable as in FL codeblock below
=IFERROR(ROUND(IF(bup[@[forecast strategy 23]:[forecast strategy 23]]="ytd.profile.cat",
((SUM(bup[@[jan 23 u]:[apr 23 u]])) / (XLOOKUP(bup[@[category]:[category]],ytd.curve[[cat.ytd]:[cat.ytd]],ytd.curve[may])))
*(XLOOKUP(bup[@[category]:[category]],cat.curve[[cat]:[cat]],cat.curve[may]))*(1+bup[@[growth override 23]:[growth override 23]]),

IF(bup[@[forecast strategy 23]:[forecast strategy 23]]="ytd.profile.subcat",
((SUM(bup[@[jan 23 u]:[apr 23 u]])) / (XLOOKUP(bup[@[sub category ]:[sub category ]],ytd.curve[[cat.ytd]:[cat.ytd]],ytd.curve[may])))
*(XLOOKUP(bup[@[sub category ]:[sub category ]],cat.curve[[cat]:[cat]],cat.curve[may]))*(1+bup[@[growth override 23]:[growth override 23]]),

IF(bup[@[forecast strategy 23]:[forecast strategy 23]]="middle.out",
(AVERAGE([@[apr 22 u]],[@[may 22 u]],[@[jun 22 u]]))*(1+bup[@[growth override 23]:[growth override 23]]),

IF(bup[@[forecast strategy 23]:[forecast strategy 23]]="logowear",
((bup[@[on order]:[on order]]+bup[@[on hand]:[on hand]])*0.8)*XLOOKUP(bup[@[category]:[category]],cat.curve[[cat]:[cat]],cat.curve[may])*(1+bup[@[growth override 23]:[growth override 23]]),

IF(bup[@[forecast strategy 23]:[forecast strategy 23]]="pattern.sa",
XLOOKUP(bup[@[pattern after sku 23]:[pattern after sku 23]],bup[[sku]:[sku]],bup[[2023 u]:[2023 u]])*
XLOOKUP(bup[@[category]:[category]],cat.curve[[cat]:[cat]],cat.curve[may])*
(1+bup[@[growth override 23]:[growth override 23]]),

IF(bup[@[forecast strategy 23]:[forecast strategy 23]]="pattern.dwo",
(XLOOKUP(bup[@[pattern after sku 23]:[pattern after sku 23]],bup[[sku]:[sku]],bup[[2022 u]:[2022 u]])/
XLOOKUP(bup[@[pattern after sku 23]:[pattern after sku 23]],bup[[sku]:[sku]],bup[[vol achieved 22]:[vol achieved 22]]))*
XLOOKUP(bup[@[category]:[category]],cat.curve[[cat]:[cat]],cat.curve[may])*
(1+bup[@[growth override 23]:[growth override 23]]),

IF(bup[@[forecast strategy 23]:[forecast strategy 23]]="opt.season",
(bup[@[2022 u]:[2022 u]]/bup[@[vol achieved 22]:[vol achieved 22]])
*XLOOKUP(bup[@[category]:[category]],cat.curve[[cat]:[cat]],cat.curve[may])*(1+bup[@[growth override 23]:[growth override 23]])))))))),0),0)



#--------------------------------------------------------------------------#-------------------------------------------#----------------------
###-------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------#-------------------------------------------#----------------------
###-------------------------------------------------------------------------------------------------------------------------------------------


### First Lite Forecast Unit Code

### will need to manually update months in ytd.profile formula, it will not drag
##### applied to the month of May in 2022, YTD needs to sum to actualized months only
##### Need to manually update the sumif portion in the middle to 

#Build on May actuals and June forecast
# matts update so that projected units cannot exceed last month EOH + Next months expected inventory

#### 2023*** FL codeblock for 2023 units from June. Need to Manually update YTD fcsts code blocks
=IF(IFERROR(ROUND(IF(bup[@[forecast strategy 23]:[forecast strategy 23]]="roll.avg.ly",
AVERAGE([@[may 22 units]],[@[jun 22 units]],[@[jul 22 units]])*
(1+bup[@[growth override 23]:[growth override 23]]),

IF(bup[@[forecast strategy 23]:[forecast strategy 23]]="roll.avg.2y",
SUM(([@[may 21 units]]*0.1133),([@[jun 21 units]]*0.1133),([@[jul 21 units]]*0.1133),
([@[may 22 units]]*0.22),([@[jun 22 units]]*0.22),([@[jul 22 units]]*0.22))*(1+bup[@[growth override 23]:[growth override 23]]),

IF(bup[@[forecast strategy 23]:[forecast strategy 23]]="pattern.sa",
XLOOKUP(bup[@[pattern after sku 23]:[pattern after sku 23]],bup[[sku]:[sku]],bup[[2023 units]:[2023 units]])*
XLOOKUP(bup[@[superstyle]:[superstyle]],style[[style]:[style]],style[jun])*
(1+bup[@[growth override 23]:[growth override 23]]),

IF(bup[@[forecast strategy 23]:[forecast strategy 23]]="pattern.dwo",
XLOOKUP(bup[@[pattern after sku 23]:[pattern after sku 23]],bup[[sku]:[sku]],bup[[2022 units]:[2022 units]])/
XLOOKUP(bup[@[pattern after sku 23]:[pattern after sku 23]],bup[[sku]:[sku]],bup[[2022 vol ach]:[2022 vol ach]])*
XLOOKUP(bup[@[superstyle]:[superstyle]],style[[style]:[style]],style[jun])*
(1+bup[@[growth override 23]:[growth override 23]]),

IF(bup[@[forecast strategy 23]:[forecast strategy 23]]="style.color.sa",
SUMIF(bup[[style code]:[style code]],bup[@[pattern after sku 23]:[pattern after sku 23]],bup[[2023 units]:[2023 units]])*
XLOOKUP(bup[@[superstyle]:[superstyle]],style[[style]:[style]],style[jun])*
XLOOKUP(bup[@[size]:[size]]&bup[@[superstyle]:[superstyle]],size[[size]:[size]]&size[[style]:[style]],size[[percent]:[percent]])*
(1+bup[@[growth override 23]:[growth override 23]]),

IF(bup[@[forecast strategy 23]:[forecast strategy 23]]="style.color.dwo",
SUMIF(bup[[style code]:[style code]],bup[@[pattern after sku 23]:[pattern after sku 23]],bup[[2022 units]:[2022 units]])*
XLOOKUP(bup[@[superstyle]:[superstyle]],style[[style]:[style]],style[jun])*
XLOOKUP(bup[@[size]:[size]]&bup[@[superstyle]:[superstyle]],size[[size]:[size]]&size[[style]:[style]],size[[percent]:[percent]])*
(1+bup[@[growth override 23]:[growth override 23]]),

IF(bup[@[forecast strategy 23]:[forecast strategy 23]]="opt.season",
(bup[@[2022 units]:[2022 units]]/bup[@[2022 vol ach]:[2022 vol ach]])*
XLOOKUP(bup[@[superstyle]:[superstyle]],style[[style]:[style]],style[jun])*
(1+bup[@[growth override 23]:[growth override 23]]),

IF(bup[@[forecast strategy 23]:[forecast strategy 23]]="ytd.profile.style",
SUM((bup[@[jan 23 units]:[may 23 units]]))/(XLOOKUP(bup[@[superstyle]:[superstyle]],ytd[[ytd]:[ytd]],ytd[may]))*
XLOOKUP(bup[@[superstyle]:[superstyle]],style[[style]:[style]],style[jun])*
(1+bup[@[growth override 23]:[growth override 23]]),

IF(bup[@[forecast strategy 23]:[forecast strategy 23]]="ytd.profile.subcat",
SUM((bup[@[jan 23 units]:[may 23 units]]))/(XLOOKUP(bup[@[sub category ]:[sub category ]],ytd[[ytd]:[ytd]],ytd[may]))*
XLOOKUP(bup[@[sub category ]:[sub category ]],style[[style]:[style]],style[jun])*
(1+bup[@[growth override 23]:[growth override 23]])))))))))),0),"shit")

>[@[may 23 inv]]+SUMIFS('on order'!$G:$G,'on order'!$C:$C,bup[@[sku]:[sku]],'on order'!$O:$O,IT$7,'on order'!$P:$P,IT$6),
[@[may 23 inv]]+SUMIFS('on order'!$G:$G,'on order'!$C:$C,bup[@[sku]:[sku]],'on order'!$O:$O,IT$7,'on order'!$P:$P,IT$6),

IFERROR(ROUND(IF(bup[@[forecast strategy 23]:[forecast strategy 23]]="roll.avg.ly",
AVERAGE([@[may 22 units]],[@[jun 22 units]],[@[jul 22 units]])*
(1+bup[@[growth override 23]:[growth override 23]]),

IF(bup[@[forecast strategy 23]:[forecast strategy 23]]="roll.avg.2y",
SUM(([@[may 21 units]]*0.1133),([@[jun 21 units]]*0.1133),([@[jul 21 units]]*0.1133),
([@[may 22 units]]*0.22),([@[jun 22 units]]*0.22),([@[jul 22 units]]*0.22))*(1+bup[@[growth override 23]:[growth override 23]]),

IF(bup[@[forecast strategy 23]:[forecast strategy 23]]="pattern.sa",
XLOOKUP(bup[@[pattern after sku 23]:[pattern after sku 23]],bup[[sku]:[sku]],bup[[2023 units]:[2023 units]])*
XLOOKUP(bup[@[superstyle]:[superstyle]],style[[style]:[style]],style[jun])*
(1+bup[@[growth override 23]:[growth override 23]]),

IF(bup[@[forecast strategy 23]:[forecast strategy 23]]="pattern.dwo",
XLOOKUP(bup[@[pattern after sku 23]:[pattern after sku 23]],bup[[sku]:[sku]],bup[[2022 units]:[2022 units]])/
XLOOKUP(bup[@[pattern after sku 23]:[pattern after sku 23]],bup[[sku]:[sku]],bup[[2022 vol ach]:[2022 vol ach]])*
XLOOKUP(bup[@[superstyle]:[superstyle]],style[[style]:[style]],style[jun])*
(1+bup[@[growth override 23]:[growth override 23]]),

IF(bup[@[forecast strategy 23]:[forecast strategy 23]]="style.color.sa",
SUMIF(bup[[style code]:[style code]],bup[@[pattern after sku 23]:[pattern after sku 23]],bup[[2023 units]:[2023 units]])*
XLOOKUP(bup[@[superstyle]:[superstyle]],style[[style]:[style]],style[jun])*
XLOOKUP(bup[@[size]:[size]]&bup[@[superstyle]:[superstyle]],size[[size]:[size]]&size[[style]:[style]],size[[percent]:[percent]])*
(1+bup[@[growth override 23]:[growth override 23]]),

IF(bup[@[forecast strategy 23]:[forecast strategy 23]]="style.color.dwo",
SUMIF(bup[[style code]:[style code]],bup[@[pattern after sku 23]:[pattern after sku 23]],bup[[2022 units]:[2022 units]])*
XLOOKUP(bup[@[superstyle]:[superstyle]],style[[style]:[style]],style[jun])*
XLOOKUP(bup[@[size]:[size]]&bup[@[superstyle]:[superstyle]],size[[size]:[size]]&size[[style]:[style]],size[[percent]:[percent]])*
(1+bup[@[growth override 23]:[growth override 23]]),

IF(bup[@[forecast strategy 23]:[forecast strategy 23]]="opt.season",
(bup[@[2022 units]:[2022 units]]/bup[@[2022 vol ach]:[2022 vol ach]])*
XLOOKUP(bup[@[superstyle]:[superstyle]],style[[style]:[style]],style[jun])*
(1+bup[@[growth override 23]:[growth override 23]]),

IF(bup[@[forecast strategy 23]:[forecast strategy 23]]="ytd.profile.style",
SUM((bup[@[jan 23 units]:[may 23 units]]))/(XLOOKUP(bup[@[superstyle]:[superstyle]],ytd[[ytd]:[ytd]],ytd[may]))*
XLOOKUP(bup[@[superstyle]:[superstyle]],style[[style]:[style]],style[jun])*
(1+bup[@[growth override 23]:[growth override 23]]),

IF(bup[@[forecast strategy 23]:[forecast strategy 23]]="ytd.profile.subcat",
SUM((bup[@[jan 23 units]:[may 23 units]]))/(XLOOKUP(bup[@[sub category ]:[sub category ]],ytd[[ytd]:[ytd]],ytd[may]))*
XLOOKUP(bup[@[sub category ]:[sub category ]],style[[style]:[style]],style[jun])*
(1+bup[@[growth override 23]:[growth override 23]])))))))))),0),"shit"))



#--------------------------------------------------------------------------#-------------------------------------------#----------------------
###-------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------#-------------------------------------------#----------------------
###-------------------------------------------------------------------------------------------------------------------------------------------


#-- 2024***FL workbook forumlas for 2024
=IFERROR(ROUND(IF(bup[@[forecast strategy 24]:[forecast strategy 24]]="roll.avg.ly",
AVERAGE([@[dec 22 units]],[@[jan 23 units]],[@[feb 23 units]])*(1+bup[@[growth override 24]:[growth override 24]]),

IF(bup[@[forecast strategy 24]:[forecast strategy 24]]="roll.avg.2y",
SUM(([@[dec 21 units]]*0.1133),([@[jan 22 units]]*0.1133),([@[feb 22 units]]*0.1133),
([@[dec 22 units]]*0.22),([@[jan 23 units]]*0.22),([@[feb 23 units]]*0.22))*(1+bup[@[growth override 24]:[growth override 24]]),

IF(bup[@[forecast strategy 24]:[forecast strategy 24]]="pattern.sa",
XLOOKUP(bup[@[pattern after sku 24]:[pattern after sku 24]],bup[[sku]:[sku]],bup[[2024 units]:[2024 units]])*
XLOOKUP(bup[@[superstyle]:[superstyle]],style[[style]:[style]],style[jan])*(1+bup[@[growth override 24]:[growth override 24]]),

IF(bup[@[forecast strategy 24]:[forecast strategy 24]]="pattern.dwo",
XLOOKUP(bup[@[pattern after sku 24]:[pattern after sku 24]],bup[[sku]:[sku]],bup[[2023 units]:[2023 units]])/
XLOOKUP(bup[@[pattern after sku 24]:[pattern after sku 24]],bup[[sku]:[sku]],bup[[2023 vol ach]:[2023 vol ach]])*
XLOOKUP(bup[@[superstyle]:[superstyle]],style[[style]:[style]],style[jan])*(1+bup[@[growth override 24]:[growth override 24]]),

IF(bup[@[forecast strategy 24]:[forecast strategy 24]]="style.color.sa",
SUMIF(bup[[style code]:[style code]],bup[@[pattern after sku 24]:[pattern after sku 24]],bup[[2024 units]:[2024 units]])*
XLOOKUP(bup[@[superstyle]:[superstyle]],style[[style]:[style]],style[jan])*
XLOOKUP(bup[@[size]:[size]]&bup[@[superstyle]:[superstyle]],size[[size]:[size]]&size[[style]:[style]],size[[percent]:[percent]])*
XLOOKUP(bup[@[color pattern]:[color pattern]]&bup[@[superstyle]:[superstyle]],color[[color]:[color]]&color[[style]:[style]],color[[percent]:[percent]])*(1+bup[@[growth override 24]:[growth override 24]]),

IF(bup[@[forecast strategy 24]:[forecast strategy 24]]="style.color.dwo",
SUMIF(bup[[style code]:[style code]],bup[@[pattern after sku 24]:[pattern after sku 24]],bup[[2023 units]:[2023 units]])*
XLOOKUP(bup[@[superstyle]:[superstyle]],style[[style]:[style]],style[jan])*
XLOOKUP(bup[@[size]:[size]]&bup[@[superstyle]:[superstyle]],size[[size]:[size]]&size[[style]:[style]],size[[percent]:[percent]])*
XLOOKUP(bup[@[color pattern]:[color pattern]]&bup[@[superstyle]:[superstyle]],color[[color]:[color]]&color[[style]:[style]],color[[percent]:[percent]])*(1+bup[@[growth override 24]:[growth override 24]]),

IF(bup[@[forecast strategy 24]:[forecast strategy 24]]="opt.season",
(bup[@[2023 units]:[2023 units]]/bup[@[2023 vol ach]:[2023 vol ach]])*
XLOOKUP(bup[@[superstyle]:[superstyle]],style[[style]:[style]],style[jan])*(1+bup[@[growth override 24]:[growth override 24]]),

IF(bup[@[forecast strategy 24]:[forecast strategy 24]]="ytd.profile.style",
SUM((bup[@[jan 24 units]:[jan 24 units]]))/(XLOOKUP(bup[@[superstyle]:[superstyle]],ytd[[ytd]:[ytd]],ytd[jan]))*
XLOOKUP(bup[@[superstyle]:[superstyle]],style[[style]:[style]],style[jan])*(1+bup[@[growth override 24]:[growth override 24]]),

IF(bup[@[forecast strategy 24]:[forecast strategy 24]]="ytd.profile.subcat",
SUM((bup[@[jan 24 units]:[jan 24 units]]))/(XLOOKUP(bup[@[sub category ]:[sub category ]],ytd[[ytd]:[ytd]],ytd[jan]))*
XLOOKUP(bup[@[sub category ]:[sub category ]],style[[style]:[style]],style[jan])*(1+bup[@[growth override 24]:[growth override 24]])))))))))),0),"shit")


#--------------------------------------------------------------------------#-------------------------------------------#----------------------
###-------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------#-------------------------------------------#----------------------
###-------------------------------------------------------------------------------------------------------------------------------------------
###-----------------------------------------------------------------------------------------------------------------------------------                      

## Indiviudal formulas for fcst workbook
#FL 1 year rolling average no weights
=IF(bup[@[forecast strategy 23]:[forecast strategy 23]]="roll.avg.ly",
AVERAGE([@[apr 22 units]],[@[may 22 units]],[@[jun 22 units]])*
(1+bup[@[growth override 23]:[growth override 23]]))

#FL 2 Year Weighted Rolling Average
=IF(bup[@[forecast strategy 23]:[forecast strategy 23]]="roll.avg.2y",
SUM(([@[apr 21 units]]*.1133),([@[may 21 units]]*.1133),([@[jun 21 units]]*.1133),
([@[apr 22 units]]*.22),([@[may 22 units]]*.22),([@[jun 22 units]]*.22))*(1+bup[@[growth override 23]:[growth override 23]]))

#pattern after sa for FL
=IF(bup[@[forecast strategy 23]:[forecast strategy 23]]="pattern.sa",
XLOOKUP(bup[@[pattern after sku 23]:[pattern after sku 23]],bup[[sku]:[sku]],bup[[2023 units]:[2023 units]])*
XLOOKUP(bup[@[superstyle]:[superstyle]],style[[style]:[style]],style[may])*
(1+bup[@[growth override 23]:[growth override 23]]))

#pattern.dwo fl
=IF(bup[@[forecast strategy 23]:[forecast strategy 23]]="pattern.dwo",
XLOOKUP(bup[@[pattern after sku 23]:[pattern after sku 23]],bup[[sku]:[sku]],bup[[2022 units]:[2022 units]])/
XLOOKUP(bup[@[pattern after sku 23]:[pattern after sku 23]],bup[[sku]:[sku]],bup[[2022 vol ach]:[2022 vol ach]])*
XLOOKUP(bup[@[superstyle]:[superstyle]],style[[style]:[style]],style[may])*
(1+bup[@[growth override 23]:[growth override 23]]))

#ytd.profile.style FL (need to update months manually for each future month)
=IF(bup[@[forecast strategy 23]:[forecast strategy 23]]="ytd.profile.style",
SUM((bup[@[jan 23 units]:[apr 23 units]]))/(XLOOKUP(bup[@[superstyle]:[superstyle]],ytd[[ytd]:[ytd]],ytd[may]))*
XLOOKUP(bup[@[superstyle]:[superstyle]],style[[style]:[style]],style[may])*
(1+bup[@[growth override 23]:[growth override 23]]))

#ytd.profile.subcat (need to update months manually for each future month)
=IF(bup[@[forecast strategy 23]:[forecast strategy 23]]="ytd.profile.subcat",
SUM((bup[@[jan 23 units]:[apr 23 units]]))/(XLOOKUP(bup[@[sub category ]:[sub category ]],ytd[[ytd]:[ytd]],ytd[may]))*
XLOOKUP(bup[@[sub category ]:[sub category ]],style[[style]:[style]],style[may])*
(1+bup[@[growth override 23]:[growth override 23]]))


#opt.season FL
=IF(bup[@[forecast strategy 23]:[forecast strategy 23]]="opt.season",
(bup[@[2022 units]:[2022 units]]/bup[@[2022 vol ach]:[2022 vol ach]])*
XLOOKUP(bup[@[superstyle]:[superstyle]],style[[style]:[style]],style[may])*
(1+bup[@[growth override 23]:[growth override 23]]))


#logowear
=IF(bup[@[forecast strategy 23]:[forecast strategy 23]]="logowear",
((bup[@[on order]:[on order]]+bup[@[on hand]:[on hand]])*0.8)*XLOOKUP(bup[@[superstyle]:[superstyle]],style[[style]:[style]],style[may])*
(1+bup[@[growth override 23]:[growth override 23]])),

#style.color.sa
=IF(bup[@[forecast strategy 24]:[forecast strategy 24]]="style.color.sa",
SUMIF(bup[[style code]:[style code]],bup[@[pattern after sku 24]:[pattern after sku 24]],bup[[2024 units]:[2024 units]])*
XLOOKUP(bup[@[superstyle]:[superstyle]],style[[style]:[style]],style[jan])*
XLOOKUP(bup[@[size]:[size]]&bup[@[superstyle]:[superstyle]],size[[size]:[size]]&size[[style]:[style]],size[[percent]:[percent]])*
XLOOKUP(bup[@[color pattern]:[color pattern]]&bup[@[superstyle]:[superstyle]],color[[color]:[color]]&color[[style]:[style]],color[[percent]:[percent]])*
(1+bup[@[growth override 24]:[growth override 24]])),

#style.color.dwo
=IF(bup[@[forecast strategy 24]:[forecast strategy 24]]="style.color.dwo",
SUMIF(bup[[style code]:[style code]],bup[@[pattern after sku 24]:[pattern after sku 24]],bup[[2023 units]:[2023 units]])*
XLOOKUP(bup[@[superstyle]:[superstyle]],style[[style]:[style]],style[jan])*
XLOOKUP(bup[@[size]:[size]]&bup[@[superstyle]:[superstyle]],size[[size]:[size]]&size[[style]:[style]],size[[percent]:[percent]])*
XLOOKUP(bup[@[color pattern]:[color pattern]]&bup[@[superstyle]:[superstyle]],color[[color]:[color]]&color[[style]:[style]],color[[percent]:[percent]])*
(1+bup[@[growth override 24]:[growth override 24]])),

#Adjustment for max inventory level based on prevoius months eoh and next months on order. need to adjust may if not dragging accross
>[@[may 23 inv]]+SUMIFS('on order'!$G:$G,'on order'!$C:$C,[@[sku]:[sku]],'on order'!$O:$O,IP$7,'on order'!$P:$P,IP$6),
[@[may 23 inv]]+SUMIFS('on order'!$G:$G,'on order'!$C:$C,[@[sku]:[sku]],'on order'!$O:$O,IP$7,'on order'!$P:$P,IP$6),

#--------------------------------------------------------------------------#-------------------------------------------#----------------------
###-------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------#-------------------------------------------#----------------------
###-------------------------------------------------------------------------------------------------------------------------------------------
###-----------------------------------------------------------------------------------------------------------------------------------   
#additional code blocks not related to unit forecasting

#forecast trigger
=IF([@status]="DWO", "dwo",
IF([@[intro season]]=2024,"new style",
IF([@[2023 vol actualized]]>0.65, "ytd.profile",
IF(AND([@[2021 vol ach]]<0.85,[@[2022 vol ach]]>0.7),"roll.avg.ly",
IF(AND([@[2021 vol ach]]>=0.85,[@[2022 vol ach]]>=0.85),"roll.avg.2y","not yet")))))

#volume achieved [need to update months as you actualize]
=IFERROR(
([@[jan 23 flag]]*XLOOKUP([@superstyle],style[style],style[jan]))+
([@[feb 23 flag]]*XLOOKUP([@superstyle],style[style],style[feb]))+
([@[mar 23 flag]]*XLOOKUP([@superstyle],style[style],style[mar]))+
([@[apr 23 flag]]*XLOOKUP([@superstyle],style[style],style[apr]))+
([@[may 23 flag]]*XLOOKUP([@superstyle],style[style],style[may])),"shit")


---------------------
#power bi filtering and calculated measures


#calculated Measures
***Revenue by year
2021 revenue = 
SUMX(FILTER('max data 4-3', YEAR('max data 4-3'[date]) = 2021), 'max data 4-3'[revenue])

2021 revenue = 
SUMX(FILTER('Append 21-22', YEAR('Append 21-22'[Date]) = 2021), 'Append 21-22'[Amount])

2022 revenue = 
SUMX(FILTER('max data 4-3', YEAR('max data 4-3'[date]) = 2022), 'max data 4-3'[revenue])

***yoy revenue
21/22 yoy revenue = 'max data 4-3'[2022 revenue]/'max data 4-3'[2021 revenue]-1

***units by year
2021 units = 
SUMX(FILTER('max data 4-3', YEAR('max data 4-3'[date]) = 2021), 'max data 4-3'[units])

2021 units = 
SUMX(FILTER('Append 21-22', YEAR('Append 21-22'[Date]) = 2021), 'Append 21-22'[Quantity])

2022 units = 
SUMX(FILTER('max data 4-3', YEAR('max data 4-3'[date]) = 2022), 'max data 4-3'[units])

***yoy units
21/22 yoy units = 'max data 4-3'[2022 units]/'max data 4-3'[2021 units]-1

--------------------------------------------------------
#power bi filtering

#update to include scheels and outfitter in "wholesale
if [Sales Channel] = "Amazon" then "Amazon"
else if [Sales Channel] = "Salesforce" then "DTC" 
else if [Memo] = "Return Store Credit" then "DTC" 
else if [Price Level] = "No Charge" then "No Charge"
else if [Sales Channel] = "Wholesale" then "Wholesale" 
else if [Price Level] = "Cabelas Canada" then "Wholesale" 
else if Text.Contains([Price Level], "NABA") then "Wholesale" 
else if Text.Contains([Price Level], "Phelps") then "Wholesale"
else if Text.Contains([Price Level], "Wholesale") then "Wholesale" 
else if Text.Contains([Shipping Addressee], "Scheels") then "Wholesale"
else if Text.Contains([Shipping Addressee], "Outfitters") then "Wholesale"
else if [Sales Channel] = "Shopify" and [Date] > #date(2022,8,21) then "Retail"
else if [Sales Channel] = "Shopify" and [Date] <= #date(2022,8,21) then "DTC"
else if [Quantity] > 3 then "Wholesale"
else if [ME SKU] = "eGiftCertificate" then "Gift Certificate"
else if [Price Level] = "Custom" and [Type] = "Cash Sale" then "DTC"
else "shit"