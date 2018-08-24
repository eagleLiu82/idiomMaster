
# coding: utf-8


import sqlite3
import random
db_file=r"lib\idiom.db"


class idioms:
    def __init__(self,filename=db_file):
        self.db=sqlite3.connect(filename)
        self.cursor=self.db.cursor()
        
    def search(self,key,search_type='exact'):
        if search_type=='fuzzy':
            search_sql="select word from idiom_table where word like '%"+key+"%'"
        elif search_type=='exact':
            search_sql="select word from idiom_table where word like '"+key+"'"
        elif search_type=='regular':
            search_sql="select word from idiom_table where word like '"+key+"'"
            search_sql=search_sql.replace('*',"%")
            search_sql=search_sql.replace("?","_")
        else:
            pass
        self.cursor.execute(search_sql)
        return self.cursor.fetchall()
    
    def get_last_word(self,key):
        return key[-1]
    
    def jielong_next(self,word):
        key=word+"*"
        return self.search(key,'regular')
    
    def jielong(self,key):
        jl_key=key
        print(jl_key,end="")
        while True:
            word=self.get_last_word(jl_key)
            jl_key=self.jielong_next(word)
            if len(jl_key)==0:
                break
            else:
                choice=random.randint(0,len(jl_key)-1)
                jl_key=jl_key[choice][0]
                print("=>"+jl_key,end="")

    
    def detail(self,key):
        search_sql="select word,pinyin,explanation,example,derivation from idiom_table where word='"+key+"';"
        self.cursor.execute(search_sql)
        return self.cursor.fetchall()
    
    def close(self):
        self.db.close()
        
    
        






