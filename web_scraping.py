import requests
import json
import os


FOLDER = os.path.dirname(os.path.realpath(__file__))
print(FOLDER)

def get_produtos_atuais():
    cookies = {
        'r_id': 'a12d946a-3781-440f-a7a5-92798ce300b2',
        'TestAB_Groups': 'sanityweb50_control.ds-web-vitals_enabled.ngage-chat-on-gallery_enabled.txp-fakedoor-buy-button_optreq.payg-discount-re-julius_ml-ranges.ppc-myplan-redirect-lp_control.goods-history-sales_enabled.ppf-free-insertion-re_enabled.ds-header-navbar_enabled.free-edtion-goods-parcela_control.delivery-quote-weight-11060_control.delivery-quote-weight-3040_control.txp-expanded-delivery-method_control.ape-profile-whatsapp-button_green.billing-history_enabled.pay-now-always_enabled.txp-retry-by-id-pay_enabled.adv-remocao-topo_enabled.ppf-myplan-new-marketplace-pos_enabled.payg-discount-julius_ml-ranges.imo-xp-linkshelf-autocomplete_enabled.ngage-chat-miniprofile_enabled.ppf-boost-motos_control.ngage-adview-miniprofile_enabled.delivery-methods-modal_enabled.re-home_enabled.bumpds-bjperformancetrackb_control.rec-adv-package_control.autospp-notshow-modal-hv-myads_enabled.adsxp-adviewlinks-bjQTZ-3020_control.ppf-edition-re_enabled.chatmod-logged-user-showphonebody_enabled.free-insertion-goods-parcela_control.contentmod-gallery-tip_control.imo-xp-adview-modules_priceInfoAtTop.acc-split-login-v2_control.rec-home-by-region_control.imo-xp-privatead_enabled.pos-cars-fee-boost_d-first',
        '__cf_bm': 'nzekBbmQeLCie6VgIqGmeXaoPHXIApp3WyiR67OboR0-1699395777-0-AcrzgNWJQT4Pc4vbjp6oSnWe4wUQ4YFh/qF3ef2+iAGXKIn2bzdAEsNZOc73OO8d340h4TWQ2EB6bZsMxz0wdGc=',
        'nl_id': 'e4e4db24-d552-4d02-87a7-329300459bd1',
        'mf_b837e449-83ee-457f-9ef5-8f976953f2bc': '||1699395778499||0||||0|0|11.8718',
        '_cfuvid': 'gXH6SbhpPUOjxh6lYjtLGQL57Z3PnOodRuG9THbHqt0-1699395778576-0-604800000',
        '_gcl_au': '1.1.1979680714.1699395779',
        '__rtbh.uid': '%7B%22eventType%22%3A%22uid%22%2C%22id%22%3A%22undefined%22%2C%22hash%22%3A%22wBiML0Lv0cEh18cEd5DU%22%7D',
        '__rtbh.lid': '%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22RavyBHxg1DSy8O1AsBJ1%22%7D',
        '_gid': 'GA1.3.1378729389.1699395779',
        '_gat_UA-70177409-2': '1',
        'lo_uid': '1699395778986-0qwk1nag170q',
        'l_id': 'e22b4ac4-13e4-40d9-9d6f-f0dbf31c7929',
        's_id': 'ecdb3b13-eb85-4506-99fa-c489847ff1482023-11-07T22:22:59.006Z',
        '_tt_enable_cookie': '1',
        '_ttp': 'j3lWfueKaWmDWgf5uYnXDQo-5dp',
        '_fbp': 'fb.2.1699395779135.1548978064',
        'lotame_domain_check': 'olx.com.br',
        '_ga_50C013M2CC': 'GS1.1.1699395778.1.1.1699395785.53.0.0',
        '_ga': 'GA1.3.2061553644.1699395779',
        '_cc_id': '9d6a960bcf453ac4a853c07f8aab1bd2',
        'panoramaId_expiry': '1700000585763',
        'panoramaId': '2a1b4be31881675c7b1f34a86c4c16d5393834f4b05f6a2cca0d740c9154b208',
        'panoramaIdType': 'panoIndiv',
        'cto_bundle': 'JSIGmF9Qa0pMSFN5T2V5NUVQcVJZd1NZaGx4UGliNW1KMHNhblNuNDdCYnBReVVHNVpMNTdaMXZQMm5zSDJRZXIlMkZqdTlRcFd3aGtKOVpzS0t3Y0JoODJSS21QYXolMkY1Sko0MzdDbnkxOUJJWnk5cnhodGZzR0ZDVTQlMkZOOEVjWlJtSlIlMkY2',
        'nvg83482': '139a29ed0ddef1610ddc827e6a10|0_312',
        '__gpi': 'UID=00000a42eb570a55:T=1699395788:RT=1699395788:S=ALNI_MagTvRkCH0hRv7EWTa6AF--WMPLfw',
        '__gads': 'ID=1c24b0be82ae687a-229022b4e7e700d5:T=1699395788:RT=1699395789:S=ALNI_MYYYkc8IV10nTQ7GqLUqldjcEg4IA',
        '_dd_s': 'rum=0&expire=1699396689858',
    }

    headers = {
        'authority': 'www.olx.com.br',
        'accept': '*/*',
        'accept-language': 'pt-BR,pt;q=0.9',
        # 'cookie': 'r_id=a12d946a-3781-440f-a7a5-92798ce300b2; TestAB_Groups=sanityweb50_control.ds-web-vitals_enabled.ngage-chat-on-gallery_enabled.txp-fakedoor-buy-button_optreq.payg-discount-re-julius_ml-ranges.ppc-myplan-redirect-lp_control.goods-history-sales_enabled.ppf-free-insertion-re_enabled.ds-header-navbar_enabled.free-edtion-goods-parcela_control.delivery-quote-weight-11060_control.delivery-quote-weight-3040_control.txp-expanded-delivery-method_control.ape-profile-whatsapp-button_green.billing-history_enabled.pay-now-always_enabled.txp-retry-by-id-pay_enabled.adv-remocao-topo_enabled.ppf-myplan-new-marketplace-pos_enabled.payg-discount-julius_ml-ranges.imo-xp-linkshelf-autocomplete_enabled.ngage-chat-miniprofile_enabled.ppf-boost-motos_control.ngage-adview-miniprofile_enabled.delivery-methods-modal_enabled.re-home_enabled.bumpds-bjperformancetrackb_control.rec-adv-package_control.autospp-notshow-modal-hv-myads_enabled.adsxp-adviewlinks-bjQTZ-3020_control.ppf-edition-re_enabled.chatmod-logged-user-showphonebody_enabled.free-insertion-goods-parcela_control.contentmod-gallery-tip_control.imo-xp-adview-modules_priceInfoAtTop.acc-split-login-v2_control.rec-home-by-region_control.imo-xp-privatead_enabled.pos-cars-fee-boost_d-first; __cf_bm=nzekBbmQeLCie6VgIqGmeXaoPHXIApp3WyiR67OboR0-1699395777-0-AcrzgNWJQT4Pc4vbjp6oSnWe4wUQ4YFh/qF3ef2+iAGXKIn2bzdAEsNZOc73OO8d340h4TWQ2EB6bZsMxz0wdGc=; nl_id=e4e4db24-d552-4d02-87a7-329300459bd1; mf_b837e449-83ee-457f-9ef5-8f976953f2bc=||1699395778499||0||||0|0|11.8718; _cfuvid=gXH6SbhpPUOjxh6lYjtLGQL57Z3PnOodRuG9THbHqt0-1699395778576-0-604800000; _gcl_au=1.1.1979680714.1699395779; __rtbh.uid=%7B%22eventType%22%3A%22uid%22%2C%22id%22%3A%22undefined%22%2C%22hash%22%3A%22wBiML0Lv0cEh18cEd5DU%22%7D; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22RavyBHxg1DSy8O1AsBJ1%22%7D; _gid=GA1.3.1378729389.1699395779; _gat_UA-70177409-2=1; lo_uid=1699395778986-0qwk1nag170q; l_id=e22b4ac4-13e4-40d9-9d6f-f0dbf31c7929; s_id=ecdb3b13-eb85-4506-99fa-c489847ff1482023-11-07T22:22:59.006Z; _tt_enable_cookie=1; _ttp=j3lWfueKaWmDWgf5uYnXDQo-5dp; _fbp=fb.2.1699395779135.1548978064; lotame_domain_check=olx.com.br; _ga_50C013M2CC=GS1.1.1699395778.1.1.1699395785.53.0.0; _ga=GA1.3.2061553644.1699395779; _cc_id=9d6a960bcf453ac4a853c07f8aab1bd2; panoramaId_expiry=1700000585763; panoramaId=2a1b4be31881675c7b1f34a86c4c16d5393834f4b05f6a2cca0d740c9154b208; panoramaIdType=panoIndiv; cto_bundle=JSIGmF9Qa0pMSFN5T2V5NUVQcVJZd1NZaGx4UGliNW1KMHNhblNuNDdCYnBReVVHNVpMNTdaMXZQMm5zSDJRZXIlMkZqdTlRcFd3aGtKOVpzS0t3Y0JoODJSS21QYXolMkY1Sko0MzdDbnkxOUJJWnk5cnhodGZzR0ZDVTQlMkZOOEVjWlJtSlIlMkY2; nvg83482=139a29ed0ddef1610ddc827e6a10|0_312; __gpi=UID=00000a42eb570a55:T=1699395788:RT=1699395788:S=ALNI_MagTvRkCH0hRv7EWTa6AF--WMPLfw; __gads=ID=1c24b0be82ae687a-229022b4e7e700d5:T=1699395788:RT=1699395789:S=ALNI_MYYYkc8IV10nTQ7GqLUqldjcEg4IA; _dd_s=rum=0&expire=1699396689858',
        'referer': 'https://www.olx.com.br/estado-sc?q=game%20boy&cg=3020',
        'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        'x-nextjs-data': '1',
    }

    params = {
        'q': 'game boy',
        'route': 'estado-sc',
    }

    response = requests.get(
        'https://www.olx.com.br/_next/data/Azzcb4OhXaKqjpbS7yL_k/pt-BR/videogames/estado-sc.json',
        params=params,
        cookies=cookies,
        headers=headers,
    )

    lista_produtos = response.json()["pageProps"]["ads"]

    return lista_produtos

