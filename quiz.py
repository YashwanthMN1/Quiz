import mysql.connector


class master:
	def __init__(self):
		self.con = mysql.connector.connect(host="localhost",username="root",passwd="007007")
		query1 = "create table if not exists easy (question_id VARCHAR(20),questions VARCHAR(50),option1 VARCHAR(20),option2 VARCHAR(20),option3 VARCHAR(20),option4 VARCHAR(20),answer VARCHAR(20))"
		query2 = "create table if not exists medium (question_id VARCHAR(20),questions VARCHAR(50),option1 VARCHAR(20),option2 VARCHAR(20),option3 VARCHAR(20),option4 VARCHAR(20),answer VARCHAR(20))"
		query3 = "create table if not exists hard (question_id VARCHAR(20),questions VARCHAR(50),option1 VARCHAR(20),option2 VARCHAR(20),option3 VARCHAR(20),option4 VARCHAR(20),answer VARCHAR(20))"
		query4 = "create table if not exists results (username VARCHAR(20),difficulty VARCHAR(6),score decimal(2))"
		cur = self.con.cursor()
		cur.execute("use mcq")
		cur.execute(query1)
		cur.execute(query2)
		cur.execute(query3)
		cur.execute(query4)


	def add_questions_to_easy(self,question_id,question,option1,option2,option3,option4,answer):
		query = "INSERT INTO EASY (question_id,questions,option1,option2,option3,option4,answer) VALUES ('{}','{}','{}','{}','{}','{}','{}')".format(question_id,question,option1,option2,option3,option4,answer)
		cur = self.con.cursor()
		cur.execute(query)
		self.con.commit()

	def add_questions_to_medium(self,question_id,question,option1,option2,option3,option4,answer):
		query = "INSERT INTO MEDIUM (question_id,questions,option1,option2,option3,option4,answer) VALUES ('{}','{}','{}','{}','{}','{}','{}')".format(question_id,question,option1,option2,option3,option4,answer)
		cur = self.con.cursor()
		cur.execute(query)
		self.con.commit()

	def add_questions_to_hard(self,question_id,question,option1,option2,option3,option4,answer):
		query = "INSERT INTO HARD (question_id,questions,option1,option2,option3,option4,answer) VALUES ('{}','{}','{}','{}','{}','{}','{}')".format(question_id,question,option1,option2,option3,option4,answer)
		cur = self.con.cursor()
		cur.execute(query)
		self.con.commit()

	def remove_quetion(self,difficulty,question_id):
		query = "delete from {} where question_id = {}".format(difficulty,question_id)
		cur = self.con.cursor()
		cur.execute(query)
		self.con.commit()

class user:
	def __init__(self):
		self.con = mysql.connector.connect(host="localhost",username="root",passwd="007007")
		cur = self.con.cursor()
		cur.execute("use mcq")

	def take_quiz(self,name):
		cur = self.con.cursor()
		print('select difficulty')
		print('for easy type 1')
		print('for medium type 2')
		print('for hard type 3')
		dif = int(input())



		if dif ==1:
			print("you have selected questions which are easy")
			cur.execute("SELECT * FROM easy")
			quests = cur.fetchall()
			score = 0
			for i in quests:
				real_ans = i[6]
				print(i[1])
				print(1,")",i[2])
				print(2,")",i[3])
				print(3,")",i[4])
				print(4,")",i[5])
				u_i = int(input())
				u_ans = i[int(u_i+1)]
				if u_ans == real_ans:
					print("Answer is ",real_ans)
					score += 1
			query = "INSERT INTO RESULTS (username,difficulty,score) VALUES ('{}','{}',{}) ".format(name,'easy',score)
			cur.execute(query)
			self.con.commit()
			print("your score",score)

		if dif == 2:
			print("you have selected questions which are medium")
			cur.execute("SELECT * FROM medium")
			quests = cur.fetchall()
			score = 0
			for i in quests:
				real_ans = i[6]
				print(i[1])
				print(1,")",i[2])
				print(2,")",i[3])
				print(3,")",i[4])
				print(4,")",i[5])
				u_i = int(input())
				u_ans = i[int(u_i+1)]
				if u_ans == real_ans:
					print("Answer is ",real_ans)
					score += 1
			query = "INSERT INTO RESULTS (username,difficulty,score) VALUES ('{}','{}',{}) ".format(name,'medium',score)
			cur.execute(query)
			self.con.commit()
			print("your score",score)

		if dif == 3:
			print("you have selected questions which are hard")
			cur.execute("SELECT * FROM hard")
			quests = cur.fetchall()
			score = 0
			for i in quests:
				real_ans = i[6]
				print(i[1])
				print(1,")",i[2])
				print(2,")",i[3])
				print(3,")",i[4])
				print(4,")",i[5])
				u_i = int(input())
				u_ans = i[int(u_i+1)]
				if u_ans == real_ans:
					print("Answer is ",real_ans)
					score += 1
			query = "INSERT INTO RESULTS (username,difficulty,score) VALUES ('{}','{}',{}) ".format(name,'hard',score)
			cur.execute(query)
			self.con.commit()
			print("your score",score)


