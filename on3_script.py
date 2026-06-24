import asyncio
import aiohttp
import pandas as pd
import re
import time
import os
import json
import undetected_chromedriver as uc
from datetime import datetime
from bs4 import BeautifulSoup
from tqdm.asyncio import tqdm_asyncio
from tqdm import tqdm

# --- CONFIGURATION ---
CLASS_YEAR = "2027"
PAGE_LIMIT = None 
CONCURRENT_LIMIT = 15
HISTORY_FILE = "recruits_history.csv" 
OUTPUT_FILE = "recruiting_board.xlsx" 

# --- GEOGRAPHY ---
US_STATE_TO_ABBREV = {
    "Alabama": "AL", "Alaska": "AK", "Arizona": "AZ", "Arkansas": "AR", "California": "CA",
    "Colorado": "CO", "Connecticut": "CT", "Delaware": "DE", "Florida": "FL", "Georgia": "GA",
    "Hawaii": "HI", "Idaho": "ID", "Illinois": "IL", "Indiana": "IN", "Iowa": "IA",
    "Kansas": "KS", "Kentucky": "KY", "Louisiana": "LA", "Maine": "ME", "Maryland": "MD",
    "Massachusetts": "MA", "Michigan": "MI", "Minnesota": "MN", "Mississippi": "MS", "Missouri": "MO",
    "Montana": "MT", "Nebraska": "NE", "Nevada": "NV", "New Hampshire": "NH", "New Jersey": "NJ",
    "New Mexico": "NM", "New York": "NY", "North Carolina": "NC", "North Dakota": "ND", "Ohio": "OH",
    "Oklahoma": "OK", "Oregon": "OR", "Pennsylvania": "PA", "Rhode Island": "RI", "South Carolina": "SC",
    "South Dakota": "SD", "Tennessee": "TN", "Texas": "TX", "Utah": "UT", "Vermont": "VT",
    "Virginia": "VA", "Washington": "WA", "West Virginia": "WV", "Wisconsin": "WI", "Wyoming": "WY",
    "District of Columbia": "DC"
}

EAST_COAST_STATES = {
    "VA", "NC", "FL", "WV", "DC", "MD", "GA", "DE", "PA", "NJ", "NY", "OH", "SC", "TN"
}

# --- SCHOOL LISTS (D1 VALIDATION) ---
P4_SCHOOLS = {
    "Alabama", "Arkansas", "Auburn", "Florida", "Georgia", "Kentucky", "LSU", "Mississippi State", "Missouri", "Oklahoma", "Ole Miss", "South Carolina", "Tennessee", "Texas", "Texas A&M", "Vanderbilt",
    "Illinois", "Indiana", "Iowa", "Maryland", "Michigan", "Michigan State", "Minnesota", "Nebraska", "Northwestern", "Ohio State", "Oregon", "Penn State", "Purdue", "Rutgers", "UCLA", "USC", "Washington", "Wisconsin",
    "Boston College", "California", "Clemson", "Duke", "Florida State", "Georgia Tech", "Louisville", "Miami", "North Carolina", "NC State", "Pittsburgh", "SMU", "Stanford", "Syracuse", "Virginia", "Virginia Tech", "Wake Forest", "Notre Dame",
    "Arizona", "Arizona State", "Baylor", "BYU", "Cincinnati", "Colorado", "Houston", "Iowa State", "Kansas", "Kansas State", "Oklahoma State", "TCU", "Texas Tech", "UCF", "Utah", "West Virginia"
}

G5_SCHOOLS = {
    "Army", "Charlotte", "East Carolina", "Florida Atlantic", "Memphis", "Navy", "North Texas", "Rice", "South Florida", "Temple", "Tulane", "Tulsa", "UAB", "UTSA", "Wichita State",
    "FIU", "Jacksonville State", "Liberty", "Louisiana Tech", "Middle Tennessee", "New Mexico State", "Sam Houston", "UTEP", "Western Kentucky", "Kennesaw State",
    "Akron", "Ball State", "Bowling Green", "Buffalo", "Central Michigan", "Eastern Michigan", "Kent State", "Miami (OH)", "Northern Illinois", "Ohio", "Toledo", "Western Michigan",
    "Air Force", "Boise State", "Colorado State", "Fresno State", "Hawaii", "Nevada", "New Mexico", "San Diego State", "San Jose State", "UNLV", "Utah State", "Wyoming",
    "Appalachian State", "Arkansas State", "Coastal Carolina", "Georgia Southern", "Georgia State", "James Madison", "Louisiana", "Louisiana-Monroe", "Marshall", "Old Dominion", "South Alabama", "Southern Miss", "Texas State", "Troy",
    "UConn", "UMass"
}

