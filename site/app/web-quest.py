from flask import Flask, render_template, request, redirect, url_for
from text_data import place_time, mi6_msg, mi6_msg2, text, err_text, err_text2, witness, agents, agents2

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def index():
	return render_template("index.html",
		place_time = place_time["1"],
		text1 = mi6_msg["1"],
		text2 = mi6_msg["1_2"],
		img_link = "static\patrick.png",
		img_link2 = "static\map.png",
		next_page = "/1")

@app.route('/1', methods=['POST'])
def page1():
	return render_template("temp_text.html",
		place_time = place_time["2"],
		text = text["1"],
		img_link = "static\harry.png",
		next_page = "/2")

@app.route('/2', methods=['POST'])
def page2():
	return render_template("temp_text.html",
		place_time = place_time["3"],
		text = text["2"],
		img_link = "static\messintheroom.png",
		next_page = "/3")

@app.route('/3', methods=['POST'])
def page3():
	msg = ""	
	next_page = "/3"
	try:
		answer = request.form['answer']
		if len(answer) == 0:
			msg = err_text2
		elif 20<len(answer)<1 or answer.lower() != "ask murphy seamrog":
			msg = err_text			
		else:
			return redirect(url_for("page4"), code=307)			
	except KeyError:
		msg = err_text2
	return render_template("temp_form.html",
		place_time = place_time["4"],
		text = text["3"],
		img_link = "static\\text.png",
		input_type = "text",
		input_name = "answer",
		input_placeholder = "Расшифровка",
		form_data = [{}],
		img_class = "no_main_img",
		err_msg = msg,
		next_page = next_page)

@app.route('/4', methods=['POST'])
def page4():
	msg = ""	
	next_page = "/4"
	try:
		answer = request.form['witness']
		if answer == "2":
			return redirect(url_for("page5"), code=307)
		else:
			msg = err_text
	except KeyError:
		msg = err_text2
	return render_template("temp_form.html",
		place_time = place_time["5"],
		text = text["4"],
		img_link = "static\witnesses.png",
		input_type = "radio",
		input_name = "witness",
		input_placeholder = "none",
		form_data = witness,
		err_msg = msg,
		next_page = next_page)

@app.route('/5', methods=['POST'])
def page5():
	return render_template("temp_text.html",
		place_time = place_time["6"],
		text = text["5"],
		img_link = "static\pub.png",
		next_page = "/6")

@app.route('/6', methods=['POST'])
def page6():
	msg = ""
	next_page = "/6"
	try:
		answer = request.form['answer']
		if len(answer) == 0:
			msg = err_text2
		elif 10<len(answer)<1 or answer != "seamrog":
			msg = err_text			
		else:
			return redirect(url_for("page7"), code=307)
	except KeyError:
		msg = err_text2
	return render_template("temp_form.html",
		place_time = place_time["7"],
		text = text["6"],
		img_link = "static\guinness1.png",
		input_type = "text",
		input_name = "answer",
		input_placeholder = "Кодовое_слово",
		form_data = [{}],
		err_msg = msg,
		next_page = next_page)

@app.route('/7', methods=['POST'])
def page7():
	return render_template("temp_text.html",
		place_time = place_time["8"],
		text = text["7"],
		img_link = "static\disckinfo.png",
		next_page = "/8")

@app.route('/8', methods=['POST'])
def page8():
	msg = ""
	next_page = "/8"
	try:
		answer = request.form.getlist('agents')
		if len(answer) == 3 and "1" in answer and "3" in answer and "5" in answer:
			return redirect(url_for("page9"), code=307)
		elif len(answer) == 0:
			msg = err_text2
		else:
			msg = err_text
	except KeyError:
		msg = err_text2
	return render_template("temp_form.html",
		place_time = place_time["9"],
		text = text["8"],
		text2 = mi6_msg2,
		text3 = text["8_2"],
		img_link = "static\\agents.png",
		input_type = "checkbox",
		input_name = "agents",
		input_placeholder = "none",
		form_data = agents,
		p_class = "msg",
		err_msg = msg,
		next_page = next_page)

@app.route('/9', methods=['POST'])
def page9():
	msg = ""
	next_page = "/9"
	try:
		answer = request.form['agents2']
		if answer == "2":
			return redirect(url_for("page10"), code=307)
		else:
			msg = err_text
	except KeyError:
		msg = err_text2
	return render_template("temp_form.html",
		place_time = place_time["10"],
		text = text["9"],
		text2 = text["10"],
		img_link = "static\\agents2.png",
		input_type = "radio",
		input_name = "agents2",
		input_placeholder = "none",
		form_data = agents2,
		err_msg = msg,
		next_page = next_page)

@app.route('/10', methods=['POST'])
def page10():
	return render_template("temp_text.html",
		place_time = place_time["11"],
		text = text["11"],
		img_link = "static\guinness2.png",
		next_page = "/11")

@app.route('/11', methods=['POST'])
def page11():
	return render_template("temp_text.html",
		place_time = place_time["12"],
		text = text["12"],
		img_link = "static\kilkeacastle.png",
		next_page = "/12")

@app.route('/12', methods=['POST'])
def page12():
	return render_template("temp_text.html",
		place_time = place_time["13"],
		text = text["13"],
		img_link = "static\wall.png",
		next_page = "/13")

#ввод нескольких значений чекбокса для одного значения клекти не проверятется,
#так как вероятность победы с учётом всех проверок маловероятна
@app.route('/13', methods=['POST'])
def page13():
	msg = ""
	next_page = "/13"
	try:
		answer = request.form.getlist('numbers')
		answer2 = request.form.getlist('right_left')
		if len(answer2) != 7:
			msg = "надо выбрать по одному значению для каждой клетки..."
		elif "" in answer:
			msg = "надо использовать все семь клеток..."
		else:
			if ("22" and "20" and "8" and "6" and "10" and "12" and "14") in answer:
				next_answer2 = 0
				flag = True
				right_answers = {
					"22" : "1",
					"20" : "0",
					"8" : "0",
					"6" : "1",
					"10" : "0",
					"12" : "0",
					"14" : "1"
				}
				for number in answer:
					if right_answers[number] != answer2[next_answer2]:
						flag = False
					next_answer2 = next_answer2 + 1
				if flag:
					return redirect(url_for("page14"), code=307)
				else:
					msg = err_text
			else:
				msg = err_text
	except KeyError:
		msg = err_text
	return render_template("temp_final.html",
		place_time = place_time["14"],
		text = text["14"],
		img_link = "static\\final.png",
		err_msg = msg,
		next_page = "/13")

@app.route('/14', methods=['POST'])
def page14():
	return render_template("temp_text.html",
		place_time = place_time["15"],
		text = text["15"],
		img_link = "static\helicopters.png",
		next_page = "/15")

@app.route('/15', methods=['POST'])
def page15():
	return render_template("temp_text.html",
		place_time = place_time["16"],
		text = text["16"],
		img_link = "static\case.png",
		value_input = "Всё...",
		next_page = "/16")

@app.route('/16', methods=['POST'])
def page16():
	return render_template("temp_info.html",
		place_time = "Have a nice day!",
		text= "Игра создана в 2016 году, на 99% состоит из ненарушающего никакие првава материала, за исключением последний головоломки, которая была взята из игры Puzzle Agent.")

if __name__ == "__main__":
    app.run()
