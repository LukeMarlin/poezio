import theming

class DarkTheme(theming.Theme):
    COLOR_INFORMATION_BAR = (-1, 236)
    COLOR_STATUS_XA = (53, -1)
    COLOR_STATUS_AWAY = (214, -1)
    COLOR_STATUS_DND = (160, -1)
    COLOR_STATUS_CHAT = (34 , -1)
    COLOR_STATUS_UNAVAILABLE = (242 , -1)
    COLOR_STATUS_ONLINE = (27 , -1)
    COLOR_STATUS_NONE = (27 , -1)

    COLOR_VERTICAL_SEPARATOR = (236, -1)
    COLOR_NEW_TEXT_SEPARATOR = (213, -1)
    COLOR_MORE_INDICATOR = (6, 4)

    COLOR_TAB_NORMAL = (-1, 236)
    COLOR_TAB_NONEMPTY = (-1, 236)
    COLOR_TAB_CURRENT = (-1, 16)
    COLOR_TAB_COMPOSING = (3, 236)
    COLOR_TAB_NEW_MESSAGE = (3, 236)
    COLOR_TAB_HIGHLIGHT = (1, 236)
    COLOR_TAB_ATTENTION = (6, 236)
    COLOR_TAB_PRIVATE = (2, 236)
    COLOR_TAB_DISCONNECTED = (13, 236)
    COLOR_TAB_SCROLLED = (66, 236)

    COLOR_TOPIC_BAR = (-1, 236)
    COLOR_SCROLLABLE_NUMBER = (220, 236, 'b')
    COLOR_SELECTED_ROW = (-1, 238)
    COLOR_PRIVATE_NAME = (173, 236)
    COLOR_CONVERSATION_NAME = (2, 236)
    COLOR_CONVERSATION_RESOURCE = (58, 236)
    COLOR_GROUPCHAT_NAME = (106, 236)
    COLOR_COLUMN_HEADER = (36, 236)

    COLOR_VERTICAL_TAB_NORMAL = (240, -1)
    COLOR_VERTICAL_TAB_CURRENT = (-1, 236)
    COLOR_VERTICAL_TAB_NEW_MESSAGE = (3, -1)
    COLOR_VERTICAL_TAB_COMPOSING = (3, -1)
    COLOR_VERTICAL_TAB_HIGHLIGHT = (1, -1)
    COLOR_VERTICAL_TAB_PRIVATE = (2, -1)
    COLOR_VERTICAL_TAB_ATTENTION = (6, -1)
    COLOR_VERTICAL_TAB_DISCONNECTED = (13, -1)

    COLOR_INFORMATION_TEXT = (244, -1)
    COLOR_LOG_MSG = (244, -1)


theme = DarkTheme()


