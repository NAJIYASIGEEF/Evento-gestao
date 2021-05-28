import sqlite3  
  
con = sqlite3.connect("bfh_event.db", check_same_thread=False)  
print("Database opened successfully")  
  
con.execute("create table if not exists login(id integer primary key autoincrement,name varchar(50),uname varchar(50),pass varchar(50))")  
con.execute("create table if not exists user(id integer primary key autoincrement,name varchar(50),email varchar(50),mob varchar(25),dob date,address text,state varchar(50),city varchar(50),pin varchar(20))")
con.execute("create table if not exists user1(id integer primary key autoincrement,userid integer,cou varchar(50),brn varchar(50),conm varchar(50),place text,yog integer,intar text)")
con.execute("create table if not exists event(id integer primary key autoincrement,uid integer,title varchar(50),dts varchar(20),dte varchar(20),mode varchar(20),location varchar(50),mp varchar(20),des text,banner blob,ts text,te text)")
con.execute("create table if not exists reg_eve(id integer primary key autoincrement,uid integer,eid integer)")
con.execute("alter table event add column ts text")
con.execute("alter table event add column te text")

print("Table created successfully")  
  
con.close() 
