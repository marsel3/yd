from loader import datebase
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup



vidsporta_type = InlineKeyboardMarkup(row_width=2,
                                      inline_keyboard=[
                                        [InlineKeyboardButton(text='Одиночный вид спорта', callback_data='solo_team')
                                         ],

                                    [InlineKeyboardButton(text='Командный вид спорта', callback_data='team_teams')
                                 ],
                                [InlineKeyboardButton(text='Поиск по названию команды(игрока)',
                                                      callback_data='search_team')]
                            ])



start_be_trener = InlineKeyboardMarkup(row_width=2,
                                 inline_keyboard=[
                                     [InlineKeyboardButton(text='Заполнить анкету', callback_data='start_be_trener')
                                      ],
                                     [InlineKeyboardButton(text='Выйти в главное меню', callback_data='back_menu')
                                      ],
                                ])

back_menu = InlineKeyboardMarkup(row_width=2,
                                 inline_keyboard=[
                                     [InlineKeyboardButton(text='Выйти в главное меню', callback_data='back_menu')
                                      ],
                                ])


edit_sostav = InlineKeyboardMarkup(row_width=2,
                                 inline_keyboard=[
                                     [InlineKeyboardButton(text='Внести измения', callback_data='edit_sostav')
                                      ],
                                ])


def make_trener(user_id):
    return InlineKeyboardMarkup(row_width=2,
                                 inline_keyboard=[
                                     [InlineKeyboardButton(text='Подтвердить статус тренера', callback_data=f'setTrener_{user_id}_True')
                                      ],
                                     [InlineKeyboardButton(text='Это лжец!',
                                                           callback_data=f'setTrener_{user_id}_False')
                                      ],
                                ])

def team_create(user_id):
    return InlineKeyboardMarkup(row_width=2,
                                 inline_keyboard=[
                                     [InlineKeyboardButton(text='Подтвердить создание команды', callback_data=f'createTeam_{user_id}_True')
                                      ],
                                     [InlineKeyboardButton(text='Не хочу!',
                                                           callback_data=f'createTeam_{user_id}_False')
                                      ],
                                ])

def team_sostav_change(user_id):
    return InlineKeyboardMarkup(row_width=2,
                                 inline_keyboard=[
                                     [InlineKeyboardButton(text='Подтвердить изменение в составе', callback_data=f'sostavChange_{user_id}_True')
                                      ],
                                     [InlineKeyboardButton(text='Не буду, я уже устал работать!',
                                                           callback_data=f'sostavChange_{user_id}_False')
                                      ],
                                ])


def vidsporta_vid(type):
    m1 = datebase.vidsporta(type)
    btns = []
    for i in m1:
        btns.append([InlineKeyboardButton(text=f'{i[1]}', callback_data=f'teamsvidsporta_{i[0]}')])
    btns.append([InlineKeyboardButton(text='Назад', callback_data='back_to_cat')])
    return InlineKeyboardMarkup(row_width=2, inline_keyboard=btns)


def team_by_vidsportaid(vidsportaid):
    m1 = datebase.teams_by_vidsporta(vidsportaid)
    team_ = datebase.vidsporta_type(vidsportaid)
    type = 'teamplayer' if team_ else 'soloplayer'
    btns = []
    for i in m1:
        btns.append([InlineKeyboardButton(text=f'{i[1]}', callback_data=f'{type}_{i[0]}')])
    btns.append([InlineKeyboardButton(text='Назад', callback_data=f'backtovidsporta_{team_}')])
    return InlineKeyboardMarkup(row_width=2, inline_keyboard=btns)


def searcher_team(team):
    m1 = datebase.search_by_team(team)
    btns = []
    for i in m1:
        type = 'teamplayer' if datebase.vidsporta_type_by_team(i[0]) else 'soloplayer'
        btns.append([InlineKeyboardButton(text=f'{i[1]}', callback_data=f'{type}_{i[0]}')])
    btns.append([InlineKeyboardButton(text='Назад', callback_data=f'back_to_cat')])
    return InlineKeyboardMarkup(row_width=2, inline_keyboard=btns)


def trener_menu(user_id):
    trener_info = datebase.trener_info(user_id)
    trener_id = trener_info[0]
    text = f'Здравствуйте, {trener_info[2]}'


    btns = []
    if datebase.team_by_trener(trener_id):
        team_info = datebase.teaminfo_by_trener(trener_id)

        text += f'\n\nГлавный тренер команды "{team_info[1]}"'
        btns.append([InlineKeyboardButton(text=f'Рейтинг команды', callback_data=f'teamstatus_{team_info[0]}')])
        btns.append([InlineKeyboardButton(text=f'Статистика игр', callback_data=f'teamrange_{team_info[0]}')])
        btns.append([InlineKeyboardButton(text=f'Изменить состав', callback_data=f'teamchang_{team_info[0]}')])

    else:
        btns.append([InlineKeyboardButton(text='Заявить команду',
                                         callback_data='team_create')])

    markup = InlineKeyboardMarkup(row_width=2, inline_keyboard=btns)

    return text, markup



def teamsolo_info(team_id):
    info = datebase.teaminfo_by_id(team_id)
    trener_info = datebase.trener_info_by_id(info[3])
    type_ = datebase.vidsporta_type_by_team(team_id)
    text = 'Команда' if type_ else "Участник"
    text += f' - {info[1]} ' \
           f'\nВыступает за {info[2]}.' \
           f'\n\nГлавный тренер - {trener_info[2]} (квалификация-{trener_info[4]})'
    btns = []

    btns.append([InlineKeyboardButton(text=f'Результаты игр', callback_data=f'teamrange_{info[0]}')])
    btns.append([InlineKeyboardButton(text=f'Рейтинг', callback_data=f'teamstatus_{info[0]}')])
    btns.append([InlineKeyboardButton(text='Назад', callback_data=f'teamsvidsporta_{info[4]}')])
    markup = InlineKeyboardMarkup(row_width=2, inline_keyboard=btns)
    return text, markup







