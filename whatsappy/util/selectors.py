class Selectors:
    QR_CODE = 'div[data-testid="qrcode"]'

    ANIMATING = 'div.app-animating'
    
    SEARCH_BAR = 'div[data-testid="chat-list-search"]'
    SEARCH_BAR_CLEAR = 'button[aria-label="Cancel search"]'

    INFO_DRAWER = 'div[data-testid="chat-info-drawer"]'

    CHAT_HEADER = 'header[data-testid="conversation-header"]'
    CHAT_INFO_TEXT = INFO_DRAWER + ' span[dir="auto"].copyable-text.selectable-text'
    CHAT_INFO_PIC = INFO_DRAWER + ' section > div img'
    CHAT_DEFAULT_PIC = INFO_DRAWER + ' span[data-testid="default-user"]'

    GROUP_SUBJECT = INFO_DRAWER + ' div[data-testid="group-info-drawer-subject-input"]'
    GROUP_DEFAULT_PIC = INFO_DRAWER + ' span[data-testid="default-group"]'
    GROUP_INFO_PIC = CHAT_INFO_PIC

    UNREAD_BADGE = 'span[data-testid="icon-unread-count"]'
    UNREAD_TITLE = 'div[data-testid="cell-frame-title"] > span'
    UNREAD_LAST_MESSAGE = 'span[data-testid="last-msg-status"]'
    XPATH_UNREAD_CONVERSATIONS = '//span[@data-testid="icon-unread-count"]/ancestor::div[@data-testid="cell-frame-container"]'