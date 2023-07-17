
# gunicorn --bind 127.0.0.1:8000 -w 1 -k uvicorn.workers.UvicornWorker channel:app --daemon

#debug mode
#uvicorn channel:app --reload --host 127.0.0.1 --port 8000

# sleep 1
# echo "Wa Channel Alive!"

# nohup python worker.py >> worker.out &