FCS_SCHOOLS = {
    "Cal Poly", "Eastern Washington", "Idaho", "Idaho State", "Montana", "Montana State", "Northern Arizona", "Northern Colorado", "Portland State", "Sacramento State", "UC Davis", "Weber State",
    "Charleston Southern", "Eastern Illinois", "Gardner-Webb", "Lindenwood", "Southeast Missouri State", "Tennessee State", "Tennessee Tech", "UT Martin", "Western Illinois",
    "Albany", "Campbell", "Delaware", "Elon", "Hampton", "Maine", "Monmouth", "New Hampshire", "North Carolina A&T", "Rhode Island", "Richmond", "Stony Brook", "Towson", "Villanova", "William & Mary", "Bryant",
    "Brown", "Columbia", "Cornell", "Dartmouth", "Harvard", "Penn", "Princeton", "Yale",
    "Delaware State", "Howard", "Morgan State", "Norfolk State", "North Carolina Central", "South Carolina State",
    "Illinois State", "Indiana State", "Missouri State", "Murray State", "North Dakota", "North Dakota State", "Northern Iowa", "South Dakota", "South Dakota State", "Southern Illinois", "Youngstown State",
    "Central Connecticut", "Duquesne", "LIU", "Merrimack", "Sacred Heart", "Saint Francis (PA)", "Stonehill", "Wagner",
    "Bucknell", "Colgate", "Fordham", "Georgetown", "Holy Cross", "Lafayette", "Lehigh",
    "Butler", "Davidson", "Dayton", "Drake", "Marist", "Morehead State", "Presbyterian", "San Diego", "St. Thomas (MN)", "Stetson", "Valparaiso",
    "Chattanooga", "The Citadel", "East Tennessee State", "Furman", "Mercer", "Samford", "VMI", "Western Carolina", "Wofford",
    "Houston Christian", "Incarnate Word", "Lamar", "McNeese", "Nicholls", "Northwestern State", "Southeastern Louisiana", "Texas A&M-Commerce",
    "Alabama A&M", "Alabama State", "Alcorn State", "Arkansas-Pine Bluff", "Bethune-Cookman", "Florida A&M", "Grambling State", "Jackson State", "Mississippi Valley State", "Prairie View A&M", "Southern", "Texas Southern",
    "Abilene Christian", "Austin Peay", "Central Arkansas", "Eastern Kentucky", "North Alabama", "Southern Utah", "Stephen F. Austin", "Tarleton State", "Utah Tech", "West Georgia"
}

ALL_D1_SCHOOLS = P4_SCHOOLS | G5_SCHOOLS | FCS_SCHOOLS

def normalize_name(name):
    if not name: return ""
    clean = re.sub(r'\b(jr\.?|sr\.?|ii|iii|iv)\b', '', name, flags=re.IGNORECASE)
    clean = re.sub(r'[^\w\s]', '', clean)
    return " ".join(clean.lower().split())

def count_p4_offers(offer_list):
    count = 0
    for offer in offer_list:
        if offer in P4_SCHOOLS:
            count += 1
        else:
            for p4 in P4_SCHOOLS:
                if p4 in offer: 
                    count += 1; break
    return count

def is_d1_offer(offer_name):
    if offer_name in ALL_D1_SCHOOLS: return True
    for school in ALL_D1_SCHOOLS:
        if school in offer_name or offer_name in school:
            return True
    return False

# --- BROWSER SETUP (ROBUST) ---
def get_selenium_cookies(url):
    print(f"Launching ghost browser for: {url}")
    options = uc.ChromeOptions()
    options.add_argument("--headless")
    
    driver = None
    cookies, ua, build_id = {}, "", None
    
    try:
        driver = uc.Chrome(options=options, version_main=122)
        driver.get(url)
        time.sleep(3) 
        if "on3.com" in url:
            try:
                next_data = driver.execute_script("return document.getElementById('__NEXT_DATA__').textContent")
                if next_data:
                    json_data = json.loads(next_data)
                    build_id = json_data.get('buildId')
                    print(f"  [+] Detected Build ID: {build_id}")
            except: pass
        cookies = {c['name']: c['value'] for c in driver.get_cookies()}
        ua = driver.execute_script("return navigator.userAgent;")
    finally:
        if driver:
            try:
                driver.quit()
            except: 
                pass
            driver.quit = lambda: None 
            
    return cookies, ua, build_id

