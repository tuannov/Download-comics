from requests_html import HTMLSession
import os


def get_data(url,**kwargs):
    session = HTMLSession()
    resp = session.get(url, **kwargs)
    return resp


def download_image(resp):
    for chapter in resp.html.find('#nt_listchapter', first=True).find('div.col-xs-5.chapter'):
        name_chapter = chapter.text
        link_chapter = chapter.find('a', first=True).attrs['href']

        try:
            os.mkdir(os.path.join(os.getcwd(), name_chapter))
        except:
            break

        resp = get_data(link_chapter)

        for item in resp.html.find('div .reading-detail.box_doc', first=True).find('img'):
            link_image = 'http:' + item.attrs['src']
            name_image = item.attrs['alt'].split('-')[-1].strip()

            querystring = {"data": "net"}
            headers = {
                "Referer": "http://www.nettruyentop.com/",
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"
            }

            resp = get_data(link_image, headers=headers, params=querystring)
            
            with open(name_chapter + '/' + name_image + '.jpg', 'wb') as f:
                f.write(resp.content)


def main():
    url = 'http://www.nettruyentop.com/truyen-tranh/the-gioi-hoan-my/'
    resp = get_data(url)
    download_image(resp)
    print('Done')


if __name__ == '__main__':
    main()
