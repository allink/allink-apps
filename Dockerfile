# <DOCKER_FROM>  # Warning: text inside the DOCKER_FROM tags is auto-generated. Manual changes will be overwritten.
FROM aldryn/base-project:3.18
# </DOCKER_FROM>
#ENV /app/allink_cmsplugins:

# node modules
# ------------
# package.json is put into / so that mounting /app for local
# development does not require re-running npm install
# ENV PATH=/node_modules/.bin:$PATH
# RUN npm install -g npm-install-retry
# COPY package.json /
# RUN (cd / && npm-install-retry -- --production && rm -rf /tmp/*)

# python requirements
# -------------------
ENV PIP_INDEX_URL=${PIP_INDEX_URL:-https://wheels.aldryn.net/v1/aldryn-extras+pypi/aldryn-baseproject/+simple/} \
    WHEELSPROXY_URL=${WHEELSPROXY_URL:-https://wheels.aldryn.net/v1/aldryn-extras+pypi/aldryn-baseproject/}
COPY requirements.* /app/
COPY addons-dev /app/addons-dev/
RUN pip-reqs compile && \
    pip-reqs resolve && \
    pip install \
        --no-index --no-deps \
        --requirement requirements.urls

# add full sourcecode
# -------------------
COPY . /app

# collectstatic
# -------------
RUN DJANGO_MODE=build python manage.py collectstatic --noinput