# --- SEMAPHORE WRAPPER ---
async def fetch_with_semaphore(semaphore, func, *args, **kwargs):
    async with semaphore: return await func(*args, **kwargs)

# --- SCRAPERS ---
class TwoFourSevenScraper:
    def __init__(self, cookies, user_agent):
        self.cookies = cookies
        self.base_url = f"https://247sports.com/season/{CLASS_YEAR}-football/recruits.json"
        self.headers = {"User-Agent": user_agent, "Accept": "application/json"}

    async def fetch_page(self, session, page):
        params = {'Items': 15, 'Page': page, 'Conf': 'all'}
        try:
            async with session.get(self.base_url, params=params, cookies=self.cookies) as resp:
                if resp.status == 200: return await resp.json()
        except: pass
        return []

    async def fetch_offers(self, session, url):
        if not url: return []
        offers = []
        try:
            async with session.get(url, cookies=self.cookies) as resp:
                if resp.status == 200:
                    html = await resp.text()
                    soup = BeautifulSoup(html, 'html.parser')
                    interest_list = soup.find("ul", class_="recruit-interest-index_lst")
                    if interest_list:
                        for li in interest_list.find_all("li"):
                            offer_span = li.select_one(".secondary_blk .offer")
                            if offer_span and "Yes" in offer_span.get_text(strip=True):
                                img = li.find("img")
                                if img and img.get("alt"): offers.append(img["alt"])
        except: pass
        return offers

    async def get_data(self, semaphore):
        async with aiohttp.ClientSession(headers=self.headers) as session:
            players = []
            page = 1
            with tqdm(desc="247 List", unit="pg") as pbar:
                while True:
                    if PAGE_LIMIT and page > PAGE_LIMIT: break
                    data = await fetch_with_semaphore(semaphore, self.fetch_page, session, page)
                    if not data: break
                    for p_obj in data:
                        if not isinstance(p_obj, dict): continue

                        p = p_obj.get('Player')
                        if not isinstance(p, dict): continue

                        if p.get('StarRating', 0) >= 5: continue 
                        hometown = p.get('Hometown') or {}
                        state_full = hometown.get('State') if isinstance(hometown, dict) else "N/A"
                        state_abbr = US_STATE_TO_ABBREV.get(state_full, state_full) #type: ignore
                        
                        # --- ROBUST POSITION (PRIORITY CHECK) ---
                        pos_abbr = "N/A"
                        # 1. Check PrimaryPlayerPosition -> Abbreviation (User Preference)
                        pos_obj = p_obj.get('PrimaryPlayerPosition')
                        if isinstance(pos_obj, dict):
                            pos_abbr = pos_obj.get('Abbreviation')
                        
                        # 2. Fallback to 'Position' key
                        if not pos_abbr or pos_abbr == "N/A":
                            pos_obj = p_obj.get('Position')
                            if isinstance(pos_obj, dict):
                                pos_abbr = pos_obj.get('Abbreviation')

                        players.append({
                            "name": p.get('FullName'),
                            "normalized": normalize_name(p.get('FullName')),
                            "id": str(p_obj.get('Key')),
                            "school": p.get('PlayerHighSchool', {}).get('Name'),
                            "state": state_abbr, 
                            "position": pos_abbr,
                            "height": p.get('Height'),
                            "weight": p.get('Weight'),
                            "stars": p.get('StarRating'),
                            "profile_url": p.get('Url'),
                            "offer_url": p_obj.get('RecruitInterestsUrl')
                        })
                    pbar.update(1)
                    page += 1
            tasks = [fetch_with_semaphore(semaphore, self.fetch_offers, session, p['offer_url']) for p in players]
            print("247: Fetching offers...")
            results = await tqdm_asyncio.gather(*tasks, desc="247 Offers", unit="player")
            for i, offers in enumerate(results): players[i]['offers'] = offers
            return players

