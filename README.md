# Learning Deployment On Render 

## Things I Learned
### websocket
* ISSUE: Using sockets to update a value in SQLite3 database changes the value on the page after button is pressed, but resets when the page is refreshed
    * FIX: Ensure "commit()" is used to make changes permanent
        * NOTE: Flask auto-commits SQL changes for you while sockets do not, so adding commit() explicitly is needed for sockets

### gevent
* ISSUE: gevent-websocket didn't work when deployed on render, but worked locally
    * FIX: Ensure the Python version on render is compatible with your packages' versions. Render used 3.11 for you, but the gevent you installed works only on 3.8 and later.
        * NOTE: Good idea to ensure compatiblity b/w things you use and deployment sites in general

### SQL execute() method
* NOTE: .execute(...) expects tuples when plugging in for ?
    * Did not need to use tuples in Flask, but that's likely b/c Flask is forgiving and processes it for you
    * Be sure to use tuples from now on in execute()
    * CAUTION: if you have only one element in a tuple, you need a common to make it a tuple --> WRONG: ("some_item")   CORRECT: ("some_item",)

REMINDER: sometimes it's best to create a test project to learn certain concepts rather than trying it on an actual project. That way, you can focus solely on the concept rather than trying to change other codes to fit the concept you're suppose to be learning. 


#### Credits
* https://flask-socketio.readthedocs.io/en/latest/deployment.html#gunicorn-web-server
* https://stackoverflow.com/questions/62075431/flask-post-request-form-data-without-refreshing-page 
* https://stackoverflow.com/questions/55657789/sqlite-why-do-i-need-the-commit-command 
* https://docs.python.org/2/library/sqlite3.html
* https://stackoverflow.com/questions/62704869/python-flask-stop-page-from-re-submitting-a-post-request