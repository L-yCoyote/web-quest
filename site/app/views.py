from flask import render_template, request
from app import app

@app.route('/')
@app.route('/index.html')
def index():
	place = "London, MI6"
	time = " / fri 28 august, 3:50 a.m."
	text = "СРОЧНО: Сегодня ночью из собственного дома в Дублине был похищен агент Патрик."
	return render_template("index.html", place_time = place+time, text = text)

@app.route('/1', methods=['POST'])
def harryhome():
	place = "London, дом агента Гарри"
	time = " / fri 28 august, 3:55 a.m."
	text = "Агент Гарри получает задание немедленно отправляться на поиске своего коллеги."
	return render_template("1.html", place_time = place+time, text = text)

@app.route('/2', methods=['POST'])
def patrichome():
	place = "Dublin, дом агента Патрика"
	time = " / fri 28 august, 9:45 a.m."
	text = "Прибыв на место проишествия агент Гарри, увидел перевёрнутое вверх дном жилище своего коллеги... Проведя немало времени в поисках хоть какой-то улики, он начал отчаяваться, как вдруг заметил небольшой листок под диваном..."
	return render_template("2.html", place_time = place+time, text = text)

@app.route('/2_2', methods=['POST'])
def patrichome3():
	error_text = ""
	persons = []
	try:
		answer = request.form['answer']
		if 20<len(answer)<1 or answer != "ask murphy seamrog":
			place = "Dublin, дом агента Патрика"
			time = " / fri 28 august, 11:30 a.m."
			text = "Прошло ещё немало времени, прежде чем агент Гарри наконец-то понял, что за шифр был использован в послание на найденом листке..."
			error_text = "надо подумать ещё..."
			html = "2_2.html"
		else:
			place = "Dublin, дом агента Патрика"
			time = " / fri 28 august, 11:40 a.m."
			text = "'Ask Murphy' что бы это значило... - подумал Гарри. Времени совсем мало, надо опросить соседей, может кто что видел. Времени хватит, что бы опросить только одного... Местные полицейкие уже всех опросили, и дали следующий список:"
			persons = [
				{	
					"number":"1",
					"text":"Джон, люитель Guinness'a и телевизора, обычно спит прямо напротив него;"
				},
				{	"number":"2",
					"text":"Джинни, часто страдает бессоницей и любит смотреть в окно;"
				},
				{	"number":"3",
					"text":"Карл, плохо слышит и видит, но в полнолуние (было этой ночью), не спит и воет на луну;"
				},
				{	"number":"4",
					"text":"Нэнси, любит поспать, любопынта, лишь когда речь заходит о местных распродажах;"
				}
			]
			html = "3.html"
	except KeyError:
		place = "Dublin, дом агента Патрика"
		time = " / fri 28 august, 11:30 a.m."
		text = "Прошло ещё немало времени, прежде чем агент Гарри наконец-то понял, что за шифр был использован в послание на найденом листке..."
		html = "2_2.html"
	return render_template(html, place_time = place+time, text = text, error_text = error_text, persons = persons)

@app.route('/3_2', methods=['POST'])
def ask():
	error_text = ""
	persons = []
	try:
		person = request.form['person']
		if person == "2":
			place = "Dublin, дом Джинни"
			time = " / fri 28 august, 11:45 a.m."
			text = "Джинни, рассказала, что не могла спать прошлой ночью, так как старый Карл постоянно выл на луну. Она смотрела в окно, и видела около дома Патрика несколько сов, когда они пролетели на фоне полной луны... Больше она ничего рассказать не смогла, кроме воя он ничего не слышала. На вопрос знает ли она Murphy, сказала что это имя владельца паба неподаёлку."
			html = "4.html"
		else:
			place = "Dublin, дом агента Патрика"
			time = " / fri 28 august, 11:40 a.m."
			text = "'Ask Murphy' что бы это значило... - подумал Гарри. Времени совсем мало, надо опросить соседей, может кто что видел. Времени хватит, что бы опросить только одного... Местные полицейкие уже всех опросили, и дали следующий список:"
			persons = [
				{	
					"number":"1",
					"text":"Джон, люитель Guinness'a и телевизора, обычно спит прямо напротив него;"
				},
				{	"number":"2",
					"text":"Джинни, часто страдает бессоницей и любит смотреть в окно;"
				},
				{	"number":"3",
					"text":"Карл, плохо слышит и видит, но в полнолуние (было этой ночью), не спит и воет на луну;"
				},
				{	"number":"4",
					"text":"Нэнси, любит поспать, любопынта, лишь когда речь заходит о местных распродажах;"
				}
			]
			error_text = "надо подумать ещё..."
			html = "3.html"	
	except KeyError:
		place = "Dublin, дом агента Патрика"
		time = " / fri 28 august, 11:40 a.m."
		text = "'Ask Murphy' что бы это значило... - подумал Гарри. Времени совсем мало, надо опросить соседей, может кто что видел. Времени хватит, что бы опросить только одного... Местные полицейкие уже всех опросили, и дали следующий список:"
		persons = [
			{	
				"number":"1",
				"text":"Джон, люитель Guinness'a и телевизора, обычно спит прямо напротив него;"
			},
			{	"number":"2",
				"text":"Джинни, часто страдает бессоницей и любит смотреть в окно;"
			},
			{	"number":"3",
				"text":"Карл, плохо слышит и видит, но в полнолуние (было этой ночью), не спит и воет на луну;"
			},
			{	"number":"4",
				"text":"Нэнси, любит поспать, любопынта, лишь когда речь заходит о местных распродажах;"
			}
		]
		error_text = "надо подумать ещё..."
		html = "3.html"	
	return render_template(html, place_time = place+time, text = text, error_text = error_text, persons = persons)

