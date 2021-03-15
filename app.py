from flask import Flask, render_template
import csv
import commit_checker as checker

app = Flask(__name__)

@app.route("/")
def project_list():
    # Get student name and git link from csv file
    data_list = []
    final_results=[]    

    # Read student information from csv and append data to data_lists
    with open (r"./k2021Project.csv", encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for c in reader:
            data_list.append(c)

    # Iterate data_list to check last commit to the repository
    for d in data_list:        
        if (d['Git'] == ''):
            result = {'name' : d['Name'], 'last_commit' : 'n/a', 'url': 'no repository'}
            final_results.append(result)         
        else:
            gitUrl = d['Git'].replace("https://github.com/", "").split('/')
            checker.gitLastCommit(d['Name'], gitUrl[0], gitUrl[1], final_results)     
    
    return render_template('project_result.html', 
                            result = final_results,
                            total = len(final_results))
@app.route("/book-store")
def bookstore_list():
    # Get student name and git link from csv file
    data_list = []
    final_results=[]    

    # Read student information from csv and append data to data_lists
    with open (r"./k2021Bookstore.csv", encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for c in reader:
            data_list.append(c)

    # Iterate data_list to check last commit to the repository
    for d in data_list:        
        if (d['Git'] == ''):
            result = {'name' : d['Name'], 'last_commit' : 'n/a', 'url': 'no repository'}
            final_results.append(result)         
        else:
            gitUrl = d['Git'].replace("https://github.com/", "").split('/')
            checker.gitLastCommit(d['Name'], gitUrl[0], gitUrl[1], final_results)     
    
    return render_template('bookstore_result.html', 
                            result = final_results,
                            total = len(final_results))

@app.route('/no')
def no_repository():
    return "repository not found"

if __name__ == "__main__":
    app.run(host = '127.0.0.1', port = 5000, debug = True)