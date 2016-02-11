import os,re,subprocess
from xml.dom.minidom import parse
import xml.dom.minidom

def upload(path):
        global index
        index=index+1
        # Open XML document using minidom parser
        DOMTree = xml.dom.minidom.parse(path)
        proj = DOMTree.documentElement
        ai=proj.getElementsByTagName('artifactId')[0].childNodes[0].data
        gi=proj.getElementsByTagName('groupId')[0].childNodes[0].data
        ve=proj.getElementsByTagName('version')[0].childNodes[0].data
        ja=path.replace(".pom",".jar")
        ex= os.path.isfile(ja)
        #print ("name : " + str(ai)+ " group : " + str(gi)+" version : " + str(ve)+ " jar:"+ja+" "+str(ex))
        if ex:
           comm="C:\\maven\\bin\\mvn deploy:deploy-file -DgroupId="+gi+" -DartifactId="+ai+" -Dversion="+ve+" -Dpackaging=jar \"-Dfile="+ja+"\" -DgeneratePom=true -Durl=http://lpr462:8080/nexus-2.5/content/repositories/ESBrepository/ -DrepositoryId=ESBrepository "
           print (str(index)+" ***"+str(subprocess.call(comm,shell=True))+" "+comm)
        else:
           print (str(index)+" ***1 not found jar"+ja)     

def Scan(PathFor,Pattern):
        #list = []
        #print('start scan:'+PathFor)
        for file in os.listdir(PathFor):
            #print("Scan for:"+PathFor +" file"+ file  )
            path = os.path.join(PathFor, file)
            
            if not os.path.isdir(path):
                #list.append(path)
               # print("Analise for file:"+path+ " MAtch result:"+str(re.match(Pattern,path)))
                if re.match(Pattern,file):
                        #print(PathFor+" *** "+file )
                        upload(path)
            else:
                #list.append(GetListForBackup(path))
                Scan(path,Pattern)
        return #list


index=0
Scan("C:\\pathtom2",".*pom$")
print('finished')