@app.route('/4', methods=['POST'])
def pub():
	place = "Dublin, Murphy's Pub"
	time = " / fri 28 august, 1:00 p.m."
	text = "Агент Гарри заказал Guinness и спросил у владельца знает ли он Патрика. Владелец посмотрел на Гарри и спросил кодовое слово."
	return render_template("4_2.html", place_time = place+time, text = text)

@app.route('/4_2', methods=['POST'])
def pub2():
	place = "Dublin, Murphy's Pub"
	time = " / fri 28 august, 1:00 p.m."
	text = "Агент Гарри заказал Guinness и спросил у владельца знает ли он Патрика. Владелец посмотрел на Гарри и спросил кодовое слово."
	error_text = ""
	try:
		answer = request.form['answer']
		if 10<len(answer)<1 or answer != "seamrog":
			error_text = "надо подумать ещё..."
			html = "4_2.html"
		else:
			place = "Dublin, Murphy's Pub"
			time = " / fri 28 august, 1:10 p.m."
			text = "Владелец сказал, что недавно Патрик оставил ему конверт. Гарри взял конверт, в нём был лишь небольшой диск."
			html = "4_3.html"
	except KeyError:
		html = "4_2.html"
	return render_template(html, place_time = place+time, text = text, error_text = error_text)

@app.route('/4_3', methods=['POST'])
def pub3():
	place = "Dublin, Murphy's Pub"
	time = " / fri 28 august, 1:20 p.m."
	text = "Гарри открыл диск на своём ноутбуке, к сожалению, он был зашифрован. Пришлось ограничется письмом в MI6, и ждать ответа..."
	return render_template("4_4.html", place_time = place+time, text = text)

@app.route('/4_4', methods=['POST'])
def pub4():
	place = "Dublin, дом агента Патрика"
	time = " / fri 28 august, 3:30 p.m."
	text = "После нескольких пинт Guinness и часов ожидания, пришло сообщения от MI6. Оказалось, что часть данных, найденная на диске, связана со старым делом TOPS7897_89, в котором учавстовавало 6 агентов сов:"
	agents = [
		{
			"number":"1",
			"name":"Сэм"
		},
		{
			"number":"2",
			"name":"Чарльз"
		},
		{
			"number":"3",
			"name":"Пирс"
		},
		{
			"number":"4",
			"name":"Джеймс"
		},
		{
			"number":"5",
			"name":"Майкл"
		},
		{
			"number":"6",
			"name":"Колин"
		}
	]
	text2 = "ДОПОЛНИТЕЛЬНО: В настоящий момент агенты Чарльз и Колин находятся на задании в Северной Америки, агент Джеймс погиб при исполнение долга год назад. Остальные агенты в данный момент не задействованы в операциях MI6. Ожидайте в ближайший час дополнительную информацию о местоположении перечисленных агентов. В ожидании дополнительной ифнормации агент Гарри решил сузить круг подозреваемых."
	return render_template("4_5.html", place_time = place+time, text = text, text2 = text2, agents = agents)

