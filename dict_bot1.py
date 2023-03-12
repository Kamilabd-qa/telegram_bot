#библиотеки, которые загружаем из вне
import telebot
TOKEN = '#токен'

from telebot import types

bot = telebot.TeleBot(TOKEN)
#добавить фотографию после приветствия
@bot.message_handler(commands=['start'])
def welcome(message):
	sti = open('sticker3.webp', 'rb')
	bot.send_sticker(message.chat.id, sti)

	#клавиатура
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("регресс")
	item2 = types.KeyboardButton("дейли")
	item3 = types.KeyboardButton("коммититься")
	item4 = types.KeyboardButton("спринт")
	item5 = types.KeyboardButton("ветка")
	item6 = types.KeyboardButton("прод")
	item7 = types.KeyboardButton("мок")
	item8 = types.KeyboardButton("реф")
	item9 = types.KeyboardButton("спека")
	item10 = types.KeyboardButton("таска")
	item11 = types.KeyboardButton("бэклог")
	item12 = types.KeyboardButton("буст")
	item13 = types.KeyboardButton("катить")
	item14 = types.KeyboardButton("комплитить")
	item15 = types.KeyboardButton("гол")
	item16 = types.KeyboardButton("консистентность")
	item17 = types.KeyboardButton("матчится")
	item18 = types.KeyboardButton("пинать")
	item19 = types.KeyboardButton("ручка")
	item20 = types.KeyboardButton("скрам")
	item21 = types.KeyboardButton("скоуп")
	item22 = types.KeyboardButton("фича")
	item23 = types.KeyboardButton("флоу")
	item24 = types.KeyboardButton("девопс")
	item25 = types.KeyboardButton("пио")
	item26 = types.KeyboardButton("пиэм")
	item27 = types.KeyboardButton("дейоф")
	item28 = types.KeyboardButton("драйвер")
	item29 = types.KeyboardButton("консёрн")
	item30 = types.KeyboardButton("окиары")
	item31 = types.KeyboardButton("оффер")
	item32 = types.KeyboardButton("поинт")
	item33 = types.KeyboardButton("эмулятор")
	item34 = types.KeyboardButton("симулятор")


	markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13, item14, item15, item16, item17, item18, item19, item20, item21, item22, item23, item24, item25, item26, item27, item28, item29, item30, item31, item32, item33, item34)

	bot.send_message(message.chat.id, "Привет {0.first_name}! Я помогу тебе быстрее влиться в айти и расшифровать непонятные для тебя термины 🤓".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)

