import os 
import getpass

os.system("tput setaf 3")
print("\n\t\t******************Welcome To My Automation Tool*******************")
os.system("tput setaf 7")
print("\n\t------------------------------------------------------------------------------------------------------")

passwd = getpass.getpass("Enter your password : ")

if passwd == "onkar":
    print("\n\t\t-----------------> you have sucessfully logged in <--------------------------")
else:
    print("Wrong password")
    exit()

os.system("tput setaf 3")
print("\n\n\t 1)-> Linux Automation   2)-> Hadoop Automation  3)-> AWS Cloud Automation   4)-> Docker Automation")
os.system("tput setaf 7")
r = input("\n\t\tWhich Automation Would You Like To Choose ?: ----> ")

if int(r) == 1:
 ws = input("\n\t\t\tSelect Your Workspace(Local/Remote) : ")

 os.system("tput setaf 3")
 print("\n\t--------------**-------------------Linux Automation Console--------------------**---------------")
 os.system("tput setaf 7")
 if ws == "Remote":
      ip = input("\n\t\t\tEnter Remote IP: ")
 while True:
       print("\n\n************************************** Menu List ************************************************")
       print("""
\n\t\t
Press 1: Show Date
press 2: Show Calender
press 3: Run any Linux Command
press 4: Create Logical Partiton
press 5: Mount The LVM Partition
press 6: Extend / Decrease the Size of Logical Volume
press 7: Add Hard Disks To Volume Group Dynamically 
press 8: Configure A Web Server
press 9: Capture Data Packets
press 10: Exit
""")
  
       ch = input("\n\t\t\t\tEnter your choice: ")
       print("\n\t-----------------------------------------------------------------------------------")


       if ws == "Local":

            if int(ch) == 1:
                print("\n\t\t\tShowing the Date")
                print("---------------------------------------------------------------------------------")
                os.system('date')
            elif int(ch) == 2:
                print("\n\t\t\tShowing the Calender")
                print("---------------------------------------------------------------------------------")
                os.system('cal')
            elif int(ch) == 3:
                cmd = input("Enter your Linux Command :")
                os.system('sudo {}'.format(cmd))
            elif int(ch) == 4:    
                dev = input("\t\t\t\tEnter Your Device Name : ")
                os.system('pvcreate {}'.format(dev))
                print("\t\t\tSucessfully Created pv : {}".format(dev))
                os.system('pvdisplay {}'.format(dev))
                print("------------------------------------------------------")
                vg = input("\t\t\t\tEnter The Name of Volume Group : ")
                os.system('vgcreate {}  {}'.format(vg , dev))
                os.system('vgdisplay {}'.format(vg))
                print("------------------------------------------------------")
                lv = input("\t\t\t\tEnter Your Logical Volume Name : ")
                sz = input("\t\t\t\tEnter the Size of Partition you want : ")
                os.system('lvcreate --size {} --name {} {}'.format(sz , lv ,vg))
                os.system("lvdisplay {}/{}".format(vg ,lv))
                print("------------------------------------------------------")
                os.system('mkfs.ext4 /dev/{}/{}'.format(vg , lv))
                print("\t\t\tLogical Volume Sucessfully Formatted ..")
            elif int(ch) == 5:
                fold = input("\t\tEnter your folder Name which you want to mount on LVM Parition : ")
                vg = input("\t\tEnter Volume Group Name : ")
                lv = input("\t\tEnter Logical Volume Name : ")
                os.system("mount /dev/{}/{}  {}".format(vg , lv , fold))
                print("\t\t\tSucessfully Mounted the LVM Partiton ..")
                os.system('df -hT')
            elif int(ch) == 6:
                ex = input("\n\tDo you want to extend/reduce the Size of LVM? : ")
                if ex == "extend":
                    ex = input("\n\t\tHow much you want to extend? : ")
                    vg = input("\t\tEnter Your Volume Group Name : ")
                    lv = input("\t\tEnter Your Logical Volume Name : ")
                    os.system('ssh {} lvextend --size {} /dev/{}/{}'.format(ip , ex , vg , lv))
                    print("\t\t\tSucessfully Extended the Size of LVM Partition ")
                    os.system('ssh {} resize2fs  /dev/{}/{}'.format(ip , vg ,lv))
                    os.system('ssh {} df -hT'.format(ip))
                    os.system('df -hT')
                elif ex == "reduce":
                    ex = input("\n\t\tHow much you want to reduce? : ")
                    vg = input("\t\tEnter Your Volume Group Name : ")
                    lv = input("\t\tEnter Your Logical Volume Name : ")
                    os.system('ssh {} lvreduce --size {} /dev/{}/{}'.format(ip , ex , vg , lv))
                    print("\t\t\tSucessfully reduced the Size of LVM Partition ")
                    os.system('ssh {} resize2fs  /dev/{}/{}'.format(ip , vg ,lv))
                    os.system('ssh {} df -hT'.format(ip))
                    os.system('df -hT') 

            elif int(ch) == 7:
                nw = input("\t\tEnter the Name of Device you want to Add in Volume Group (LVM) : ")
                vg = input("\t\tEnter Volume Group Name : ")
                os.system('vgextend {} {}'.format(vg , nw))
                print("\t\tDynamically Added Extra Storage or Volume in LVM")
                print("-------------------------------------------------------------------")
                os.system('vgdisplay {}'.format(vg))

            elif int(ch) == 8:
                os.system('yum install httpd -y')
                os.system('setenforce 0')
                os.system('systemctl start httpd')


            elif int(ch) == 9:
                nn = input("\t\tEnter Your System Network Card Name : ")
                ok = input("\t\tEnter Type of Protocol : ")
                pn = input("\t\tEnter Port Number from which Data Packets are coming : ")
                os.system('tcpdump -i {} {} port {} -n -X'.format(nn , ok , pn))
     
            elif int(ch) == 10:
                break


       elif ws == "Remote":
            

            if int(ch) == 1:
                print("\n\t\t\tShowing the Date")
                print("---------------------------------------------------------------------------------")
                os.system('ssh {} date'.format(ip))
            elif int(ch) == 2:
                print("\n\t\t\tShowing thr Calender")
                print("---------------------------------------------------------------------------------")
                os.system('ssh {} cal'.format(ip))
            elif int(ch) == 3:
                cmd = input("Enter your Linux Command :")
                os.system('ssh {} sudo {}'.format(ip , cmd))

            elif int(ch) == 4:
                dev = input("\t\t\t\tEnter Your Device Name : ")
                os.system('ssh {} pvcreate {}'.format(ip , dev))
                print("\t\t\tSucessfully Created pv : {}".format(dev))
                os.system('ssh {} pvdisplay {}'.format(ip , dev))
                print("------------------------------------------------------")
                vg = input("\t\t\t\tEnter The Name of Volume Group : ")
                os.system('ssh {} vgcreate {}  {}'.format(ip , vg , dev))
                os.system('ssh {} vgdisplay {}'.format(ip , vg))
                print("------------------------------------------------------")
                lv = input("\t\t\t\tEnter Your Logical Volume Name : ")
                sz = input("\t\t\t\tEnter the Size of Partition you want : ")
                os.system('ssh {} lvcreate --size {} --name {} {}'.format(ip , sz , lv ,vg))
                os.system("ssh {} lvdisplay {}/{}".format(ip , vg ,lv))
                print("------------------------------------------------------")
                os.system('ssh {} mkfs.ext4 /dev/{}/{}'.format(ip ,vg , lv))
                print("\t\t\tLogical Volume Sucessfully Formatted ..")
            elif int(ch) == 5:
                fold = input("\t\tEnter your folder Name which you want to mount on LVM Parition : ")
                vg = input("\t\tEnter Volume Group Name : ")
                lv = input("\t\tEnter Logical Volume Name : ")
                os.system("ssh {} mount /dev/{}/{}  {}".format(ip , vg , lv , fold))
                print("\t\t\tSucessfully Mounted the LVM Partiton ..")
                os.system('ssh {} df -hT'.format(ip))
            elif int(ch) == 6:
                ex = input("\n\tDo you want to extend/reduce the Size of LVM? : ")
                if ex == "extend":
                    ex = input("\n\t\tHow much you want to extend? : ")
                    vg = input("\t\tEnter Your Volume Group Name : ")
                    lv = input("\t\tEnter Your Logical Volume Name : ")
                    os.system('ssh {} lvextend --size {} /dev/{}/{}'.format(ip , ex , vg , lv))
                    print("\t\t\tSucessfully Extended the Size of LVM Partition ")
                    os.system('ssh {} resize2fs  /dev/{}/{}'.format(ip , vg ,lv))
                    os.system('ssh {} df -hT'.format(ip))
                    os.system('ssh {} df -hT'.format(ip))
                elif ex == "reduce":
                    ex = input("\n\t\tHow much you want to reduce? : ")
                    vg = input("\t\tEnter Your Volume Group Name : ")
                    lv = input("\t\tEnter Your Logical Volume Name : ")
                    os.system('ssh {} lvreduce --size {} /dev/{}/{}'.format(ip , ex , vg , lv))
                    print("\t\t\tSucessfully Reduced the Size of LVM Partition ")
                    os.system('ssh {} resize2fs  /dev/{}/{}'.format(ip , vg ,lv))
                    os.system('ssh {} df -hT'.format(ip))
                    os.system('ssh {} df -hT'.format(ip))
            elif int(ch) == 7:
                nw = input("\t\tEnter the Name of Device you want to Add in Volume Group (LVM) : ")
                vg = input("\t\tEnter Volume Group Name : ")
                os.system('ssh {} vgextend {} {}'.format(ip , vg , nw))
                print("\t\tDynamically Added Extra Storage or Volume in LVM")
                print("-------------------------------------------------------------------")
                os.system('ssh {} vgdisplay {}'.format(ip , vg))

            elif int(ch) == 8:
                os.system('ssh {} yum install httpd -y'.format(ip))
                os.system('ssh {} setenforce 0'.format(ip))
            
            
            elif int(ch) == 9:
                nn = input("\t\tEnter Your System Network Card Name : ")
                ok = input("\t\tEnter Type of Protocol : ")
                pn = input("\t\tEnter Port Number from which Data Packets are coming : ")
                os.system('tcpdump -i {} {} port {} -n -X'.format(nn , ok , pn))
            
       elif int(ch) == 10:
           break
    
              


