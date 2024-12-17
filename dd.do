


clear all
import excel "Panel_Data.xlsx", clear firstrow
encode Provincia, gen(prov)
encode Delitos, gen(del)
sort del
drop Delitos Provincia
drop if prov==.
save "total.dta", replace
* 42 integridad
keep if inlist(del,  5, ///  Abandono seguido de muerte
	20,  ///  Abuso sexual agravado por acceso carnal
	22, /// Abuso sexual cometido contra un menor de 18 años, aprovechando la situacion de convivencia preexistente con el mismo
	31, /// Abuso sexual seguido de muerte
	63, /// femicidio
	60, /// Estupro
	61, /// Estupro agravado
	65, /// homicidio criminis causa
	67, /// homicidio calificado
	68, /// Homicidio calificado a miembros de seguridad, policial o penitenciaria
	69, /// Homicidio calificado por el vinculo
	70, /// Homicidio con el proposito de causar sufrimiento a una persona con la que se mantiene o ha mantenido una relacion
	71, /// Homicidio con ensañamiento, alevosia, insidia
	78, /// Homicidio por placer, codicia, odio racial o religioso
	79, /// Homicidio por precio o promesa remuneratoria
	80, /// Homicidio premeditado
	83, /// Homicidio simple
	84, /// Homicidio utilizando medio catastrofico
	85, /// Infanticidio
	95, /// Lesiones gravisimas calificadas
	103, /// Promocion o facilitacion de la corrupcion de menores calificada
	119) /// Violacion calificada

collapse (sum) Valor, by(Año prov)
save "collapsed.dta", replace


clear all
set more off
cd "/Users/federicolopez/Library/CloudStorage/OneDrive-Personal/Documents/UDESA/08/APLICADA/PROPUESTA/JURADOS"
* Import the dataset
import excel "panel_delitos_sexuales-.xlsx", firstrow clear

* Define treatment timing
encode Provincia, gen(prov)
destring, replace
xtset prov Año

merge 1:1 Año prov using collapsed.dta

* Step 1: Generate a flag to check if Treated is ever NOT 1 for each province
gen not_always_treated = 0
bysort Provincia (Año): replace not_always_treated = 1 if Treated != 1

* Step 2: Collapse the flag to the provincial level
bysort Provincia (Año): gen drop_unit = sum(not_always_treated)
bysort Provincia (Año): replace drop_unit = drop_unit[_N]

* Step 3: Drop units where drop_unit == 0 (meaning Treated is always 1)
drop if drop_unit == 0

* Step 4: Clean up intermediate variables
drop not_always_treated drop_unit


* Generate variable eventually treated
bys prov: egen eventually=max(year_treated)
replace eventually=1 if eventually!=.
recode eventually (.=0)

* Check if there are never treated (if there are no obs in eventually=0, all the states are eventually treated)
tab eventually 

* Check years when states start to be treated
tab year_treated

/*
* Basic Graph (pre treatment by year)
bysort Año eventually: egen mean=mean(y)
twoway (connected mean Año if even==1 & Año<2018) (connected mean Año if even==0 & Año<2018, lpattern(longdash)), ytitle(Mean Outcome)  xtitle (Year) legend(order(1 "Eventually treated" 2 "Controls")) scheme(sj)


drop mean
drop if Treated==1 & (year<2020)
bysort Año even: egen mean=mean(y)

twoway (connected mean Año if even==1 & Año<2020) (connected mean Año if even==0 & Año<2020, lpattern(longdash)), ytitle(Mean Outcome)  xtitle (Year) legend(order(1 "Eventually treated" 2 "Controls")) scheme(sj)
*/

*ssc install eventdd
*ssc install matsort
*ssc install boottest
/*
local treat_id prov
local time Año
local treatment Treated
local outcome y
local treatment_year year_treated

gen timeToTreat = `time' - `treatment_year'

save temp.dta, replace

eventdd `outcome' i.`time', timevar(timeToTreat) method(fe,cluster(`treat_id'))  graph_op(ytitle("Outcome") xlabel(-5(1)5))
 
* Test the joint significance for leads and lags (CAUTION! the leads are the negative ones and the lags the positive ones).	
estat eventdd

* Test the joint significance for leads and lags using wild bootstrap (importart because there are few observations in some of the dots.
estat eventdd, wboot seed(1234)

* You can choose the number of leads and lags, but you must specify what to do with the remaining ones: accumulate, in range or keep the ones that are balanced.

local treat_id prov
local time Año
local treatment Treated
local outcome Valor
local treatment_year year_treated

eventdd `outcome' i.`time', timevar(timeToTreat) method(fe,cluster(`treat_id')) keepdummies graph_op(ytitle("Outcome") xlabel(-5(1)5)) accum

*/
****************************************
****************************************
****************************************
****************************************
* Basic Graph (pre treatment by year)
bysort Año eventually: egen mean=mean(Valor)
twoway (connected mean Año if even==1 & Año<2018) (connected mean Año if even==0 & Año<2018, lpattern(longdash)), ytitle(Sentencias Condenatorias)  xtitle (Year) legend(order(1 "Eventually treated" 2 "Controls")) scheme(sj)


drop mean
drop if Treated==1 & (year<2019)
bysort Año even: egen mean=mean(Valor)

twoway (connected mean Año if even==1 & Año<2020) (connected mean Año if even==0 & Año<2020, lpattern(dash) lwidth(thin) ), ytitle(Sentencias Condenatorias)  xtitle (Year) legend(order(1 "Eventually treated (5)" 2 "Controls (13)" )  position(4) ring(0) cols(1) textwidth(35) symxsize(5)) 


drop mean
drop if Treated==1 & (year<2021)
bysort Año even: egen mean=mean(Valor)

twoway (connected mean Año if even==1 & Año<2021) (connected mean Año if even==0 & Año<2021, lpattern(longdash)), ytitle(Sentencias Condenatorias)  xtitle (Year) legend(order(1 "Eventually treated" 2 "Controls")) 
****************************************
local treat_id prov
local time Año
local treatment Treated
local outcome Valor
local treatment_year year_treated

gen timeToTreat = `time' - `treatment_year'

save temp.dta, replace

eventdd `outcome' i.`time', timevar(timeToTreat) method(fe,cluster(`treat_id'))  graph_op( ytitle("Sentencias Condenatorias") xlabel(-5(1)3)  
* Test the joint significance for leads and lags (CAUTION! the leads are the negative ones and the lags the positive ones).	
estat eventdd
****************************************