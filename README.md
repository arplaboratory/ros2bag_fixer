# ros2bag_fixer

1. Use the SQLite3 tool to create a .sql file 
   ```
   sqlite3 corrupt.db3 .recover >data.sql
   ```
2.  Convert sql file to csv  https://products.groupdocs.app/conversion/sql-to-csv#google_vignette
3.  Edit the jupyter Notebook to point the topic id and file name 