#назначаем действие для клавиатуры
@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.chat.type == 'private':
		if message.text == 'регресс':
			bot.send_message(message.chat.id, 'Определение: Проверить что новый функционал не сломал существующий')
		elif message.text == 'дейли':
			bot.send_message(message.chat.id, 'Определение: От англ. daily (дословно — ежедневно) — ежедневные короткие (от 5 до 30 минут) встречи команды с целью поделиться прогрессом по выполненным задачам за предыдущий день и озвучить план работ на текущий день. Также дейли могут называть стендапом (от daily standup), потому что обычно такие встречи происходят стоя — для большей эффективности.')
		elif message.text == 'коммититься':
			bot.send_message(message.chat.id, 'Определение:Глагол от англ. существительного commitment (дословно — ответственность). Коммититься — значит обещать выполнить определенный объем работы в оговоренные сроки. Это не просто обещание, это сознательное обязательство перед собой и командой. Человек, который закоммитился, обязан сделать всё возможное, чтобы выполнить то, что сам и пообещал реализовать.')
		elif message.text == 'спринт':
			bot.send_message(message.chat.id, 'Определение: От англ. sprint (дословно — бег на короткую дистанцию) — заданный отрезок времени, за который нужно выполнить запланированный объем работы, чтобы в конце этого отрезка был ожидаемый результат. Термин используют не только те, кто работает по скраму, но и те, кто просто хочет организовать свою работу и сформировать ясные рамки, во время которых должны быть выполнены задачи.')
		elif message.text == 'ветка':
			bot.send_message(message.chat.id, 'Определение: От англ. branch (дословно — ветка) — тот редкий случай, когда в ходу русский перевод термина. Веткой (термин git) называют полную копию проекта, в которой ведется разработка. В проекте может быть создано много веток, что позволяет работать одновременно с разными частями кода. Потом все ветки загружаются в мастер. Процесс «ответвления» иногда называют «бранчеванием», уже как раз от branch.')
		elif message.text == 'прод':
			bot.send_message(message.chat.id, 'Определение: От англ. production (дословно — промышленная среда) — ветка с рабочей версией продукта, которую видят пользователи. Это окончательная точка куда попадает результат разработки. Иногда так же называют мастер.')
		elif message.text == 'мок':
			bot.send_message(message.chat.id, 'Определение: От англ. mock-up (дословно — эскиз) — макет с UX-дизайном для разработки. Несмотря на то, что слово дословно переводится как «эскиз» или «прототип», в Wrike моками называют готовые проработанные макеты с дизайном.')
		elif message.text == 'реф':
			bot.send_message(message.chat.id, 'Определение: От англ. reference (дословно — пример) — схожий функционал или внешний вид, который используется для ориентира. Он служит для сравнения.')
		elif message.text == 'спека':
			bot.send_message(message.chat.id, 'Определение: От англ. specification (дословно — спецификация) — документ с подробным описанием требований, условий и технических характеристик, как должен работать разрабатываемый функционал.')
		elif message.text == 'таска':
			bot.send_message(message.chat.id, 'Определение: От англ. task (дословно — задача) — задача, заведенная или планируемая на любого работника.')
		elif message.text == 'бэклог':
			bot.send_message(message.chat.id, 'Определение: От англ. backlog (дословно — очередь работ) — еще не запланированный объем работы, который требуется выполнить команде. Каждая созданная задача вначале попадает в бэклог, а потом уже в спринт. Как и в случае со спринтом, термин используется и в отрыве от скрама. Часто бэклогом называют отложенные задачи. Которые сделать нужно, но не сейчас.')
		elif message.text == 'буст':
			bot.send_message(message.chat.id, 'Определение: От англ. boost (дословно — ускорение) — процесс повышения производительности, ускорение загрузки.')
		elif message.text == 'катить':
			bot.send_message(message.chat.id, 'Определение: Отправлять готовую работу в деплой, предпринимать шаги для подготовки ветки к мерджу в продуктовую ветку.')
		elif message.text == 'комплитить':
			bot.send_message(message.chat.id, 'Определение: От англ. complete (дословно — заканчивать) — завершать задачу, закрывать задачу, когда она полностью готова')
		elif message.text == 'гол':
			bot.send_message(message.chat.id, 'Определение: От англ. goal (дословно — цель) — цель спринта (бывает одна или несколько), которую команда берется сделать. Цель состоит из ряда задач, которые нужно выполнить, чтобы его достигнуть.')
		elif message.text == 'консистетность':
			bot.send_message(message.chat.id, 'Определение: От англ. consistency (дословно — системность) — общее единообразие во всех частях продукта.')
		elif message.text == 'матчится':
			bot.send_message(message.chat.id, 'Определение: От англ. match (дословно — совпадать) — полное соответствие чего-либо с чем-либо. Процесс приведения к единообразию.')
		elif message.text == 'пинать':
			bot.send_message(message.chat.id, 'Определение: Термин, подобный глаголу «пинать», который также имеет значение «делать» и «работать». Конкретное значение определяется по приставке. Подопнуть — сделать немного, допинать — доделать.')
		elif message.text == 'ручка':
			bot.send_message(message.chat.id, 'Определение: От англ. handler (дословно — обработчик) — бэкэнд-термин, означающий ответ от сервера, в котором приходят данные. Также называют Запрос,Метод,Эндпоинт,Хендлер')
		elif message.text == 'скрам':
			bot.send_message(message.chat.id, 'Определение: Scrum — это методология по управлению проектами. Набор принципов, ценностей, политик, ритуалов для организации работы. В скраме полно терминов, но в ежедневный обиход попала и закрепилась только часть из них.')
		elif message.text == 'скоуп':
			bot.send_message(message.chat.id, 'Определение: От англ. scope (дословно — объем) — набор фич и частей продукта, закрепленных за отдельной командой.')
		elif message.text == 'фича':
			bot.send_message(message.chat.id, 'Определение: От англ. feature (дословно — характеристика) — определенная часть или деталь от общего продукта, которая разрабатывается изолированно.')
		elif message.text == 'флоу':
			bot.send_message(message.chat.id, 'Определение: От англ. flow (дословно — течение) — порядок действий при работе над задачей. Например, вначале задача берётся в разработку, потом проходит ревью, далее тестируется и т.д.')
		elif message.text == 'девопс':
			bot.send_message(message.chat.id, 'Определение: От англ. DevOps, сокращенно от Developer Operations (дословно — интеграция разработки и эксплуатации) — специалист, занимающийся внедрением DevOps-методологии. Полное название должности — DevOps-инженер, но в речи вторую часть всегда отбрасывают.')
		elif message.text == 'пио':
			bot.send_message(message.chat.id, 'Определение: От англ. PO, сокращенно от Product Owner (дословно — владелец продукта) — роль по скрам-методологии, человек, ответственный за проработку продукта и распределение бэклога. Он знает о требованиях пользователя и возможностях команды. ')
		elif message.text == 'пиэм':
			bot.send_message(message.chat.id, 'Определение: От англ. PM, сокращенно от Product Manager (дословно — менеджер продукта) — менеджер, который отвечает за продукт, его обязанности совпадают с обязанностями пио, отличие только в том, что это название должности, а не роли в скраме. Так же, как пио, пиэмов могут называть продакт.')
		elif message.text == 'дейоф':
			bot.send_message(message.chat.id, 'Определение: От англ. day-off (дословно — выходной) — просто выходной. ')
		elif message.text == 'консёрн':
			bot.send_message(message.chat.id, 'Определение: От англ. concern (дословно — тревога, участие) — в английском языке слово «консёрн» имеет много различных значений, при этом очень часто употребляется в русской речи. Какое именно значение вкладывает в него автор, известно только ему самому. Иногда — это смесь многих значений, таких как: особый интерес, беспокойство, цель, настороженность, опасение и т.д. ')
		elif message.text == 'драйвер':
			bot.send_message(message.chat.id, 'Определение: От англ. driver (дословно — водитель) — человек, который берет на себя инициативу управления проектом/процессом/задачей. В его обязанности входит следить за тем, как протекает созданный им процесс, и руководить им. Он мотивирует других людей выполнять работу для достижения поставленных целей. ')
		elif message.text == 'окиары':
			bot.send_message(message.chat.id, 'Определение: От англ. OKR, сокращенно от Objectives and Key Results (дословно — цели и ключевые результаты) — система по постановке и достижению целей. Она нужна для синхронизации работы всех участников компании/отдела/команды, чтобы все двигались в одном направлении, с понятными приоритетами и постоянным ритмом. В отличие от KPI, это амбициозное целеполагание, достижение окиаров (окров) на 70-80% — отличный результат.')
		elif message.text == 'оффер':
			bot.send_message(message.chat.id, 'Определение:От англ. offer (дословно — предложение) — предложение о работе / приглашение на работу.')
		elif message.text == 'поинт':
			bot.send_message(message.chat.id, 'Определение: От англ. point (дословно — точка) — чаще всего употребляется в значении «точка зрения», сокращенно от point of view. Также в значениях: «суть», «смысл», «довод». ')
		elif message.text == 'эмулятор':
			bot.send_message(message.chat.id, 'Определение: Эмулирует (повторяет или воспроизводит) поведение операционки и технического оснащение. Более приближен к реальному устройству, чем симулятор. Пример: Android Studio,Эмуляторов iOS-устройств не бывает.')
		elif message.text == 'симулятор':
			bot.send_message(message.chat.id, 'Определение:  Имитирует (повторяет или воспроизводит) поведение только операционки. Симуляторы для iOS-устройств предоставляется в среде разработки Xcode.')
		else:
			bot.send_message(message.chat.id, 'Не знаю что ответить😢')


bot.polling(none_stop=True)
