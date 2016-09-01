name = 'Дозоры'

actions = [ 'Остановить бой', 'Уйти' ]


def get_actions(user):
	return actions


def enter(user, reply):
	reply(
		'C незапамятных времен рыцари, называющие себя воинами Света, '
		'ловят ведьм и колдунов, истязающих род человеческий. '
		'Но однажды на пути воинов Света встали воины Тьмы. '
		'И никто не хотел уступить. И начался бой кровавый и беспощадный. '
		'И когда битва дошла до Небес великий Гесер увидел что силы равны. '
		'И если не остановить бой - погибнут все... \n'
	)


def action(user, reply, text):
	if text == actions[0]:
		reply(
			'И он остановил бой. И заключили силы Света и силы Тьмы договор о перемирии. '
			'И было сказано, что отныне ни добро ни зло нельзя творить без соглассия. '
			'И было сказано, что будет Дневной дозор, чтобы следить за силами Света. '
			'И было сказано, что будет Ночной дозор, чтобы следить за силами Тьмы.\n'
		)

	user.leave(reply)