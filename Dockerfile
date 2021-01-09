FROM python:3.6

ARG project_dir=/app/
ARG template_dir=/app/templates/

ADD requirements.txt $project_dir
ADD reply.py $project_dir
ADD templates/index.html $template_dir

WORKDIR $project_dir

RUN pip install flask
RUN pip install -r requirements.txt

CMD ["python", "reply.py"]