elif int(r) == 2:
 os.system("tput setaf 3")
 print("\n\t--------------**------------------Hadoop Automation Console---------------------**----------")
 os.system("tput setaf 7")
 while True:
       print("\n\n************************************** Menu List ************************************************")
       print("""
\n\t\t
Press 1: Install Hadoop Requirements
press 2: Configure Name Node
press 3: Configure Data Node
press 4: Configure Hadoop Client
press 5: Limit The Data Node Storage
press 6: Upload Data To Hadoop Cluster
press 7: Read Client Data from Hadoop Cluster
press 8: Delete Client Data
press 9: Stop Name Node
press 10: Stop Data Node
press 11: Exit
""")
       ch = input("\n\t\t\t\tEnter your choice : ") 
       print("\n\t-----------------------------------------------------------------------------------")

       if int(ch) == 1:
           os.system('rpm -ivh /root/jdk-8u171-linux-x64.rpm')
           os.system('rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm  --force')
           print("\n\tHadoop Requirements Sucessfully Installed In Name Node")
           print("\n\t---------------------------------------------------------------------")
           ab = input("Enter Your Data Node IP :")
           os.system('ssh {} rpm -ivh jdk-8u171-linux-x64.rpm'.format(ab))
           os.system('ssh {} rpm -ivh  hadoop-1.2.1-1.x86_64.rpm  --force'.format(ab))
           print("\n\tHadoop Requirements Sucessfully Installed In Data Node")
           print("\n\t---------------------------------------------------------------------")
           bb = input("Enter Your Client Node IP :")
           os.system('ssh {} rpm -ivh jdk-8u171-linux-x64.rpm'.format(bb))
           os.system('ssh {} rpm -ivh  hadoop-1.2.1-1.x86_64.rpm  --force'.format(bb))
           print("\n\tHadoop Requirements Sucessfully Installed In Client Node")
           print("\n\t---------------------------------------------------------------------")
           
       elif int(ch) == 2:
           dir = input("\n\t\tEnter your Name Node directory name : ")
           print("\t\t\t\tConfiguring hdfs-site.xml file ............")
           os.system("echo -e '<?xml version=\"1.0\"?> \n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' > /root/hdfs-site.xml")
           os.system("echo -e '\n<!-- Put site-specific property overrides in this file. -->' >> /root/hdfs-site.xml")
           os.system('echo -e "\n<configuration>" >> /root/hdfs-site.xml')
           os.system('echo -e "\n<property>" >> /root/hdfs-site.xml')
           os.system('echo -e "<name>dfs.name.dir</name>" >> /root/hdfs-site.xml')
           os.system('echo -e "<value>{}</value>" >> /root/hdfs-site.xml'.format(dir))
           os.system('echo -e "</property>" >> /root/hdfs-site.xml')
           os.system('echo -e "\n</configuration>" >> /root/hdfs-site.xml')
           os.system('rm -rf /etc/hadoop/hdfs-site.xml')
           os.system('cp  /root/hdfs-site.xml  /etc/hadoop')
           os.system('rm -rf /root/hdfs-site.xml')
           print("\n\tFormatting the Name Node ..............................")
           print()
           os.system('hadoop namenode -format')
           print()
           print()
           nip = input("Enter Name Node IP :")
           print("\t\t\t\tConfiguring core-site.xml file ...........")
           os.system("echo -e '<?xml version=\"1.0\"?> \n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' > /root/core-site.xml")
           os.system('echo -e "\n<!-- Put site-specific property overrides in this file. -->" >> /root/core-site.xml')
           os.system('echo -e "\n<configuration>" >> /root/core-site.xml')
           os.system('echo -e "\n<property>" >> /root/core-site.xml')
           os.system('echo -e "<name>fs.default.name</name>" >> /root/core-site.xml')
           os.system('echo -e "<value>hdfs://{}:9001</value>" >> /root/core-site.xml'.format(nip))
           os.system('echo -e "</property>" >> /root/core-site.xml')
           os.system('echo -e "\n</configuration>" >> /root/core-site.xml')
           os.system('rm -rf /etc/hadoop/core-site.xml')
           os.system('cp  /root/core-site.xml  /etc/hadoop')
           os.system('rm -rf /root/core-site.xml')
           print("\n\t--------------------------------------------------------------")
           print("\n\t Starting Hadoop Name Node Services .............................")
           os.system('hadoop-daemon.sh start namenode') 
           os.system('jps')

       elif int(ch) == 3:
           dip = input("\t\tEnter Data Node IP : ")
           dio = input("\t\tEnter your Data Node directory name : ")
           print("\t\t\t\tConfiguring hdfs-site.xml file ............")
           os.system("echo -e '<?xml version=\"1.0\"?> \n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' > /root/hdfs-site.xml")
           os.system("echo -e '\n<!-- Put site-specific property overrides in this file. -->' >> /root/hdfs-site.xml")
           os.system('echo -e "\n<configuration>" >> /root/hdfs-site.xml')
           os.system('echo -e "\n<property>" >> /root/hdfs-site.xml')
           os.system('echo -e "<name>dfs.data.dir</name>" >> /root/hdfs-site.xml')
           os.system('echo -e "<value>{}</value>" >> /root/hdfs-site.xml'.format(dio))
           os.system('echo -e "</property>" >> /root/hdfs-site.xml')
           os.system('echo -e "\n</configuration>" >> /root/hdfs-site.xml')
           os.system('scp  /root/hdfs-site.xml  {}:/etc/hadoop'.format(dip))
           os.system('rm -rf /root/hdfs-site.xml')
           niq = input("Enter Name Node IP :")
           print("\t\t\t\tConfiguring core-site.xml file ...........")
           os.system("echo -e '<?xml version=\"1.0\"?> \n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' > /root/core-site.xml")
           os.system('echo -e "\n<!-- Put site-specific property overrides in this file. -->" >> /root/core-site.xml')
           os.system('echo -e "\n<configuration>" >> /root/core-site.xml')
           os.system('echo -e "\n<property>" >> /root/core-site.xml')
           os.system('echo -e "<name>fs.default.name</name>" >> /root/core-site.xml')
           os.system('echo -e "<value>hdfs://{}:9001</value>" >> /root/core-site.xml'.format(niq))
           os.system('echo -e "</property>" >> /root/core-site.xml')
           os.system('echo -e "\n</configuration>" >> /root/core-site.xml')
           os.system('scp  /root/core-site.xml  {}:/etc/hadoop'.format(dip))
           os.system('rm -rf /root/core-site.xml')
           print("\n\t--------------------------------------------------------------")
           print("\n\t Starting Hadoop Data Node Services .............................")
           os.system('ssh {} hadoop-daemon.sh start datanode'.format(dip))
           os.system('ssh {} jps'.format(dip))
           print("\n\t--------------------------------------------------------------")
           print("\n\t Showing Hadoop Cluster Report ..............................")
           os.system('ssh {} hadoop dfsadmin -report'.format(dip))

      
       elif int(ch) == 4:
           yu = input("Enter Name Node IP : ")
           print("\t\t\t\tConfiguring core-site.xml file ...........")
           ip = input("\n\t\tEnter Client IP : ")
           os.system("echo -e '<?xml version=\"1.0\"?> \n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' > /root/core-site.xml")
           os.system('echo -e "\n<!-- Put site-specific property overrides in this file. -->" >> /root/core-site.xml')
           os.system('echo -e "\n<configuration>" >> /root/core-site.xml')
           os.system('echo -e "\n<property>" >> /root/core-site.xml')
           os.system('echo -e "<name>fs.default.name</name>" >> /root/core-site.xml')
           os.system('echo -e "<value>hdfs://{}:9001</value>" >> /root/core-site.xml'.format(yu))
           os.system('echo -e "</property>" >> /root/core-site.xml')
           os.system('echo -e "\n</configuration>" >> /root/core-site.xml')
           os.system('scp  /root/core-site.xml  {}:/etc/hadoop'.format(ip))
           print("\t\tHadoop Client Sucessfully Configured.........")

       elif int(ch) == 5:
           ip = input("\n\tEnter Data Node IP : ")
           si = input("\n\tDo You want to extend/reduce Data Node Storage? : ")
           if si == "extend":
               os.system('ssh {} df -hT'.format(ip))
               ex = input("\n\t\tHow much you want to extend? : ")
               vg = input("\t\tEnter Your Volume Group Name : ")
               lv = input("\t\tEnter Your Logical Volume Name : ")
               os.system('ssh {} lvextend --size {} /dev/{}/{}'.format(ip , ex , vg , lv))
               print("\t\t\tSucessfully Extended the  Data Node Storage ")
               os.system('ssh {} resize2fs  /dev/{}/{}'.format(ip , vg ,lv))
               print("------------------------------------------------------------")
               os.system('ssh {} df -hT'.format(ip))
           elif si == "reduce":
               os.system('ssh {} df -hT'.format(ip))
               ex = input("\n\t\tHow much you want to reduce? : ")
               vg = input("\t\tEnter Your Volume Group Name : ")
               lv = input("\t\tEnter Your Logical Volume Name : ")
               os.system('ssh {} lvextend --size {} /dev/{}/{}'.format(ip , ex , vg , lv))
               print("\t\t\tSucessfully Reduced Data Node Storage ")
               os.system('ssh {} resize2fs  /dev/{}/{}'.format(ip , vg ,lv))
               print("------------------------------------------------------------")
               os.system('ssh {} df -hT'.format(ip))
       
       elif int(ch) == 6:
           ci = input("\t\tEnter Client IP : ")
           fiz = input("\t\tEnter The Name of File You want to upload on Hadoop Cluster : ")
           os.system('ssh {} hadoop fs -put {} /'.format(ci , fiz))
           print("\t\t\tFile Sucessfully Uploaded .......................")
           os.system('ssh {} hadoop fs -ls /'.format(ci))
       
       elif int(ch) == 7:
           co = input("\t\tEnter Client IP : ")
           fii = input("\t\tEnter Your File Name : ")
           os.system('ssh {} hadoop fs -cat /{}'.format(co , fii))

       elif int(ch) == 8:
           ty = input("\t\tEnter Client IP : ")
           foi = input("\t\tEnter Your File Name : ")
           os.system('ssh {} hadoop fs -rm /{}'.format(ty , foi))
           print("\t\tSucessfully Deleted File {} ".format(foi))
       
       elif int(ch) == 9:
           os.system('hadoop-daemon.sh stop namenode')
           os.system('jps')

       elif int(ch) == 10:
           ip = input("\n\tEnter Data Node IP : ")
           os.system('ssh {} hadoop-daemon.sh stop datanode'.format(ip))
           os.system('ssh {} jps'.format(ip))
       
       elif int(ch) == 11:
           break




