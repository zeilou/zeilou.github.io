cd /root/zeilou.io/ && python3 main.py
cd /root/zeilou.io/docs && cp -rf .vuepress/dist/* . && git pull origin master && git add -A && git commit -m "latest" && git push origin master