class On3Scraper:
    def __init__(self, cookies, build_id):
        self.cookies = cookies
        self.base_url = f"https://www.on3.com/_next/data/{build_id}/rivals" if build_id else None
        self.headers = {"User-Agent": "Mozilla/5.0"}

    async def fetch_details(self, session, slug):
        url = f"{self.base_url}/{slug}.json"
        try:
            async with session.get(url, params={"id": slug}, cookies=self.cookies) as resp:
                if resp.status == 200: return await resp.json()
        except: pass
        return None

    async def get_data(self, semaphore):
        if not self.base_url: return []
        async with aiohttp.ClientSession(headers=self.headers) as session:
            players = []
            page = 1
            with tqdm(desc="On3 List", unit="pg") as pbar:
                while True:
                    if PAGE_LIMIT and page > PAGE_LIMIT: break
                    url = f"{self.base_url}/search.json"
                    params = {"minClassYear": CLASS_YEAR, "maxClassYear": CLASS_YEAR, 
                              "sportKey": "1", "maxStars": "4", "minStars": "3", "page": page}
                    async with semaphore:
                        async with session.get(url, params=params, cookies=self.cookies) as resp:
                            if resp.status != 200: break
                            data = await resp.json()
                    
                    raw = data.get('pageProps', {}).get('searchData', {}).get('list', [])
                    if not raw: break
                    for p in raw:
                        if not isinstance(p, dict): continue
                        
                        rating = p.get('rating')
                        stars = rating.get('stars', 0) if isinstance(rating, dict) else 0
                        if stars >= 5: continue
                        
                        players.append({
                            "key": str(p.get('key')),
                            "slug": p.get('slug'),
                            "name": f"{p.get('firstName')} {p.get('lastName')}",
                            "normalized": normalize_name(f"{p.get('firstName')} {p.get('lastName')}")
                        })
                    pbar.update(1)
                    page += 1
            tasks = [fetch_with_semaphore(semaphore, self.fetch_details, session, p['slug']) for p in players]
            print("On3: Fetching details...")
            responses = await tqdm_asyncio.gather(*tasks, desc="On3 Details", unit="player")
            processed = []
            for i, resp in enumerate(responses):
                if isinstance(resp, BaseException) or not resp: continue
                try:
                    d = resp; 
                    if not isinstance(d, dict): continue
                    props = d.get('pageProps', {})
                    p_info = props.get('player', {})
                    if not isinstance(p_info, dict): continue

                    offers = set()
                    top_teams = props.get('topTeams', {})
                    if isinstance(top_teams, dict):
                        team_list = top_teams.get('list', [])
                        if isinstance(team_list, list):
                            for item in team_list:
                                if not isinstance(item, dict): continue
                                org = item.get('team') or item.get('organization')
                                if isinstance(org, dict) and item.get('status') == "Offered": 
                                    offers.add(org.get('name'))
                    
                    asset = p_info.get('defaultAsset') or {}
                    headshot = f"https://on3static.com{asset.get('source')}" if isinstance(asset, dict) and asset.get('source') else None
                    
                    hs = p_info.get('highSchool') or {}
                    school_name = hs.get('name') if isinstance(hs, dict) else "N/A"
                    ht = p_info.get('hometownState') or {}
                    state_abbr = ht.get('abbreviation') if isinstance(ht, dict) else "N/A"

                    pos_abbr = p_info.get('positionAbbreviation')
                    if not pos_abbr:
                        pos_obj = p_info.get('position')
                        if isinstance(pos_obj, dict):
                            pos_abbr = pos_obj.get('abbreviation') or pos_obj.get('name')

                    processed.append({
                        "name": p_info.get('name'),
                        "normalized": normalize_name(p_info.get('name')),
                        "id": players[i]['key'],
                        "school": school_name,
                        "position": pos_abbr,
                        "height": p_info.get('height'),
                        "weight": p_info.get('weight'),
                        "stars": (p_info.get('ranking') or {}).get('stars') if isinstance(p_info.get('ranking'), dict) else 0,
                        "headshot": headshot,
                        "profile_url": f"https://www.on3.com/db/{players[i]['slug']}/", 
                        "offers": list(offers),
                        "state": state_abbr
                    })
                except Exception as e: 
                    pass
            return processed

