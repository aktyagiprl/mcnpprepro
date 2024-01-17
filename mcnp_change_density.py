import os                                                                       
import shutil                                                                   
def mcnp_change_density():
    # input deck open. Get the name of file and change density factor f          
    mcnp_inp = input("Enter the name of the file for which density is to be changed \n")
    mcnp_out = mcnp_inp+"_den_by"+f                                                 
    print("\ndensity factor f=new/old density.\n") 
    f = input("e.g. if new density is 4 and old density is 8 f= 4/8 = 0.5 : ")
    shutil.copyfile(mcnp_inp,mcnp_out)                                              
    f = float(f)                                                                    
    # input deck close                                                              
    
    # remove old log file                                                           
    print("removing old log file")                                                  
    logfile = "den_changelog.txt" # log file for changes                           
    if (os.path.isfile(logfile) == 'True'):
        os.remove(logfile)                   

    print("Changing density")                                                       
    file1 = open(mcnp_inp, 'r')
    cells=[]
    count = 0
    material = []
    old_density = []
    new_density = []
    for line in file1:
        if not line.strip():
            break
        else:
            count += 1
            #print("Line{}: {}".format(count, line.strip()))
            tmp = line[0:5]
            if "\t" in tmp or "c" in tmp or " " in tmp or "C" in tmp:
                pass
            else:                                                               
            #print(count,"Cell")                                            
                tmp1 = line.split()                                             
                cell = tmp1[0]                                                 
                matno = tmp1[1]                                                
                #print(matno)
                material.append(matno) 
                cells.append(cell)
                if matno == "0": # this is vacuum no change                     
                    old_str=(cell+" "+matno)                                    
                    new_str=(cell+" "+matno)                                    
                    old_density.append(matno)
                    with open(logfile,'a') as log:                              
                        log.write(old_str+" to "+new_str+" \n")                 
                    #print("No change")                                         
                else:                              
                    mat_oden = tmp1[2]                                          
                    old_density.append(mat_oden)
                    mat_nden = round(float(mat_oden)*f,7)                       
                    new_density.append(mat_nden)
                    old_str=(cell+" "+matno+" "+mat_oden)                       
                    new_str=(cell+" "+matno+" "+str(mat_nden))                  
                    with open(logfile,'a') as log:                              
                        log.write(old_str+" to "+new_str+" \n")                 
                    with open(mcnp_out, 'r') as file:                           
                        data = file.read()                                      
                        data = data.replace(old_str, new_str)                   
                    with open(mcnp_out, 'w') as file:                           
                        file.write(data)                                        
                    #print(old_str," to ",new_str)                              
    print("the change log is written to  :"+logfile+"\n")                           

    print("\nThe output file with new density is :  "+mcnp_out+"\n")    
    return cells, material, old_density, new_density
    file1.close()
    file.close
