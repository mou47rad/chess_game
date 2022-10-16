import requests
import time
import urllib3
import io
import random







def get_ruselt(game_id, after_move, new_move, san):
	data = {'from':after_move,'to':new_move,'san':san,'promotion':'','game_id':game_id,'tte':'0'}
	login = s.get('https://chess.cool/play/with_computer/game',data=data, timeout=20)
	html = login.text
	html = str(html)
	begin = html.find('jsmoves&quot;:[')
	end   = html.find(']',begin)
	data = html[begin+len('jsmoves&quot;:['):end].strip()
	#print(data)
	with io.open('htm.html', 'w', encoding='utf-8') as f:
		f.write(str(login.text))
	data = data.split('{')

	for i in data:
		if 'from_cell' in i:
			begin = i.find('from_cell&quot;:&quot;')
			end   = i.find('&quot;,&quot',begin)
			from_cell = i[begin+len('from_cell&quot;:&quot;'):end].strip()
			#print(f'from cell {from_cell}')
		if 'to_cell' in i:
			begin = i.find('to_cell&quot;:&quot;')
			end   = i.find('&quot;,&quot',begin)
			to_cell = i[begin+len('to_cell&quot;:&quot;'):end].strip()
			#print(f'to cell: {to_cell}')

		try:
			print(f'from {from_cell} to > {to_cell}')
		except:
			pass

def send_move(game_id, after_move, new_move, san):
	data = {'from':after_move,'to':new_move,'san':san,'promotion':'','game_id': game_id,'tte':'0'}
	login = s.post('https://chess.cool/play/with_computer.html?action=submit_move', data=data, timeout=20)
	return login.text


s = requests.Session()
s.headers.update({
	'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	'accept-encoding':'gzip, deflate, br',
	'accept-language':'en-US,en;q=0.9,ar;q=0.8',
	'cache-control':'max-age=0',
	'content-length':'183',
	'content-type':'application/x-www-form-urlencoded',
	'origin':'https://chess.cool',
	'referer':'https://chess.cool/play/with_computer.html',
	'sec-ch-ua':'"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
	'sec-ch-ua-mobile':'?0',
	'sec-ch-ua-platform':'"Windows"',
	'sec-fetch-dest':'document',
	'sec-fetch-mode':'navigate',
	'sec-fetch-site':'same-origin',
	'sec-fetch-user':'?1',
	'upgrade-insecure-requests':'1',
	'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
	})


data = {'color':'1','ai_strength':'500','game_type':'1','position_type':'0','position_strength':'100','first_turn':'0','opening_id':'','opening_must_play':'0','limit_type':'0','limit_time_turn':'60','limit_time_game':'300','limit_plus':'1'}
login = s.post('https://chess.cool/play/with_computer.html?vk=&embed=&', data=data, timeout=20)

# get game id
time.sleep(5)
login = s.get('https://chess.cool/play/with_computer/game', data=data, timeout=20)
html = login.text
html = str(html)
begin = html.find('game_id" value="')
end   = html.find('" />',begin)
game_id = html[begin+len('game_id" value="'):end].strip()



s.headers.update({
	'accept':'application/json, text/javascript, */*; q=0.01',
	'accept-encoding':'gzip, deflate, br',
	'accept-language':'en-US,en;q=0.9',
	'content-length':'55',
	'content-type':'application/x-www-form-urlencoded; charset=UTF-8',
	'origin':'https://chess.cool',
	'referer':'https://chess.cool/play/with_computer/game',
	'sec-ch-ua':'"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
	'sec-ch-ua-mobile':'?0',
	'sec-ch-ua-platform':'"Windows"',
	'sec-fetch-dest':'empty',
	'sec-fetch-mode':'cors',
	'sec-fetch-site':'same-origin',
	'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
	'x-requested-with':'XMLHttpRequest',

	})


while True:
	after_move = str(input('after move: '))
	new_move   = str(input('new move: '))
	san        = str(input('Name: '))  	
	send_move(game_id, after_move, new_move, san)
	time.sleep(20)
	get_ruselt(game_id, after_move, new_move, san)



input('______main______')