@app.route('/4_5', methods=['POST'])
def pub5():
	place = "Dublin, Murphy's Pub"
	time = " / fri 28 august, 3:10 p.m."
	text = "После нескольких пинт Guinness и часов ожидания, пришло сообщения от MI6. Оказалось, что часть данных, найденная на диске, связана со старым делом TOPS7897_89, в котором учавстовавало 6 агентов сов:"
	agents = [
		{
			"number":"1",
			"name":"Сэм"
		},
		{
			"number":"2",
			"name":"Чарльз"
		},
		{
			"number":"3",
			"name":"Пирс"
		},
		{
			"number":"4",
			"name":"Джеймс"
		},
		{
			"number":"5",
			"name":"Майкл"
		},
		{
			"number":"6",
			"name":"Колин"
		}
	]
	text2 = "ДОПОЛНИТЕЛЬНО: В настоящий момент агенты Чарльз и Колин находятся на задании в Северной Америки, агент Джеймс погиб при исполнение долга год назад. Остальные агенты в данный момент не задействованы в операциях MI6. Ожидайте в ближайший час дополнительную информацию о местоположении перечисленных агентов. В ожидании дополнительной ифнормации агент Гарри решил сузить круг подозреваемых."
	error_text = ""
	html = "4_5.html"
	try:
		agents2 = request.form.getlist('agent')
		if len(agents2) == 3 and "1" in agents2 and "3" in agents2 and "5" in agents2:
			place = "Dublin, Murphy's Pub"
			time = " / fri 28 august, 4:15 p.m."
			text = "Спустя ещё одну пинту Guinness и час ожидания, пришло новое сообщение, c местоположением всех агентов:"
			agents2 = [
				{
					"number":"1",
					"name":"Сэм"
				},
				{
					"number":"2",
					"name":"Пирс"
				},
				{
					"number":"3",
					"name":"Майкл"
				}
			]
			text2 = "Теперь осталось трое. Надо выбрать из них главного подозреваемого."
			html = "4_6.html"
		else:
			error_text = "надо подумать ещё..."
	except KeyError:
		html = "4_5.html"
	return render_template(html, place_time = place+time, text = text, text2 = text2, agents = agents, agents2 = agents2, error_text = error_text)

@app.route('/5', methods=['POST'])
def castle1():
	place = "Dublin, Murphy's Pub"
	time = " / fri 28 august, 4:15 p.m."
	text = "Спустя ещё одну пинту Guinness и час ожидания, пришло новое сообщение, c местоположением всех агентов:"
	agents2 = [
		{
			"number":"1",
			"name":"Сэм"
		},
		{
			"number":"2",
			"name":"Пирс"
		},
		{
			"number":"3",
			"name":"Майкл"
		}
	]
	text2 = "Теперь осталось трое. Надо выбрать из них главного подозреваемого."
	html = "4_6.html"
	error_text = ""
	try:
		agent = request.form['agent']
		if agent == "2":
			place = "Килдэр, Kilkea Castle"
			time = " / fri 28 august, 6:30 p.m."
			text = "Агент Гарри не успел насладится красотой замка, в котором по информации MI6 находится агент Пирс, так как сразу был схвачен охраной. После выпитого сопротивлятся сил не было..."
			html = "5.html"
		else:
			error_text = "надо подумать ещё..."
	except KeyError:
		error_text = "надо подумать ещё..."
	return render_template(html, place_time = place+time, text = text, text2 = text2, agents2 = agents2, error_text = error_text)

@app.route('/5_2', methods=['POST'])
def castle2():
	place = "Dublin, дом агента Патрика"
	time = " / fri 28 august, 8:30 a.m."
	text = "Очнулся он уже в темнице, через пару часов... Он был не один, рядом с ним сидел агент Патрик. Который был рад, что коллега накоец проснулся. Он рассказал, что был похищен ночью из-за того, что Пирс не смог найти у него дома диск... Узнав, что диск сейчас в безопасности, он предложил выбираться из плена. В темнице он нашёл потойной ход, скрываемый за стеной с замком-головоломкой, которую ему пока не удалось решить..."
	return render_template("5_2.html", place_time = place+time, text = text)

@app.route('/5_3', methods=['POST'])
def castle3():
	place = "Dublin, дом агента Патрика"
	time = " / fri 28 august, 8:35 a.m."
	text = "Загадку со стены, я перересовал на листок. - Сказал Патрик. - Необходимо изменить положение препятсвий в клетках с цифрами таким образом, что бы оттакливаясь от них дойти от старта до финиша, минуя серые клекти:"
	return render_template("5_2.html", place_time = place+time, text = text)




