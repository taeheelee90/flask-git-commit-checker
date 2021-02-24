from datetime import datetime
from datetime import timedelta
import requests

def gitLastCommit(name, username, repository, final_results):
    #url & headers
    url = f"https://api.github.com/repos/{username}/{repository}"
    request_headers={'Authorization' : 'token WRITE TOKEN HERE'}

    #request to json
    repo_data = requests.get(url, headers=request_headers).json()
            
    # get info from API
    pushed_at_str = repo_data.get('pushed_at')
    url_to_repository = repo_data.get('svn_url')
    
    # current datetime in String
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # convert now to datetime
    now = datetime.strptime(now, '%Y-%m-%d %H:%M:%S')

    if ('message' in repo_data):
        result = {'name' : name, 'last_commit' : 'n/a', 'url': 'no repository'}
        final_results.append(result)  
    else: 
    # convert string to datetime (in UTC+2: HELSINKI)
        last_pushed_date = datetime.strptime(pushed_at_str, '%Y-%m-%dT%H:%M:%SZ') + timedelta(hours=2)
        daysAgo = (now - last_pushed_date).days

        if (daysAgo == 0): # if last update was within last 24hrs
            result = {'name' : name, 'last_commit' : 'today', 'url': url_to_repository}
        else:
            result = {'name' : name, 'last_commit' : str(daysAgo) + ' days ago', 'url': url_to_repository}
      
        final_results.append(result)   