elif int(r) == 3:
 os.system("tput setaf 3")
 print("\n\t-----------------**----------------AWS Automation Console---------------------**---------------")
 os.system("tput setaf 7")
 while True:
       print("\n\n************************************** Menu List ************************************************")
       print("""
\n\t\t
Press 1: Login To AWS Cloud
press 2: Create a key Pair
press 3: Create a Security Group
press 4: Set Up Inbound Rule 
press 5: Launch an EC2 Instance
press 6: Create an EBS Volume
press 7: Attach EBS Volume to EC2 Instance
press 8: Configure A Webserver Inside EC2 Instance
press 9: Static Partitioning & Mounting Document Root(/var/www/html) To EBS  
press 10: Create S3 Bucket 
press 11: Upload the Content to S3 Bucket
press 12: Create Cloud Front Distribution
press 13: Delete A Key pair
press 14: Detach EBS Volume from  EC2 Insatnce
presss 15: Shut Down EC2 Instance
press 16: Terminate EC2 Instance
press 17: Delete Content From S3 Bucket
press 18: Delete S3 Bucket
press 19: Delete Security Group
press 20: Exit
""")
       ch = input("\n\t\t\t\tEnter your choice : ")
       print("\n\t-----------------------------------------------------------------------------------")
       if int(ch) == 1:
        
           os.system('aws configure')
           print("\n\t\t\t---------------->You Have Sucessfully Logged In AWS Cloud<----------------------------")
     
       elif int(ch) == 2:
           nm = input("Enter Key Name : ")
           pq = nm
           os.system('aws ec2 create-key-pair --key-name {} --query "KeyMaterial" > {}.pem'.format(nm ,pq))
           os.system('chmod 0400 {}.pem'.format(nm))
           print("\n\tSucessfully Created the Key Pair") 
        
       elif int(ch) == 3:
           p = input("Enter Security Group Name : ")
           q = input("Give Description of Security Group : ")
           os.system('aws ec2 create-security-group --group-name {} --description "{}"'.format(p , q))
           print("\n\t----------------------------------------------------------------------------")
           
       elif int(ch) == 4:    
           print("\n\tJust Provide Some IP Permesssions  Below ...")
           sg = input("\n\tEnter Your Security Group ID : ")
           pt = input("\tEnter Port No : ")
           io = input("\tEnter Your Protocol Name : ")
           cb = input("\tEnter CIDR Block Value : " )
           os.system('aws ec2 authorize-security-group-ingress --group-id {} --protocol {} --port {} --cidr {}'.format(sg , io , pt , cb))
           
           print("\n\tSucessfully Set Up The Inbound Rule ......")  
       
       elif int(ch) == 5:
           s = input("Enter Your Security Group ID :")
           t = input("Enter Your Instance Type :")
           k = input("Enter Your Key Name :")
           ami = input("Enter AMI ID : ")
           c = input("How many Instances You want To Launch? :")
           os.system("aws ec2 run-instances --security-group-ids {} --instance-type {} --image-id {}  --key-name {} --count {} ".format(s , t , ami , k , c))
         
       elif int(ch) == 6:
           vt = input("Enter Your Volume Type(gp2/io1/io2/sc1/st1/standard) :")
           siz = input("How Much Amount of EBS You want :")
           az = input("Enter Your Availability Zone :")
           os.system('aws ec2 create-volume --volume-type {} --size {} --availability-zone {}'.format(vt , siz , az))
       
       elif int(ch) == 7:
           vid = input("Enter Your Volume ID :")
           id = input("Enter Your Instance ID :")
           os.system('aws ec2 attach-volume --volume-id {} --instance-id {} --device /dev/sdf'.format(vid , id))

       elif int(ch) == 8:
           ip = input("Enter Your Instance Public IP :")
           ky = input("Enter Private Key Name For Login Into EC2 : ")
           os.system('ssh -l ec2-user {} -i {}.pem sudo yum install httpd -y'.format(ip , ky))
           os.system('ssh -l ec2-user {} -i {}.pem sudo systemctl start httpd'.format(ip , ky))
           os.system('ssh -l ec2-user {} -i {}.pem sudo systemctl enable httpd'.format(ip , ky))
           os.system('ssh -l ec2-user {} -i {}.pem sudo systemctl status httpd'.format(ip , ky))
           print("\n\t\tWebserever Configured Sucessfully ..............................")
      
       elif int(ch) == 9:
           ip = input("Enter Public IP of EC2 : ")
           ky = input("Enter Private Key Name For Login Into EC2 : ")
           os.system('ssh -l ec2-user {} -i {}.pem sudo fdisk -l'.format(ip , ky))
           na = input("\n\tEnter Partition Name To be Mounted on /var/www/html : ")
           os.system('ssh -l ec2-user {} -i {}.pem sudo mkfs.ext4 {}'.format(ip , ky , na))
           os.system('ssh -l ec2-user {} -i {}.pem sudo mount {}  /var/www/html'.format(ip , ky , na))
           print("------------------------------------------------------------------")
           os.system('ssh -l ec2-user {} -i {}.pem sudo df -hT'.format(ip , ky))
           print("\n\tEBS Volume Mounted Sucessfully........................")
       
       elif int(ch) == 10:
           sn = input("Give Name to Your S3 Bucket : ")
           rn = input("Enter Your Region Name : ")
           rs = rn
           os.system('aws s3api create-bucket --bucket {} --region {} --create-bucket-configuration LocationConstraint={}'.format(sn , rn , rs)) 
           print("--------------------------------------------------------------------------")

       elif int(ch) == 11:    
           print("\n\tProvide The Details Given Below To Upload Your Content In S3 Bucket")
           fi = input("Enter Your File/Folder/Images Name that You want to Uplaod :")
           se = input("Enter your S3 Bucket Name : ")
           pe = input("Enter the permissions for your content in S3 : ")
           os.system('aws s3 cp  {}  s3://{}/  --acl {}'.format(fi , se , pe))

       elif int(ch) == 12:
           wq = input("Enter Your S3 Bucket Name :")
           os.system('aws cloudfront create-distribution  --origin-domain-name {}.s3.amazonaws.com'.format(wq))
      
       elif int(ch) == 13:
           kn = input("Enter Your Key Name : ")
           os.system('aws ec2 delete-key-pair --key-name {}'.format(kn))
      
       elif int(ch) == 14:
           vid = input("Enter ID of EBS To be Detached : ")
           os.system('aws ec2 detach-volume --volume-id {}'.format(vid))
           print("\n\tEBS Volume Detached Sucessfully.......................")

       elif int(ch) == 15:
           id = input("Enter ID of EC2 Instance To be Terminated : ")
           os.system('aws ec2 terminate-instances --instance-ids {}'.format(id))
       elif int(ch) == 16:
           id = input("Enter ID of EC2 Instance To be Terminated : ")
           os.system('aws ec2 terminate-instances --instance-ids {}'.format(id))
       elif int(ch) == 17:
           on = input("Enter The Name of Object You want to Delete from S3 :")
           sn = input("Enter S3 Bucket Name : ")
           os.system('aws s3 rm s3://{}/{}'.format(sn , on))
       elif int(ch) == 18:
           sn = input("Enter S3 Bucket Name that You want To Delete : ")
           os.system('aws s3api delete-bucket --bucket {} --region ap-south-1'.format(sn))
       elif int(ch) == 19:
           sg = input("Enter ID of Security Group that you want to Delete : ")
           os.system('aws ec2 delete-security-group --group-id {}'.format(sg))
       elif int(ch) == 20:
           break


           
