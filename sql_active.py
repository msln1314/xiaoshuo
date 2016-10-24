import pymssql
class MSSQL:
    def __init__(self,host,port,user,pwd,db):
        self.host = host
        self.port=port
        self.user = user 
        self.pwd = pwd
        self.db =db 
#得到连接信息,返回：conn.cursor()
    def __GetCoonnect(self):
        if not self.db:
            raise (NameError,"没有设置数据库信息")
        self.conn = pymssql.connect( host =self.host,port=self.port,user=self.user,password=self.pwd,database=self.db,charset="utf8" )
        cur = self.conn.cursor()
        if not cur:
            raise(NameError,"连接数据库失败")
        else:
            return cur
#执行查询语句，返回的是一个包含tuple的list,list 的元素是记录行，tuple的元素是记录行的字段
    def ExecQuery(self,sql):
        
        cur=self.__GetCoonnect()
        cur.execute(sql)
        resList = cur.fetchall()
        #查询完毕后必须关闭连接
        self.conn.close()
        return resList
#执行非查询语句
    def ExecNonQuery(self,sql):
        cur =self.__GetCoonnect()
        cur.execute(sql)
        self.conn.commit()
        self.conn.close()

ms = MSSQL(host="192.168.0.230",port="50171",user="sa",pwd="Vmware@123",db="quanshubooks")
# ms.ExecNonQuery("insert into books (title ,content) values ('kshdf','llllllllllllllllllllllllllll');")
resList =ms.ExecQuery("SELECT  id,title,content from books ")
for (id,title,content) in resList:
    print(str(id),title,content)

  
