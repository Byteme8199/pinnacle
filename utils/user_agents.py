#import logging

#logger = logging.getLogger('custom')


def is_amazon_webview(user_agent):
    '''
    Check if the client is an Amazon WebView.

    See the amazon developer page for specific user agents:
    https://developer.amazon.com/sdk/webapps/faq.html#distribution

    :param user_agent A string with the user agent to check
    :return boolean
    '''
    if 'amazonwebapp' in user_agent.lower():
        return True
    else:
        return False


def check_request_amazon(request):
    '''

    :param request:
    :return: boolean
    '''
    if request.META.get('HTTP_USER_AGENT'):
        return is_amazon_webview(request.META.get('HTTP_USER_AGENT'))
    else:
        return False


def is_android_webview(user_agent):
    '''
    Check if the client is an Android WebView.

    :param user_agent A string with the user agent to check
    :return boolean
    '''
    if 'wgerandroidwebapp' in user_agent.lower():
        return True
    else:
        return False


def check_request_android(request):
    '''

    :param request:
    :return: boolean
    '''
    if request.META.get('HTTP_USER_AGENT'):
        return is_android_webview(request.META.get('HTTP_USER_AGENT'))
    else:
        return False
