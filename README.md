# kaggle-leaderboard-scraper
Scrape public leaderboard from competition for later use.

`/etc/systemd/system/kaggle-leaderboard-scraper.service`
```
[Unit]  
Description=Kaggle Leaderboard Scraper  
  
[Service]  
WorkingDirectory=/root/kaggle-leaderboard-scraper 
ExecStart=/bin/bash run.sh  
User=root  
```

`/etc/systemd/system/kaggle-leaderboard-scraper.timer`
```
[Unit]  
Description=Runs Kaggle Leaderboard Scraper every hour  
  
[Timer]  
OnCalendar=*-*-* *:*:00
Persistent=true  
  
[Install]  
WantedBy=timers.target  
```

```
systemctl daemon-reload  
systemctl start kaggle-leaderboard-scraper.timer  
systemctl enable kaggle-leaderboard-scraper.timer  
systemctl list-timers  
```