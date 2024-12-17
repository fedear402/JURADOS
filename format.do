clear all
cd "/Users/federicolopez/Library/CloudStorage/OneDrive-Personal/Documents/UDESA/08/APLICADA/PROPUESTA/JURADOS"
import excel "panel_delitos_sexuales.xlsx", sheet("2016") firstrow clear

* Stack the regional columns into long format while keeping Año and Delito
stack BuenosAires CABA Catamarca Chaco Chubut Córdoba Corrientes EntreRíos Formosa Jujuy ///
      LaPampa LaRioja Mendoza Misiones Neuquén RíoNegro Salta SanJuan SanLuis ///
      SantaCruz SantaFe SdelEstero TdelFuego Tucumán, into(Año) wide clear

* Rename the generated variable for regions
rename _stack Region

* Label regions based on their position in the stack
label define regions 1 "Buenos Aires" 2 "CABA" 3 "Catamarca" 4 "Chaco" ///
                     5 "Chubut" 6 "Córdoba" 7 "Corrientes" 8 "Entre Ríos" 9 "Formosa" ///
                     10 "Jujuy" 11 "La Pampa" 12 "La Rioja" 13 "Mendoza" 14 "Misiones" ///
                     15 "Neuquén" 16 "Río Negro" 17 "Salta" 18 "San Juan" 19 "San Luis" ///
                     20 "Santa Cruz" 21 "Santa Fe" 22 "Sdel Estero" 23 "Tdel Fuego" 24 "Tucumán"

label values Region regions

* Check the new structure
list Año Delito Region


* Reshape wide to long
reshape long BuenosAires CapitalFederal Catamarca Chaco Chubut Cordoba Corrientes EntreRios Formosa ///
              Jujuy LaPampa LaRioja Mendoza Misiones Neuquen RioNegro Salta SanJuan SanLuis ///
              SantaCruz SantaFe SantiagoDelEstero TierraDelFuego Tucuman, ///
              i(Año Delito) j(Region) string

list