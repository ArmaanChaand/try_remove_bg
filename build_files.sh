echo "Build Start"
python3.9 -m pip install -r requirements.txt
python3.9 -m pip manage.py collectstatic --noinput --clear
echo "Build End"