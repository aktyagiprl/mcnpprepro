# mcnpprepro
pre-processing and post-processing python scripts for mcnp files
Following spython cripts are available 
~~~
Markup : 1. Density changer
           This will scale the density of material in all cell by a common factor (f = new/old density). Running MCNP with reduced density is helpful in generating the weight windows in shorter time.
         2. Material change
            This changes the material of the cell(s) as per the requirement. The inputs are to be provided in another file with following format.
~~~ 