# --- HISTORY LOGIC ---
def load_id_cache(history_file):
    seen_on3, seen_247, history_offers = set(), set(), {}
    if os.path.exists(history_file):
        try:
            df = pd.read_csv(history_file, dtype=str)
            if 'On3_ID' in df.columns: seen_on3 = set(df['On3_ID'].dropna().unique())
            if '247_ID' in df.columns: seen_247 = set(df['247_ID'].dropna().unique())
            for _, row in df.iterrows():
                name_key = normalize_name(row.get('Name', ''))
                offers_str = str(row.get('Offers_List', ''))
                history_offers[name_key] = set(offers_str.split(", ")) if offers_str != "nan" else set()
        except Exception as e: print(f"Cache Error: {e}")
    return seen_on3, seen_247, history_offers

def compare_with_history(current_data, seen_on3, seen_247, history_offers):
    updated_data = []
    for player in current_data:
        norm_name = normalize_name(player['Name'])
        current_offers = set(player['Offers_List'].split(", ")) if player['Offers_List'] else set()
        
        is_known = False
        if str(player.get('On3_ID', 'N/A')) in seen_on3: is_known = True
        if str(player.get('247_ID', 'N/A')) in seen_247: is_known = True
        is_new_player = not is_known
        
        if not is_new_player:
            old_offers = history_offers.get(norm_name, set())
            added = current_offers - old_offers
            removed = old_offers - current_offers
            changes = []
            if added: changes.append(f"Added: {list(added)}")
            if removed: changes.append(f"Removed: {list(removed)}")
            player['New Offers'] = "; ".join(changes)
            player['Prev_Offer_Count'] = len(old_offers)
            player['Recent_Offers_Raw'] = list(added)
        else:
            player['New Offers'] = ""
            player['Prev_Offer_Count'] = 0
            player['Recent_Offers_Raw'] = list(current_offers)
        
        player['New Player'] = "Yes" if is_new_player else "No"
        updated_data.append(player)
    return updated_data

# --- FIRST D1 OFFER TAB LOGIC ---
def get_first_d1_offer_tab(df):
    df_new = df[df['State'].apply(lambda x: str(x) in EAST_COAST_STATES)].copy()
    
    def is_valid_event(row):
        offers_prev_count = row['Prev_Offer_Count']
        is_new_player = row['New Player'] == "Yes"
        recent_offers = row['Recent_Offers_Raw']
        
        d1_offers_found = []
        for off in recent_offers:
            if is_d1_offer(off):
                d1_offers_found.append(off)
        
        if not d1_offers_found: return False
        
        d1_count = len(d1_offers_found)
        
        if is_new_player:
            if d1_count == 1: 
                row['Recent_Offers_Raw'] = d1_offers_found 
                return True
            return False
            
        if not is_new_player and offers_prev_count == 0 and d1_count == 1:
            row['Recent_Offers_Raw'] = d1_offers_found
            return True
            
        return False

    df_new = df_new[df_new.apply(is_valid_event, axis=1)]
    
    if df_new.empty:
        print("[DEBUG] No players matched First D1 Offer criteria (Check csv history/state/offer count)")
        return pd.DataFrame(columns=['Name', 'Position', 'Height', 'Weight', 'State', 'School', 'Recent_Offers'])

    df_new['Recent_Offers'] = df_new['Recent_Offers_Raw'].apply(lambda x: ", ".join(sorted(x)) if isinstance(x, list) else "")
    
    cols_to_keep = ['Name', 'Position', 'Height', 'Weight', 'State', 'School', 'Recent_Offers']
    df_new = df_new.sort_values(by=['New Player', 'Name'], ascending=[False, True])
    final_cols = [c for c in cols_to_keep if c in df_new.columns]
    return df_new[final_cols]

