# ros2bag_fixer
This is a repository on how to recover Ros2 bags that were corrupted as in they closed before a graceful shutdown. BOTH formats .db3 and .mcap require a footer/metadata so require a tool to fix this. THE ROS2 COMMAND REINDEX DOES NOT WORK FOR EITHER BAG FORMAT IN HUMBLE!

## How To Recover a corrupted sqlite3 or .db3 

1. Use the SQLite3 tool to create a .sql file DO THE .db3 NOT THE DIRECTORY!
   ```
   chmod +x sqlite3
   sqlite3 path_to_corrupt.db3 .recover >data.sql
   ```
2.  Convert sql file to csv ([There are Online website or use the sqlite3 tool (Forgot how I did it)] (https://www.sqlite.org/cli.html))
3.  Edit the jupyter Notebook to point the topic id and file name 

## How To Recover a corrupted .mcap file 
This tool comes from foxglove stuido so use that for plotting https://github.com/foxglove/mcap/releases/tag/releases%2Fmcap-cli%2Fv0.0.46
1. Use the mcap tool in the repository
   
   ```
   chmod +x mcap-linux-amd64
   ./mcap-linux-amd64 recover in.mcap -o out.mcap
   ```
