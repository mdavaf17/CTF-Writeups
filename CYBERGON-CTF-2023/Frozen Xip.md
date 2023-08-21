# Forensic


## Frozen Xip

Extract the data and repair it!

https://media.discordapp.net/attachments/758115188796162088/1142977520078168156/Cybergon.jpg?width=634&height=628

---

### Solution

```bash
$ file xipper.PNG 
xipper.PNG: Zip archive data, at least v2.0 to extract, compression method=deflate

$ unzip xipper.PNG
Archive:  xipper.PNG
  inflating: flag.txt

$ cat flag.txt
The woods are lovely, dark and deep / But I have promises to keep / And miles to go before I sleep.
— Robert Frost, “Stopping By Woods on a Snowy Evening"	     	 
      	 		    	    	   	      	  	     	 
	    	 	    	     	 	      	     	      	 
  	 	     	  	      	   		  	      	     
       	  	  	       		      		  	  	     
      	  	      	     	      	       	   		     	    
 	      	  	      	      	      	       	   	  	       
     	   	 	     	    	    	  	     	     	 
	  	       	     	   	    	    		  	   
    		 	       	      	     
                                                                                                                                                                             
```

```bash
$ stegsnow -C flag.txt
CyberGonCTF{Z1pp3R_4nD_573G5n0W}
```




CyberGonCTF{Z1pp3R_4nD_573G5n0W}