# --- MAIN ---
async def main():
    semaphore = asyncio.Semaphore(CONCURRENT_LIMIT)
    seen_on3, seen_247, history_offers = load_id_cache(HISTORY_FILE)
    print(f"Loaded Cache: {len(seen_on3)} On3 IDs, {len(seen_247)} 247 IDs.")

    on3_cookies, _, on3_build_id = get_selenium_cookies("https://www.on3.com/rivals/search/")
    t247_cookies, t247_ua, _ = get_selenium_cookies(f"https://247sports.com/season/{CLASS_YEAR}-football/recruits/")
    
    print("\n--- Starting Scraping ---")
    on3_data, t247_data = await asyncio.gather(
        On3Scraper(on3_cookies, on3_build_id).get_data(semaphore),
        TwoFourSevenScraper(t247_cookies, t247_ua).get_data(semaphore)
    )
    
    print("--- Merging Data ---")
    t247_map = {p['normalized']: p for p in t247_data}
    final_list = []
    
    for on3 in on3_data:
        match = t247_map.pop(on3['normalized'], None)
        combined_offers = set(on3['offers'])
        if match: combined_offers.update(match['offers'])
        p4_count = count_p4_offers(combined_offers)
        star_rating = on3['stars'] if on3['stars'] else (match['stars'] if match else None)
        state = on3['state'] if (on3['state'] and on3['state'] != "N/A") else (match['state'] if match else "N/A")
        pos = on3['position'] if on3['position'] else (match['position'] if match else "N/A")

        # --- HEIGHT/WEIGHT PRIORITY LOGIC ---
        height = on3['height']
        weight = on3['weight']
        if match:
            height = match['height']
            weight = match['weight']

        final_list.append({
            "Name": on3['name'], "Source": "Both" if match else "On3 Only",
            "P4_Offers": p4_count, "Total_Offers": len(combined_offers),
            "State": state, "School": on3['school'], "Position": pos,
            "Height": height, "Weight": weight, "Stars": star_rating,
            "ID_Latest": max(int(on3['id']), int(match['id'])) if match else int(on3['id']),
            "On3_ID": on3['id'], "247_ID": match['id'] if match else "N/A",
            "Rivals_URL": on3['profile_url'], "247_URL": match['profile_url'] if match else "N/A",
            "Offers_List": ", ".join(sorted(combined_offers)), "Headshot": on3['headshot']
        })
        
    for t247 in t247_map.values():
        p4_count = count_p4_offers(t247['offers'])
        final_list.append({
            "Name": t247['name'], "Source": "247 Only",
            "P4_Offers": p4_count, "Total_Offers": len(t247['offers']),
            "State": t247['state'], "School": t247['school'], "Position": t247['position'],
            "Height": t247['height'], "Weight": t247['weight'], "Stars": t247['stars'],
            "ID_Latest": int(t247['id']), "On3_ID": "N/A", "247_ID": t247['id'],
            "Rivals_URL": "N/A", "247_URL": t247['profile_url'],
            "Offers_List": ", ".join(sorted(t247['offers'])), "Headshot": "N/A"
        })

    final_list = compare_with_history(final_list, seen_on3, seen_247, history_offers)
    df = pd.DataFrame(final_list)
    
    # Master Sort
    def get_tier(row):
        try: stars = float(row['Stars']); is_quality = stars >= 3
        except: is_quality = False
        offers, p4 = row['Total_Offers'], row['P4_Offers']
        if is_quality and offers > 0 and p4 == 0: return 1
        if is_quality and offers == 0: return 2
        return 3

    df['Tier'] = df.apply(get_tier, axis=1)
    df['Is_New_Sort'] = df['New Player'].apply(lambda x: 1 if x == "Yes" else 0)
    df_master = df.sort_values(by=["Tier", "Is_New_Sort", "ID_Latest"], ascending=[True, False, False])
    df_master = df_master.drop(columns=['Tier', 'Is_New_Sort', 'Recent_Offers_Raw', 'Prev_Offer_Count'])
    
    # New Tab
    df_first_offers = get_first_d1_offer_tab(df)
    
    # --- EXCEL SAVE LOGIC (UPDATED) ---
    print(f"Saving to {OUTPUT_FILE}...")
    today_str = datetime.now().strftime("%Y-%m-%d")
    new_sheet_name = f"First D1 Offer - {today_str}"
    
    if os.path.exists(OUTPUT_FILE):
        # File exists: Append new tab, Replace Master
        with pd.ExcelWriter(OUTPUT_FILE, mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
            df_master.to_excel(writer, sheet_name="Master List", index=False)
            # Add the new tab (unique name per day)
            df_first_offers.to_excel(writer, sheet_name=new_sheet_name, index=False)
    else:
        # Create fresh
        with pd.ExcelWriter(OUTPUT_FILE, engine='openpyxl') as writer:
            df_master.to_excel(writer, sheet_name="Master List", index=False)
            df_first_offers.to_excel(writer, sheet_name=new_sheet_name, index=False)
            
    df_master.to_csv(HISTORY_FILE, index=False)
    print("Done!")

if __name__ == "__main__":
    try: asyncio.run(main())
    except Exception as e: print(f"Error: {e}")