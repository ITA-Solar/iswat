import urllib.request
import os
from bs4 import BeautifulSoup

def update_schedule():
    url = "https://docs.google.com/document/d/e/2PACX-1vRhdEzTaUK0rMwvJhPUCOtJb2bl_RCNAQNNFN7QTbgbza41rhgeiARe5OPsDQqqVu5pMy17M21nama8/pub"
    schedule_md_path = os.path.join(os.path.dirname(__file__), "docs", "schedule.md")
    
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read().decode('utf-8')
            
        soup = BeautifulSoup(html, 'html.parser')
        contents = soup.find('div', id='contents')
        
        if not contents:
            print("Error: Could not find div id='contents' in Google Doc HTML.")
            return
            
        contents['style'] = "width: 100%; background: white; padding: 1rem; border-radius: 8px; overflow-x: auto;"
        
        with open(schedule_md_path, 'r', encoding='utf-8') as f:
            md_content = f.read()
            
        start_token = '<!-- START SCHEDULE -->'
        end_token = '<!-- END SCHEDULE -->'
        
        if start_token in md_content and end_token in md_content:
            start_idx = md_content.find(start_token) + len(start_token)
            end_idx = md_content.find(end_token)
            
            new_md = md_content[:start_idx] + "\n" + str(contents) + "\n" + md_content[end_idx:]
            
            with open(schedule_md_path, 'w', encoding='utf-8') as f:
                f.write(new_md)
                
            print("Successfully updated schedule.md with Google Doc content!")
        else:
            print("Error: Could not find START/END SCHEDULE markers in schedule.md.")
            
    except Exception as e:
        print(f"Error during schedule update: {e}")

def on_pre_build(config, **kwargs):
    print("Running schedule extraction hook...")
    update_schedule()

if __name__ == "__main__":
    update_schedule()
