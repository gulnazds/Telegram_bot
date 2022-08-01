FROM python:slim
ENV TOKEN
COPY . .   
#откуда и куда, можно папки прописывать и тд
RUN pip install -r req.txt
#CMD ['python','bot.py'] или
CMD python bot.py
