from google_play_scraper import Sort, reviews 
import csv 
from datetime import datetime 
import schedule 
import logging 
import time 
from utils.logger import setup_basic_logger

# Set up Logging 
setup_basic_logger()

def scrape_play_store_reviews(appId,bankName,exportFileName): 
    APP_ID = appId
    logging.info("Fetching reviews...") 
    try: 
        results, _ = reviews( 
            APP_ID, 
            lang='en', 
            country='us', 
            sort=Sort.NEWEST,  # FIXED: 'sort' not 'cort'
            count=5000, 
            filter_score_with=None 
        )

        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'../data/{exportFileName}_{timestamp}.csv' 
        
        with open(filename, mode='w', newline='', encoding='utf-8') as file: 
            writer = csv.DictWriter(file, fieldnames=['review_text', 'rating', 'date', 'bank_name', 'source']) 
            writer.writeheader()

            for entry in results: 
                writer.writerow({ 
                    'review_text': entry['content'], 
                    'rating': entry['score'], 
                    'date': entry['at'].strftime('%Y-%m-%d'), 
                    'bank_name': bankName, 
                    'source': 'Google Play' 
                }) 
        
        logging.info(f"Saved {len(results)} reviews to {filename}") 
    except Exception as e: 
        logging.error(f"Error occurred: {e}") 


# === Schedule the job outside the function ===
schedule.every().day.at("16:18").do(lambda: scrape_play_store_reviews('com.dashen.dashensuperapp','Dashen Bank of Ethiopia','Dashen'))  # Daily at 4:18 PM
schedule.every().day.at("16:18").do(lambda: scrape_play_store_reviews('com.boa.boaMobileBanking','Bank of Abyssinia','Abyssinia'))  # Daily at 4:18 PM
schedule.every().day.at("16:18").do(lambda: scrape_play_store_reviews('com.combanketh.mobilebanking','Commercial Bank of Ethiopia','Commercial'))  # Daily at 4:18 PM

# schedule.every(6).hours.do(scrape_play_store_reviews)         # Every 6 hours
# schedule.every().monday.do(scrape_play_store_reviews)         # Every Monday
# schedule.every().hour.do(scrape_play_store_reviews)           # Every hour

# === Initial immediate run (optional) ===
# scrape_play_store_reviews()

while True: 
    schedule.run_pending() 
    time.sleep(1)
