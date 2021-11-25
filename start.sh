if [ -f ./tweets.json ]
then
    echo "tweets.json exist"
else
    touch tweets.json
    echo "tweets.json created" 
fi
if [ -f ./users.json ]
then
    echo "users.json exist"
else
    touch users.json
    echo "users.json created"
fi
source venv/bin/activate || .\venv\Scripts\activate
uvicorn main:app --reload