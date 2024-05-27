# ros2bag_fixer

1. Use the SQLite3 tool to create a .sql file 
   ```
   sqlite3 corrupt.db3 .recover >data.sql
   ```
2.  Convert sql file to csv ([There are Online website to do this or look it up for Python later] (https://www.sqlite.org/cli.html))
3.  Edit the jupyter Notebook to point the topic id and file name 
