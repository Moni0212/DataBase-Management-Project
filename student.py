
import mysql.connector
import streamlit as st

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="StudentLogin",
)
mycursor=mydb.cursor(buffered=True)
print("connection establish")


#create def function
def main():
   st.title("Students Information Portal")
   #disply operation
   option=st.sidebar.selectbox("Select On Operation",("login","Read","Update Details","Delete Record"))
   #perform operation
   if option=="login":
    st.subheader("Userlogin")
    id=st.text_input("Enter StudentId")
    name=st.text_input("Enter  Name")
    emaild=st.text_input("Enter  Emaild")
    department=st.text_input("Enter Department")
    if st.button("Create"):
      sql="insert into Student(id,name,emaild,department) values(%s,%s,%s,%s)"
      val=(id,name,emaild,department)
      mycursor.execute(sql,val)
      mydb.commit()
      st.success("Record Created Successfully!!!")
       
   elif option=="Read":
       st.subheader("Read Details")
       mycursor.execute("select * from Student")
       result=mycursor.fetchall()
       Student= [desc[0] for desc in mycursor.description]
       data = [dict(zip(Student, row)) for row in result]
       st.table(data)
       #for row in result:
          #st.write(row)
          
      
   elif option=="Update Details":
       st.subheader("Update a Record")
       id=st.number_input("Enter ID",min_value=1)
       name=st.text_input("Enter New Name")
       emaild=st.text_input("Enter  New Emaild")
       department=st.text_input("Enter New Department")
       if st.button("Update"):
          sql="Update Student set name=%s, emaild=%s, department=%s where id=%s"
          val=(name,emaild,department,id)
          mycursor.execute(sql,val)
          mydb.commit()
          st.success("Update Successfully!!!")
                          
   elif option=="Delete Record":
      st.subheader("Delete a Record")
      id=st.number_input("Enter ID")
      if st.button("Delete"):
         sql="Delete from Student where id =%s "
         val=(id,) 
         mycursor.execute(sql,val)
         mydb.commit()
         st.success("Delete Successfully!!!")  


if __name__ == "__main__":
  main()