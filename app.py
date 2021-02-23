from flask import Flask, render_template
import csv
import commit_checker as checker

app = Flask(__name__)

@app.route("/")
def studnt_list():
    # Get student name and git link from csv file
    data_list = []
    final_results=[]
    final_links = []

    # Read student information from csv and append data to data_lists
    with open (r"./k2021Project.csv", encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for c in reader:
            data_list.append(c)

    # Iterate data_list to check last commit to the repository
    for d in data_list:
        if (d['Git'] == ''):
            final_results.append(d['Name'] + ", please submit repository!")
        else:
            gitUrl = d['Git'].replace("https://github.com/", "").split('/')
            checker.gitLastCommit(d['Name'], gitUrl[0], gitUrl[1], final_results)     
      
    return render_template('result.html', result = final_results)


if __name__ == "__main__":
    app.run(host = '127.0.0.1', port = 5000, debug = True)