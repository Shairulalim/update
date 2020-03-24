import requests
import os

rs = requests.Session()

url = rs.get('https://api.kawalcorona.com')

data = url.json()

indo = data[37]['attributes']

negara = indo['Country_Region']
positif = indo['Confirmed']
mati = indo['Deaths']
sembuh = indo['Recovered']

def menu():
	os.system('clear')
	print('')
	print('    [ DATA KASUS CORONA DI INDONESIA ]')
	print('')
	print('    [•] Author  : shairul alim')
	print('    [•] Contact : WA : 085743664916')
	print('                  FB : syairul alim')
	print('    [•] Versi   : 1.0')
	print('')
	print("    [*] Data diambil dari 'https://kawalcorona.com'")
	print('')
	print('    ==================================')
	info()
	
def info():
	print('')
	print('    [•] Negara :',negara)
	print('    [•] Positif Corona : ' + str(positif) + ' orang')
	print('    [•] Meniggal : ' + str(mati) + ' orang')
	print('    [•] Sembuh : ' + str(sembuh) + ' orang')
	print('')
	print('    [ Terima Kasih Telah Menggunakan Tools ini ]')
	print('')
	print('    [*] Silahkan tunggu update selanjutnya [*]')
	print('')
menu()