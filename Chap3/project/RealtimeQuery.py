import requests, json
from requestweather import fetchWeather

def query_realtime(city):
	'''query realtime weather'''
	r = fetchWeather(city)
	result = json.loads(r)
	temperature = result["results"][0]['now']['temperature']
	weather = result["results"][0]['now']['text']
	get_weather = [city,  weather , temperature + "���϶�"]
	log_append(str(get_weather[0]) + str(get_weather[1]) + str(get_weather[2]))
	return get_weather

def documentation(filename):
	'''��ӡfilename�ĵ�������'''
	with open(filename, "r", encoding = "utf-8") as f:
		return f.read()

def log():
	'''������־�ļ�'''
	with open("log.txt", "w", encoding = "utf-8") as f:
		f.write("���Ĳ�ѯ��¼���£�\n")

def log_append(content):
	'''������־��¼'''
	with open("log.txt", "a", encoding = "utf-8") as f:
		f.write(content + "\n")

if __name__ == "__main__":
	while True:
		user_input = input("��������л�ָ�")

		if user_input in {"quit", "exit"}:
			break
		elif user_input == "history":
			print(documentation("log.txt"))
		elif user_input == "help":
			print(documentation("README.md"))
		else:
			print(query_realtime(user_input))