elif int(r) == 4:
 os.system("tput setaf 3")   
 print("\n\t------------------**------------Docker Automation Console-------------------**-----------------")
 os.system("tput setaf 7")
 while True:
       print("\n\n************************************** Menu List ************************************************")
       print("""
\n\t\t
Press 1: Install Docker Tool
press 2: Download Docker Images
press 3: Launch a Webserver Inside Docker Container
press 4: Show the Information of Running Container
press 5: Show Downloaded Docker Images
press 6: Launch a Python Interpreter Inside Docker Container
press 7: Machine Learning Prediction From Dataset
press 8: Remove/Stop the Container
press 9: Delete Docker Images
press 10: Exit
""")
       ch = input("\n\t\t\t\tEnter your choice : ")
       print("\n\t--------------------------------------------------------------------------")      
       if int(ch) == 1:
           os.system('dnf install docker-ce --nobest -y')
       elif int(ch) == 2:
           img = input("Which Docker Image You Want To Download? : ") 
           os.system('docker pull {}'.format(img))
       elif int(ch) == 3:
           nk = input("Enter The Image Name for Launching the Container :")
           mg = input("Give Name to the Container :")
           os.system('docker create -it -p 9091:80 --name {} {}'.format(mg , nk))
           os.system('docker start {}'.format(mg))
           os.system('docker ps')
           os.system('docker exec -it {} yum install httpd -y'.format(mg))
           os.system('sudo docker cp /root/home.html {}:/var/www/html/'.format(mg))
           print("--------------------------------------------------------------")
           print("Checking the Status of Webserver Services .....")
           os.system('docker exec -it {} /usr/sbin/httpd'.format(mg))
           os.system('docker exec -it {} /usr/sbin/httpd'.format(mg))
       
       elif int(ch) == 4:
           mn = input("Enter Your Container Name : ")
           os.system('docker inspect {}'.format(mn))
       
       elif int(ch) == 5:
           os.system('docker images')

       elif int(ch) == 6:
           hn = input("Enter Name of Running Docker Container : ")
           os.system('docker start {}'.format(hn))
           os.system('docker exec -it {} yum install python3 -y'.format(hn))
           os.system('docker exec -it {} python3'.format(hn))
       
       elif int(ch) == 7:
           print("\n\t\tAutomating Integration of Machine Learning &  Docker")
           hn = input("\nEnter Name of Running Docker Container : ")
           os.system('docker exec -it {} pip3 install sklearn'.format(hn))
           os.system('docker exec -it {} pip3 install pandas'.format(hn))
           os.system('docker exec -it {} pip3 install joblib'.format(hn))
           os.system('docker cp /root/salarydata.csv {}:/'.format(hn))
           os.system('docker cp /root/model.py {}:/'.format(hn))
           print("\n\t\t---------------Prediction Automation----------------------------------")
           os.system('docker exec -it {} python3 model.py'.format(hn))
           

      
       elif int(ch) == 8:
           ii = input("Enter Name of Docker Container :")
           we = input("\n\tDo you want to Stop/Remove the Container :")
           if we == "Stop":
               os.system('docker stop {}'.format(ii))
               print("\tContainer {} Stopped Sucessfully........".format(ii))
               os.system('docker ps -a')
           elif we == "Remove":
               os.system('docker rm {}'.format(ii))
               print("\tContainer {} Removed Sucessfully .....".format(ii))

       elif int(ch) == 9:
           uy = input("Enter Your Image Name you want to delete : ")
           os.system('docker rmi {}'.format(uy))    
           os.system('docker images')
       elif int(ch) == 10:
           break
      
               
    






                     