def get_produtos_resumidos():
    lista_produtos_atual = []

    for produto in lista_produtos:
        if not "title" in produto:
            continue
        lista_produtos_atual.append({
            "listId": produto["listId"],
            "title": produto["title"],
            "url": produto["url"],
            "price": produto["price"],
        })
    return lista_produtos_atual

def get_produtos_antigos():
    lista_antiga_produtos = []
    with open(FOLDER + "/ads.json", "r+") as file:
        lista_antiga_produtos = json.loads(file.read())
    return lista_antiga_produtos

def get_produtos_novos(lista_produtos_atual, lista_antiga_produtos):
    lista_produtos_novos = []
    for produto_novo in lista_produtos_atual:
        if not produto_novo in lista_antiga_produtos:
            lista_produtos_novos.append(produto_novo)
    
    return lista_produtos_novos

def notificar_produto_novo(produto_novo):
    TELEGRAM_TOKEN = "TOKEN"
    CHAT_ID = 0

    url = "https://api.telegram.org/bot{}/sendMessage".format(TELEGRAM_TOKEN)

    print(produto_novo["title"])
    message = "Produto novo! {}\nURL: {}\nPreço: {}".format(produto_novo["title"], produto_novo["url"], produto_novo["price"])
    requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": message
    })

if __name__ == "__main__":
    lista_produtos = get_produtos_atuais()
    lista_produtos_atual = get_produtos_resumidos()
    lista_antiga_produtos = get_produtos_antigos()
    lista_produtos_novos = get_produtos_novos(lista_produtos_atual, lista_antiga_produtos)

    with open(FOLDER + "/ads.json", "w+") as file:
        file.write(json.dumps(lista_produtos_atual))

    for produto_novo in lista_produtos_novos:
        notificar_produto_novo(produto_novo)
