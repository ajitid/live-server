from bs4 import BeautifulSoup, Comment


def inject_live_server_script(path):
    with open(path) as fp:
        soup = BeautifulSoup(fp, features='html.parser')
        head = soup.find('head')
        if head is None:
            head_tag = soup.new_tag('head')
            soup.append(head_tag)
            head = soup.find('head')
        live_server_script_tag = soup.new_tag(
            name='script', attrs={'src': '/liveServer.js'})
        head.append(Comment('injected by live-server'))
        head.append(live_server_script_tag)
        b_soup = soup.encode()
        return b_soup
