# RIAT 
команды к серверу делал через CURL

Послать данные
curl --request POST --header 'Content-Type: application/json' --data '{"K":10,"Sums":[1.01,2.02],"Muls":[1,4]}' 'http://127.0.0.1:5000/PostInputData'

Получить решение
curl http://127.0.0.1:5000/GetAnswer
