import sys
import os
import urllib

given=sys.argv[1]
dirname=os.getcwd()+"/"+given
os.popen("echo '<script> function myFunction(cbox, pbox) { var checkBox = document.getElementById(cbox); var text = document.getElementById(pbox); if (checkBox.checked == true){ text.style.display = \"block\";} else { text.style.display = \"none\"; }} </script>' > index.html")
os.popen("echo '<body style=\"background-color:Thistle;\">' >> index.html")
os.popen("echo '<h1 style=\"text-align:center\">%s</h1>' >> index.html"%given)
iplist=os.listdir(dirname)
s=1
for d in iplist:
    os.popen("echo '<hr>' >> index.html")
    os.popen("echo '<br>' >> index.html")
    os.popen("echo '<h2 style=\"text-align:center\">%s</h1>' >> index.html"%d)
    
    for path, dirs, png_fls in os.walk(dirname+"/"+d,topdown=True):
        if dirs:
    
            for dt in dirs:
            	chk=dt.split("_")[0].strip()+"-"+str(s)
            	phk=dt.split("_")[1].strip()+"-"+str(s)
            	s=s+1
            	phk="'"+phk+"'"
            	print phk
                os.popen("echo '<h2>%s <input type=\"checkbox\" id=\"%s\" onclick=\"myFunction(&#39;%s&#39;,&#39;%s&#39;)\"></h2>' >> index.html"%(dt.replace('_',':').strip(),phk,urllib.unquote(phk),chk))
                os.popen("echo '<div id=\"%s\" style=\"display:none\">' >> index.html"%chk)
                #os.popen("echo '<script> function myFunction() { var checkBox = document.getElementById(\"%s\"); var text = document.getElementById(\"%s\"); if (checkBox.checked == true){ text.style.display = \"block\";} else { text.style.display = \"none\"; }} </script>' >> index.html"%(phk,chk))
                #os.popen("echo '<script> function myFunction() { var checkBox = document.getElementById(\"%s\"); var text = document.getElementById(\"%s\"); if (checkBox.checked == true){ text.style.display = \"block\";} else { text.style.display = \"none\"; }}</script>' >> index.html")
                for fl in  os.listdir(path+"/"+dt):
                    pngfl=path+"/"+dt+"/"+fl
                    os.popen("echo '<a href=%s><img src=\"%s\" alt=\"%s\" width=\"550\" height=\"300\"></a>' >> index.html"%(pngfl,pngfl,pngfl))
                os.popen("echo '</div>' >> index.html")
            
                #if s ==3:
                #	exit(1)

                

