# Description: build a lightweight log callback collector.
#
# Copyright (c) 2024-2025 honeok <honeok@duck.com>
#
# Licensed under the GNU General Public License, Version 3 or later.
# This program is distributed WITHOUT ANY WARRANTY.
# See <https://www.gnu.org/licenses/gpl-3.0.en.html>.

FROM python:3-alpine
WORKDIR /signalhub
COPY . .
RUN apk upgrade \
    && apk add --no-cache --virtual .build-deps \
        build-base \
        mariadb-connector-c-dev \
    && apk add --no-cache tzdata \
    && python3 -m pip install --no-cache-dir -r requirements.txt --root-user-action=ignore \
    && mkdir -p instance \
    && apk del .build-deps \
    && rm -rf /var/cache/apk/* /tmp/*
ENV FLASK_APP=app.py
ENV FLASK_ENV=production
ENV DB_TYPE=sqlite
ENV TZ=Asia/Shanghai
EXPOSE 5000
ENTRYPOINT ["gunicorn"]
CMD ["-w", "4", "-b", "0.0.0.0:5000", "app:app"]